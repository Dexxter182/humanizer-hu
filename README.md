# Humanizer-hu

Magyar írásstílus-skill agenteknek, generáláshoz. A szabályok írás közben hatnak, nem a kész szöveg utólagos tisztításakor: a hívó feladat adja a szerkezetet (user story, specifikáció, ADR, jegy, dokumentáció, ügyfélszöveg), a Humanizer-hu a nyelvet. A másik alapszabálya, hogy csak azt állítja, amit a kérés vagy a forrás tartalmaz: nevet, számot, dátumot, idézetet és hivatkozást nem talál ki, hanem elkéri, vagy egyszerűbb mondatot ír.

Az agenttel íratott magyar dokumentumon látszik, hogy gép írta: erőltetett hármasok, "kerül" passzív, felfújt jelzők, gondolatjel minden tagmondat között, tegezés és magázás váltakozva. A Humanizer-hu ezt a réteget cseréli le. 26 mintát ad hat csoportban, és egy dokumentumszintű döntéssort, ami az első mondat előtt lefut. A minták magyar példákon állnak, magyar nyelvtani háttérrel, és kettőnek angolul nincs is értelme: a tükörfordításnak és a megszólításnak.

## Miben más

- Dokumentumszintű réteg. Hosszúság, folyó szöveg vagy felsorolás, alcím, zárójel, megszólítás és részletesség az első mondat előtt dől el, mert ezek utólag, mondatonként nem javíthatók.
- Magyar nyelvtani háttér. A "kerül" passzív, a terpeszkedő szerkezet, a pro-drop, a birtokos szórend és a magyar tipográfia saját mintát kap, a hivatkozások a [docs/nyelveszeti-forrasok.md](docs/nyelveszeti-forrasok.md) fájlban vannak.
- Gépi ellenőrzés. A `scripts/lint-hu.py` LLM nélkül jelzi a szabálysértéseket, tehát nem az a modell nézi át a szöveget, amelyik írta. A mintalistát a `SKILL.md`-ből olvassa, és nem ír át semmit.
- Hangillesztés. Írásmintából átveszi a mondathosszt, a szóválasztást és az írásjeleket, és a minta felülírja a skill saját tipográfiai szabályait.

## Példa

Ügyfélnek szóló funkcióleírás egy parkolási alkalmazás új funkciójáról. A neveket, a számokat és a menü helyét a kérés adja; amit a kérés nem tartalmaz, azt a skill nem találja ki, hanem megkérdezi.

Amit a modell alapból ír:

> Örömmel jelentjük be, hogy elérhetővé vált a Kedvencek funkció — ez nem csupán egy új gomb az alkalmazásban, hanem a parkolási élmény teljes újragondolása. ✨
>
> A funkció bevezetésre került annak érdekében, hogy a felhasználók számára zökkenőmentes, gyors és intuitív élményt biztosítsunk. Mostantól a leggyakrabban használt parkolási zónák egyetlen érintéssel elmenthetők, így a parkolás indítása még soha nem volt ilyen egyszerű. Ez egy kulcsfontosságú lépés a mindennapi városi közlekedés digitalizációjában.
>
> **Főbb Előnyök:**
> - **Gyorsaság:** A parkolás indítása jelentős mértékben felgyorsul.
> - **Kényelem:** Nem szükséges minden alkalommal megkeresni a zónát.
> - **Biztonság:** A rendszer továbbra is ellenőrzi a zóna érvényességét.
>
> A Kedvencek a Beállítások menüből érhető el, és legfeljebb tíz zóna tárolható benne. Reméljük, hogy az új funkció elnyeri tetszését – kérdés esetén ügyfélszolgálatunk készséggel áll rendelkezésére!
>
> A jövő izgalmas. Együtt alakítjuk a városi mobilitást.

Amit a Humanizer-hu szabályaival ír:

> Az alkalmazásban megjelent a Kedvencek funkció. A gyakran használt parkolási zónákat egy érintéssel el lehet menteni, és a következő parkolást már a mentett zónából lehet indítani, keresés nélkül. A rendszer a mentett zónánál is ellenőrzi az érvényességet.
>
> A Kedvencek a Beállítások menüből érhető el, legfeljebb tíz zóna tárolható benne. Kérdés esetén keresse az ügyfélszolgálatot.

## Telepítés

A Skills CLI-vel:

```bash
npx skills add Dexxter182/humanizer-hu --global
```

A `--global` nélkül csak az aktuális projektbe települ. A `--agent <n>` vagy `--agent '*'` kapcsolóval választható, melyik agent kapja meg; utána töltsd újra a skilleket. A skill a `/humanizer-hu` parancsra hallgat.

A Skills CLI jelenleg 79 agenthez telepít, köztük a Claude Code, a Codex, a Cursor, a GitHub Copilot, a Gemini CLI, a Windsurf, a Zed és az OpenCode. A teljes listát az `npx skills add . --agent '?'` hibaüzenete írja ki.

Claude Code 2.1.142 vagy újabb alatt pluginként is telepíthető:

```text
/plugin marketplace add Dexxter182/humanizer-hu
/plugin install humanizer-hu@humanizer-hu
```

Így a skill neve `/humanizer-hu:humanizer-hu`, és megjön az ellenőrző parancs is.

Claude Desktopban töltsd le a repót ZIP-ként, és töltsd fel skillként. Kézi telepítéshez másold a `SKILL.md`-t az agent skill mappájába.

## Használat

A tipikus hívás egy generáló feladat mellé teszi:

```text
Írj egy ADR-t a fizetési szolgáltató cseréjéről, és használd hozzá a humanizer-hu skillt.
```

Az ADR adja a szakaszokat és a szerkezetet, a Humanizer-hu a nyelvet. Ugyanígy megy user storyval, specifikációval, jeggyel, dokumentációval és ügyfélnek szóló szöveggel. A kimenet a kész dokumentum, vázlat és szabálylista nélkül.

A már legenerált szövegre ugyanezek a szabályok érvényesek:

```text
A második szakasz túl hosszú, írd rövidebbre, a humanizer-hu szabályai szerint.
```

Gép-gép kimenetre (JSON, log, séma, parancs, strukturált adat) ne használd. Angol szövegre sem.

### Hangillesztés

Ha azt szeretnéd, hogy a szöveg rád hasonlítson, adj írásmintát:

```text
Itt egy minta a saját írásomból:
[2-3 bekezdés a saját szövegedből]

Írj ebben a hangban egy összefoglalót a sprint eredményéről, humanizer-hu szabályokkal.
```

A skill a minta ritmusát, szóválasztását, írásjeleit és szándékos furcsaságait követi. A minta felülírja a skill saját tipográfiai szabályait is.

## Ellenőrzés

A skill generáláshoz ad szabályokat. A kész szöveg átnézése külön futtatási mód, és jelentést ad, nem javít: megmondja, hol és melyik minta sérül, a javításról utána te döntesz.

Gépi kör azért van a csomagban, mert a szabályokat ugyanaz a modell sérti meg, amelyik a szöveget írta, és a saját kimenetét nézi át a legrosszabbul. A `lint-hu.py` LLM nélkül fut, így a találatai nem attól függnek, melyik modell olvassa a szöveget. Regex viszont csak a kimondott kifejezéseket látja, ezért a két kör egymás mellett áll: a script a biztosat fogja meg, a `/humanizer-hu:ellenoriz` azt, amihez olvasni kell.

Gépi kör, LLM nélkül:

```bash
python3 scripts/lint-hu.py FÁJL.md
```

A kerülendő kifejezéseket a `SKILL.md` `Kerüld` soraiból olvassa ki, tehát a mintákkal együtt frissül. Az egyszavas tételeket ragozott alakban is megtalálja, a több szavasakat szó szerint keresi. Két szintet ad: a BIZTOS találat szabálysértés a darabszámtól függetlenül, a gyanús emberi döntést kér. Az idézetblokkot és a táblázatsort kihagyja, mert a "Mit hagyj békén" szakasz szerint az idézet nem számít.

Teljes kör, pluginként telepítve:

```text
/humanizer-hu:ellenoriz FÁJL.md
```

Ez előbb a scriptet futtatja, majd azt nézi át, amit regex nem lát: a 6. minta hármasát, a 14. homályos kapcsolatát, a 23. kitalált tényeit, a 25. előző verzióját és a 26. megszólításkeveredését.

## A 26 minta

A minták a leggyakoribbal kezdődnek. A teljes leírás, a kerülendő kifejezésekkel és példákkal, a `SKILL.md`-ben van.

### A. Színpadiasság

| # | Minta | Ne írd | Így írd |
| --- | --- | --- | --- |
| 1 | Hamis ellentét (nem X, hanem Y) | "Nem csupán technikai módosítás, hanem a teljes ügyfélélmény újragondolása" | Mondd ki a lényeget |
| 2 | Egysoros zárások és töredékek | "Nincs migráció. Nincs leállás. Nincs kockázat. Ez a lényeg." | Természetes mondathossz, konkrét állítás |
| 3 | Mélynek hangzó szólamok | "A naplózás a rendszer memóriája" | A konkrét állítás |
| 4 | Felvezetés a lényeg előtt | "Az alábbiakban áttekintjük", "Nézzük meg közelebbről" | Kezdd a tartalommal |
| 5 | Vita senkivel | "Csábító megoldás lenne..., de" | Csak valódi alternatíva |

### B. Ritmus és tükörfordítás

| # | Minta | Ne írd | Így írd |
| --- | --- | --- | --- |
| 6 | Erőltetett hármasok | "gyors, megbízható és könnyen bővíthető" | Annyi elem, amennyit a jelentés kér |
| 7 | Ismétlődő mondatkezdés | "A rendszer... A rendszer... A rendszer..." | Vond össze, vagy hagyd el az alanyt |
| 8 | Gondolatjel mint kötőelem | "## Teljesítmény — mit mértünk" | Kettőspont a címben; pont, vessző, zárójel a mondatban |
| 9 | Halmozott bizonytalanítás | "esetleg akár talán" | "lehet" |
| 10 | Anglicizmusok és tükörfordítások | "Ez egy jelentős kihívás", "navigálni a kihívások között" | Magyar szerkezet, a szakszó marad angolul |
| 11 | Passzív és elrejtett cselekvő | "betöltésre kerülnek", "a mentés automatikusan történik" | Nevezd meg, ki mit csinál |

### C. Felfújás

| # | Minta | Ne írd | Így írd |
| --- | --- | --- | --- |
| 12 | Túlhasznált AI-szavak | "átfogó, robusztus, zökkenőmentes, kulcsfontosságú" | Köznapi szó vagy konkrétum |
| 13 | Felfújt jelentőség | "mérföldkövet jelentett", "a jövő fényes" | A tény, zárás az utolsó konkrétummal |
| 14 | Homályos kapcsolat | "a lassulás a release-hez köthető" | Nevezd meg a viszonyt, ha a forrás adja |
| 15 | Felületes határozói igenevek | "biztosítva a megbízható kézbesítést" | Csak amit a forrás alátámaszt |
| 16 | Reklámnyelv | "intuitív, letisztult felületen" | Mondd meg, mi a dolog |
| 17 | Kölcsönzött tekintély | "a best practice szerint", "a Netflix is így csinálja" | Valódi forrás, vagy hagyd el |
| 18 | A létige kerülése | "felületeként szolgál", "négy nézettel rendelkezik" | Mi micsoda, és minek mije van |

### D. Formázás

| # | Minta | Ne írd | Így írd |
| --- | --- | --- | --- |
| 19 | Félkövér mint dekoráció | "**jelentősen** javítja", "**Teljesítmény:** A teljesítmény javult" | Kiemelés nélkül, folyó szövegben |
| 20 | Dekoratív címsorok | "Migrációs Terv És Visszaállítás", emoji, nyíl, vonal | Mondatkezdő nagybetű, dísz nélkül |
| 21 | Tipográfiai idézőjelek | `„a projekt”`, `“a projekt”` | `"a projekt"` |

### E. Maradványok

| # | Minta | Ne írd | Így írd |
| --- | --- | --- | --- |
| 22 | Chatbot-maradvány | "Remélem, segítettem! Szólj, ha..." | Tartalommal kezdj, ténnyel zárj |
| 23 | Tudáskorlát és találgatás | "feltehetően a config.yaml-ban beállított korlát" | Mondd meg, mi ismert, vagy hagyd el |
| 24 | Címsor megismételve | "## Hibakezelés" + "A hibakezelés fontos része a rendszernek." | Hagyd a címsort dolgozni |
| 25 | Az előző verzióról írni | "a korábbi megközelítést váltja ki" | Írd le, mit csinál most |

### F. Megszólítás

| # | Minta | Ne írd | Így írd |
| --- | --- | --- | --- |
| 26 | Tegezés és magázás keveredése | "Kattints a gombra... indítsa újra a böngészőt" | Egy forma végig |

## Dokumentumszintű döntések

Ezek a döntések az első mondat előtt születnek, és utólag nem javíthatók mondatonként. Az eredeti skillben nincs megfelelőjük.

| Döntés | Szabály |
| --- | --- |
| Hosszúság | Annyit, amennyit a feladat kér. Nincs bevezető és nincs záró gondolat. |
| Folyó szöveg vagy felsorolás | Összefüggő gondolat bekezdésbe. Felsorolás csak tételes tartalomhoz. |
| Alcímek | Csak ha az olvasó ugrani akar. A sablon szakaszai a címsorok. |
| Zárójel | Csak új információ. Nincs zárójeles fordítás és nincs magyarázat az egyértelműhöz. |
| Megszólítás | Egy forma végig. A dokumentum fajtája dönt. |
| Részletesség | Az első mondat előtt dönts. Általánosítani szabad, kitalálni nem. |
| Hang | Semleges és szakmai, váltakozó mondathosszal. Az írásminta felülír. |

## Eredet és eltérések

A 26 minta számozása a [blader/humanizer](https://github.com/blader/humanizer) 3.0.0-s változatát követi, mert onnan indult a lista. A leképezés:

- 1-9 és 12-25: a téma és a számozás azonos, a tartalom magyar. A példák, a kerülendő kifejezések, a nyelvtani indoklás és a kivételek a magyar nyelvhez készültek; a 8. és a 21. minta szabálya a magyar tipográfiához igazodik.
- 10: az eredeti "kötőjeles szópárok" helyett anglicizmusok és tükörfordítások, mert a kötőjeles szópárnak magyarul nincs értelme.
- 11: az eredeti "passzív és hiányzó alany", kibővítve a magyar "kerül" és "történik" passzívpótlóval és a láncolt főnevesítéssel.
- 26: új, csak a magyar verzióban. A tegezés és a magázás keveredése.

Amit a magyar verzió a mintákon felül hoz:

- Csak magyar szöveget kezel. Ha angolt kap, jelzi, és az eredeti humanizert ajánlja.
- Dokumentumszintű réteg és persona: tapasztalt magyar elemző, aki emberi olvasónak ír dokumentációt.
- Az angol szakzsargon (agent, sprint, backlog, deploy, ticket, endpoint) marad angolul, zárójeles magyar fordítás nélkül. A tükörfordítás-minta csak a szerkezetet nézi.
- Gondolatjel: a hosszú `—` sehol nem áll, címsorban sem. A szóközös `–` marad a számintervallumban, a kötőjeles tulajdonnévben és a felsorolás elválasztójaként, ahol a kettőspont foglalt.
- Idézőjel: egyenes `"..."` áll a szövegben, a magyar `„...”` és az angol `“...”` helyén is. Publikálandó ügyfélszövegben marad a magyar alak.

A 2.0.0 óta a két projekt célja eltér: az eredeti meglévő szöveget ír át, a Humanizer-hu generáláshoz ad szabályokat. Az upstream továbbra is hasznos bemenet egy új mintához, de a fájl szerkezete már nem követi.

A 12. minta szójegyzéke megfigyelésen alapul, nem korpuszon. Ez a repo élő része: ha egy szó hiányzik vagy fölösleges, nyiss issue-t. A skill módosításának szabályai az [AGENTS.md](AGENTS.md) fájlban vannak; publikálás előtt a `python3 scripts/validate-package.py` ellenőrzi a csomagot.

## Források

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) a mintalista forrása, a [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) gondozza.
- [blader/humanizer](https://github.com/blader/humanizer) az eredeti skill, amelyből ez a projekt indult.
- [docs/nyelveszeti-forrasok.md](docs/nyelveszeti-forrasok.md) gyűjti a mintákhoz talált magyar nyelvészeti hátteret, hivatkozásokkal: kizáró ellentét (1), halmozás (6), pro-drop és topikfolytonosság (7), -hat/-het és episztemikus modalitás (9), fordításnyelv és birtokos szórend (10), terpeszkedő szerkezet (11), igenévképző és alanyazonosság (15), a címek helyesírása (20).
- A 12. minta szójegyzéke, a dokumentumszintű döntések és a 8. minta címsoros megfigyelése megfigyelésen alapul, nem korpuszon. Magyar nyelvű LLM-szógyakorisági vizsgálatot kerestünk, de nem találtunk.

## Verziótörténet

- 2.4.8 - A lint a kettőspont utáni nagybetűt mondatkezdésnek veszi, nem címstílusnak, ezért az `US-2.5.2-4: A felugró ablak` alakú címsorra nem jelez Title Case-t.
- 2.4.7 - A lint két javítása. A címsor azonosító-előtagját ("US-2", "ADR-002", "2.5.1") már nem nézi a cím szavának, ezért nem jelez Title Case-t a mögötte álló névelőre. A kimenet szóhasználata követi a 2.4.3-at: megszólításkeveredés a regiszterkeveredés helyett.
- 2.4.6 - A §20 kivételt kap: az önálló fájl, például egy README, a saját címét viszi H1-ként. A lint az egyszavas kerülendő tételeket ragozott alakban is megtalálja, és kiírja, hogy a §21 ügyfélszöveg-kivételét nem ismeri. A `SKILL.md` és az `AGENTS.md` két mondata átfogalmazva, mert maguk is a §1 alakját mutatták.
- 2.4.5 - A README a két megkülönböztető szabállyal kezd: a skill generálás közben hat, és nem talál ki tényt. Új "Miben más" szakasz a dokumentumszintű rétegről, a magyar nyelvtani háttérről, a lintről és a hangillesztésről. A csomagleírások és a kulcsszavak bővültek, hogy a skill megtalálható legyen, a telepítési szakasz megnevezi a támogatott agenteket, az Ellenőrzés szakasz pedig megmondja, miért van a csomagban gépi kör.
- 2.4.4 - A README végig magyar, az angol bevezető kikerült. Sem a skill, sem a README nem irányítja át az angol szöveggel érkezőt a forrásprojektre, mert az más feladatra való: az meglévő szöveget ír át, ez generál. Az attribúció a Források és a Licenc szakaszban marad.
- 2.4.3 - Szóhasználat: "agent", "megszólítás" és "szójegyzék" váltja az "ügynök", "regiszter" és "szólista" szót a skillben és a dokumentációban. Az "Eredet és eltérések" szakasz pontosabban írja le, mi maradt az eredetiből.
- 2.4.2 - A README újraírva, a skill saját szabályaival. A Példa a telepítés elé került, a szakaszok átrendeződtek, és megszűnt a tegezés és a magázás keveredése.
- 2.4.1 - Formázási javítás a SKILL.md-ben.
- 2.4.0 - Új ellenőrző mód. A `scripts/lint-hu.py` magyar szöveget ellenőriz a minták ellen, pluginként pedig a `/humanizer-hu:ellenoriz` parancs is elérhető. Mindkettő jelentést ad, egyik sem ír át semmit.
- 2.3.0 - Hét javítás az éles próba után. Kivételt kapott a kitalált példadokumentum, az idővonalak elválasztójele, a szerkesztői T/1 és a publikálandó ügyfélszöveg; a 11., 19. és 23. minta pontosabb lett.
- 2.2.0 - Új dokumentumszintű döntés: Részletesség. A hívó feladat és a dokumentum fajtája felülírhatja azokat a mintákat, amik a cselekvő, a viszony és a forrás megnevezését kérik.
- 2.1.0 - Mind a 26 minta átdolgozva magyar szempontból: magyar nyelvtani háttér, műszaki példaanyag a korábbi életrajzi helyett, és két tárgyi javítás a 20. és a 21. mintában. Új fájl: docs/nyelveszeti-forrasok.md.
- 2.0.0 - A skill generálásra való, nem átírásra: a hívó feladat adja a szerkezetet, ez a nyelvet, és a kimenet a kész szöveg. Új dokumentumszintű réteg (hosszúság, próza vagy felsorolás, alcímek, zárójel, regiszter, hang) és persona. A négylépéses átíró folyamat helyére egy hétpontos ellenőrző kör lép, az "Előtte/Utána" példák helyére "Ne írd/Így írd". A 8. minta már csak a hosszú gondolatjelet tiltja feltétel nélkül, a 21. tipográfiai szabállyá vált, a 19. abszolút: nincs félkövér kiemelés. Megszűnt a regiszter- és szakszó-szabály kettőzése, és az "önmagában gyenge" küszöb, aminek generálásnál nincs értelme. Mind a 26 minta megmaradt.
- 1.1.0 - A skill új szöveg megírására is szolgál, nem csak átírásra: a description és a nyitó bekezdés mindkét módot egyenrangúan nevezi meg. A description teljesen magyar, trigger-kifejezésekkel ("humanizáld", "írd meg emberi hangon"), hajtogatott YAML blokkban.
- 1.0.0 - Első kiadás. A blader/humanizer 3.0.0 magyar adaptációja: 26 minta hat csoportban, magyar példákkal. Új 10. minta (anglicizmusok és tükörfordítások), kibővített 11. minta ("kerül" passzív), új 26. minta (tegezés és magázás keveredése). Munkahelyi szöveg mint alapértelmezett hang, regiszterszabály, szakzsargon-kivétel, kötőjeles és egyenes idézőjeles tipográfia.

## Licenc

MIT. Az eredeti szerzői jog Siqi Chené (blader/humanizer), a magyar adaptációé Oroszi Györgyé. Részletek a LICENSE fájlban.
