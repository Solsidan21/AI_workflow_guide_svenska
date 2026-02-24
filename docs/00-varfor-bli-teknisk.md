# Kapitel 00 — Varfor det lonar sig att bli lite teknisk

> *Du ar redan bra pa AI. Har ar det lilla extra som tar dig till en helt annan niva.*

Du vet hur man skriver en bra prompt. Du far bra svar fran Claude eller ChatGPT. Men varje gang du startar en ny session borjar du fran noll — samma kontext, samma instruktioner, samma format.

Det beror inte pa att du gor nagot fel. Det beror pa att du saknar ett ordforrad — en handfull tekniska begrepp som oppnar dorren till verktyg dar AI faktiskt kan minnas, folja regler och arbeta med dina filer.

Det har ar de tio begreppen. Inget av dem ar svarare an att lara sig ett nytt Excel-kortkommando. Men tillsammans forandrar de hur du arbetar med AI.

---

## 1. Filer och mappar

**Vad det ar:** Datorns satt att organisera information. En fil ar ett enskilt dokument. En mapp samlar filer som hor ihop.

**Analogi:** Tank dig ett dokumentskap pa kontoret. Varje lada ar en mapp, och pappren inuti ar filer. Ladorna kan ligga inuti varandra (undermappar).

**Varfor det spelar roll:** I nasta steg av AI-arbete pekar du AI mot mappar med data istallet for att klistra in text i en chatt. Dina filnamn och mappnamn blir instruktioner i sig sjalva — `data/finansiellt/arsredovisning-2024.pdf` talar om for AI exakt vad filen innehaller utan att du behover forklara det.

---

## 2. Terminalen

**Vad det ar:** Ett textbaserat satt att ge instruktioner till din dator. Istallet for att klicka pa ikoner skriver du kommandon.

**Analogi:** Skillnaden mellan att peka pa saker i en butik och att skriva en bestallningslista. Bada fungerar, men skriftliga instruktioner kan vara mycket mer exakta: "Oppna mappen portfoljbolag-x, las alla PDF:er i data/finansiellt/ och skriv en sammanfattning."

**Varfor det spelar roll:** Claude Code lever i terminalen. Du behover inte lara dig kommandon — Claude hjalper dig. Men att veta att terminalen finns, och att den inte ar farlig, ar steget som skipper dig fran "chattanvandare" till "AI-systembyggare".

---

## 3. Markdown

**Vad det ar:** Ett enkelt satt att formatera text med vanliga tecken. En rubrik skrivs med `#`, fetstil med `**dubbelstjarnor**`, listor med bindestreck.

**Analogi:** I Word klickar du pa knappar for att formatera. I Markdown skriver du formateringen rakt i texten. Det ar lattare an det later — du laser faktiskt Markdown just nu om du tittar pa den har filen.

**Varfor det spelar roll:** CLAUDE.md, skills, och nastan all AI-dokumentation skrivs i Markdown. Det tar fem minuter att lara sig grunderna, och det ar nyckeln till att skriva regler och instruktioner som AI foljer automatiskt.

### Snabbreferens

```
# Rubrik 1
## Rubrik 2
### Rubrik 3

**Fetstil**
*Kursivt*

- Punkt i lista
- Annan punkt

1. Numrerad lista
2. Andra punkten
```

---

## 4. Git

**Vad det ar:** Ett system for versionshantering — det haller reda pa varje andring du gor i dina filer.

**Analogi:** Tank pa "Spara version" i Word, men pa steroider. Git fungerar for alla filer i ett helt projekt, later flera personer arbeta samtidigt, och du kan alltid atervanda till exakt hur allt sag ut vid en specifik tidpunkt.

**Varfor det spelar roll:** Nar du arbetar med Claude Code ar Git ditt sakerhetsnat. Varje andring loggas. Du kan experimentera fritt — om nagot inte fungerar gar du bara tillbaka. Det gor att du aldrig behover vara radd att AI forstort nagot.

---

## 5. Repository (repo)

**Vad det ar:** En projektmapp som overvakas av Git. Alla filer plus hela andringshistoriken bildar ett repository.

**Analogi:** Om Git ar versionshanteringssystemet sa ar ett repo den specifika arbetsytan — som en projektmapp med inbyggd dagbok som skriver ner varje andring.

**Varfor det spelar roll:** Nar nagon sager "klona repot" menar de "ladda ner projektmappen." Det repo du laser just nu ar ett bra exempel. Det ar sa man delar och samarbetar kring dokument och struktur i AI-varlden.

---

## 6. CLAUDE.md

**Vad det ar:** En speciell fil som du lagger i ditt projekt for att ge Claude instruktioner. Claude laser den automatiskt innan den borjar arbeta.

**Analogi:** Tank dig att du far en ny konsult pa kontoret. Forsta dagen ger du hen ett introduktionsdokument: "Sa har jobbar vi, det har ar vara konventioner, de har filerna ar viktiga." CLAUDE.md ar exakt det dokumentet — fast for AI.

**Varfor det spelar roll:** Det har ar den enskilt viktigaste grejen i hela den har guiden. Med en CLAUDE.md behover du aldrig upprepa samma instruktioner. Claude foljer dina regler, din stil och din struktur — automatiskt, varje gang. Det ar skillnaden mellan att chatta med AI och att ha ett system.

---

## 7. API

**Vad det ar:** API star for Application Programming Interface. Det ar ett standardiserat satt for program att prata med varandra.

**Analogi:** Tankt pa en restaurang. Du (programmet) vill ha mat fran koket (en annan tjanst). Du pratar inte direkt med kocken — du ger din bestallning till kyparen (API:et), som vidarebefordrar den och kommer tillbaka med ratt.

**Varfor det spelar roll:** Nar nagon sager "kopplat Claude till sitt system via API:et" menar de att deras verktyg kan skicka fragor till Claude och fa svar automatiskt — utan att nagon sitter i chatten. Du behover inte bygga nagot med API:er sjalv, men att forsta begreppet gor att du kan ha en informerad diskussion med tekniska kollegor.

---

## 8. Kontext (context)

**Vad det ar:** All information som Claude har tillgang till nar den svarar — din prompt, tidigare meddelanden, bifogade dokument och eventuella instruktionsfiler.

**Analogi:** Ju mer relevant bakgrund du ger en konsult innan ett mote, desto battre forberedd ar konsulten. Claudes kontext fungerar likadant.

**Varfor det spelar roll:** Du forstar redan att bra prompts ger bra svar. Men nasta steg ar att forsta att kontext ar mer an bara din prompt. Med CLAUDE.md, mappstruktur och skills bygger du ett **permanent kontextlager** som alltid finns dar — istallet for att skriva om det varje gang.

---

## 9. Prompt

**Vad det ar:** Din instruktion till AI. Du vet redan vad det ar — du skriver dem varje dag.

**Varfor det spelar roll har:** I chatten ar prompten allt du har. I Claude Code ar prompten bara en del av bilden. Resten ar CLAUDE.md (regler), skills (ateranvandbara arbetsfloden), och mappstruktur (kontext). Det ar darfor denna guide fokuserar pa systemet runt prompten — inte pa prompten i sig.

---

## 10. Token

**Vad det ar:** Den enhet som AI anvander for att mata textlangd. En token ar ungefar tre fjardedelar av ett ord pa engelska (lite mindre pa svenska).

**Analogi:** Ordraknaren i Word, fast for AI. Claude bryter ner text i tokens och bearbetar dem en i taget. Varje modell har en maximal kontextlangd matt i tokens.

**Varfor det spelar roll:** Om nagon sager "det ryms inte i kontextfonstret" menar de att texten overskrider AI:ns tokengraans. Du slipper rakna tokens i praktiken, men det forklarar varfor du ibland behover sammanfatta (med `/compact` i Claude Code) for att frigora plats.

---

## Du ar redo

Tio begrepp. Inget av dem ar raketvetenskap. Men tillsammans ger de dig ett sprak for att ta dig bortom chatten.

Det viktiga ar inte att du memorerar definitionerna. Det viktiga ar att du inte kanns avskrackt nar du ser orden dyka upp. Du har nu kartan — resten av guiden visar vagen.

> *Nasta kapitel: [01 — Fran chatt till system](01-fran-chatt-till-system.md)*
