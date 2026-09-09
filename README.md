# Humanizer-hu

Humanizer-hu is the Hungarian adaptation of [blader/humanizer](https://github.com/blader/humanizer): an agent skill that rewrites AI-sounding Hungarian text so it reads like the writer wrote it, without changing what it says. It handles Hungarian text only; for English use the original. The rest of this README is in Hungarian.

A Humanizer-hu az AI-jellegű magyar szöveget írja át úgy, hogy az író hangján szóljon, és a tartalma ne változzon. Egyetlen Markdown fájl, ezért minden skilleket támogató ügynökkel működik. A [blader/humanizer](https://github.com/blader/humanizer) 3.0.0-s változatának magyar adaptációja: az eredeti 25 mintából 24 marad, egy cserélődik, egy új magyar minta jön hozzá, és a minták példái, szólistái és szabályai a magyar nyelvhez igazodnak.

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

Hívd közvetlenül:

```
/humanizer-hu

[ide jön a szöveg]
```

Vagy kérd szabadon:

```
Humanizáld ezt a szöveget: [szöveg]
```

Fájl átírásához add meg az útvonalát:

```
Humanizáld a prózát a docs/kiadasi-jegyzet.md fájlban
```

Ha csak a végeredmény kell, mondd meg, és a skill a vázlat és a jellista nélkül, egyben adja vissza.

### Hangillesztés

Ha azt szeretnéd, hogy az átírás rád hasonlítson, adj mintát:

```
/humanizer-hu

Itt egy minta a saját írásomból a hangillesztéshez:
[2-3 bekezdés a saját szövegedből]

Most humanizáld ezt:
[az AI-szöveg]
```

A skill a minta ritmusát, szóválasztását, írásjeleit és szándékos furcsaságait követi.

## Miben más a magyar verzió

- Csak magyar szöveget kezel. Ha angolt kap, jelzi, és az eredeti humanizert ajánlja.
- Az alapértelmezett hang a munkahelyi szöveg: specifikáció, dokumentáció, jegy, e-mail, ügyfélanyag. Semleges és szakmai, nem chatbot és nem hivatalnok. A személyes hangot írásmintával lehet behozni.
- Regiszter: a forrás domináns formáját tartja (tegezés, magázás, személytelen). Döntetlennél dokumentációban személytelen, ügyfélnek szóló szövegben önözés.
- Az angol szakzsargon (sprint, backlog, deploy, ticket) marad. A tükörfordítás-minta csak a szerkezetet nézi.
- Gondolatjel: a végleges szövegben nem marad hosszú gondolatjel (—) és nagykötőjel (–). Ahol közbevetés kell, szóközös kötőjel ( - ), de a pont, vessző, kettőspont és zárójel az elsődleges.
- Idézőjel: a végleges szövegben egyenes idézőjel ("...") áll; a magyar „...” és az angol “...” egyaránt cserélődik.
- A 10. minta az eredetiben a kötőjeles angol szópárokról szólt, aminek magyarban nincs értelme. A helyén az anglicizmusok és tükörfordítások állnak.
- A 11. minta (passzív) kibővült a magyar "kerül" és "történik" passzívpótlóval és a láncolt főnevesítéssel.
- Új 26. minta: a tegezés és magázás keveredése.
- A 12. minta szólistája megfigyelésen alapul, nem korpuszon. Ez a repo élő része: ha egy szó hiányzik vagy fölösleges, nyiss issue-t.

## A 26 minta

### A. Színpadiasság a kijelentés helyett

| # | Minta | Előtte | Utána |
| --- | --- | --- | --- |
| 1 | Nem X, hanem Y | "Nem csupán technikai módosítás, hanem a teljes ügyfélélmény újragondolása" | Mondd ki a lényeget |
| 2 | Egysoros zárások és töredékek | "Nem volt előfeltevése. Nem volt kedvence. Ennyi." | Természetes mondathossz, konkrét állítás |
| 3 | Mélynek hangzó szólamok | "A következetesség a bizalom nyelve" | A konkrét állítás |
| 4 | Felvezetés a lényeg előtt | "Nézzük meg közelebbről", "Őszintén?" | Kezdd a tartalommal |
| 5 | Vita senkivel | "Csábító megoldás lenne..., de" | Vedd ki a hamis alternatívát, tartsd a valódit |

### B. Ritmus szabály szerint és angolból fordítva

| # | Minta | Előtte | Utána |
| --- | --- | --- | --- |
| 6 | Erőltetett hármasok | "innováció, inspiráció és betekintés" | Annyi elem, amennyit a jelentés kér |
| 7 | Ismétlődő mondatkezdés | "A rendszer... A rendszer... A rendszer..." | Vond össze, vagy cseréld az alanyt |
| 8 | Gondolatjel mint kötőelem | "a szabályzat — amit bejelentettek — érinti" | Pont, vessző, kettőspont, zárójel |
| 9 | Halmozott bizonytalanítás | "esetleg akár talán" | "lehet" |
| 10 | Anglicizmusok és tükörfordítások | "Ez egy jelentős kihívás", "-ra fókuszál" | Magyar szerkezet, a szakszó marad |
| 11 | Passzív és hiányzó alany | "betöltésre kerülnek", "a mentés automatikusan történik" | Nevezd meg, ki mit csinál |

### C. Felfújás és kölcsönzött tekintély

| # | Minta | Előtte | Utána |
| --- | --- | --- | --- |
| 12 | Túlhasznált AI-szavak | "átfogó, robusztus, zökkenőmentes, kulcsfontosságú" | Köznapi szavak |
| 13 | Felfújt jelentőség | "mérföldkövet jelentett", "a jövő fényes" | Tartsd a tényt, zárj az utolsó konkrétummal |
| 14 | Homályos kapcsolat | "a csapathoz kötődik" | Nevezd meg a viszonyt, ha a forrás adja |
| 15 | Felületes -va/-ve farkak | "ezzel is hangsúlyozva az elkötelezettséget" | Csak amit a forrás alátámaszt |
| 16 | Reklámnyelv | "a cég szívében megbújó, elismert csapat" | Mondd meg, mi a dolog |
| 17 | Kölcsönzött tekintély | "szakértők szerint", "idézte a Portfolio, a HVG, a Forbes és az Index" | Valódi forrás, vagy húzd ki |
| 18 | A létige kerülése | "felületeként szolgál", "nézettel rendelkezik" | "X az Y", "X-nek Y-ja van" |

### D. Formázás szabály szerint

| # | Minta | Előtte | Utána |
| --- | --- | --- | --- |
| 19 | Félkövér mint dekoráció | "**Teljesítmény:** A teljesítmény javult" | Próza, ha a lista nem ad hozzá |
| 20 | Dekoratív címsorok | "Stratégiai Tárgyalások És Partnerségek", emoji, nyíl | Mondatkezdő nagybetű, díszítés nélkül |
| 21 | Tipográfiai idézőjelek | „a projekt”, “a projekt” | "a projekt" |

### E. Maradványok a chatből és a vázlatból

| # | Minta | Előtte | Utána |
| --- | --- | --- | --- |
| 22 | Chatbot-maradvány | "Remélem, segítettem! Szólj, ha..." | Vedd ki |
| 23 | Tudáskorlát és találgatás | "az elérhető forrásokban korlátozottan dokumentált... valószínűleg" | Mondd meg, mi ismert, vagy húzd ki |
| 24 | Címsor megismételve | "## Teljesítmény" + "A sebesség számít." | Hagyd a címsort dolgozni |
| 25 | Az előző verzióról írni | "Ez a függvény a korábbi megközelítést váltja ki" | Írd le, mit csinál most |

### F. Regiszter

| # | Minta | Előtte | Utána |
| --- | --- | --- | --- |
| 26 | Tegezés és magázás keveredése | "Kattints a gombra... indítsa újra a böngészőt" | Egy forma végig |

## Teljes példa

Ügyfélnek szóló funkcióleírás egy parkolási alkalmazás új funkciójáról. A neveket, számokat és a menü helyét a forrás adja; ami nincs benne, azt a skill nem találja ki, hanem megkérdezi.

Előtte (AI-jellegű):

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

Utána:

> Az alkalmazásban megjelent a Kedvencek funkció. A gyakran használt parkolási zónákat egy érintéssel el lehet menteni, és a következő parkolást már a mentett zónából lehet indítani, keresés nélkül. A rendszer a mentett zónánál is ellenőrzi az érvényességet.
>
> A Kedvencek a Beállítások menüből érhető el, legfeljebb tíz zóna tárolható benne. Kérdés esetén keresse az ügyfélszolgálatot.

## Leképezés az eredetire

Az eredeti 3.0.0 számozását tartjuk, hogy egy későbbi upstream változás könnyen átvezethető legyen.

- 1-9: azonos az eredetivel, magyar példákkal és szólistákkal.
- 10: az eredeti "kötőjeles szópárok" helyett "anglicizmusok és tükörfordítások".
- 11: az eredeti "passzív és hiányzó alany", kibővítve a "kerül" és "történik" passzívpótlóval és a láncolt főnevesítéssel.
- 12-25: azonos az eredetivel, magyar példákkal és szólistákkal. A 8 és a 21 szabálya a magyar verzió tipográfiai döntéseihez igazodik.
- 26: új, csak a magyar verzióban.

## Források

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) a mintalista forrása, a [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) gondozza.
- [blader/humanizer](https://github.com/blader/humanizer) az eredeti skill, amelynek ez a magyar adaptációja.
- A magyar nyelvi jelek (10, 11, 26) és a 12. minta szólistája megfigyelésen alapulnak, nem kurált korpuszon.

## Verziótörténet

- 1.1.0 - A skill új szöveg megírására is szolgál, nem csak átírásra: a description és a nyitó bekezdés mindkét módot egyenrangúan nevezi meg. A description teljesen magyar, trigger-kifejezésekkel ("humanizáld", "írd meg emberi hangon"), hajtogatott YAML blokkban.
- 1.0.0 - Első kiadás. A blader/humanizer 3.0.0 magyar adaptációja: 26 minta hat csoportban, magyar példákkal. Új 10. minta (anglicizmusok és tükörfordítások), kibővített 11. minta ("kerül" passzív), új 26. minta (tegezés és magázás keveredése). Munkahelyi szöveg mint alapértelmezett hang, regiszterszabály, szakzsargon-kivétel, kötőjeles és egyenes idézőjeles tipográfia.

## Licenc

MIT. Az eredeti szerzői jog Siqi Chené (blader/humanizer), a magyar adaptációé Oroszi Györgyé. Részletek a LICENSE fájlban.
