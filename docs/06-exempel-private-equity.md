# Exempel: Private Equity — Hela firmans AI-system

> *Du har lärt dig verktygen. Nu visar vi hur en hel PE-firma kan använda dem: från screening till exit, med en AI som blir bättre för varje uppdrag.*

---

De tidigare kapitlen har gått igenom koncepten: trappan, kontexthantering, mappstruktur, CLAUDE.md och skills. Det här kapitlet visar hur allt hänger ihop i praktiken, genom att följa en fiktiv PE-firma, **Norvik Capital**, genom hela deras arbetsdag.

Norvik Capital finns inte på riktigt. Men strukturen, arbetsflödena och exemplen är byggda för att vara realistiska. Du ska kunna ta dem och anpassa till din egen firma.

> Allt som refereras i det här kapitlet finns som färdiga filer i [`templates/private-equity/firma-exempel/`](../templates/private-equity/firma-exempel/). Du kan ge dem som utgångspunkt till Claude Code. Beskriv vad du vill anpassa så bygger Claude resten.

---

## Norvik Capital i korthet

| | |
|---|---|
| **Firma** | Norvik Capital |
| **Grundat** | 2018 |
| **Kontor** | Stockholm |
| **Strategi** | Nordisk mid-market PE: majoritets- och betydande minoritetsinvesteringar |
| **Team** | 6 personer: 2 partners, 2 VP/directors, 1 analytiker, 1 IR/admin |
| **Aktiv fond** | Norvik Capital Fund I (vintage 2020, 500 MSEK) |
| **Portfölj** | 4 bolag: CloudFlow (SaaS), Nordisk Precision (industri), Arbetslyft (bemanning), MedTech Nordic (medtech) |

Norvik är ett litet team som hanterar en bred portfölj. Varje person bär flera hattar. Det gör dem till det perfekta exemplet. Det är exakt i sådana organisationer som AI ger störst effekt.

---

## Firmans mappstruktur

Mappstrukturen speglar firmans verksamhet: firma, fonder, portföljbolag, pipeline och delade resurser. Principerna från [kapitel 03](03-mappstruktur-och-arbetssatt.md) (beskrivande namn, logisk hierarki, separation av data och analys) tillämpas konsekvent.

```
firma-exempel/
│
├── CLAUDE.md                         ← Firmabrett: regler som gäller överallt
│
├── firma/                            ← Firmanivå
│   ├── compliance/                      Regulatorisk, AML/KYC, policyer
│   ├── fundraising/                     Kapitalanskaffning
│   ├── investor-relations/              LP-kommunikation
│   └── team/                            Organisation, onboarding
│
├── fonder/                           ← En mapp per fond
│   └── fond-I/
│       ├── CLAUDE.md                    Fondspecifik kontext
│       ├── fonddata/                    Villkor, commitments, cap table
│       ├── rapportering/                Kvartals- och årsrapporter
│       └── prestanda/                   IRR, MOIC, benchmarking
│
├── portfoljbolag/                    ← En mapp per bolag
│   ├── cloudflow-ab/
│   │   ├── CLAUDE.md                    Bolagsspecifik kontext
│   │   ├── bolagsdata/                  Finansiell data, KPI:er
│   │   ├── analys/                      Värderingar, scenariomodeller
│   │   ├── styrelsearbete/              Styrelsepaket, protokoll
│   │   ├── vardeskapande/               100-dagarsplan, initiativ
│   │   └── output/                      Färdiga leveranser
│   ├── nordisk-precision-ab/
│   ├── arbetslyft-ab/
│   └── medtech-nordic-ab/
│
├── pipeline/                         ← Nya investeringsmöjligheter
│   ├── CLAUDE.md                        Screeningkriterier och regler
│   ├── screening/                       Initiala screeningar
│   ├── aktiva-processer/                Pågående DD
│   └── avslutade/                       Arkiv med motiveringar
│
└── gemensamt/                        ← Delade resurser
    ├── mallar/                          Dokumentmallar
    ├── skills/                          Claude-skills
    ├── ramverk/                         Analysramverk
    ├── learnings/                       Ackumulerade lärdomar
    └── branschdata/                     Multiplar, benchmarks
```

### Logiken bakom strukturen

Strukturen speglar tre separata nivåer med helt olika informationsbehov:

| Nivå | Mappar | Vad som händer här | Tempo |
|------|--------|--------------------|-------|
| **Firma** | `firma/`, `gemensamt/` | Compliance, fundraising, team | Förändras sällan |
| **Fond** | `fonder/fond-I/` | LP-rapportering, fondprestanda | Kvartalsvis |
| **Portföljbolag** | `portfoljbolag/[bolag]/` | Analys, styrelsematerial, värdeskapande | Löpande |

Separationen gör att Claude får **rätt kontext utan brus**. När du arbetar i `portfoljbolag/cloudflow-ab/` behöver Claude inte veta om fundraising eller LP-villkor, men den behöver veta allt om CloudFlows SaaS-nyckeltal.

### Strukturen följer en investerings livscykel

```
SOURCING           SCREENING          DUE DILIGENCE       INVESTERING
pipeline/          pipeline/          pipeline/            portfoljbolag/
screening/         screening/         aktiva-processer/    [nytt bolag]/

VÄRDESKAPANDE      RAPPORTERING       EXIT
portfoljbolag/     fonder/fond-I/     portfoljbolag/
[bolag]/           rapportering/      [bolag]/analys/
vardeskapande/
```

Mappen `gemensamt/` är firmans kunskapsbibliotek: mallar, skills, ramverk och branschdata som används på flera ställen. Principen: **en källa, många användare.**

---

## CLAUDE.md-hierarkin i praktiken

CLAUDE.md-hierarkin (beskriven i [kapitel 03](03-mappstruktur-och-arbetssatt.md)) appliceras på tre nivåer hos Norvik Capital.

### Nivå 1: Firmabrett (rot-CLAUDE.md)

Allt som gäller oavsett om du arbetar med ett portföljbolag, en pipeline-deal eller en LP-rapport:

```markdown
## Roll
Du är en erfaren Private Equity-professionell på Norvik Capital. Du har djup
kunskap om nordiska mid-market-transaktioner, portföljbolagsstyrning,
värdeskapande och LP-rapportering.

## Generella regler

### Språk och format
- Skriv alltid på svenska om inte annat anges
- Valuta: MSEK som standard, en decimal (t.ex. 42,3 MSEK)
- Tusentalsavgränsare: mellanslag (1 000)
- Datum: YYYY-MM-DD
- Tabeller för all finansiell data

### Analysstandard
- Börja alltid med en Executive Summary (max 5 punkter)
- Avsluta med handlingsbara rekommendationer
- Utgå från kassaflödesperspektiv
- Inkludera scenarioanalys (bas, bull, bear) vid värdering
```

### Nivå 2: Fond- eller pipeline-specifikt

Fond-I:s CLAUDE.md lägger till det som är specifikt för fonden:

```markdown
## Fondöversikt
| | |
|---|---|
| **Fond** | Norvik Capital Fund I |
| **Vintage** | 2020 |
| **Committed capital** | 500 MSEK |
| **Status** | Fullinvesterad — 4 portföljbolag |

## LP-rapportering
- Kvartalsrapporter: 45 dagar efter kvartalets slut
- Ton: Transparent, balanserad — flagga risker proaktivt
- NAV-metodik: Fair value enligt IPEV-riktlinjer
```

Pipeline-mappens CLAUDE.md fokuserar på screeningkriterier:

```markdown
## Screeningkriterier

### Hårda kriterier
| Kriterium | Krav |
|-----------|------|
| Enterprise value | 100–500 MSEK |
| Geografi | Norden |
| Lönsamhet | Positiv EBITDA |
| Storlek | Minst 30 MSEK i omsättning |
```

### Nivå 3: Bolagsspecifikt

Varje portföljbolag har sin egen CLAUDE.md. CloudFlows innehåller SaaS-specifika KPI:er:

```markdown
## Bolagsspecifika nyckeltal
| KPI | Definition | Senast känt |
|-----|-----------|-------------|
| ARR | Annual Recurring Revenue | 80 MSEK |
| NRR | Net Revenue Retention | Mål: >110% |
| Churn rate | Andel kunder som lämnar per år | Tracka månadsvis |
| LTV/CAC | Avkastning per förvärvad kund | Mål: >3x |
| Rule of 40 | ARR-tillväxt + EBITDA-marginal | Mål: >40 |

### Definitioner att vara noga med
- ARR: Inkludera BARA kontrakterade återkommande intäkter.
  Exkludera engångsintäkter.
```

Nordisk Precisions CLAUDE.md ser helt annorlunda ut. Den fokuserar på industrispecifika KPI:er som OEE, orderbok och kapacitetsutnyttjande.

---

## Rätt verktyg för rätt uppgift

PE-arbete innebär dussintals olika uppgifter. Nyckeln är att välja rätt verktyg baserat på uppgiftens karaktär.

### Claude Chat — med Projekt

Utmärkt för arbete med specifika dokument. Skapa ett Projekt, ladda upp filer, och skriv projektinstruktioner som gäller alla konversationer.

**Analysera en årsredovisning:**
> *"Sammanfatta de viktigaste trenderna i CloudFlows årsredovisning. Fokusera på tillväxt, marginal och kassaflöde."*

**Jämföra DD-rapporter:**
> *"Jag har laddat upp en kommersiell DD och en finansiell DD. Identifiera alla punkter där de överlappar eller motsäger varandra."*

**Bollplank inför styrelsemöte:**
> *"Baserat på board-packet, vilka tre frågor borde jag som styrelseledamot ställa?"*

### Claude i Excel

Perfekt när du redan har data i ett kalkylblad:

> *"Skriv en formel som beräknar rullande 12-månaders EBITDA baserat på månadsdata i kolumn C."*

> *"Kontrollera om balansräkningen stämmer, balanserar tillgångar med skulder plus eget kapital?"*

### Claude i PowerPoint

Hjälper med struktur och innehåll:

> *"Skapa en presentationsstruktur med 12 slides för ett IC-memo. Bolaget är ett nordiskt SaaS-bolag med 80 MSEK ARR."*

> *"Skriv speaker notes till en kvartalsvis LP-uppdatering."*

### Claude Code

Allt som gynnas av kontext, automatisering och konsistens. Så här beskriver du typiska uppgifter:

**Screening med kontext:**
```
> Vi fick en teaser på ett svenskt logistikbolag, TransportOptima AB.
> 120 MSEK omsättning, EBITDA ~18 MSEK, 12% tillväxt.
> Grundarlett, ägaren vill sälja majoriteten. Gör en screening.
```

Claude läser automatiskt `pipeline/CLAUDE.md` (med screeningkriterierna) och skapar ett strukturerat screening-memo.

**Kvartalsrapport till styrelsen:**
```
> Sammanställ kvartalsrapporten för Q3.
> ARR landade på 92 MSEK mot budget 95, NRR föll till 108%.
> Vi fick tre nya enterprise-kunder.
```

Claude läser CloudFlows CLAUDE.md, vet vilka KPI:er som ska trackas och hur styrelsepaket ska struktureras.

**LP-rapport:**
```
> Sammanställ LP-rapporten för Q3. Netto-IRR 18%, TVPI 1,4x.
> CloudFlow hade starkt kvartal, Nordisk Precision hade marginalpress.
```

### Claude Cowork

Delegation av tidskrävande research:

> *"Kartlägg den nordiska marknaden för logistik-SaaS. Identifiera de 10 största spelarna med uppskattad ARR, tillväxt, ägarbild och positionering."*

> *"Sammanställ de 10 senaste PE-transaktionerna inom nordisk bemanning de senaste 24 månaderna."*

### Kombinera verktygen

| Steg | Verktyg | Uppgift |
|------|---------|---------|
| 1 | **Cowork** | Researcha nordisk logistik-SaaS-marknad |
| 2 | **Code** | Bearbeta data, skapa jämförelsetabell |
| 3 | **Code** | Kör screening-skill på intressant bolag |
| 4 | **Excel** | Bygg snabb LBO-modell |
| 5 | **Code** | Generera IC-presentation som Markdown |
| 6 | **PowerPoint** | Finjustera presentationen visuellt |

---

## Samarbete i praktiken — hur teamet delar strukturen

Norvik Capital är sex personer. Hur delar de på strukturen?

### Vad som delas vs vad som är individuellt

| Lager | Vad | Hur det delas | Verktyg |
|-------|-----|---------------|---------|
| **Gemensam infrastruktur** | Mallar, skills, CLAUDE.md-filer, ramverk | Git-repo (GitHub/GitLab) | Claude Code |
| **Gemensam kunskap** | Årsredovisningar, DD-rapporter, styrelsematerial | Delade Projects i Claude Chat | Claude Chat |
| **Individuellt arbete** | Pågående analyser, utkast, anteckningar | Privata konversationer | Valfritt verktyg |

**Git-repot** innehåller allt som inte är konfidentiellt men som alla behöver: mappstrukturen, CLAUDE.md-filerna, skills, mallar. Det är firmans "AI-playbook".

**Delade Projects i Claude Chat** är var det dagliga arbetet sker för de flesta. Partnern skapar ett projekt för "CloudFlow AB — Styrelsemöte Q3", laddar upp styrelsepaket och kvartalsdata, och skriver projektinstruktioner baserade på CloudFlows CLAUDE.md.

### En typisk vecka på Norvik

**Måndag — Ny deal-teaser.** Analytikern öppnar Claude Code i `pipeline/` och kör screening-skillen. Memo:t pushas till repot. Partnern läser det i GitHub.

**Tisdag — Styrelsemöte förbereds.** VP:n öppnar det delade Chat-projektet "CloudFlow — Styrelsearbete" och ber Claude sammanfatta avvikelser mot budget.

**Onsdag — Snabb fråga.** Partnern öppnar Claude Chat på telefonen: *"Typiska EV/EBITDA-multiplar för nordisk bemanning?"*

**Torsdag — Modellarbete.** Analytikern använder Claude i Excel för att validera formler i en LBO-modell. Senare kör han Claude Code för ett screening-memo.

**Fredag — LP-underlag.** IR-ansvarig använder Cowork för att sammanställa underlag till LP-uppdatering. Hon itererar på utkastet i Claude Chat.

Notera mönstret: alla sex personerna använder AI, men med **olika verktyg** beroende på roll och uppgift. Alla drar nytta av samma underliggande struktur.

### Rollfördelning

| Roll | Huvudverktyg | Bidrar med | Konsumerar |
|------|-------------|------------|------------|
| **Analytiker** | Claude Code, Excel | Bygger skills, underhåller CLAUDE.md | Branschdata, ramverk |
| **VP / Director** | Claude Chat (Projects) | Styrelsematerial, bolagsanalyser | Skills som processdokumentation |
| **Partner** | Claude Chat, telefon | Strategiska beslut, snabba frågor | Screening-memon, rapporter |
| **IR / Admin** | Claude Chat, Cowork | LP-rapporter, fonddokumentation | Mallar, lärdomar |

### Datasäkerhet

| Typ av data | Hör hemma i | Hör INTE hemma i |
|-------------|-------------|-------------------|
| CLAUDE.md-filer, skills, mallar | Git-repo | — |
| Anonymiserade ramverk och branschdata | Git-repo | — |
| Årsredovisningar, finansiell data | Claude Chat Projects (delat) | Git-repo |
| DD-rapporter, avtal | Claude Chat Projects (begränsad åtkomst) | Git-repo |
| Pågående utkast, hypoteser | Privata konversationer | Git-repo, delade Projects |

---

## Självinlärning — hur Claude blir bättre över tid

### Konceptet

AI-modellen i sig förändras inte mellan sessioner. Men du kan bygga minnet **utanför modellen**.

**Analogi:** Tänk på en konsultfirma som dokumenterar projekterfarenheter. Individerna kommer och går, men kunskapen stannar.

Norvik Capitals självinlärningssystem:

1. **Claude utför en uppgift,** till exempel en kvartalsrapport
2. **Claude reflekterar:** vad fungerade, vad var problematiskt?
3. **En lärdom dokumenteras:** konkret, generaliserbar, formulerad som instruktion
4. **Användaren granskar:** bekräftar att lärdomen är korrekt
5. **Lärdomen inarbetas:** skrivs in i relevant CLAUDE.md eller skill-fil
6. **Nästa session blir bättre:** Claude läser den uppdaterade instruktionen automatiskt

### Implementering

**Instruktioner i rot-CLAUDE.md:**

```markdown
## Självinlärning

### Efter varje slutförd uppgift — fråga dig själv:
1. Vad lärde jag mig om data (format, kvalitet, var den fanns)?
2. Vad lärde jag mig om struktur (mapporganisation, konventioner)?
3. Vad lärde jag mig om format (vad fungerade i output)?
4. Vad lärde jag mig om process (arbetsordning, effektivitet)?

Om svaret innehåller något värdefullt — dokumentera det.
```

**En lärdomar-fil** (`gemensamt/learnings/LEARNINGS.md`):

```markdown
### LP-rapporter kräver aggregerad data — inte bolagsspecifika detaljer
- **Datum:** 2024-11-08
- **Uppgift:** Kvartalsrapport till LP:er för Q3
- **Problematiskt:** Första utkastet inkluderade detaljerade KPI:er per
  portföljbolag som är för granulära för LP-rapportering.
- **Lärdom:** Vid LP-rapportering, sammanfatta per bolag på hög nivå:
  omsättning, EBITDA, tillväxt, strategisk status.
- **Status:** [GRANSKAD]
```

**Livscykel med fyra stadier:**

| Status | Betydelse |
|--------|-----------|
| **[NY]** | Dokumenterad av Claude — väntar på granskning |
| **[GRANSKAD]** | Godkänd av användaren — redo att inarbetas |
| **[INARBETAD]** | Inskriven i CLAUDE.md eller skill — aktiv i systemet |
| **[ARKIVERAD]** | Inte längre aktuell |

### Begränsningar — var vaksam

**Lärdomar kan vara felaktiga.** Mänsklig granskning är inte valfritt.

**Instruktionsbloat.** Varje inarbetad lärdom gör CLAUDE.md längre. Var disciplinerad: inarbeta bara det som verkligen förbättrar konsistensen.

**Dåliga mönster kan förstärkas.** Om en felaktig lärdom inarbetas fortsätter Claude att följa den. Granskningssteget är ditt skydd.

---

## Kom igång — så här beskriver du det för Claude Code

### Börja i chatten

Öppna Claude Chat och beskriv din situation:

> *"Jag jobbar på en PE-firma med [X] portföljbolag. Vi gör nordisk mid-market PE, och jag behöver ett AI-system som hjälper med screening, portföljbolagsanalys, styrelsematerial och LP-rapportering. Hjälp mig tänka igenom vad det borde innehålla."*

Diskutera och iterera. Be sedan chatten ta fram en terminalredo prompt.

### En exempelprompt för Claude Code

Här är en prompt du kan anpassa och ge till Claude Code:

```
Skapa ett PE-firmaprojekt med följande struktur:

- firma/ med undermappar för compliance, fundraising och investor-relations
- fonder/fond-I/ med fonddata, rapportering och prestanda
- portfoljbolag/ med en mapp per bolag (bolag-x), vardera med
  bolagsdata, analys, styrelsearbete, vardeskapande och output
- pipeline/ med screening, aktiva-processer och avslutade
- gemensamt/ med mallar, skills, ramverk, learnings och branschdata

Skapa en CLAUDE.md i roten med:
- Roll: erfaren PE-analytiker, nordisk mid-market
- Regler: svenska, MSEK, en decimal, Executive Summary först,
  rekommendation sist
- Markera saknad data med [DATA SAKNAS]

Skapa bolagsspecifika CLAUDE.md-filer för bolag-x med relevanta KPI:er.

Skapa en pipeline/CLAUDE.md med screeningkriterier:
- EV: 100–500 MSEK, Norden, positiv EBITDA, minst 30 MSEK omsättning

Skapa skills för:
- /screening — screening av nya investeringsmöjligheter
- /kvartalsrapport — sammanställ kvartalsrapport för portföljbolag
- /lp-rapport — sammanställ LP-rapport för fonden

Initiera ett Git-repo.
```

Claude Code skapar hela strukturen: alla mappar, CLAUDE.md-filer på varje nivå, skills och Git-repo.

### Nästa steg

1. **Lägg in dina filer:** kopiera årsredovisningar, kvartalsdata och andra dokument till rätt `bolagsdata/`-mappar
2. **Extrahera till Markdown:** be Claude Code läsa PDF:erna och skapa Markdown-versioner
3. **Testa med en riktig uppgift:** till exempel: *"Sammanfatta nyckeltal för de senaste tre åren för bolag X"*
4. **Iterera:** be Claude Code justera CLAUDE.md, lägga till fler skills, starta en lärdomsfil

### Vad ger mest effekt snabbast?

| Åtgärd | Effekt |
|--------|--------|
| Ge Claude Code en bra projektbeskrivning | Hela grundstrukturen skapas på minuter |
| Kopiera in bolagsdata och extrahera till Markdown | Claude hittar rätt data utan att du pekar |
| Testa en vanlig uppgift (screening, kvartalsrapport) | Du ser direkt vad som fungerar och behöver justeras |
| Starta en lärdomsfil | Systemet börjar bli bättre över tid |

Börja enkelt. Varje session gör systemet lite bättre.

---

## Avslutning

Det här kapitlet har visat hur koncepten från Del 1 hänger ihop i PE-praktiken:

- **Mappstruktur** som speglar firmans verksamhet: från fond till portföljbolag till pipeline
- **CLAUDE.md-hierarki** med firmaregler, fondspecifikt och bolagsspecifikt
- **Rätt verktyg för rätt uppgift:** Chat, Excel, PowerPoint, Code och Cowork i kombination
- **Teamsamarbete** där alla bidrar och konsumerar, med olika verktyg
- **Självinlärning** som gör systemet bättre för varje session

Norvik Capital är fiktivt. Men strukturen och arbetsflödena är byggda för att vara direkt användbara. Kopiera det som passar. Anpassa det som behöver justeras. Och börja enkelt.

---

> *Föregående kapitel: [05 — Exempel: Studier](05-exempel-studier.md)*
>
> *Nästa kapitel: [07 — Exempel: Marknadsförare](07-exempel-marknadsforing.md)*
