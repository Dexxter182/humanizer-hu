#!/usr/bin/env python3
"""Magyar szöveg gépi ellenőrzése a Humanizer-hu mintái ellen.

Jelentést ad, nem ír át. A kerülendő kifejezéseket a SKILL.md-ből olvassa ki,
hogy egyetlen igazságforrás maradjon.

Használat:
    python3 scripts/lint-hu.py FÁJL [FÁJL ...]
    python3 scripts/lint-hu.py --strict FÁJL     # 1-es kilépőkód, ha van biztos találat
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"

# Leíró tételek, amiket nem lehet szó szerint keresni.
LEIRO = re.compile(
    r"\b(ahol|helyett|alakban|váltakozása|keveredése|szerkezet|forma|mód|szórend"
    r"|megfordítása|beékelés|névelő|tőmondat|bekezdés|szakasz|nyitás|farok)\b",
    re.I,
)
FOLYTATAS = re.compile(r"^(hogy|hanem|ha|majd|de|illetve|valójában|azt|amely|ami)\b", re.I)


def kerulendo_kifejezesek(skill: str) -> tuple[dict[str, tuple[int, re.Pattern]], int]:
    """A Kerüld sorokból kiszedi a kereshető kifejezéseket. Visszaadja a
    kifejezés -> mintaszám leképezést és a kihagyott leíró tételek számát."""
    talalt: dict[str, tuple[int, re.Pattern]] = {}
    kihagyott = 0
    for m in re.finditer(r"(?m)^### (\d+)\. .*\n\n?\*\*Kerüld:\*\* (.+)$", skill):
        szam, sor = int(m.group(1)), m.group(2)
        # zárójeles és szögletes részek maszkolása, hogy a bennük levő
        # elválasztók ne törjék szét a tételeket
        maszk: list[str] = []

        def elrejt(mm: re.Match[str]) -> str:
            maszk.append(mm.group(0))
            return f"\x00{len(maszk) - 1}\x00"

        sor = re.sub(r"\([^)]*\)|\[[^]]*\]|\"[^\"]*\"", elrejt, sor)
        darabok = [d.strip() for d in re.split(r"[;,]\s+", sor) if d.strip()]

        osszevont: list[str] = []
        for d in darabok:
            if osszevont and FOLYTATAS.match(d):
                osszevont[-1] += ", " + d
            else:
                osszevont.append(d)

        for d in osszevont:
            vissza = re.sub(r"\x00(\d+)\x00", lambda mm: maszk[int(mm.group(1))], d)
            tiszta = re.sub(r"\s*\([^)]*\)", "", vissza).strip().strip('"')
            if not tiszta or len(tiszta) < 4 or LEIRO.search(tiszta) or len(tiszta.split()) > 6:
                kihagyott += 1
                continue
            k = tiszta.lower()
            talalt.setdefault(k, (szam, re.compile(r"(?<![\w\u00c0-\u017f])" + re.escape(k) + r"(?![\w\u00c0-\u017f])")))
    return talalt, kihagyott


# Szerkezeti ellenőrzések: ezekre a skill maga mondja, hogy egy előfordulás is elég.
BIZTOS = [
    (8, re.compile(r"—"), "hosszú gondolatjel"),
    (8, re.compile(r"(?<=\s)--(?=\s)"), "dupla kötőjel"),
    (21, re.compile(r"[„“”»«]"), "görbe idézőjel"),
    (11, re.compile(r"\b\w+(?:ásra|ésre)\s+kerül\w*", re.I), "kerül passzív"),
    (11, re.compile(r"\b\w+(?:ás|és)a?\s+(?:automatikusan\s+)?történik\b", re.I), "történik + főnév"),
]
CIMSOR_EMOJI = re.compile(r"[\U0001F300-\U0001FAFF←-⇿✀-➿✨⭐]")
KISSZO = {"és", "vagy", "a", "az", "de", "mint", "hogy", "ha", "nem", "is", "meg"}


def kodmentes(sorok: list[str]) -> list[bool]:
    """Igaz azokra a sorokra, amik nem kódblokkban vannak."""
    ki, kodban = [], False
    for s in sorok:
        if s.lstrip().startswith("```"):
            kodban = not kodban
            ki.append(False)
        else:
            ki.append(not kodban)
    return ki


def tisztit(sor: str) -> str:
    """Inline kód, URL és link-cél kivétele, hogy ne adjon hamis találatot."""
    sor = re.sub(r"`[^`]*`", " ", sor)
    sor = re.sub(r"https?://\S+", " ", sor)
    sor = re.sub(r"\]\([^)]*\)", "] ", sor)
    return sor


def ellenoriz(ut: Path, kifejezesek: dict, sajat_skill: bool) -> list[tuple]:
    sorok = ut.read_text(encoding="utf-8").split("\n")
    elo = kodmentes(sorok)
    talalatok = []
    ne_ird = False
    minta = 0

    for i, nyers in enumerate(sorok, 1):
        if not elo[i - 1]:
            continue
        if sajat_skill:
            # a Ne írd blokkok és a szabálysorok szándékosan tartalmaznak tiltottat
            if nyers.startswith("**Ne írd:**"):
                ne_ird = True
                continue
            fej = re.match(r"### (\d+)\. ", nyers)
            if fej:
                minta = int(fej.group(1))
            elif nyers.startswith("## "):
                minta = 0
            if nyers.startswith(("**Így írd:**", "**Probléma:**", "### ", "## ")):
                ne_ird = False
            if ne_ird or nyers.startswith(("**Kerüld:**", "**Szabály:**")):
                continue
        # A "Mit hagyj békén" szerint az idézet nem számít: az idézetblokk és a
        # táblázatcella idézett anyag, azt a lint sem minősíti.
        if nyers.lstrip().startswith(">") or nyers.lstrip().startswith("|"):
            continue
        sor = tisztit(nyers)

        for szam, rx, mit in BIZTOS:
            if sajat_skill and minta in (8, 21) and szam in (8, 21):
                continue  # ezek a minták maguk nevezik meg a tiltott jelet
            for m in rx.finditer(sor):
                talalatok.append(("biztos", i, szam, m.group(0).strip(), mit))

        if sor.startswith("#"):
            cim = sor.lstrip("#").strip()
            if CIMSOR_EMOJI.search(cim):
                talalatok.append(("biztos", i, 20, cim[:40], "dísz a címsorban"))
            szavak = [w for w in cim.split() if not re.fullmatch(r"[0-9]+\.|[A-F]\.", w)]
            nagyok = [w for w in szavak[1:] if w[:1].isupper() and w.lower() in KISSZO]
            if nagyok:
                talalatok.append(("biztos", i, 20, " ".join(nagyok), "Title Case a címsorban"))

        if re.match(r"\s*[-*]\s+\*\*", sor):
            talalatok.append(("biztos", i, 19, sor.strip()[:40], "félkövér címke a felsorolásban"))

        if not (sajat_skill and nyers.startswith("#")):
            kisbetus = sor.lower()
            for kif, (szam, rx) in kifejezesek.items():
                if rx.search(kisbetus):
                    talalatok.append(("gyanús", i, szam, kif, "kerülendő kifejezés"))

    return talalatok


def main() -> int:
    argv = sys.argv[1:]
    strict = "--strict" in argv
    fajlok = [a for a in argv if not a.startswith("--")]
    if not fajlok:
        print(__doc__)
        return 2

    kifejezesek, kihagyott = kerulendo_kifejezesek(SKILL.read_text(encoding="utf-8"))
    print(f"{len(kifejezesek)} kerülendő kifejezés a SKILL.md-ből, "
          f"{kihagyott} leíró tétel kihagyva (azokhoz ítélet kell).\n")

    biztos_db = 0
    for nev in fajlok:
        ut = Path(nev)
        if not ut.is_file():
            print(f"Nem olvasható: {nev}")
            continue
        talalatok = ellenoriz(ut, kifejezesek, ut.resolve() == SKILL)
        biztos = [t for t in talalatok if t[0] == "biztos"]
        gyanus = [t for t in talalatok if t[0] == "gyanús"]
        biztos_db += len(biztos)

        print(f"== {nev}")
        if not talalatok:
            print("   tiszta\n")
            continue
        for _, sor, szam, szoveg, mit in biztos:
            print(f"   BIZTOS  {sor:>4}  §{szam:<2} {mit}: {szoveg}")
        if gyanus:
            szamlalo: dict[tuple, list[int]] = {}
            for _, sor, szam, szoveg, _mit in gyanus:
                szamlalo.setdefault((szam, szoveg), []).append(sor)
            for (szam, szoveg), sorok_ in sorted(szamlalo.items()):
                helyek = ", ".join(str(x) for x in sorok_[:5])
                tobb = f" (+{len(sorok_) - 5})" if len(sorok_) > 5 else ""
                print(f"   gyanús  {helyek}{tobb}  §{szam:<2} \"{szoveg}\" x{len(sorok_)}")
        print()

    print("Az idézetblokk (>) és a táblázatsor (|) kimarad: a Mit hagyj békén")
    print("szerint az idézet nem minősül kerülendőnek.")
    print("A gyanús találat nem hiba: emberi döntést kér. A §12 saját szövege "
          "mondja ki, hogy egy szó egyszeri előfordulása még nem gépiesség.")
    print("Amit ez a script nem lát: §6 hármas, §14 homályos kapcsolat, "
          "§23 kitalált tény, §25 előző verzió, §26 regiszterkeveredés.")
    return 1 if (strict and biztos_db) else 0


if __name__ == "__main__":
    raise SystemExit(main())
