# Humanizer-hu

Humanizer-hu is a Hungarian writing-style skill for agents: it supplies the prose rules for generating Hungarian documents that do not read as AI-written, while the calling task supplies the structure. It handles Hungarian only; for English use [blader/humanizer](https://github.com/blader/humanizer), which this project adapts. The rest of this README is in Hungarian.

A Humanizer-hu a magyar próza megfogalmazási szabályait adja szöveg generálásához. Nem sablon és nem folyamat: a szerkezetet a hívó feladat adja (user story, specifikáció, ADR, jegy, dokumentáció, ügyfélszöveg), ez a skill a nyelvet. Egyetlen Markdown fájl, ezért minden skilleket támogató ügynökkel működik. A [blader/humanizer](https://github.com/blader/humanizer) 3.0.0-s változatából indult, a magyar nyelvhez igazított mintákkal és egy dokumentumszintű réteggel, ami az eredetiben nincs.

## Telepítés

A Skills CLI-vel:

```bash
npx skills add Dexxter182/humanizer-hu --global
```

A `--global` nélkül csak az aktuális projektbe települ. A `--agent <n>` vagy `--agent '*'` kapcsolóval választható, melyik ügynök kapja meg; utána töltsd újra a skilleket. A skill a `/humanizer-hu` parancsra hallgat.

Claude Code 2.1.142 vagy újabb pluginként is telepítheti:

```text
/plugin marketplace add Dexxter182/humanizer-hu
/plugin install humanizer-hu@humanizer-hu
```

A plugin a `/humanizer-hu:humanizer-hu` parancsra hallgat.

Claude Desktopban töltsd le a repót ZIP-ként, és töltsd fel skillként. Kézi telepítéshez másold a `SKILL.md`-t az ügynök skill mappájába.

## Használat

A tipikus hívás egy generáló feladat mellé teszi:

```
Írj egy ADR-t a fizetési szolgáltató cseréjéről, és használd hozzá a humanizer-hu skillt.
```

Az ADR adja a rovatokat és a szerkezetet, a Humanizer-hu a nyelvet. Ugyanígy működik user storyval, specifikációval, jeggyel, dokumentációval és ügyfélnek szóló szöveggel. A kimenet a kész dokumentum, vázlat és jellista nélkül.

Ha a már legenerált szövegen iterálsz, ugyanazok a szabályok érvényesek rá:

```
A második rovat túl hosszú, írd rövidebbre, a humanizer-hu szabályai szerint.
```

Gép-gép kimenetre (JSON, log, séma, parancs, strukturált adat) ne használd.

### Hangillesztés

Ha azt szeretnéd, hogy a szöveg rád hasonlítson, adj írásmintát:

```
Itt egy minta a saját írásomból:
[2-3 bekezdés a saját szövegedből]

Írj ebben a hangban egy összefoglalót a sprint eredményéről, humanizer-hu szabályokkal.
```

A skill a minta ritmusát, szóválasztását, írásjeleit és szándékos furcsaságait követi, és a minta felülírja a skill saját tipográfiai szabályait.

## Mit ad hozzá a magyar verzió

- Csak magyar szöveget kezel. Ha angolt kap, jelzi, és az eredeti humanizert ajánlja.
- Dokumentumszintű réteg: hosszúság, próza vagy felsorolás, alcímek, zárójel, regiszter, hang. Ezek a döntések az első mondat előtt születnek, és az eredeti skillben nincsenek benne.
- Persona: tapasztalt magyar elemző, aki emberi olvasónak ír dokumentációt. Nem chatbot és nem hivatalnok.
- Regiszter: egy szövegben egy forma. A dokumentum fajtája dönt: a belső, szakmai olvasónak szóló szöveg személytelen, az ügyfélnek szóló önöz.
- Az angol szakzsargon (sprint, backlog, deploy, ticket, endpoint) marad angolul, és nem kap zárójeles magyar fordítást. A tükörfordítás-minta csak a szerkezetet nézi.
- Gondolatjel: hosszú gondolatjel (—) nincs a szövegben. A nagykötőjel (–) szabályos magyar írásjel: a közbevetésben álló cserélődik, a számintervallum és a kötőjeles tulajdonnév marad.
- Idézőjel: egyenes idézőjel ("...") áll a szövegben; a magyar „...” és az angol “...” egyaránt cserélődik.
- A 10. minta az eredetiben a kötőjeles angol szópárokról szólt, aminek magyarban nincs értelme. A helyén az anglicizmusok és tükörfordítások állnak.
- A 11. minta (passzív) kibővült a magyar "kerül" és "történik" passzívpótlóval és a láncolt főnevesítéssel.
- Új 26. minta: a tegezés és magázás keveredése.
- A 12. minta szólistája megfigyelésen alapul, nem korpuszon. Ez a repo élő része: ha egy szó hiányzik vagy fölösleges, nyiss issue-t.

## Dokumentumszintű döntések

| Döntés | Szabály |
| --- | --- |
| Hosszúság | Annyit, amennyit a feladat kér. Nincs bevezető és nincs záró gondolat. |
| Próza vagy felsorolás | Összefüggő gondolat bekezdésbe. Felsorolás csak tételes tartalomhoz. |
| Alcímek | Csak ha az olvasó ugrani akar. A sablon rovatai a címsorok. |
| Zárójel | Csak új információ. Nincs zárójeles fordítás és nincs magyarázat az egyértelműhöz. |
| Regiszter | Egy forma végig. A dokumentum fajtája dönt. |
| Hang | Semleges és szakmai, váltakozó mondathosszal. Az írásminta felülír. |

## A 26 minta

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
| 7 | Ismétlődő mondatkezdés | "A rendszer... A rendszer... A rendszer..." | Vond össze, vagy cseréld az alanyt |
| 8 | Gondolatjel mint kötőelem | "## Teljesítmény — mit mértünk" | Kettőspont a címben; pont, vessző, zárójel a mondatban |
| 9 | Halmozott bizonytalanítás | "esetleg akár talán" | "lehet" |
| 10 | Anglicizmusok és tükörfordítások | "Ez egy jelentős kihívás", "navigálni a kihívások között" | Magyar szerkezet, a szakszó marad |
| 11 | Passzív és elrejtett cselekvő | "betöltésre kerülnek", "a mentés automatikusan történik" | Nevezd meg, ki mit csinál |

### C. Felfújás

| # | Minta | Ne írd | Így írd |
| --- | --- | --- | --- |
| 12 | Túlhasznált AI-szavak | "átfogó, robusztus, zökkenőmentes, kulcsfontosságú" | Köznapi szó vagy konkrétum |
| 13 | Felfújt jelentőség | "mérföldkövet jelentett", "a jövő fényes" | A tény, zárás az utolsó konkrétummal |
| 14 | Homályos kapcsolat | "a csapathoz kötődik" | Nevezd meg a viszonyt, ha a forrás adja |
| 15 | Felületes határozói igenevek | "biztosítva a megbízható kézbesítést" | Csak amit a forrás alátámaszt |
| 16 | Reklámnyelv | "az új irányítópult intuitív, letisztult felületen" | Mondd meg, mi a dolog |
| 17 | Kölcsönzött tekintély | "a best practice szerint", "a Netflix is így csinálja" | Valódi forrás, vagy hagyd el |
| 18 | A létige kerülése | "felületeként szolgál", "nézettel rendelkezik" | Mi micsoda, és minek mije van |

### D. Formázás

| # | Minta | Ne írd | Így írd |
| --- | --- | --- | --- |
| 19 | Félkövér mint dekoráció | "**jelentősen** javítja", "**Teljesítmény:** A teljesítmény javult" | Kiemelés nélkül, prózában |
| 20 | Dekoratív címsorok | "Migrációs Terv És Visszaállítás", emoji, nyíl, vonal | Mondatkezdő nagybetű, dísz nélkül |
| 21 | Tipográfiai idézőjelek | „a projekt”, “a projekt” | "a projekt" |

### E. Maradványok

| # | Minta | Ne írd | Így írd |
| --- | --- | --- | --- |
| 22 | Chatbot-maradvány | "Remélem, segítettem! Szólj, ha..." | Tartalommal kezdj, ténnyel zárj |
| 23 | Tudáskorlát és találgatás | "feltehetően a config.yaml-ban beállított korlát" | Mondd meg, mi ismert, vagy hagyd el |
| 24 | Címsor megismételve | "## Hibakezelés" + "A hibakezelés fontos része a rendszernek." | Hagyd a címsort dolgozni |
| 25 | Az előző verzióról írni | "a korábbi megközelítést váltja ki" | Írd le, mit csinál most |

### F. Regiszter

| # | Minta | Ne írd | Így írd |
| --- | --- | --- | --- |
| 26 | Tegezés és magázás keveredése | "Kattints a gombra... indítsa újra a böngészőt" | Egy forma végig |

## Példa

Ügyfélnek szóló funkcióleírás egy parkolási alkalmazás új funkciójáról. A neveket, számokat és a menü helyét a kérés adja; ami nincs benne, azt a skill nem találja ki, hanem megkérdezi.

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

## Eredet

A 26 minta számozása a [blader/humanizer](https://github.com/blader/humanizer) 3.0.0-s változatát követi, mert onnan indult a lista.

- 1-9: azonos az eredetivel, magyar példákkal és szólistákkal.
- 10: az eredeti "kötőjeles szópárok" helyett "anglicizmusok és tükörfordítások".
- 11: az eredeti "passzív és hiányzó alany", kibővítve a "kerül" és "történik" passzívpótlóval és a láncolt főnevesítéssel.
- 12-25: azonos az eredetivel, magyar példákkal és szólistákkal. A 8. és a 21. minta szabálya a magyar tipográfiához igazodik.
- 26: új, csak a magyar verzióban.

A 2.0.0 óta a két projekt célja eltér: az eredeti meglévő szöveget ír át, a Humanizer-hu generáláshoz ad szabályokat, és a dokumentumszintű rétegnek nincs upstream megfelelője. Az upstream továbbra is hasznos bemenet egy új mintához, de a fájl szerkezete már nem tükrözi.

## Források

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) a mintalista forrása, a [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) gondozza.
- [blader/humanizer](https://github.com/blader/humanizer) az eredeti skill, amelyből ez a projekt indult.
- A magyar nyelvi megfigyelések (10, 11, 26), a 12. minta szólistája és a dokumentumszintű döntések megfigyelésen alapulnak, nem kurált korpuszon.

## Verziótörténet

- 2.1.0 - Mind a 26 minta végigjárva magyar szempontból. A "Figyeld" címke helyett "Kerüld", mert a skill ír, nem felismer; ugyanezért a "jel" helyett "gépiesség". A szabályokból kikerült minden konkrét dokumentumtípus, azokat csak a description tartja meg. Az életrajzi és enciklopédiás példaanyag helyére műszaki dokumentum lépett. A magyar-specifikus minták nyelvtani alapot kaptak: kizáró ellentét (1), halmozás (6), pro-drop és topikfolytonosság (7), -hat/-het és episztemikus modalitás (9), fordításnyelv és birtokos szórend (10), terpeszkedő szerkezet (11), alanyazonosság és igenévképző (15). Két tárgyi hiba javítva: a minden szót nagybetűző cím nem ismeretlen a magyarban, csak az állandó címekre áll (20), és a magyar idézőjelpár rosszul volt írva (21). A 21. minta megkapta a hiányzó "Ne írd" és "Így írd" párost, ami eddig egyedül nála hiányzott. Új fájl: docs/nyelveszeti-forrasok.md a hivatkozásokkal.
- 2.0.0 - A skill generálásra való, nem átírásra: a hívó feladat adja a szerkezetet, ez a nyelvet, és a kimenet a kész szöveg. Új dokumentumszintű réteg (hosszúság, próza vagy felsorolás, alcímek, zárójel, regiszter, hang) és persona. A négylépéses átíró folyamat helyére egy hétpontos ellenőrző kör lép, az "Előtte/Utána" példák helyére "Ne írd/Így írd". A 8. minta már csak a hosszú gondolatjelet tiltja feltétel nélkül, a 21. tipográfiai szabállyá vált, a 19. abszolút: nincs félkövér kiemelés. Megszűnt a regiszter- és szakszó-szabály kettőzése, és az "önmagában gyenge" küszöb, aminek generálásnál nincs értelme. Mind a 26 minta megmaradt.
- 1.1.0 - A skill új szöveg megírására is szolgál, nem csak átírásra: a description és a nyitó bekezdés mindkét módot egyenrangúan nevezi meg. A description teljesen magyar, trigger-kifejezésekkel ("humanizáld", "írd meg emberi hangon"), hajtogatott YAML blokkban.
- 1.0.0 - Első kiadás. A blader/humanizer 3.0.0 magyar adaptációja: 26 minta hat csoportban, magyar példákkal. Új 10. minta (anglicizmusok és tükörfordítások), kibővített 11. minta ("kerül" passzív), új 26. minta (tegezés és magázás keveredése). Munkahelyi szöveg mint alapértelmezett hang, regiszterszabály, szakzsargon-kivétel, kötőjeles és egyenes idézőjeles tipográfia.

## Licenc

MIT. Az eredeti szerzői jog Siqi Chené (blader/humanizer), a magyar adaptációé Oroszi Györgyé. Részletek a LICENSE fájlban.
