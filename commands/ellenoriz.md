---
description: Magyar szöveg átnézése a Humanizer-hu 26 mintája ellen. Jelentést ad, nem ír át.
argument-hint: [fájl vagy útvonal]
---

Nézd át a megadott magyar szöveget a Humanizer-hu mintái ellen, és adj róla
jelentést. **Ne írd át a fájlt, és ne javíts benne semmit.** A javításról a
felhasználó dönt, utána.

Ellenőrizendő: $ARGUMENTS

Ha nincs megadva fájl, kérdezd meg, melyiket nézzed.

## 1. Gépi kör

Futtasd:

```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/lint-hu.py <fájl>
```

Ha a szöveg publikálandó (ügyféllevél, cikk), add hozzá a `--published`
kapcsolót: ott a magyar idézőjel szabályos, a §21 találata nem hiba.

Ez a szabálykészletet a `SKILL.md` `Kerüld` soraiból olvassa ki, tehát mindig
a mintákkal együtt frissül. Két szintet ad:

- **BIZTOS**: szabálysértés a darabszámtól függetlenül (hosszú gondolatjel,
  magányos gondolatjel tagmondatok között, görbe idézőjel, Title Case-szerű címsor, dísz a címsorban, `kerül` passzív,
  félkövér címke a felsorolásban).
- **gyanús**: emberi döntést kér. A §12 saját szövege mondja ki, hogy egy szó
  egyszeri előfordulása még nem gépiesség. Ezeket mérlegeld, ne jelentsd
  automatikusan hibának.

## 2. Ítéletalapú kör

Olvasd el a `${CLAUDE_PLUGIN_ROOT}/SKILL.md`-t, majd a szöveget, és keresd azt,
amit a script nem lát:

- §6 erőltetett hármas: három értékelő melléknév vagy három párhuzamos
  szerkezet, ami nem valódi három.
- §7 ismétlődő mondatkezdés: kiírt alany ott, ahol a magyar elhagyná.
- §13 felfújt jelentőség, főleg új tényt nem adó záró szakasz.
- §14 homályos kapcsolat: elkent okság, vagy feltevés, ami nem vállalja magát.
- §17 kölcsönzött tekintély: meg nem nevezett best practice, vagy nagy cég neve
  indoklás helyett.
- §23 kitalált tény: név, útvonal, verzió, érték, ami nincs a forrásban.
- §24 a címsort megismétlő első mondat.
- §25 az előző verzió leírása a mostani működés helyett.
- §26 megszólításkeveredés: tegezés és magázás, `Ön` és `ön`, szerkesztői T/1 és
  személytelen váltakozása.

Nézd a bekezdések alakját is, ne csak a mondatokat.

## 3. Jelentés

Egy listát adj vissza, fájl és sor szerint, a leginkább zavarótól a
legkevésbé felé:

```
sor    minta   mi a baj                       idézet
```

Minden tételhez írd oda, mit tennél helyette, de **csak javaslatként, egy
mondatban**. A fájlt ne módosítsd.

A végén két dolgot mondj meg:

- Mi az a három tétel, ami a legtöbbet javítana a szövegen.
- Mi az, amit szándékosan hagynál békén, és miért. Ha a szöveg fajtája vagy a
  hívó feladat felülír egy mintát (§11, §14 és §17 a Részletesség alszakasz
  szerint, vagy a §23 példadokumentum esetén), azt mondd ki, ne jelentsd
  hibának.
