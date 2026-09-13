# Próba-prompt

Ezt a promptot **friss sessionben** kell lefuttatni. Egy olyan session, amelyik
maga dolgozta át a skillt, nem alkalmas a próbára: ismeri a szabályokat, és
akaratlanul is betartja őket akkor is, amikor a skill nincs betöltve.

A prompt szándékosan nem mondja meg, mit kellene találni. Mindkét irányban
kérdez: mit nem fogott meg a skill, és hol korrigált túl.

---

A `/Users/gyorgy.oroszi/Claude/Projects/humanizer-hu` projektben van egy magyar
írásstílus-skill (`SKILL.md`). Frissen dolgoztuk át, és éles próbára van
szükség. Te vagy a próba, ezért ne kezdd a skill elemzésével: úgy használd,
ahogy egy hívó feladat használná.

**Első lépés, a skill nélkül.** Írd meg az alábbi négy rövid magyar szöveget.
A munkafájlokat a scratchpadbe tedd, ne a repóba.

1. User story egy jelszó-visszaállítási funkcióhoz, elfogadási feltételekkel.
2. ADR arról, hogy a csapat a saját e-mail-küldés helyett külső szolgáltatóra
   vált.
3. Végfelhasználóknak szóló release note egy keresőfejlesztésről, magázva.
4. Incidensleírás egy éjszakai adatbázis-túlterhelésről, ahol az ok még nem
   biztos.

**Második lépés.** Töltsd be a skillt, és írd meg ugyanezt a négyet újra.

**Harmadik lépés, értékelés.** Vesd össze a két készletet, és válaszolj:

- Mit változtatott a skill? Hol lett jobb a szöveg, és hol nem változott semmi?
- A 26 minta közül melyiket szegi meg a skillel készült szöveg is?
- Túlkorrigált-e valahol? Van-e olyan mondat, ami a szabály miatt lett
  mesterkéltebb vagy szegényebb magyar, mint a skill nélküli változat?
- Érthető volt-e minden szabály elolvasásra, vagy volt, amin gondolkodnod
  kellett?

A 4. szöveg azt méri, megmarad-e a sejtés sejtésként (§14, §23). A 3. azt, hogy
a magas szintű, cselekvő nélküli fogalmazás belefér-e (Részletesség alszakasz).

A megállapításokat írd le. A `SKILL.md`-t **ne módosítsd**: a javításokról
külön döntünk.

---

## Éles adat: a repo saját szövege

A fenti prompt kitalált feladatokat ad. A másik próbatípus valódi munkán méri a
skillt: egy friss session újraírja vele a repo egyik saját szövegét (README,
AGENTS.md, a GitHub-leírás), aztán a `scripts/lint-hu.py` és a
`/humanizer-hu:ellenoriz` átnézi az eredményt. Ez szigorúbb próba, mert a
tények adottak, a szerkezetet a meglévő fájl kötelezővé teszi, és a hiba azonnal
látszik a saját dokumentációnkon.

## Mérési napló

Minden mérés ide kerül, verzióval és dátummal, hogy később ne kelljen találgatni,
melyik állapotot mérte utoljára valaki.

### 2026-09-12, 2.2.0, szintetikus próba

A fenti négy szöveg, friss sessionben, skill nélkül és skillel. Hét javítás lett
belőle a 2.3.0-ban. A legmélyebb találat: a skill végig feltételezte, hogy van
forrás, ezért a kitalált példadokumentumot kérő feladattal ellentmondásba
került. A többi hat a §8 nagykötőjelét, a szerkesztői T/1-et, a Részletesség és
a §23 tautológiáját, a §11 lexikális "kerül" alakját, a §19 fejblokkját és a §21
ügyfélszövegét érintette.

### 2026-09-12, 2.4.1, éles adat: a README újraírása

A README újraírása a skill saját szabályaival, a 2.4.2-ben. A hívó feladat adta
a szerkezetet és a kötelező tényeket, a skill a fogalmazást. Egy valódi hibát
talált: a régi README keverte a tegezést és a magázást, ami a §26 megsértése
volt a saját dokumentációnkban, és ugyanaznap a §26 külön tárgyalása sem hozta
elő. Az új fájlon a lint nulla BIZTOS találatot adott.

### 2026-09-13, 2.4.5, éles adat: a GitHub-leírás

A GitHub-leírás generálása a skillel, majd visszaellenőrzés a lint és az
ítéletalapú kör mindkét körével. A lint tiszta volt, az ítéletalapú kör a §11
rejtett cselekvőjét, a §6 hármasát és a §23 alá eső agentlistát fogta meg.

Amit egyik kör sem fogott meg, a felhasználó viszont igen: a "Tényt nem talál
ki: csak azt állítja, amit a forrás tartalmaz." mondat kettőspontja. A két fél
ugyanazt mondja tagadva és állítva, tehát ez a §1 szétosztott ellentéte és a §2
ismétlő zárása egyszerre, de kettősponttal, és erre az alakra egyik minta
szövege sem tér ki. Bemenet a következő átvilágításhoz.

### 2026-09-13, 2.4.5, szintetikus próba

A négy szöveg friss sessionben, skill nélkül és skillel. A lint a skill nélküli
készleten 16 BIZTOS és 13 gyanús találatot adott, a skillesen 6 BIZTOS-t és
nulla gyanúsat, a hat találat viszont mind téves riasztás a §21 ügyfélszöveg-
kivétele miatt. A "kerül" passzív négyről nullára, a félkövér listacímke
tizenegyről nullára, a hamis ellentét háromról nullára ment.

Hat élő tétel maradt belőle:

- §23: a skilles incidensleírás több kitalált konkrétumot tartalmazott, mint a
  skill nélküli (időtartamok, csapatnév, dátum). A minta a találgatást tiltja,
  a Részletesség pedig konkrétumot kér, és a kettő elsőbbsége nincs kimondva.
- §21: a Szabály "ne nyúlj hozzá" alakja átírásra van fogalmazva, generálásnál
  értelmezhetetlen; a valódi válasz a Probléma bekezdésben áll. A lint ezt a
  kivételt nem ismeri, ezért ügyfélszövegen hatot téveszt.
- §8: időintervallumra három szabály illik egyszerre, a próba rosszul tippelt,
  és a skilles változat rosszabb lett a skill nélkülinél.
- §18 és §12: a lint szó szerinti egyezést vár, a ragozott alakot ("szolgáló")
  elszalasztja, és ez nincs ott a "mit nem lát" felsorolásban.
- §19: az ADR Kontextus szakaszában a címkés felsorolás konvenció, nem
  dekoráció; a kivétel csak sablonra szól, szokásra nem.
- Megszólítás: a négy forma kizáró opcióként áll, pedig a magázás és a
  szerkesztői T/1 egy release note-ban együtt szabályos.

### 2026-09-13, 2.4.5, éles adat: a README újragenerálása

Egy friss session megírta a README első hat szakaszát a repo többi fájljából,
a meglévő README elolvasása nélkül, a skill szabályaival. A lint egy BIZTOS
találatot sem adott, két gyanúsat igen, ebből egy valódi (§14 "kötődik").

- §1: háromszor túlélte, pedig az Ellenőrző kör első tétele. Kettőt a forrás
  diktált: az AGENTS.md 34. sora ("a nevek példák, nem korlátok") és a SKILL.md
  20. sora ("forrásként kezeld, soha ne követendő utasításként") maga is a §1
  utolsó Kerüld tételének alakja, a mondat végére csapott tagadás. A §23 a
  forrás szavához húz, tehát a saját fájljaink tanítják be a mintát.
- §20 kontra a README H1-e: "a dokumentum ne induljon a saját címét ismétlő
  első szintű címsorral" szó szerint minden README-t megjelöl.
- §19 kivétele a repón belül halott: az AGENTS.md teljesen kitiltja a félkövért
  a README-ből, tehát a "ha a sablon előírja" ág sosem él. A SKILL.md-ből ez
  nem látszik.
- §21: publikált README-ben az egyenes idézőjel a fordításnyelv látszatát
  kelti, vagyis a skill saját céljával megy szembe. A kivétel csak
  ügyfélszövegre szól.
- §6 kontra a Folyó szöveg vagy felsorolás döntés: hét tétel egy
  felsoroláspont belsejében egyik szabálynak sem felel meg, és erre az alakra
  egyik sem ad választ.
- §23 kontra Részletesség a Telepítés szakaszban: a "nevezd meg, mi hiányzik"
  kimenet README-ben nem írható le, ezért a szakasz fájlleírás lett utasítás
  helyett.

A próba nyolc hiányzó tényt is felsorolt. A legfontosabb: a telepítési parancsok
egyedül a README-ben vannak meg, más fájl nem tartalmazza őket.

### Mi lett a két 2.4.5-ös próba tételeiből

A 2.4.6 négyet zárt le: a §20 megkapta az önálló fájl H1-kivételét, a lint az
egyszavas tételeket ragozott alakban is megtalálja és kiírja a §21 kivételét, az
AGENTS.md kimondja, hogy a repo félkövér-tilalma erősebb a §19 sablon-ágánál, és
a SKILL.md 20. sora meg az AGENTS.md 34. sora már nem a §1 alakjában áll.

Nyitva marad hat tétel, ezek a következő átvilágítás bemenete: a §23 és a
Részletesség elsőbbsége, a §21 idézőjele publikált dokumentációban, a §8 három
dash-szabálya időintervallumra, a §6 kontra Folyó szöveg vagy felsorolás hét
tétel esetén, a §19 ADR-kontextusa, és a Megszólítás négy formájának viszonya
(olvasó megszólítása vagy a szöveg egész személyhasználata).

A 2.4.6 után két új tétel jött a szűz agent próbájából. A §20 friss
H1-kivétele ütközik a §24-gyel: ha a szöveg saját címsort kap, az első
mondat könnyen a cím szavait ismétli. A dátum írásmódjáról pedig nincs
szabály, pedig az ISO alak ragozva ("2026-09-10-én") magyar mondatban
olvashatatlan, a "Mit hagyj békén" viszont csak az azonosítót és az
adatot védi.

### A módszer korlátja

Az eddigi próbák mindegyike kitalált tartalmat kért. A négy szintetikus feladat
nem adott adatot: az incidensleíráshoz nem tartozott időpont, mérés vagy
csapatnév, a user storyhoz nem tartozott lejárati idő. Ezekben a szövegekben a
konkrétum csak kitalált értékből jöhet, tehát a §23 találatait a feladat
alakja is okozhatta; ezt a próba nem különíti el.

Amit ebből mérni lehet: megmarad-e a sejtés sejtésként, egységes-e a
megszólítás, eltűnik-e a "kerül" passzív és a félkövér címke. Amit nem: hűséges
marad-e a skill egy valódi forráshoz, mert forrás eddig nem volt.

A következő próba ezért valódi anyaggal megy: egy meglévő jegy, napló vagy
levelezés a forrás, és a kérdés az, hogy a kész szövegben szerepel-e olyan
tény, ami a forrásban nincs. Amíg ez nem futott le, a §23 és a Részletesség
viszonyáról nincs mérésünk.

---

## Mérés fix forrással

Az eddigi próbák gyengéje, hogy a feladat nem adott forrást, tehát a kitalált
tény nem volt megszámolható. Ez a protokoll ezt zárja ki: minden futás ugyanabból
a forrásdokumentumból dolgozik, és a pontozás egy előre elkészített tényleltárhoz
képest történik.

A forrás és a leltár a repón kívül van, mert munkahelyi anyag, ez a repo pedig
nyilvános. Az útvonaluk a projekt jegyzetében szerepel. A repóba se a forrás, se
a belőle generált szöveg nem kerül be, csak a mérés eredménye.

### Amit a forrásnak tudnia kell

- pontos számok, nevek és leképezések, amiket a kimenetnek vissza kell adnia
- legalább egy kimondott hiány ("egyeztetendő", "később küldik"), ami méri, hogy
  a szöveg kérdez, kihagy, vagy kitalál
- legalább egy eldöntetlen szabály, ami a §14-et teszi próbára
- ha van benne elgépelés vagy önellentmondás, az ingyen kapott hűségpróba: a jó
  kimenet megtartja vagy jelzi, a rossz csendben kijavítja

### A két kimenet

1. User storyk elfogadási feltételekkel a forrás egyetlen, zárt szakaszáról.
   Kötött forma, ezért főleg a mintalistát terheli, és itt a legszigorúbb, hogy
   minden szám a forrásból jön-e.
2. Rövid összefoglaló a megrendelőnek ugyanarról a változásról, körülbelül 1500
   karakter. Folyó szöveg, ezért ez méri a dokumentumszintű réteget: hosszúság,
   bekezdés vagy felsorolás, megszólítás, részletesség.

Együtt nagyjából két képernyő futásonként. Ennél többet ne kérj: háromszor kell
átnézni.

### A három futás

Mindhárom ugyanazt a két kimenetet kéri, ugyanabból a forrásból, friss
sessionben:

- skill nélkül, viszonyítási alapnak
- a teljes skillel
- a karcsúsított skillel, amiből egy script kivette a Probléma sorokat

A harmadik futás dönti el, hogy az indoklás dolgozik-e, vagy csak fogyaszt.

### Pontozás

Futásonként négy szám, mind eldönthető vitatkozás nélkül:

- hány leltári tény szerepel helyesen
- hány leltári tény maradt ki, ami a feladathoz kellett volna
- hány olyan állítás van a szövegben, ami a leltárban nincs; ezen belül külön
  számolva a szám, név, útvonal és érték, mert a §23 ezeket tiltja, az
  általánosítást nem
- hány BIZTOS találat a linten

Ötödikként az ítéletalapú kör mintánkénti találatai jönnek, idézettel.

Az eredmény a fenti mérési naplóba kerül, verzióval és dátummal.

### 2026-09-13, 2.4.6, első mérés fix forrással

Valódi mobilfejlesztési specifikáció a forrás, 38 tényes leltárral. Két kimenet
futásonként: user storyk a specifikáció egyetlen zárt szakaszáról, és egy 1500
karakteres megrendelői összefoglaló az egész változásról. Három futás friss
sessionben.

| Mérés | Skill nélkül | Teljes skill | Karcsú skill |
| --- | --- | --- | --- |
| Leltári tény a szakaszból | 10/10 | 10/10 | 10/10 |
| Kimondott hiány kezelése | jelezte | jelezte | jelezte |
| Kitalált szám, név vagy útvonal | 0 | 0 | 0 |
| Lint BIZTOS | 4, mind téves | 0 | 0 |
| Lint gyanús | 1 | 0 | 1 |
| Ítéletalapú találat | 0 | 0 | 1 (§26) |
| Story darabszám | 7 | 4 | 3 |
| Összes karakter | 5882 | 5050 | 4527 |

A tényhűség mindhárom futásban teljes. Ezen a feladaton a skillnek nincs mit
javítania ezen a téren: a forrás pontos, a feladat kötött formájú, és a
viszonyítási alap sem talált ki semmit. A §23 méréséhez olyan feladat kell,
ahol a kért dokumentum többet kívánna, mint amennyit a forrás ad.

Három különbség maradt:

- A karcsú futás keverte a személytelen fogalmazást a szerkesztői T/1-gyel
  ("Három ponthoz kérünk döntést"), a teljes futás ugyanezt személytelenül írta
  ("Néhány részlet még egyeztetésre vár"), és a jelentésében külön kiírta, hogy
  emiatt kerülte a T/1-et. A §26 Kerüld sora mindkét változatban benne van, a
  keveredés magyarázata viszont csak a teljesben. Egy adatpont amellett, hogy a
  Probléma bekezdés dolgozik. (Ezt a megismételt mérés megcáfolta, lásd a
  következő bejegyzést.)
- A forrás önellentmondását (a parkolási kategória két különböző neve) a skill
  nélküli és a karcsú futás csendben feloldotta az egyik alak választásával. A
  teljes futás általánosított ("külön kategóriával megy a zónalekérdezésbe"),
  ezért nem kellett állást foglalnia egy ellentmondó forrásban.
- Ugyanazt a tíz tényt a skill nélküli futás hét storyba, a teljes négybe, a
  karcsú háromba osztotta. A hosszúságszabály tehát hat, és a Probléma sorok
  nélkül is hat.

Ez a mérés nem dönti el a karcsúsítás kérdését: egy feladat, futásonként egy
minta. Annyit mond, hogy a karcsú változat tényhűségben nem rosszabb, egy
megszólítási szabályt viszont elejtett.

Tokenfogyasztás futásonként, a teljes agent-munkára értve:

| | Skill nélkül | Teljes skill | Karcsú skill |
| --- | --- | --- | --- |
| Token | 68 541 | 97 606 | 84 449 |
| A skill nélkülihez képest | - | +42% | +23% |
| Eszközhívás | 3 | 8 | 6 |
| Futásidő | 40 mp | 107 mp | 62 mp |

Ezek a számok az agent teljes munkáját mérik: a betöltött fájlt, a saját
gondolkodását és az eszközhívásait együtt. A két skillfájl különbsége 9,4 KB,
magyar szövegben nagyjából három-négyezer token, a mért különbség viszont
tizenháromezer. A többlet tehát nem a fájlból jön, hanem abból, hogy a hosszabb
szabálykészlet hosszabb mérlegelést és több visszalapozást hoz. Ez a
karcsúsítás mellett szóló érv, és erősebb, mint a fájlméret.

A lint négy BIZTOS találata mind téves riasztás volt, és új hibát mutat: a
`## US-2 A besorolás...` alakú címsorban az azonosító-előtag után álló névelőt
a script a cím második szavának nézi, és Title Case-t jelez. A számozott
előtagot ismeri, a betűs azonosítót nem.

### 2026-09-13, 2.4.7, a mérés megismételve, kondíciónként három minta

Ugyanaz a forrás, ugyanaz a két kimenet, kondíciónként három futás.

| | Skill nélkül | Teljes skill | Karcsú skill |
| --- | --- | --- | --- |
| Leltári tény | 10/10, 10/10, 10/10 | 10/10, 10/10, 10/10 | 10/10, 10/10, 10/10 |
| Kimondott hiány jelezve | 3/3 | 3/3 | 3/3 |
| Kitalált szám vagy azonosító | 0 | 0 | 0 |
| Lint BIZTOS | 0 | 0 | 0 |
| §12 "valamint" | 3/3 | 1/3 | 1/3 |
| §26 megszólításkeveredés | 0/3 | 1/3 | 1/3 |
| Story darabszám | 7, 6, 5 | 4, 3, 4 | 3, 3, 3 |
| Karakter átlaga | 5094 | 4338 | 4124 |
| Token átlaga | 68 243 | 92 514 | 86 069 |

Négy következtetés.

A tényhűség kilenc futásból kilencszer teljes, kitalált szám és azonosító
sehol. Ez a feladattípus tehát nem méri a §23-at, és nincs értelme tovább
futtatni rajta. A következő mérés olyan kimenetet kérjen, ami többet kíván,
mint amennyit a forrás ad: becslést, ütemezést vagy kockázatelemzést.

A skill mérhető hatása ezen a feladaton a tömörítés és a tagolás. Ugyanazt a
tíz tényt a skill nélküli futások hét, hat és öt storyba osztották, a skillesek
három vagy négy storyba, és a szöveg is rövidebb lett. A karcsú változat
csinálta a legegyöntetűbben, mindhárom futásban három storyval. A
dokumentumszintű réteg tehát dolgozik, és a Probléma sorok nélkül is.

Az első mérés §26-os következtetése téves volt. A megismételt mérésben a
megszólítás egyszer a teljes skillel keveredett és egyszer a karcsúval, a
viszonyítási alapban egyszer sem. Nem a karcsúsítás ejti el a szabályt: a §26 és
a Megszólítás szakasz nem elég egyértelmű ahhoz, hogy bármelyik változat
megbízhatóan betartsa. Új nyitott tétel, és annál súlyosabb, hogy a skill
nélküli futásokban nem fordult elő.

A tokenkülönbség kisebb, mint az egymintás becslés mutatta. A teljes skill 36,
a karcsú 26 százalékkal fogyaszt többet a viszonyítási alapnál, a kettő közötti
különbség 6445 token, vagyis 7,5 százalék. Az első mérés tizenháromezret
mutatott, mert a teljes ág első futása kiugró volt.

Ez a mérés tehát nem zárja le a karcsúsítás kérdését, de szűkíti: a karcsú
változat ezen a feladaton semmit nem veszít, és 7,5 százalékot spórol. Amit nem
mér, az épp a Probléma bekezdések tartalma, vagyis a kivételek. Ahhoz olyan
feladat kell, ami kivételhelyzetbe viszi a szabályokat.

### Nyitott lint-hibák (a félkövér azóta javítva)

Éles kimeneten előjött két szerkezet, amit a script nem lát:

- A sor eleji `**Címke:**` félkövér a §19 első felét sérti, a script viszont
  csak a felsoroláspont élén álló félkövér címkét keresi.
- A `kerül megjelenítésre` fordított szórendű "kerül" passzív. A BIZTOS minta
  csak a `megjelenítésre kerül` sorrendet fogja.

### 2026-09-13, 2.4.7, ugyanez a mérés egy gyengébb modellen

Az Opus-mérés gyengéje, hogy a viszonyítási alap hibátlan volt, tehát a skillnek
nem maradt hely javítani. Ugyanez a forrás és ugyanez a két kimenet lefutott a
kisebb, gyorsabb modellel is, kondíciónként négy futással.

| | Skill nélkül | Teljes skill |
| --- | --- | --- |
| Leltári tény | 5, 7, 7, 4 | 6, 6, 6, 6 |
| Lint BIZTOS | 2 futásban | egyikben sem |
| Reklámnyelv az összefoglalóban | 3 futásban | egyikben sem |
| Karakter átlaga | 5793 | 3448 |
| Token átlaga | 54 112 | 70 308 |

Itt a viszonyítási alap végre hibázik, és a hibák pont azok, amikre a skill
készült. A skill nélküli összefoglalók kitalált tényeket állítanak: az egyik
differenciált díjazásról ír, pedig a forrás díjat sehol nem említ, a másik
"intelligensen optimalizált alapértékekről" és "információ-gazdaságosságról". A
§12 és a §16 szókincse is megjelenik (`zökkenőmentes`, `egyedülálló`), és két
futásban BIZTOS lint-találat is van, egy "kerül" passzív és két hosszú
gondolatjel.

A skilles ág egyik futásában sincs sem BIZTOS találat, sem reklámnyelv, sem
kitalált állítás. A maradék gyanús találatok is enyhébbek: főleg a §18
létigekerülése (`rendelkezik`, `biztosít`, `kínál`).

A másik különbség az egyöntetűség. A négy skilles futás pontosan ugyanazt a hat
tényt fedte le, a négy skill nélküli négy és hét között ingadozott, futásonként
más összetételben. A skill tehát nemcsak az átlagot javítja, hanem a szórást is
csökkenti, és éles munkában ez ér többet.

Amit viszont a skill nem old meg: egyik ág sem fedte le a 2.5.2 első bekezdését,
az ősfeltöltésről és a DB ágról szólót, és a férőhely szerinti besorolás
kihagyását sem. Az erősebb modell ezt kilencből kilencszer megírta. A hiányzó
tények tehát modellképesség kérdése, nem szabálykérdés: a skill a kitalálást
fogja meg, a kifelejtést nem.

A tokenmérés itt is a skill ellen szól: a betöltése 30 százalékkal drágítja a
futást. Cserébe a kimenet 40 százalékkal rövidebb, mert a kitalált tartalom
kimarad belőle.

### 2026-09-13, 2.4.7, a három képességszint összevetése

Ugyanaz a forrás, ugyanaz a két kimenet, három modellen, kondíciónként négy
futással a két gyengébbnél és hárommal a legerősebbnél. A lint mindenhol az
azóta javított változat.

| | Erős modell | Középső modell | Kisebb modell |
| --- | --- | --- | --- |
| Tényfedés skill nélkül | teljes | teljes, egy hiánnyal | 4-7 tíz leltári tényből |
| Tényfedés skillel | teljes | teljes | hat tíz tényből, mind a négy futásban ugyanaz |
| Lint BIZTOS skill nélkül | 0 | 0 | 3 találat két futásban |
| Lint BIZTOS skillel | 0 | 0 | 0 |
| Kitalált állítás skill nélkül | nincs | nincs | három futásban |
| Kitalált állítás skillel | nincs | nincs | nincs |

A törés a középső és a kisebb modell között van, nem feljebb. A középső modell
skill nélkül is lefedi az ősfeltöltést, a férőhely kihagyását és az inaktív
gombot, tehát azt a három tényt is, amit a kisebb modell egyik ága sem talált
el, és sem kitalált állítás, sem BIZTOS lint-találat nincs a szövegeiben.

Ebből az következik, hogy a skill tényhűségi haszna a kisebb modelleknél
jelentkezik. A két erősebbnél a haszna más természetű: a terjedelem és a
tagolás kiszámíthatóvá válik, a szöveg rövidebb lesz, és eltűnnek az egyszavas
gyanús találatok is.

A megszólítás tizenegy skilles futásból kettőben keveredett, a középső és az
erős modellnél egyszer-egyszer (`jelöljük` és `várunk` személytelen szöveg
mellett, illetve `egyeztetjük Önökkel`). A kisebb modell négy futásából egyszer
sem, mert ott a szöveg végig személytelen maradt. A szabály tehát nem a
modellképességen bukik el, hanem a saját megfogalmazásán: minél inkább képes egy
modell regisztert váltani, annál valószínűbb, hogy a Megszólítás szakaszt
félreérti.

A tokenmérés mindhárom szinten ugyanazt mutatja: a skill betöltése 29 és 36
százalék közötti többletet jelent.

### 2026-09-13, 2.4.9, Gemini-kör és a §19 újrapontozása

Egy negyedik modell, másik gyártótól, a felhasználó céges előfizetésén,
chatfelületen. Kondíciónként egy futás, Gemini 3.6 Thinking.

| | Skill nélkül | Teljes skill |
| --- | --- | --- |
| Lint BIZTOS | 11 | 0 |
| Lint gyanús | 5 | 0 |
| Sor eleji félkövér | 10 | 0 |
| `Mint ... felhasználó` tükörfordítás | 2 | 0 |
| Kitalált szó | 5 | 0 |
| Karakter | 4900 | 4237 |

A skill nélküli futás kitalálta a parkolási díjat, kétszer is, pedig a forrás
díjról egy szót sem ír. Ugyanaz a hiba, amit a kisebb Claude-modell is
elkövetett ugyanezen a hiányon: két különböző gyártó modellje ugyanoda talál ki
tartalmat. Mellette `precízebb`, `dinamikus`, `intelligensebbé`,
`zökkenőmentes`, és a platformlistát is átírta. A skilles futásban egyik sincs,
és a kimondott hiányt is pontosan jelezte.

Ez az első gyártófüggetlen mérés: a skill eddig csak Claude-modelleken futott,
ahol felmerülhetett, hogy a saját családjára van hangolva.

A §19 újrapontozása: a Gemini-futás tíz sor eleji félkövér címkéje mutatta
meg, hogy a lint a §19 első felét nem látta: csak a felsoroláspont élén álló
címkét kereste. A szabály most a sor eleji félkövért és a félkövér címkét is
fogja, a mondat belsejében álló kiemelés pedig gyanús szintre került.

Ezzel mind a 27 eddigi futás újrapontozódott, és a kép megváltozott:

| Ág | BIZTOS találatos futások |
| --- | --- |
| Erős modell, skill nélkül | 3-ból 2 (0, 5, 5) |
| Középső modell, skill nélkül | 4-ből 3 (7, 3, 0, 8) |
| Kisebb modell, skill nélkül | 4-ből 4 (10, 13, 10, 2) |
| Másik gyártó, skill nélkül | 1-ből 1 (11) |
| Bármelyik modell, skillel | 12-ből 1 (a kisebb modell egyik futása, 5) |

A korábbi bejegyzések nulla BIZTOS találatot írtak az erős modell futásaira. Az
a szám a lint vakságát mérte, nem a szövegét. A félkövér dekoráció tehát a
skill legkövetkezetesebb, modellfüggetlen hatása, és eddig egyszerűen nem
láttuk.

### 2026-09-13, 2.4.9, négy chatfelületes modell

A negyedik és ötödik gyártói modellcsalád, chatfelületen, a felhasználó céges
előfizetésein. Kondíciónként egy futás. A tokenfogyasztás itt nem mérhető, és
nem is lenne összevethető az agent-futásokkal.

| Modell | Skill nélkül | Skillel | Megjegyzés |
| --- | --- | --- | --- |
| Gemini 3.6 Thinking | 11 BIZTOS | 0 | skill nélkül kitalálta a parkolási díjat |
| Gemini 3.1 Pro | 3 BIZTOS | 0 | a skilles futás is kitalált egy indokot |
| Gemini 3.6 Flash | 7 BIZTOS | 3 BIZTOS | angol sablon skill nélkül |
| ChatGPT 5.6 Sol extraHigh | 6 BIZTOS | 0 | teljes tényfedés mindkét ágon |

Három következtetés.

A félkövér dekoráció az egyetlen minta, ami minden gyártónál, minden skill
nélküli futásban megjelent, háromtól tizenegy találatig. Skillel négyből három
modellnél nullára ment. Ez a skill legkövetkezetesebb hatása.

A tényhűség viszont a modellen múlik, nem a skillen. A ChatGPT-futás mindkét
ágon lefedte az ősfeltöltést is, amit a Gemini-család egyik futása sem, és amit
a kisebb Claude-modell sem talált el. A skill a kitalálást szűri, a kifelejtést
nem pótolja.

A skill nem garancia. A Gemini 3.1 Pro a skill jelenlétében is okot talált ki
egy leíráshoz ("a pontosabb parkolási és e-matrica díjszabás miatt", a forrás
díjról egy szót sem ír), és egyik Pro-futás sem jelezte a forrás kimondott
hiányát, pedig azt minden más modell skilles futása jelezte. A Flash pedig
megtartotta a félkövér sablont, csak a nyelvét fordította magyarra.

Egy tétel ötödször jött elő, most már öt modellcsaládnál: a user story félkövér
sablonja. A §19 megengedi a félkövér címkét, ha a sablon előírja, csak épp nem
dönthető el, mi számít sablonnak, amikor a hívó feladat nem ad formátumot. Ez a
nyitott tételek közül a legtöbbet jelzett.

### 2026-09-13, 2.4.9, egy gyors chatmodell

| | Skill nélkül | Skillel |
| --- | --- | --- |
| Lint BIZTOS | 13 | 0 |
| Ebből görbe idézőjel | 12 | 0 |
| Sor eleji félkövér | 3 | 0 |
| Kimondott hiány jelezve | nem | igen |
| Karakter | 4155 | 4114 |

Formailag ez a mérés legnagyobb javulása: tizenhárom szabálysértésből nulla, és
a skilles futás a forrás kimondott hiányát is jelezte, a skill nélküli nem.

Tartalmilag viszont itt bukott ki a legélesebben a következő tétel.

## Részben lezárt tétel: a Hosszúság szabály levág forrásbeli tényt (2.5.0)

### Mi történt

A gyors chatmodell skill nélküli futása megírta a 2.5.2 első bekezdését:

> Az ősfeltöltés során a DB ág motorkerékpárnál W1, tehergépkocsinál W3 értéket
> tölthet. Az alkalmazás logikája ősfeltöltés nélkül is működik.

Ugyanaz a modell, ugyanaz a forrás, ugyanaz a feladat, skillel: ez a bekezdés
eltűnt. A skilles futás két storyt írt, mindkettőt a felugró ablakról.

Ugyanez a mintázat a kisebb Claude-modellnél is megvolt: mind a négy skilles
futás pontosan hat tényt fedett le a tízből, és mind a négyszer ugyanaz a négy
hiányzott, köztük az ősfeltöltés. A két erős Claude-modellnél a jelenség nem
jelentkezett, ott a skilles futások is teljes fedést adtak.

### Melyik szabály okozza

A Hosszúság alszakasz első mondata: "Írj annyit, amennyit a feladat kér, és ne
többet."

A feladat ebben a mérésben kifejezetten a szakasz lefedését kérte ("annyi
storyt írj, amennyire a szakasz bomlik"). A skill saját elve szerint a hívó
feladat felülír, mégis a rövidség nyert.

### Miért nem egyértelmű a szabály

A "ne többet" két különböző dolgot tilthat, és a szöveg nem választja szét őket:

- ne írj tartalmatlan tölteléket (bevezető, összefoglalás, záró gondolat), ami a
  szabály eredeti célja, és amit a szakasz többi mondata is ezzel magyaráz
- ne fedd le a forrás minden szakaszát, ami nem volt cél, viszont a gyengébb
  modellek így olvassák

A második olvasat ellen a skillben nincs mondat. A Részletesség alszakasz a
mennyiségről szól, de az általánosítás és a kitalálás határáról, nem arról,
hogy egy forrásbeli szakasz kihagyható-e.

### Mit kell eldönteni

Kell-e a Hosszúság szabály mellé egy mondat, ami kimondja, hogy a rövidítés a
megfogalmazásra vonatkozik, nem a forrás lefedettségére. És ha igen, hogyan
viszonyul ez a Részletesség alszakaszhoz, ami épp azt engedi meg, hogy szélesebb
közönségnek szóló szövegben ne szerepeljen minden részlet.

### A döntés

A 2.5.0 kimondja a szabályban, hogy a rövidítés a megfogalmazásra vonatkozik,
nem a forrás lefedettségére, és hogy egy szakasz feldolgozásánál annak minden
ténye a szövegbe kerül. A Részletesség alszakasz ezzel nem ütközik: az arról
szól, mennyit árul el a szöveg egy tényről, nem arról, hogy egy forrásbeli
szakasz kihagyható-e.

### A javítás visszamérése

A 2.5.0-s skillel mindkét érintett modell újrafutott.

A gyors chatmodellnél a javítás fogott: a levágott bekezdés szó szerint
visszakerült, a lint továbbra is tiszta, a szöveg száz karakterrel hosszabb.

A kisebb Claude-modellnél nem fogott. Négy új futásból egyik sem említi az
ősfeltöltést, ugyanúgy, mint a 2.4.9-es körben. A formai oldal ráadásul
zajosabb lett: a 2.4.9-ben négyből egy futásban volt BIZTOS találat (összesen
öt), a 2.5.0-ban négyből háromban (összesen kilenc), és a találatok jórészt a
félkövér story-sablonból jönnek ("Mint felhasználó, szeretném"). Négy-négy
minta mellett ez lehet szórás is, de a Hosszúság szakasz a javítással hosszabb
lett, és gyengébb modellnél a hosszabb szabályszöveg hígítja a figyelmet.

A tétel ezért nem lezárt. Amit tudunk: a megfogalmazás ott segít, ahol a modell
elég erős ahhoz, hogy a szabályt pontosan alkalmazza. Ahol nem, ott a
lefedettséget nem a stílusszabály fogja megoldani, hanem a hívó feladat
pontosabb kérése vagy egy ellenőrző kör.

### Hogyan reprodukálható

A mérési készlet két futása: a gyors chatmodell skill nélküli és skilles
kimenete, illetve a kisebb Claude-modell négy skilles futása. Mind a repón
kívül, a mérési könyvtárban.
