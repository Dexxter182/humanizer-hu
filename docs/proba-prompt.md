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
