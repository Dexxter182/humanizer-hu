# Útmutató ügynököknek

Ez a fájl elmondja, hogyan lehet a Humanizer-hu-t módosítani anélkül, hogy a csomag vagy a prompt elromlana.

## Mi van a repóban

A Humanizer-hu egy Markdownban írt ügynök-skill: a magyar szöveg megfogalmazási szabályait adja szöveg generálásához. A szerkezetet a hívó feladat adja, ez a skill a nyelvet. A `SKILL.md` a prompt, amit az ügynökök olvasnak. Nincs build lépés.

Tartsd a skillt hordozhatónak. Ne írj olyan utasítást, ami egy vagy két ügynök-eszközre korlátozza.

## Fő fájlok

- `SKILL.md` az igazság forrása és a repo egyetlen skill fájlja. Hordozható YAML metaadatot, egy magyarázatot arról, miért hangzik így az AI-szöveg, egy dokumentumszintű réteget (számozatlan, az első mondat előtti döntések), hat csoportba rendezett számozott mintákat és egy ellenőrző kört tartalmaz.
- `README.md` a telepítést, a használatot, a mintákat, az eredetet és a verziótörténetet írja le.
- `.claude-plugin/plugin.json` a Claude plugint írja le, és a skill betöltőjét a gyökér `SKILL.md`-re irányítja.
- `.claude-plugin/marketplace.json` teszi lehetővé, hogy a repót Claude marketplace-ként lehessen hozzáadni.
- `agents/openai.yaml` a megjelenített nevet, a rövid leírást és az alapértelmezett promptot tartalmazza OpenAI-kompatibilis ügynökökhöz.
- `scripts/validate-package.py` ellenőrzi a csomagfájlokat és a közös értékeket.

## Viszony az eredetihez

A 2.0.0 óta a két projekt célja eltér: a blader/humanizer meglévő szöveget ír át, a Humanizer-hu generáláshoz ad szabályokat. A 26 minta számozása azért követi az eredeti 3.0.0-t, mert onnan indult a lista, és a hivatkozások erre épülnek. Az eltérések: a 10. minta cserélődött (anglicizmusok és tükörfordítások), a 11. bővült ("kerül" passzív), a 26. új, a dokumentumszintű rétegnek pedig nincs upstream megfelelője. A leképezés a README "Eredet" szakaszában van.

Az upstream továbbra is hasznos bemenet egy új mintához, de nem kötelező tükör. Ha átveszel onnan valamit, fogalmazd meg generálási szabályként, és a README verziótörténetében hivatkozz az upstream verzióra.

## Szabályok a változtatáshoz

Tartsd szinkronban a `SKILL.md`-t és a `README.md`-t.

- Minták: a minták 1-től hézag nélkül számozottak, a legerősebb és leggyakoribb elöl. Egy új megfigyelés csak akkor kap saját mintát, ha egyetlen meglévő minta sem foglalja már magában; inkább illeszd be egy meglévőbe. Ha mintát adsz hozzá, veszel el vagy számozol át, frissítsd a README tábláit, a README szakaszcímét, az Eredet szakaszt és minden §hivatkozást. Ha egy minta nyelvtani vagy helyesírási állítást tesz, a hivatkozás a `docs/nyelveszeti-forrasok.md` fájlba kerüljön, ne a SKILL.md-be. A validátor a címsorokból számolja a darabszámot.
- Verzió: ugyanaz a verzió legyen a `SKILL.md`-ben a `metadata.version` alatt, a README első verzióbejegyzésében és a `.claude-plugin/plugin.json`-ban. Ne adj a skillhez felső szintű `version` mezőt.
- Kompatibilitás: a telepítési és használati utasítás maradjon ügynök-semleges. A Claude Code, OpenCode, Codex nevek példák, nem korlátok.
- Történet: minden viselkedésváltozáshoz vagy nem nyilvánvaló javításhoz írj rövid README verziójegyzetet.
- Ellenőrzés: publikálás előtt futtasd: `python3 scripts/validate-package.py`, `npx skills add . --list`, `claude plugin validate .`.

## Tipográfia a repóban

A repo saját szövegei ugyanazokat a szabályokat követik, amiket a skill előír: egyenes idézőjel, kötőjel gondolatjel helyett, félkövér csak ott, ahol a promptban szerkezeti címke (Kerüld, Szabály, Probléma, Ne írd, Így írd). A `README.md` és ez a fájl nem használ félkövért. A `SKILL.md` "Ne írd" példáiban a gondolatjel, az emoji, a görbe idézőjel és a félkövér szándékos: azt mutatják, mit kell elkerülni.

## Írásmód

Használj közérthető nyelvet a megjegyzésekben, promptokban, dokumentációban, leírásokban, validációs üzenetekben és jelentésekben.

- Kezdd a lényeggel.
- Használj köznapi szavakat és cselekvő szerkezetet.
- Rövid mondatok, rövid bekezdések.
- Egy fogalomra egy szó.
- A követelményhez "kell".
- Címsor, lista, táblázat csak ott, ahol segíti az olvasót.
- Vedd ki az ismétlő és fölösleges szavakat.
- Kevés rövidítés, a szakkifejezést magyarázd.
- Kerüld a kettős tagadást.
- Tartsd meg pontosan az azonosítókat, parancsokat, útvonalakat, sémamezőket, idézeteket, figyelt kifejezéseket és a viselkedést hordozó példákat.
- Tartsd meg a teljes technikai jelentést.
- Az angol szakszavakat hagyd angolul, ha a csapat így használja őket.

## A skill szerkesztése

- A YAML metaadat maradjon érvényes.
- A metaadat alatti prompt a termék.
- A skill generálásra való. Ne írj bele átíró folyamatot, kimeneti jelentést vagy fájlkezelést; azok a hívó feladat dolgai.
- Minden minta a `Ne írd` és az `Így írd` párost adja. Ahol van `Kerüld:` szólista, a `Ne írd` egy mondat; ahol a gépiesség szerkezeti, ott állhat több soros példa.
- Egy rövid, világos utasítás jobb, mint még egy kivétel vagy ismételt magyarázat.
- A 12. minta szólistája megfigyelésen alapul. Új szó csak akkor kerüljön be, ha több AI-szövegben előfordult, és emberi szövegben ritka.
