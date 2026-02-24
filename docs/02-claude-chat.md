# Kapitel 02 — Claude Chat: Din AI-assistent pa claude.ai

> **Sammanfattning:** I det har kapitlet lar du dig anvanda Claude via webben — fran att skapa ditt forsta konto till att bygga projekt med egna kunskapsbaser, ge battre instruktioner och fa ut mer av varje konversation.

---

## Innehall

1. [Grunderna — Skapa konto och komma igang](#grunderna--skapa-konto-och-komma-igang)
2. [Hur en konversation fungerar](#hur-en-konversation-fungerar)
3. [Gratis vs Pro-prenumeration](#gratis-vs-pro-prenumeration)
4. [Projekt (Projects)](#projekt-projects)
5. [Prompttekniker — Sa ger du battre instruktioner](#prompttekniker--sa-ger-du-battre-instruktioner)
6. [Filhantering](#filhantering)
7. [Minne och kontinuitet](#minne-och-kontinuitet)
8. [Artifacts](#artifacts)
9. [Nasta steg](#nasta-steg)

---

## Grunderna — Skapa konto och komma igang

### 1. Ga till claude.ai

Oppna din webblasare och navigera till [claude.ai](https://claude.ai). Det fungerar bast i Chrome, Edge eller Safari.

### 2. Skapa ett konto

Klicka pa **Sign up** och valj inloggningsmetod:

- **E-post** — du far en verifieringslank.
- **Google-konto** — snabbaste sattet om du redan anvander Google Workspace.
- **Single Sign-On (SSO)** — om din organisation har ett Enterprise-avtal med Anthropic.

### 3. Borja skriva

Nar du ar inloggad mots du av ett tomt chattfalt. Skriv din fraga eller uppgift, tryck Enter, och Claude svarar direkt. Det ar verkligen sa enkelt att komma igang.

> **Tips:** Spara garna claude.ai som bokmarke eller fasta fliken i din webblasare. Manga anvandare har Claude oppet hela arbetsdagen — precis som e-post eller kalender.

---

## Hur en konversation fungerar

For att anvanda Claude effektivt ar det bra att forsta en grundlaggande mekanism: **kontextfonster** (context window).

### Kontextfonstret — Claudes "arbetsminne"

Nar du chattar med Claude har den tillgang till allt som skrivits i den pagaende konversationen — bade dina meddelanden och Claudes svar. Det ar kontextfonstret.

Tank pa det som ett stort skrivbord. Sa lange konversationen pagar ligger alla papper pa skrivbordet och Claude kan referera till dem. Men skrivbordet har en begransad yta. For mycket material och de aldsta papperen borjar ramla av kanten.

**I praktiken:**

| Scenario | Hur det paverkar dig |
|----------|---------------------|
| Kort konversation (nagra meddelanden) | Claude har full koll pa allt ni diskuterat |
| Lang konversation (50+ meddelanden) | Claude kan borja "glomma" det som sades i borjan |
| Ny konversation | Claude har ingen aning om vad ni pratade om forut (om inte Memory ar aktivt — mer om det senare) |

### Claude "glommer" mellan konversationer

Det har ar den viktigaste saken att forsta: **varje ny konversation borjar fran noll.** Om du igår bad Claude analysera ett foretags kassaflode och idag oppnar en ny konversation, vet Claude inget om det.

Det finns tva losningar pa det har problemet:

1. **Projekt** — ge Claude persistent kunskap och instruktioner (se nedan).
2. **Minne (Memory)** — lat Claude komma ihag preferenser over tid (se langre ned).

> **Analogi:** Tank pa det sa har. Claude ar som en extremt kompetent konsult som har fullstandig amnesi varje morgon. Inom ett mote (en konversation) ar hen brilliant. Men nasta mote borjar hen helt fran borjan — om du inte forbereder en briefing (Projekt) eller hen har anteckningar fran forr (Memory).

---

## Gratis vs Pro-prenumeration

Claude kan anvandas gratis, men den betalda versionen ger dig betydligt mer.

| | **Gratis** | **Pro** (20 USD/manad) |
|---|---|---|
| Tillgang till Claude | Ja, men med begransad anvandning | Betydligt hogre granser |
| Basta modellen (Opus) | Begransad tillgang | Full tillgang |
| Projekt (Projects) | Nej | Ja |
| Filuppladdning | Ja, med granser | Hogre granser |
| Minne (Memory) | Begransat | Ja |
| Prioritet vid hog belastning | Nej | Ja |
| Claude i Excel/PowerPoint | Nej | Ja |

**Rekommendation for kunskapsarbetare:** Om du anvander Claude mer an nagra ganger i veckan ar Pro-prenumerationen vard det. Projekt ensamt motiverar kostnaden for de flesta professionella anvandare.

> **Organisation?** Anthropic erbjuder ocksa **Team** och **Enterprise**-planer med centraliserad administration, hogre granser och avancerade sakerhetsalternativ. Prata med din IT-avdelning om ni vill rulla ut Claude bredare.

---

## Projekt (Projects)

Projekt ar en av de mest kraftfulla funktionerna i Claude — och den som flest anvandare missar.

### Vad ar ett projekt?

Ett projekt ar en behallare som samlar:

1. **Custom Instructions** — permanenta instruktioner som Claude foljer i varje konversation inom projektet.
2. **Project Knowledge** — dokument som Claude alltid har tillgang till inom projektet.
3. **Konversationer** — alla chattar som tillhor projektet.

Tank pa det som att skapa en specialiserad version av Claude for en specifik uppgift eller ett specifikt omrade.

### Hur du skapar ett projekt

1. Klicka pa **Projects** i vanstermenyn pa claude.ai.
2. Klicka pa **Create Project**.
3. Ge projektet ett beskrivande namn, till exempel "Portfoljbolag Norden AB — Due Diligence".
4. Lagg till Custom Instructions (se nedan).
5. Ladda upp relevanta dokument till Project Knowledge.
6. Borja en konversation inom projektet.

### Project Knowledge — din kunskapsbas

Har laddar du upp dokument som Claude alltid ska ha tillgang till nar du arbetar inom projektet. Det kan vara:

- PDF-filer (arsredovisningar, rapporter, avtal)
- Textfiler och Word-dokument
- Excel-filer
- Bilder och diagram

**Skillnaden mot att ladda upp filer i en vanlig konversation:** I en vanlig konversation "forsvinner" den uppladdade filen nar konversationen ar slut. I ett projekt finns dokumenten kvar och ar tillgangliga i *alla* konversationer inom projektet.

### Custom Instructions — bestandiga instruktioner

Custom Instructions ar text som Claude laser innan varje konversation i projektet. Det ar som en briefing som Claude alltid har med sig.

**Exempel pa Custom Instructions for ett PE-projekt:**

```
Du ar en erfaren PE-analytiker som hjalper mig analysera portfoljbolag.

Kontext:
- Jag arbetar pa ett nordiskt PE-bolag
- Vi fokuserar pa mid-market B2B-bolag (50-500 MSEK i omsattning)
- Vara nyckeltal ar EBITDA-marginal, organisk tillvaxt och kassaflodeskonvertering

Nar du analyserar finansiell data:
- Presentera alltid nyckeltal i tabellformat
- Jamfor med branschsnitt nar det ar mojligt
- Flagga potentiella risker och mojligheter
- Skriv pa svenska

Nar du skriver sammanfattningar:
- Borja med en executive summary (3-5 rader)
- Anvand punktlistor for nyckelinsikter
- Avsluta med "Rekommenderade nasta steg"
```

### PE-exempel: Projekt for "Portfoljbolag X"

Lat oss saga att du ska gora en fordjupad analys av ett potentiellt forvarvsobjekt. Sa har kan du satta upp det:

**Projektnamn:** Portfoljbolag X — Forvarvsanalys

**Project Knowledge (uppladdade dokument):**
- Arsredovisning 2023, 2024, 2025
- Senaste kvartalsrapporten
- Branschrapport fran relevant branschorganisation
- Intern investeringspromemoria (om sadan finns)
- Organisationsschema

**Custom Instructions:**
```
Du hjalper mig med due diligence pa Portfoljbolag X, ett nordiskt
tillverkningsforetag med ca 200 MSEK i omsattning.

Anvand alltid de uppladdade arsredovisningarna som kallmaterial.
Nar du anger siffror, referera till specifik sida och ar.
Flagga eventuella inkonsekvenser mellan aren.
```

**Nu kan du stalla fragor som:**
- "Sammanfatta omsattningstillvaxten de senaste tre aren och jamfor med branschgenomsnittet."
- "Vilka ar de storsta riskerna baserat pa den senaste arsredovisningen?"
- "Gor en forenklad DCF-vardering baserat pa de kassafloden du ser i rapporterna."

Claude har da tillgang till alla dokument *utan att du behover ladda upp dem varje gang*.

---

## Prompttekniker — Sa ger du battre instruktioner

En "prompt" ar det du skriver till Claude. Battre prompter ger battre svar. Har ar de viktigaste teknikerna.

### 1. Var specifik — beratta vad du vill ha

**Vagt (daligt):**
> "Analysera det har foretaget."

**Specifikt (bra):**
> "Analysera kassaflodet for det har foretaget for perioden 2022-2024. Presentera resultatet i en tabell med arliga forandringar i procent. Fokusera pa operativt kassaflode och investeringskassaflode."

Ju tydligare du ar med *vad* du vill ha, *i vilket format*, och *for vilken publik*, desto battre blir resultatet.

### 2. Ge kontext — beratta vem du ar och varfor

Claude anpassar sitt svar efter kontexten du ger. Jamfor dessa tva prompter:

**Utan kontext:**
> "Forklara EBITDA."

**Med kontext:**
> "Jag ar en PE-analytiker som ska presentera for min investmentcommittee. Forklara EBITDA pa ett satt som ar korrekt men ocksa begripligt for kommitteledamoter som inte ar finansexperter. Inkludera ett konkret raknexempel."

Det andra svaret blir mer relevant, battre anpassat och mer anvandbart.

### 3. Steg for steg — be Claude tanka hogt

For komplexa analyser, be Claude resonera stegvis:

> "Jag vill att du utforder varderingen av det har bolaget steg for steg:
> 1. Borja med att identifiera relevanta nyckeltal fran arsredovisningen.
> 2. Jamfor med branschsnitt.
> 3. Gora en forenklad DCF med dina antaganden tydligt redovisade.
> 4. Sammanfatta med en varderingsrange och de viktigaste ossakerheterna."

Nar Claude tvingas resonera stegvis minskar risken for slarvfel och du kan lattare kontrollera varje steg.

### 4. Iterera — forsta svaret ar sallan perfekt

Arbeta med Claude som du skulle arbeta med en kollega. Ge feedback och bygg vidare:

- "Bra start, men kan du fordjupa analysen av rorelsekapitalet?"
- "Det har ar for tekniskt. Kan du skriva om det for en publik som inte ar finansexperter?"
- "Kan du lagga till en riskanalys ocksa?"
- "Formatera det har som en executive summary, max en A4-sida."

### 5. Formatera output — be om ratt struktur

Claude ar utmarkt pa att formatera information. Var explicit:

- "Presentera det har som en numrerad lista med max 10 punkter."
- "Gor en tabell med kolumnerna: Nyckeltal, 2023, 2024, Forandring (%)."
- "Skriv det har som ett internt PM med rubrikerna: Bakgrund, Analys, Rekommendation."
- "Anvand bullet points och fet stil for nyckelinsikter."

### Praktiska exempel med PE-vinkel

**Exempel 1 — Analysera kassaflode:**

> "Jag laddar upp arsredovisningen for Foretag X. Gor foljande:
> 1. Extrahera operativt kassaflode, investeringskassaflode och finansieringskassaflode for 2022-2024.
> 2. Berakna fritt kassaflode (FCF) for varje ar.
> 3. Presentera i en tabell.
> 4. Kommentera trender och eventuella varningssignaler.
> 5. Jamfor FCF-marginal med typiska nivaer for tillverkningsforetag i Norden."

**Exempel 2 — Skriv en investment thesis:**

> "Baserat pa det vi diskuterat om Foretag X, skriv en investment thesis (1-2 sidor) med foljande struktur:
> - Executive summary (3-5 meningar)
> - Bolaget i korthet (verksamhet, marknad, storlek)
> - Investeringsrationale (3-5 nyckelpunkter)
> - Vardeskapandeplan (vad vi kan gora battre)
> - Nyckelrisker och hur vi hanterar dem
> - Forenklad vardering och avkastningspotential
>
> Skriv professionellt men inte overdriven finansjargong. Publiken ar var investmentcommittee."

---

## Filhantering

Claude kan ta emot och analysera filer direkt i konversationen.

### Filtyper som stods

| Filtyp | Fungerar bra for |
|--------|-----------------|
| **PDF** | Arsredovisningar, rapporter, avtal, presentationer |
| **Excel (.xlsx, .csv)** | Finansiell data, listor, tabeller |
| **Word (.docx)** | PM, utkast, analysrapporter |
| **Bilder (.png, .jpg)** | Diagram, organisationsscheman, screenshots |
| **Text (.txt, .md)** | Anteckningar, datautdrag |

### Begransningar att kanna till

- **Filstorlek:** Det finns en ovre grans per fil (for narvarande runt 30 MB, men det kan andras). Stora Excel-filer med manga flikar kan vara problematiska.
- **Antal filer:** Du kan ladda upp flera filer i samma konversation, men ju fler filer desto mer av kontextfonstret anvands.
- **Excel-flikar:** Claude kan inte alltid se alla flikar i en komplex arbetsbok. Det kan vara battre att exportera relevanta flikar som separata filer eller CSV.
- **Skannade PDF:er:** Om en PDF ar en inskannad bild (inte sokbar text) kan Claude anvanda bildigenkanning, men resultatet ar inte lika bra som med textbaserade PDF:er.

### Basta praxis

1. **Ladda upp kontext-dokument tidigt.** Om du ska stalla flera fragor om ett dokument — ladda upp det i ditt forsta meddelande. Da har Claude tillgang till det genom hela konversationen.

2. **Beratta vad filen innehaller.** Ge Claude en kort introduktion:
   > "Jag laddar upp arsredovisningen for Foretag X (2024). Det ar ett tillverkningsforetag med 350 MSEK i omsattning. Borja med att sammanfatta de viktigaste finansiella nyckeltalen."

3. **Anvand Projekt for dokument du aterkommer till.** Om du regelbundet analyserar samma arsredovisning — lagg den i Project Knowledge istallet for att ladda upp den varje gang.

4. **Exportera komplexa Excel-filer.** Istallet for att ladda upp en hel arbetsbok med 20 flikar, exportera den relevanta fliken som CSV. Claude hantera det battre och du sparar kontextfonster.

---

## Minne och kontinuitet

### Hur Memory fungerar

Memory ar en funktion som latar Claude spara information mellan konversationer. Nar Memory ar aktiverat kan Claude:

- **Komma ihag dina preferenser** — till exempel att du alltid vill ha svar pa svenska, att du foredrar tabeller framfor lopande text, eller att du arbetar inom PE.
- **Komma ihag kontext om dig** — till exempel ditt namn, din roll, vilka branscher du fokuserar pa.
- **Bygga upp en bild av dig over tid** — ju mer du interagerar, desto battre anpassar sig Claude.

### Hur du styr vad Claude minns

Du har full kontroll over Claudes minne:

- **Explicit sparande:** Saga rakt ut "Kom ihag att jag alltid vill ha finansiella siffror i MSEK, inte KSEK."
- **Granska minnen:** I installningarna pa claude.ai kan du se allt Claude har sparat, och ta bort enskilda minnen.
- **Radera allt:** Du kan nar som helst rensa hela minnesbanken.

### Tips for effektiv anvandning av Memory

1. **Var explicit om vad som ska sparas.** Saga inte bara "jag jobbar pa ett PE-bolag". Saga:
   > "Kom ihag: Jag arbetar som analytiker pa ett nordiskt PE-bolag. Vi fokuserar pa mid-market B2B-foretag i Norden. Jag foredrar analyser pa svenska med nyckeltal i MSEK."

2. **Granska regelbundet.** Ga igenom sparade minnen ibland och rensa det som inte langre stammer.

3. **Minne ersatter inte Projekt.** Memory ar bra for personliga preferenser. For dokumentation och specifik kunskap, anvand Projekt istallet.

> **Integritet:** Minnen ar kopplade till ditt konto och anvands inte for att trana Claudes modeller. Du kan nar som helst ta bort dem via installningarna.

---

## Artifacts

### Vad ar artifacts?

Artifacts ar fristaende innehallsdelar som Claude skapar bredvid konversationen. De visas i en separat panel till hoger pa skarmen och kan vara:

- **Dokument** — langre texter, PM, rapporter
- **Tabeller** — strukturerad data
- **Kod** — programkod eller formler
- **Diagram** — visuella framstallningar (med hjalp av kod)
- **Webbsidor** — enklare HTML-baserade verktyg eller presentationer

### Nar skapas artifacts?

Claude skapar automatiskt en artifact nar innehallet:

- Ar tillrackligt langt och fristaende (inte bara en kort kommentar)
- Ar nagot du sannolikt vill spara, kopiera eller anvanda vidare
- Ar strukturerat (tabeller, kod, dokument)

Du kan ocksa be om det explicit: "Skapa en artifact med det har innehallet."

### Hur du anvander artifacts effektivt

1. **Kopiera och anvand vidare.** Artifacts har en kopieringsknapp. Skriv ut en rapport som artifact, kopiera texten och klistra in i Word eller PowerPoint.

2. **Iterera pa en artifact.** Du kan be Claude uppdatera en befintlig artifact:
   > "Uppdatera tabellen i artifacten och lagg till en kolumn for 2025-prognos."

3. **Anvand for rapporter och PM.** Be Claude skriva ett helt PM som en artifact. Da far du ett rent, formaterat dokument att kopiera.

4. **Diagram och visualisering.** Claude kan skapa enkla diagram som artifacts. Det ar inte lika kraftfullt som Excel, men bra for snabba illustrationer:
   > "Skapa ett stapeldiagram som visar omsattningstillvaxten 2020-2024."

> **Tips:** Tankt pa artifacts som Claudes "leverabler". Den vanliga konversationen ar diskussionen — artifacts ar de faktiska dokumenten som diskussionen producerar.

---

## Nasta steg

Nu har du verktygen for att anvanda Claude Chat effektivt — fran grundlaggande konversationer till organiserade projekt med egna kunskapsbaser.

I nasta kapitel tittar vi pa hur Claude kan arbeta direkt inne i **Excel och PowerPoint** — sa att du slipper kopiera data fram och tillbaka mellan claude.ai och dina kalkylblad.

**Ga vidare till: [Kapitel 03 — Claude i Excel och PowerPoint](03-excel-powerpoint.md)**

---

*Kapitel 02 av Claude-instruktionsboken. Se [innehallsforteckningen](../README.md) for alla kapitel.*
