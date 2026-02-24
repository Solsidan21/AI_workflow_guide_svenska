# Kapitel 03 — Claude i Excel och PowerPoint

> **Sammanfattning:** Claude finns som tillagg direkt i Microsoft Excel och PowerPoint. I det har kapitlet lar du dig installera tilllaggen, anvanda dem i praktiken och forsta nar du ska anvanda tilllaggen respektive Claude Chat.

---

## Innehall

1. [Oversikt — Vad ar Claude i Excel och PowerPoint?](#oversikt--vad-ar-claude-i-excel-och-powerpoint)
2. [Installation](#installation)
3. [Claude i Excel](#claude-i-excel)
4. [Claude i PowerPoint](#claude-i-powerpoint)
5. [Jamforelse med Claude Chat](#jamforelse-med-claude-chat)
6. [Tips och begransningar](#tips-och-begransningar)
7. [Nasta steg](#nasta-steg)

---

## Oversikt — Vad ar Claude i Excel och PowerPoint?

Under 2025 slappte Anthropic officiella tillagg (add-ins) for Microsoft Excel och PowerPoint. Det innebar att du kan anvanda Claude direkt inne i programmen du redan arbetar i — utan att behova vaxla till claude.ai, kopiera data och klistra in svar.

**Grundtanken ar enkel:** Markera data i Excel och stall en fraga. Eller be Claude skapa en presentation direkt i PowerPoint. Allt sker i samma fonster dar du redan arbetar.

### Krav

| Krav | Detalj |
|------|--------|
| **Microsoft 365** | Tilllaggen kraver Microsoft 365 (tidigare Office 365). Friliggande versioner av Excel/PowerPoint stods inte. |
| **Claude-prenumeration** | Du behover minst **Claude Pro** (20 USD/manad). Team- och Enterprise-planer fungerar ocksa. Den kostnadsfria Claude-planen racker inte. |
| **Plattform** | Fungerar i Excel och PowerPoint for Windows, Mac och webben (Office Online). |

---

## Installation

Installationen gar genom Microsoft 365:s inbyggda system for tillagg.

### Steg for steg

1. **Oppna Excel eller PowerPoint.**

2. **Ga till tilllagg.** Klicka pa **Infoga** (Insert) i menyraden och sedan **Tillagg** (Add-ins) eller **Hamta tillagg** (Get Add-ins).

3. **Sok efter Claude.** Skriv "Claude" eller "Anthropic" i sokfaltet i tilllaggsbutiken.

4. **Installera.** Klicka pa **Lagg till** (Add) bredvid "Claude for Excel" respektive "Claude for PowerPoint".

5. **Logga in.** Forsta gangen du anvander tillagget ombeds du logga in med ditt Claude-konto (samma konto som pa claude.ai).

6. **Klart.** Claude dyker nu upp som en panel eller flik inne i ditt program.

> **IT-administratorer:** Om tilllaggsbutiken ar lasd i er organisation behover IT-avdelningen godkanna Anthropics tillagg via Microsoft 365 Admin Center. Ber dem soka efter "Claude for Microsoft 365" i listan over tillgangliga tillagg.

---

## Claude i Excel

### Hur det fungerar

Nar du har installerat tillagget visas en Claude-panel i Excel. Arbetsfloden ar:

1. **Markera de celler** som innehaller data du vill arbeta med.
2. **Oppna Claude-panelen** (vanligtvis via en knapp i menyraden eller en sidopanel).
3. **Stall din fraga** — beskriv vad du vill gora med den markerade datan.
4. **Granska svaret** — Claude svarar med text, formler eller foreslar andringar.
5. **Applicera** — du valjer sjalv om och hur du anvander Claudes forslag.

### Praktiska exempel

#### Analysera finansiell data

Du har ett kalkylblad med kvartalsvis kassaflode for ett portfoljbolag. Markera dataintervallet och fraga:

> "Sammanfatta trenderna i detta kassaflode. Vilka kvartal avviker och vad kan forklara det?"

Claude analyserar siffrorna, identifierar monster och ger en skriftlig sammanfattning — direkt i Excel.

#### Skapa formler

Du vet vad du vill berakna, men inte exakt vilken Excel-formel som behovs:

> "Skriv en formel som beraknar IRR for kassaflodena i B2:B10, dar den initiala investeringen star i B2."

Claude returnerar en fardig formel som du kan klistra in i ratt cell:

```
=IRR(B2:B10)
```

For mer komplexa fall — till exempel modifierad IRR (MIRR) med angivna rantor — formulerar Claude formeln at dig och forklarar parametrarna.

#### Rengora data

Dina data ar rörigt importerade fran olika kallor. Namnen ar ibland "AB Foretag X", ibland "Foretag X AB", ibland "foretag x":

> "Hjalp mig identifiera och harmonisera foretagsnamnen i kolumn A. Ge mig en lista med dubbletter och foresla en standardiserad version."

Claude kan ocksa foresla formler for datarengoring, till exempel TRIM, CLEAN, PROPER eller SUBSTITUTE.

#### Scenario-analys

Du har byggt en varderingsmodell och vill testa kansligheten:

> "Vad hander med varderingen i cell F25 om tillvaxten i cell C5 sjunker fran 8% till 3%? Gora en kanslighetstabell med tillvaxt fran 2% till 10% i steg om 1 procentenhet."

Claude kan hjalpa dig strukturera scenarioanalysen och foresla hur du bygger en datatabell (Data Table) i Excel.

### Styrkor

- **Snabbt och bekvämt.** Du slipper vaxla fonster. Fragan och svaret sker dar datan ar.
- **Ingen kontextvaxling.** Du behover inte kopiera data till claude.ai och sedan tillbaka.
- **Bra for snabba fragor.** "Vad gor den har formeln?" eller "Varfor ger den har cellen #REF?" ar perfekta anvandningsomraden.
- **Formelstod.** Manga anvandare tycker att formelhjalp ar den allra mest vardefulla funktionen.

### Svagheter

- **Begransad kontext.** Tillagget kan inte se hela arbetsboken pa en gang. Det arbetar framst med den data du markerar, vilket innebar att det saknar den helhetsbild som du sjalv har.
- **Enklare analyser.** For djupare resonemang — till exempel en fullstandig vardering med flera steg — ar Claude Chat battre lämpad.
- **Ingen Project Knowledge.** Tillagget har inte tillgang till dina projekt pa claude.ai. Det kan inte referera till arsredovisningar du laddat upp i ett projekt.

---

## Claude i PowerPoint

### Hur det fungerar

Claude-tillagget i PowerPoint hjalper dig skapa och redigera presentationer. Du kan:

1. **Beskriva en presentation** i text, och Claude skapar ett utkast med slides.
2. **Markera befintliga slides** och be Claude omformulera, forkorta eller utoka.
3. **Generera innehall** for enskilda slides — text, bullet points, speaker notes.

### Praktiska exempel

#### Skapa presentationsutkast fran text

Du har skrivit en textsammanfattning av en kvartalsrapport och vill gora en presentation:

> "Skapa en presentation med 8-10 slides baserat pa foljande sammanfattning av Q3-resultatet for Portfoljbolag X. Inkludera en titelsida, agenda, finansiell oversikt, operativa hojdpunkter, utmaningar, nasta steg och en avslutande sammanfattningssida."

Claude genererar ett utkast med text och struktur for varje slide. Du far en solid grund att arbeta vidare fran.

#### Omformatera befintliga slides

Du har en presentation med for mycket text pa varje slide:

> "Forkorta texten pa den har sliden till max 4 bullet points. Behall nyckelbudskapet men gor det mer presentationsvanligt."

#### Generera speaker notes

Du har en presentation med bra slides men saknar talanteckningar:

> "Skriv speaker notes for den har sliden. Anteckningarna ska vara 3-4 meningar som utvecklar punkterna pa sliden och ger exempel."

#### PE-exempel: Quarterly update for investerare

Du ska skapa en kvartalspresentation for era investerare:

> "Skapa en presentation for var kvartalsvisa investeraruppdatering med foljande struktur:
>
> Slide 1: Titelsida — 'Q3 2025 Investor Update, Fond IV'
> Slide 2: Agenda
> Slide 3: Fondoversikt (nyckeltal: NAV, DPI, TVPI)
> Slide 4-6: Portfoljbolagens utveckling (ett bolag per slide)
> Slide 7: Vardeskapandeinitiativ — status
> Slide 8: Pipeline och kommande aktiviteter
> Slide 9: Avslutning och Q&A
>
> Anvand ett professionellt, aterstallt spraak. Inkludera platshallare dar jag behover fylla i siffror."

### Styrkor

- **Snabb forsta draft.** Istallet for att stirra pa en tom presentation kan du ha en struktur pa minuter.
- **Bra for innehallsstruktur.** Claude ar stark pa att organisera information logiskt och valja ratt detaljniva for en presentationsformat.
- **Speaker notes.** Att generera talanteckningar ar en av de allra mest tidsbesparande funktionerna.

### Svagheter

- **Begransad designkontroll.** Claude kan inte finjustera layouter, fargscheman eller grafik. Resultatet ar funktionellt men inte visuellt polerat.
- **Fungerar bast som startpunkt.** Tankt pa Claudes output som en "forsta draft" — du behover alltid ga igenom och justera. Speciellt grafiska element och exakt formatering.
- **Mallar.** Tillagget har begransad formaga att folja din organisations PowerPoint-mall perfekt. Du kan behova applicera mallen manuellt efterat.

> **Tips:** Det mest effektiva arbetsfloden ar att lata Claude skapa strukturen och innehallet, och sedan sjalv finjustera design och formatering. Forsok inte fa Claude att producera en "fardig" presentation — anvand den som en snabb startpunkt.

---

## Jamforelse med Claude Chat

En vanlig fraga ar: "Nar ska jag anvanda tillagget i Excel/PowerPoint, och nar ska jag anvanda Claude Chat pa claude.ai?" Har ar en oversikt.

### Anvand tilllaggen nar:

| Situation | Varfor tillagget ar battre |
|-----------|--------------------------|
| Du vill ha hjalp med en specifik formel | Claude ser dina celler direkt |
| Du vill forsta vad en formel gor | Markera cellen och fraga |
| Du behover en snabb sammanfattning av ett dataintervall | Snabbare an att kopiera datan |
| Du vill skapa en forsta presentation fran en beskrivning | Resultatet hamnar direkt i PowerPoint |
| Du jobbar i flodet och vill inte vaxla fonster | Mindre friktion |

### Anvand Claude Chat nar:

| Situation | Varfor Chat ar battre |
|-----------|----------------------|
| Du behover analysera flera dokument samtidigt | Chat har storre kontextfonster och Project Knowledge |
| Analysen ar komplex och kraver flera steg | Chat ar battre pa langa resonemang |
| Du vill iterera och bygga vidare pa analysen | Konversationsformatet ar overlägset |
| Du behover referera till information fran olika kallor | Projekt med kunskapsbas slår allt annat |
| Du vill ha en langre rapport eller PM | Artifacts ger snyggare output |

### Tumregel

> **Tillagget** = snabba, avgransade fragor nar du redan arbetar i Excel eller PowerPoint.
>
> **Claude Chat** = djupare analyser, langre dokument, arbete som kraver mer kontext.

Manga anvandare anvander bada dagligen: tillagget for det snabba och operativa, Claude Chat for det strategiska och analytiska.

---

## Tips och begransningar

### Dataintegritet — Vad skickas till Anthropic?

Nar du anvander tilllagget skickas den data du markerar (eller hela presentationen, beroende pa fragan) till Anthropics servrar for att bearbetas av Claude. Det ar viktigt att forsta:

- **Data som skickas behandlas enligt Anthropics anvandarpolicy.** Med betalda planer (Pro, Team, Enterprise) anvands inte din data for att trana modeller.
- **Enterprise-planer** erbjuder ytterligare garantier, inklusive databehandling inom specifika regioner.
- **Kontrollera med din organisation.** Om du arbetar med konfidentiell information (till exempel klintdata eller opublicerade finansiella uppgifter), kontrollera med din IT-avdelning eller compliancefunktion innan du anvander tillagget.

> **Rekommendation:** Behandla Claude-tillaggen som du skulle behandla vilken molntjanst som helst. Om du inte skulle ladda upp datan till Google Drive eller OneDrive av integritetsskal, var forsiktig med att anvanda den i Claude-tillagget ocksa.

### Begransningar i nuvarande version

- **Ingen offlinekapacitet.** Tillaggen kraver internetuppkoppling.
- **Svarstider.** Komplexa fragor kan ta nagra sekunder. For mycket komplexa fragor (stora dataomraden, flera steg) kan det ta langre.
- **Begransad formatering i PowerPoint.** Tillagget ar starkt pa innehall men begransat pa avancerad design.
- **Sprakstod.** Tillaggen fungerar bra pa svenska, men menyerna kan vara pa engelska beroende pa din Microsoft 365-installning.
- **Uppdateringar.** Anthropic uppdaterar tillaggen regelbundet. Funktionaliteten som beskrivs har kan utvidgas over tid.

### Basta praxis for att fa bra resultat

1. **Markera relevant data, inte hela arket.** Ju mer fokuserad data du ger Claude, desto battre och snabbare svar far du.

2. **Ge kontext i din fraga.** Aven i tilllagget hjalper det att vara specifik:
   > "Det har ar kassaflodesdata for ett tillverkningsforetag 2020-2024. Vilka trender ser du?"
   ar battre an:
   > "Analysera den har datan."

3. **Anvand tillagget for formler, Chat for strategiska insikter.** Om du vill ha en formel ar tillagget perfekt. Om du vill ha en investeringsrekommendation, anvand Claude Chat med ett projekt.

4. **Dubbelkolla alltid formler.** Claude ar bra pa Excel-formler, men inte ofelbar. Kontrollera att formeln refererar till ratt celler och ger ett rimligt resultat innan du anvander den vidare.

5. **Spara regelbundet.** Nar Claude gor andringar i ditt kalkylblad eller din presentation — spara en version innan du applicerar forslagen. Da kan du alltid ga tillbaka om nagot inte blev som tankt.

---

## Nasta steg

Du har nu sett hur Claude kan arbeta direkt inne i dina vanligaste verktyg. Men ibland behover du mer kraft, mer kontext och mer kontroll an vad tilllaggen kan erbjuda.

I nasta kapitel utforskar vi **Claude Code** — Claudes mest kraftfulla granssnitt. Det kraver en terminal, men oroa dig inte: vi tar det steg for steg, och du behover inte vara programmerare for att fa ut enormt mycket av det.

**Ga vidare till: [Kapitel 04 — Claude Code](04-claude-code.md)**

---

*Kapitel 03 av Claude-instruktionsboken. Se [innehallsforteckningen](../README.md) for alla kapitel.*
