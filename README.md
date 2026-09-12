# Humanizer-hu

Humanizer-hu is a Hungarian writing-style skill for agents. The calling task supplies the structure of the document, this skill supplies the prose rules, so the generated Hungarian does not read as AI-written. It is a single Markdown file and works with any agent that can load skills. Hungarian only; for English use [blader/humanizer](https://github.com/blader/humanizer), which this project adapts. The rest of this README is in Hungarian.

Az agenttel íratott magyar dokumentumon látszik, hogy gép írta: erőltetett hármasok, "kerül" passzív, felfújt jelzők, gondolatjel minden tagmondat között, tegezés és magázás váltakozva. A Humanizer-hu ezt a réteget cseréli le. 26 mintát ad hat csoportban, és egy dokumentumszintű döntéssort, ami az első mondat előtt lefut. A szerkezetet továbbra is a hívó feladat adja (user story, specifikáció, ADR, jegy, dokumentáció, ügyfélszöveg), a skill a nyelvet adja hozzá. A minták magyar példákon állnak, magyar nyelvtani háttérrel, és kettőnek angolul nincs is értelme: a tükörfordításnak és a megszólításnak.

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

Gép-gép kimenetre (JSON, log, séma, parancs, strukturált adat) ne használd. Angol szövegre sem: arra az eredeti [blader/humanizer](https://github.com/blader/humanizer) való.

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

Gépi kör, LLM nélkül:

```bash
python3 scripts/lint-hu.py FÁJL.md
```

A kerülendő kifejezéseket a `SKILL.md` `Kerüld` soraiból olvassa ki, tehát a mintákkal együtt frissül. Két szintet ad: a BIZTOS találat szabálysértés a darabszámtól függetlenül, a gyanús emberi döntést kér. Az idézetblokkot és a táblázatsort kihagyja, mert a "Mit hagyj békén" szakasz szerint az idézet nem számít.

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

- 2.4.3 - Szóhasználat. Az "ügynök" helyett "agent": a szakma így hívja, az ügynök magyarul mást jelent, és a 10. minta szabálya épp az ilyen szakszavakat hagyja angolul. Az "agent" be is került a 10. minta szakszólistájába. A "Regiszter" helyett "Megszólítás", mert IT-környezetben a regiszter processzorregisztert jelent, és a repo nem nyelvészeknek szól; a skill amúgy is megszólításként magyarázta. A "szólista" helyett "szójegyzék", mert a szólista magyarul szólóénekest is jelent, és a Kerüld sorok nagy része nem szó, hanem kifejezés. A forrás skill kevésbé hangsúlyos: a bevezetőből kikerült, a licencben és a Források szakaszban marad, mert ott kötelező. Az "Eredet és eltérések" pontosabb lett: az eredetiből a számozás és a minták témája maradt, a tartalom magyar.
- 2.4.2 - A README újraírva, a skill saját szabályaival. A szerkezetet és a formai követelményeket a feladat adta, a fogalmazást a SKILL.md; ez a projekt valódi használati esete. A Példa a telepítés elé került, mert a "kell-e ez nekem" kérdésre a rossz és a jó változat egymás mellett válaszol a leggyorsabban. A "Mit ad hozzá a magyar verzió" és az "Eredet" szakasz egybeolvadt, mert erősen fedték egymást. A tipográfiai karakterek inline kódba kerültek, amit a "Mit hagyj békén" kivesz a hatály alól. A csere egy valódi hibát is javított: a régi README keverte a tegezést és a magázást ("telepítheti" a tegező szövegben), ami a 26. minta megsértése volt a saját dokumentációnkban. A verziótörténet, a telepítési parancsok, a linkek és a mintaszámozás változatlanul átkerültek.
- 2.4.1 - Az új lint első valódi találata a saját fájlon: a "Miért hangzik így az AI-szöveg" szakasz hat felsoroláspontja félkövér címkével állt. A félkövér itt nem csinált semmit, mert a címke amúgy is a sor elején áll, ponttal lezárva. Kiesett, a lista és a hat csoportnévre mutató leképezés megmaradt. A SKILL.md-ben ezzel nincs BIZTOS szintű lint-találat.
- 2.4.0 - Ellenőrző mód, két szinten. A `scripts/lint-hu.py` magyar szöveget ellenőriz a minták ellen LLM nélkül, és a kerülendő kifejezéseket a SKILL.md Kerüld soraiból olvassa ki, hogy a kettő ne csússzon szét. Két szintet ad: a BIZTOS találat szabálysértés a darabszámtól függetlenül, a gyanús emberi döntést kér, mert a 12. minta saját szövege mondja ki, hogy egy szó egyszeri előfordulása még nem gépiesség. Az idézetblokkot és a táblázatsort kihagyja, a "Mit hagyj békén" szakasz alapján. A `commands/ellenoriz.md` a plugin parancsa: előbb a scriptet futtatja, majd azt nézi át, amihez ítélet kell. Mindkettő jelentést ad, egyik sem ír át semmit; a javításról a felhasználó dönt. A SKILL.md nem változott: az ellenőrzés hívó feladat, nem a skill dolga.
- 2.3.0 - Az éles próba hét javítása. A szépirodalmi kivétel kiterjedt a példa- és mintadokumentumra: ha a feladat kitalált tartalmat kér, a kitalált érték a munka része, de maradjon felismerhetően példa. A 8. minta engedi a szóközös nagykötőjelet ott, ahol a felsorolásban tényleg elválasztó kell és a kettőspont foglalt (idővonal, változásnapló). A Regiszter alszakasz negyedik formaként felveszi a szerkesztői T/1-et, amire a 26. minta eddig is hivatkozott. A Részletesség alszakasz megmondja, mi a teendő, ha nincs kit kérdezni: hagyd el a mondatot vagy nevezd meg, mi hiányzik, de tartalmatlan mondatot ne írj. A 11. minta tiltása kimondottan igéből képzett főnévre vonatkozik, a lexikális "kerül" nem ide tartozik. A 19. minta engedi a fejblokk mezőcímkéit. A 21. minta kivételt ad publikálandó ügyfélszövegre, ahol a magyar idézőjel marad. A kísérő fájlok is átnézve: a marketplace-leírás a 2.0.0 előtti pozicionálást őrizte (átírás generálás helyett), az agents/openai.yaml a "próza" szót, a SKILL.md és a README pedig a "jellista" maradványt a korábbi "jel" terminusból.
- 2.2.0 - A nyitott kérdések lezárása. Új dokumentumszintű alszakasz: Részletesség. A 11., 14. és 17. minta alapértelmezés, de a hívó feladat és a dokumentum fajtája felülírja; a fék a 23. mintából jön, vagyis általánosítani szabad, kitalálni nem. A nyitó bekezdés precedencia-mondata is kiterjedt a részletességi szintre, eddig csak formára vonatkozott. Szócserék: a "rovat" helyett "szakasz", mert az űrlap- és újságnyelv; a "próza" helyett "folyó szöveg" ott, ahol felsorolással áll szemben, és "szöveg" ott, ahol egyszerűen szöveget jelent. A mintaválaszok átvizsgálva a többi szabály ellen: a 8. minta példájában a címsor és a szöveg nem ugyanarról szólt, a 17. mintaválaszában a "skálázódik" elrejtette a cselekvőt. A "jó eséllyel" nem került a 9. mintába, a cím végi pont nem került a 20-ba, mert az nem helyesírási szabály, hanem szerkesztési konvenció.
- 2.1.0 - Mind a 26 minta végigjárva magyar szempontból. A "Figyeld" címke helyett "Kerüld", mert a skill ír, nem felismer; ugyanezért a "jel" helyett "gépiesség". A szabályokból kikerült minden konkrét dokumentumtípus, azokat csak a description tartja meg. Az életrajzi és enciklopédiás példaanyag helyére műszaki dokumentum lépett. A magyar-specifikus minták nyelvtani alapot kaptak: kizáró ellentét (1), halmozás (6), pro-drop és topikfolytonosság (7), -hat/-het és episztemikus modalitás (9), fordításnyelv és birtokos szórend (10), terpeszkedő szerkezet (11), alanyazonosság és igenévképző (15). Két tárgyi hiba javítva: a minden szót nagybetűző cím nem ismeretlen a magyarban, csak az állandó címekre áll (20), és a magyar idézőjelpár rosszul volt írva (21). A 21. minta megkapta a hiányzó "Ne írd" és "Így írd" párost, ami eddig egyedül nála hiányzott. Új fájl: docs/nyelveszeti-forrasok.md a hivatkozásokkal.
- 2.0.0 - A skill generálásra való, nem átírásra: a hívó feladat adja a szerkezetet, ez a nyelvet, és a kimenet a kész szöveg. Új dokumentumszintű réteg (hosszúság, próza vagy felsorolás, alcímek, zárójel, regiszter, hang) és persona. A négylépéses átíró folyamat helyére egy hétpontos ellenőrző kör lép, az "Előtte/Utána" példák helyére "Ne írd/Így írd". A 8. minta már csak a hosszú gondolatjelet tiltja feltétel nélkül, a 21. tipográfiai szabállyá vált, a 19. abszolút: nincs félkövér kiemelés. Megszűnt a regiszter- és szakszó-szabály kettőzése, és az "önmagában gyenge" küszöb, aminek generálásnál nincs értelme. Mind a 26 minta megmaradt.
- 1.1.0 - A skill új szöveg megírására is szolgál, nem csak átírásra: a description és a nyitó bekezdés mindkét módot egyenrangúan nevezi meg. A description teljesen magyar, trigger-kifejezésekkel ("humanizáld", "írd meg emberi hangon"), hajtogatott YAML blokkban.
- 1.0.0 - Első kiadás. A blader/humanizer 3.0.0 magyar adaptációja: 26 minta hat csoportban, magyar példákkal. Új 10. minta (anglicizmusok és tükörfordítások), kibővített 11. minta ("kerül" passzív), új 26. minta (tegezés és magázás keveredése). Munkahelyi szöveg mint alapértelmezett hang, regiszterszabály, szakzsargon-kivétel, kötőjeles és egyenes idézőjeles tipográfia.

## Licenc

MIT. Az eredeti szerzői jog Siqi Chené (blader/humanizer), a magyar adaptációé Oroszi Györgyé. Részletek a LICENSE fájlban.
