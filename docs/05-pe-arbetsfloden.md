# Kapitel 05 — PE-arbetsflöden med Claude

> *Du har lärt dig verktygen. Nu visar vi hur en hel firma kan använda dem — från screening till exit, med en AI som blir bättre för varje uppdrag.*

---

De tidigare kapitlen har gått igenom verktygen: chatten, Claude Code, Cowork, mappstruktur och CLAUDE.md. Du vet vad de gör. Det här kapitlet visar hur allt hänger ihop i praktiken — genom att följa en fiktiv PE-firma, **Norvik Capital**, genom hela deras arbetsdag.

Norvik Capital finns inte på riktigt. Men strukturen, arbetsflödena och exemplen är byggda för att vara realistiska — du ska kunna ta dem och anpassa till din egen firma.

!!! note "Kapitlet bygger på en komplett exempelstruktur"
    Allt som refereras i det här kapitlet finns som färdiga filer i [`templates/private-equity/firma-exempel/`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates/private-equity/firma-exempel). Du kan kopiera hela mappen och börja använda den direkt.

---

## Norvik Capital i korthet

| | |
|---|---|
| **Firma** | Norvik Capital |
| **Grundat** | 2018 |
| **Kontor** | Stockholm |
| **Strategi** | Nordisk mid-market PE — majoritets- och betydande minoritetsinvesteringar |
| **Team** | 6 personer: 2 partners, 2 VP/directors, 1 analytiker, 1 IR/admin |
| **Aktiv fond** | Norvik Capital Fund I (vintage 2020, 500 MSEK) |
| **Portfölj** | 4 bolag: CloudFlow (SaaS), Nordisk Precision (industri), Arbetslyft (bemanning), MedTech Nordic (medtech) |

Norvik är ett litet team som hanterar en bred portfölj. Varje person bär flera hattar. Det gör dem till det perfekta exemplet — det är exakt i sådana organisationer som AI ger störst effekt, eftersom tid och resurser är knappa.

---

## Firmans mappstruktur

I [kapitel 04](04-mappstruktur-och-kontext.md) lärde du dig att mappstruktur är kontext — att filnamn och mappar i sig själva ger AI information. Här tar vi det ett steg längre: en hel firma organiserad så att Claude alltid har rätt kontext för rätt uppgift.

### Den kompletta strukturen

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
| **Firma** | `firma/`, `gemensamt/` | Compliance, fundraising, team — saker som gäller oavsett fond eller bolag | Förändras sällan |
| **Fond** | `fonder/fond-I/` | LP-rapportering, fondprestanda, fondvillkor — specifikt för en fond | Kvartalsvis |
| **Portföljbolag** | `portfoljbolag/[bolag]/` | Analys, styrelsematerial, värdeskapande — det dagliga arbetet | Löpande |

Separationen gör att Claude får **rätt kontext utan brus**. När du arbetar i `portfoljbolag/cloudflow-ab/` behöver Claude inte veta om fundraising eller LP-villkor — men den behöver veta allt om CloudFlows SaaS-nyckeltal och värdeskapandeplan.

### Strukturen följer en investerings livscykel

En mappstruktur som speglar verkligheten gör att du aldrig behöver fundera över var något hör hemma:

```
SOURCING           SCREENING          DUE DILIGENCE       INVESTERING
pipeline/          pipeline/          pipeline/            portfoljbolag/
screening/         screening/         aktiva-processer/    [nytt bolag]/

     ↓                  ↓                   ↓                    ↓

VÄRDESKAPANDE      RAPPORTERING       EXIT-FÖRBEREDELSE    EXIT
portfoljbolag/     fonder/fond-I/     portfoljbolag/       fonder/fond-I/
[bolag]/           rapportering/      [bolag]/analys/      prestanda/
vardeskapande/
```

**Analogi:** Tänk på ett bokföringssystem. Transaktioner hamnar automatiskt på rätt konto baserat på typ. Du behöver inte fundera — systemet styr. Mappstrukturen fungerar på samma sätt. Ett screening-memo hamnar i `pipeline/screening/`. En kvartalsrapport till styrelsen hamnar i `portfoljbolag/[bolag]/styrelsearbete/`. En LP-rapport hamnar i `fonder/fond-I/rapportering/`.

### Gemensamma resurser undviker duplicering

Mappen `gemensamt/` är firmans kunskapsbibliotek — mallar, skills, ramverk och branschdata som används på flera ställen. Principen är enkel: **en källa, många användare.** När du uppdaterar DD-checklistan i `gemensamt/ramverk/` gäller den överallt.

---

## CLAUDE.md-hierarkin

I kapitel 02 och 04 lärde du dig att CLAUDE.md är instruktionsfilen som Claude läser automatiskt. Här bygger vi ut konceptet: en **hierarki** av CLAUDE.md-filer där generella regler gäller på toppen och specifik information finns längst ner.

### Principen: ärv, upprepa inte

```
firma-exempel/
├── CLAUDE.md                      ← Nivå 1: Gäller ALLT arbete
│
├── fonder/fond-I/
│   └── CLAUDE.md                  ← Nivå 2: Gäller fond-arbete
│
├── portfoljbolag/cloudflow-ab/
│   └── CLAUDE.md                  ← Nivå 3: Gäller CloudFlow-arbete
│
└── pipeline/
    └── CLAUDE.md                  ← Nivå 2: Gäller pipeline-arbete
```

Claude Code läser alla CLAUDE.md-filer **uppåt i hierarkin** från den mapp du arbetar i. Om du öppnar Claude Code i `portfoljbolag/cloudflow-ab/` läser den:

1. `portfoljbolag/cloudflow-ab/CLAUDE.md` (CloudFlow-specifikt)
2. `CLAUDE.md` i roten (firmabrett)

Det innebär att du aldrig behöver upprepa generella regler i varje CLAUDE.md-fil. Skriv det **en gång**, på rätt nivå.

### Nivå 1: Firmabrett (rot-CLAUDE.md)

Det här är fundamentet. Allt som gäller oavsett om du arbetar med ett portföljbolag, en pipeline-deal eller en LP-rapport. Ur Norvik Capitals rot-CLAUDE.md:

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

**Vad hör hemma här:** Allt som alla i teamet alltid ska följa — språk, format, ton, generella analysregler, firmakontext och mappöversikt.

### Nivå 2: Fond- eller pipeline-specifikt

Fond-I:s CLAUDE.md lägger till det som är specifikt för fonden — utan att upprepa de generella reglerna:

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

Pipeline-mappens CLAUDE.md fokuserar istället på screeningkriterier:

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

**Vad hör hemma här:** Det som gäller för alla uppgifter *inom den kontexten* men inte för resten av firman.

### Nivå 3: Bolagsspecifikt

Varje portföljbolag har sin egen CLAUDE.md med det som gör just det bolaget unikt. CloudFlows CLAUDE.md innehåller SaaS-specifika KPI:er:

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

Nordisk Precisions CLAUDE.md ser helt annorlunda ut — den fokuserar på industrispecifika KPI:er som OEE, orderbok och kapacitetsutnyttjande.

**Vad hör hemma här:** Allt som är unikt för detta specifika bolag — affärsmodell, investeringstes, specifika KPI:er, styrelseinformation.

### Tumregler för vad som hör hemma var

| Fråga att ställa | Svaret styr placeringen |
|-------------------|------------------------|
| "Gäller det oavsett vilket bolag jag arbetar med?" | → Rot-CLAUDE.md |
| "Gäller det bara för den här fonden / pipeline-arbete?" | → Fond-/pipeline-CLAUDE.md |
| "Gäller det bara för det här specifika bolaget?" | → Bolagets CLAUDE.md |
| "Gäller det bara för den här specifika uppgiften?" | → En skill-fil istället |

---

## Rätt verktyg för rätt uppgift

PE-arbete innebär dussintals olika uppgifter — från snabba frågor till stora sammanställningar. Ingen enskild verktygsyta är bäst för allt. Nyckeln är att välja rätt verktyg baserat på uppgiftens karaktär.

### Översikt

| Verktyg | Bäst för | Begränsning |
|---------|----------|-------------|
| **Claude Chat** (med Projekt) | Snabba frågor, bollplank, dokumentanalys | Inget minne mellan sessioner (utan Projekt), manuell copy-paste |
| **Claude i Excel** | Finansiell analys direkt i kalkylbladet | Ingen kontext, varje fråga från noll |
| **Claude i PowerPoint** | Presentationsutkast och struktur | Ingen kontext, begränsat formatstöd |
| **Claude Code** | Allt som gynnas av regler, kontext och automatisering | Kräver terminal |
| **Claude Cowork** | Längre research och autonoma uppgifter | Behöver tydliga instruktioner, resultat kräver granskning |

### Claude Chat — med Projekt

Claude Chat med Projects är utmärkt för arbete med specifika dokument. Du laddar upp filer och skriver projektinstruktioner som gäller för alla konversationer inom projektet.

**Exempel 1: Analysera en årsredovisning**

Skapa ett Projekt, ladda upp årsredovisningen, och skriv i projektinstruktionerna:

> *"Du analyserar årsredovisningar för Norvik Capital. Fokusera på omsättning, EBITDA, kassaflöde och skuldsättning. Svara alltid på svenska med siffror i MSEK."*

Sedan kan du ställa frågor i flera konversationer som alla delar samma kontext:

> *"Sammanfatta de viktigaste trenderna i CloudFlows årsredovisning. Fokusera på tillväxt, marginal och kassaflöde."*

**Exempel 2: Jämföra DD-rapporter**

Ladda upp två DD-rapporter i samma Projekt:

> *"Jag har laddat upp en kommersiell DD och en finansiell DD för samma bolag. Identifiera alla punkter där de överlappar eller motsäger varandra. Rangordna de tre viktigaste riskerna som lyfts i båda rapporterna."*

**Exempel 3: Bollplank inför styrelsemöte**

Ladda upp det senaste styrelsepaketet:

> *"Jag förbereder mig för CloudFlows styrelsemöte imorgon. Baserat på board-packet, vilka tre frågor borde jag som styrelseledamot ställa? Fokusera på områden där data pekar åt olika håll eller där information saknas."*

**Exempel 4: Snabb marknadsfråga**

Utan uppladdade filer — enkel chattfråga:

> *"Vad är typiska EV/EBITDA-multiplar för nordiska industribolag inom CNC-bearbetning? Ge mig ett intervall och nämn 2–3 jämförbara transaktioner om du känner till dem."*

**Styrkan:** Snabbt, enkelt, bra för engångsanalyser och bollplank. Med Projects slipper du upprepa kontexten.

**Begränsningen:** Du arbetar fortfarande med copy-paste. Det finns inga skills, inget automatiskt minne mellan sessioner, och Claude kan inte skriva tillbaka till dina filer.

### Claude i Excel

Excel-tillägget är perfekt när du redan har data i ett kalkylblad och vill få hjälp med analys utan att lämna verktyget.

**Exempel 1: Formelhjälp**

> *"Skriv en formel som beräknar rullande 12-månaders EBITDA baserat på månadsdata i kolumn C."*

**Exempel 2: Trendanalys**

Markera en dataserier med kvartalsvis omsättning:

> *"Sammanfatta trenden i dessa siffror. Vad är CAGR över perioden? Finns det säsongsmönster?"*

**Exempel 3: Scenariomodellering**

Med en befintlig LBO-modell öppen:

> *"Jag har en LBO-modell med bas, bull och bear-scenario. Hjälp mig att lägga till ett fjärde scenario — 'recession' — med 15% omsättningstapp år 1, återhämtning år 2–3. Vilka celler behöver jag ändra?"*

**Exempel 4: Datavalidering**

> *"Kontrollera om balansräkningen i de här cellerna stämmer — balanserar tillgångar med skulder plus eget kapital för varje år?"*

**Styrkan:** Du stannar i Excel. Ingen kontextväxling. Perfekt för snabba operativa frågor.

**Begränsningen:** Ingen kontext, inga regler, varje fråga från noll. Passar inte för uppgifter som kräver firmakontext.

### Claude i PowerPoint

PowerPoint-tillägget hjälper med struktur och innehåll — men det tunga designarbetet gör du fortfarande själv (eller med firmans mallar).

**Exempel 1: IC-presentation**

> *"Skapa en presentationsstruktur med 12 slides för ett IC-memo. Bolaget är ett nordiskt SaaS-bolag med 80 MSEK ARR. Inkludera: executive summary, marknad, bolag, finansiell analys, värdering (tre scenarier), risker och rekommendation."*

**Exempel 2: LP-uppdatering**

> *"Skriv speaker notes till en kvartalsvis LP-uppdatering. Fonden har fyra portföljbolag, netto-IRR 18%, TVPI 1,4x. CloudFlow hade ett starkt kvartal. Nordisk Precision hade marginalpress pga materialpriser."*

**Exempel 3: Styrelsematerial**

> *"Jag har en slide med CloudFlows KPI-tabell. Skriv en sammanfattande bullet-lista (max 5 punkter) som lyfter det viktigaste — vad ska styrelseledamöterna fokusera på?"*

**Exempel 4: Exitpresentation**

> *"Skapa en disposition för en exit-presentation till potentiella köpare. Bolaget är Nordisk Precision, ett industribolag med 220 MSEK omsättning och 18% EBITDA-marginal. Betona kvalitet, marknadsposition och tillväxtpotential."*

**Styrkan:** Snabbt sätt att få struktur och innehåll på plats.

**Begränsningen:** PowerPoint-tillägget har begränsat formatstöd. Det producerar text och struktur, inte visuell design. Bäst som startpunkt som du sedan finsliper.

### Claude Code

Här sker språnget. Claude Code arbetar med dina lokala filer, följer CLAUDE.md-regler och använder skills. Det är verktyget för allt som gynnas av kontext, automatisering och konsistens.

**Exempel 1: Screening med en skill**

Du står i `pipeline/`-mappen och skriver:

```
> Vi fick en teaser på ett svenskt logistikbolag, TransportOptima AB.
> 120 MSEK omsättning, EBITDA ~18 MSEK, 12% tillväxt.
> Grundarlett, ägaren vill sälja majoriteten. Gör en screening.
```

Claude läser automatiskt `pipeline/CLAUDE.md` (med screeningkriterierna) och aktiverar screening-memo-skillen. Den vet att den ska kontrollera mot hårda och mjuka kriterier, formulera investeringslogik, identifiera risker och ge en tydlig rekommendation. Resultatet sparas som en strukturerad fil i `pipeline/screening/`.

**Exempel 2: Kvartalsrapport till styrelsen**

Du står i `portfoljbolag/cloudflow-ab/` och skriver:

```
> Sammanställ kvartalsrapporten för Q3 2025 inför styrelsemötet.
> ARR landade på 92 MSEK mot budget 95, NRR föll till 108%.
> Vi fick tre nya enterprise-kunder.
```

Claude läser CloudFlows CLAUDE.md, vet vilka SaaS-KPI:er som ska trackas, vilka trafikljuströsklar som gäller och hur styrelsepaket ska struktureras. Rapporten innehåller automatiskt MRR-bridge, KPI-dashboard med trafikljus och statusuppdatering på värdeskapandeinitiativ.

**Exempel 3: LP-rapport**

Du står i `fonder/fond-I/` och skriver:

```
> Sammanställ LP-rapporten för Q3 2025. Netto-IRR 18%, TVPI 1,4x.
> CloudFlow hade starkt kvartal, Nordisk Precision hade marginalpress.
```

Claude läser fond-I:s CLAUDE.md, vet att LP-rapporter ska vara på aggregerad nivå (inte bolagsinterna KPI:er), inkludera fondnyckeltal med jämförelse mot föregående kvartal, och hålla en transparent men balanserad ton.

**Exempel 4: Automatisera rapportgenerering**

```
> Skapa en PDF av kvartalsrapporten jag just skrev.
> Använd layouten i gemensamt/mallar/ med Norvik Capitals
> sidhuvud och sidfot.
```

Claude Code kan konvertera Markdown till formaterade PDF:er eller Word-dokument — direkt från terminalen.

**Styrkan:** Kontext, regler och automatisering. Samma quality varje gång. Noll upprepning.

**Begränsningen:** Kräver terminal. Bäst när du redan har en uppbyggd mappstruktur.

### Claude Cowork

Cowork är den autonoma agenten som arbetar självständigt i molnet. Du ger ett uppdrag, Cowork researchar, analyserar och levererar. Du behöver inte ha datorn igång.

**Exempel 1: Marknadskartläggning**

> *"Kartlägg den nordiska marknaden för logistik-SaaS. Identifiera de 10 största spelarna med uppskattad ARR, tillväxt, ägarbild och positionering. Inkludera en marknadssammanfattning med TAM/SAM-uppskattning. Presentera allt i tabellformat med kort kommentar per bolag."*

**Exempel 2: Transaktionsresearch**

> *"Sammanställ de 10 senaste PE-transaktionerna inom nordisk bemanning och HR-tech de senaste 24 månaderna. Inkludera köpare, säljare, transaktionsvärde, EV/EBITDA-multipel och eventuella strategiska motiveringar. Presentera som tabell."*

**Exempel 3: Konkurrentdjupdyk**

> *"Gör en djupanalys av Descartes Systems Group som konkurrent till CloudFlow. Dekonstruera deras affärsmodell, intäktsströmmar, förvärvsstrategi och nordiska närvaro. Sammanfatta styrkor och svagheter ur CloudFlows perspektiv."*

**Exempel 4: Regulatorisk kartläggning**

> *"Kartlägg regulatoriska krav som påverkar nordiska medtech-bolag 2025–2027. Fokusera på MDR-övergången, CSRD-rapportering och AI-regulering för medicinteknik. Sammanfatta i en tabell med tidslinje, påverkan och rekommenderade åtgärder."*

**Styrkan:** Delegation av tidskrävande research som skulle ta timmar manuellt. Du kan starta uppdraget på morgonen och ha resultatet vid lunch.

**Begränsningen:** Instruktionskvalitet är avgörande — vaga uppdrag ger vaga resultat. Granska alltid resultatet. Behandla det som ett utkast från en junior analytiker.

### Kombinera verktygen

De mest effektiva arbetsflödena kombinerar flera verktyg:

| Steg | Verktyg | Uppgift |
|------|---------|---------|
| 1 | **Cowork** | Researcha nordisk logistik-SaaS-marknad |
| 2 | **Code** | Läs Cowork-rapporten, bearbeta data, skapa jämförelsetabell |
| 3 | **Code** | Kör screening-skill på intressant bolag från researchen |
| 4 | **Excel** | Bygg snabb LBO-modell baserat på screening-data |
| 5 | **Code** | Generera IC-presentation som Markdown |
| 6 | **PowerPoint** | Finjustera presentationen visuellt |

Cowork gör det tunga lyftet. Code gör det precisa arbetet med kontext och regler. Excel och PowerPoint avslutar med operativa detaljer och visuell polish.

---

## Självinlärning — hur Claude blir bättre över tid

Det här är kapitlets viktigaste avsnitt. Allt annat — mappstruktur, CLAUDE.md, skills — är värdefullt i sig. Men **självinlärning** är det som gör systemet bättre för varje uppdrag istället för att stå stilla.

### Konceptet

AI-modellen i sig förändras inte mellan sessioner. Claude har ingen inbyggd förmåga att "minnas" vad som fungerade förra gången. Men det behöver den inte — för du kan bygga det minnet utanför modellen.

**Analogi:** Tänk på en konsultfirma som dokumenterar projekterfarenheter i en kunskapsdatabas. Individerna kommer och går, men kunskapen stannar. Nya konsulter läser sig in och gör samma misstag en gång istället för tre.

Norvik Capitals självinlärningssystem fungerar på samma sätt:

1. **Claude utför en uppgift** — till exempel en kvartalsrapport
2. **Claude reflekterar** — vad fungerade, vad var problematiskt, vad borde göras annorlunda?
3. **En lärdom dokumenteras** — konkret, generaliserbar, formulerad som instruktion
4. **Användaren granskar** — bekräftar att lärdomen är korrekt och värdefull
5. **Lärdomen inarbetas** — skrivs in i relevant CLAUDE.md eller skill-fil
6. **Nästa session blir bättre** — Claude läser den uppdaterade instruktionen automatiskt

### Hur det är implementerat

Systemet består av tre delar:

**1. Instruktioner i rot-CLAUDE.md**

Norvik Capitals rot-CLAUDE.md innehåller explicita instruktioner om reflektion:

```markdown
## Självinlärning

### Efter varje slutförd uppgift — fråga dig själv:
1. Vad lärde jag mig om data (format, kvalitet, var den fanns)?
2. Vad lärde jag mig om struktur (mapporganisation, konventioner)?
3. Vad lärde jag mig om format (vad fungerade i output)?
4. Vad lärde jag mig om process (arbetsordning, effektivitet)?

Om svaret innehåller något värdefullt — dokumentera det.
```

**2. En lärdomar-fil**

Alla lärdomar samlas i `gemensamt/learnings/LEARNINGS.md`. Varje lärdom har ett standardformat:

```markdown
### ARR-data ska alltid exkludera engångsintäkter vid CloudFlow-analys
- **Datum:** 2024-09-15
- **Uppgift:** Kvartalsanalys av CloudFlows finansiella utveckling Q3 2024
- **Fungerade bra:** Snabb sammanställning av alla SaaS-KPI:er.
- **Problematiskt:** Första beräkningen inkluderade implementationsintäkter
  som låg i samma datafil. Gav ett ARR som var ~5% för högt.
- **Lärdom:** Kontrollera alltid att ARR-data exkluderar engångsintäkter
  vid analys av CloudFlow. Filtrera på intäktskategori "recurring".
- **Status:** [NY]
```

**3. En livscykel med fyra stadier**

Varje lärdom genomgår en livscykel:

| Status | Betydelse | Vad som händer |
|--------|-----------|----------------|
| **[NY]** | Nyligen dokumenterad av Claude | Väntar på mänsklig granskning |
| **[GRANSKAD]** | Användaren har godkänt lärdomen | Redo att inarbetas |
| **[INARBETAD]** | Inskriven i relevant CLAUDE.md eller skill | Aktiv i systemet — Claude följer den automatiskt |
| **[ARKIVERAD]** | Inte längre aktuell | Kontexten har förändrats |

### Konkret scenario: från uppgift till permanent lärdom

Låt oss följa ett exempel hela vägen.

**Steg 1: Uppgiften**

En analytiker på Norvik ber Claude sammanställa en LP-rapport för Q3:

```
> Sammanställ LP-rapporten för Q3. Fondnyckeltal: netto-IRR 18%, TVPI 1,4x.
> Portföljbolagsdata finns i respektive bolags bolagsdata-mapp.
```

**Steg 2: Claude utför uppgiften**

Claude läser fond-I:s CLAUDE.md, sammanställer data från portföljbolagen, och skapar rapporten. I första utkastet inkluderar Claude detaljerade KPI:er per bolag — exakta churn-siffror för CloudFlow, OEE per maskin för Nordisk Precision.

**Steg 3: Analytikern reagerar**

"Det här är för detaljerat för LP:er. De vill se fondutveckling, inte operativa detaljer. Skriv om med aggregerade siffror per bolag."

**Steg 4: Claude reflekterar och dokumenterar**

Efter att ha gjort om rapporten skriver Claude en lärdom:

```markdown
### LP-rapporter kräver aggregerad data — inte bolagsspecifika detaljer
- **Datum:** 2024-11-08
- **Uppgift:** Kvartalsrapport till LP:er för Q3 2024
- **Fungerade bra:** Fondnyckeltalsberäkningen gick smidigt.
- **Problematiskt:** Första utkastet inkluderade detaljerade KPI:er per
  portföljbolag som är för detaljerade för LP-rapportering.
- **Lärdom:** Vid LP-rapportering, sammanfatta per bolag på hög nivå:
  omsättning, EBITDA, tillväxt, strategisk status. Inkludera aldrig
  bolagsinterna KPI:er utan explicit instruktion.
- **Status:** [NY]
```

**Steg 5: Granskning**

Nästa gång analytikern granskar LEARNINGS.md ser hen lärdomen, bekräftar att den är korrekt och ändrar status till `[GRANSKAD]`.

**Steg 6: Inarbetning**

Claude (eller analytikern) föreslår en ändring i fond-I:s CLAUDE.md:

```markdown
## LP-rapportering
- ...befintliga regler...
- Portföljbolags detaljerade finansiella data ska aggregeras i
  LP-rapporter — inte exponera bolagsinterna KPI:er i detalj
```

Lärdomen skrivs in, status ändras till `[INARBETAD]`.

**Steg 7: Nästa session**

Nästa gång Claude får i uppdrag att skriva en LP-rapport läser den den uppdaterade CLAUDE.md — och producerar rätt detaljnivå *automatiskt*, utan att analytikern behöver påpeka det igen.

### Granskningscykeln

En process för granskning behöver inte vara komplicerad:

**Frekvens:** Var 2–4:e vecka, eller när det ackumulerats 5+ nya lärdomar.

**Vad du letar efter:**

- **Korrekta lärdomar** — Stämmer observationen? Är instruktionen rimlig?
- **Dubbletter** — Säger två lärdomar samma sak? Slå ihop dem.
- **Mogna lärdomar** — Har tre separata observationer pekat åt samma håll? Dags att inarbeta.
- **Inaktuella lärdomar** — Gäller lärdomen fortfarande, eller har kontexten förändrats?

**Konsolideringsregeln:** Var femte ny lärdom (eller när du granskar) kan Claude föreslå konkreta ändringar i CLAUDE.md eller skills baserat på mönster i lärdomarna. Men — och detta är kritiskt — Claude **ändrar aldrig instruktionsfiler automatiskt**. Den föreslår ändringar och väntar på godkännande.

### Begränsningar — var vaksam

Självinlärningssystemet har viktiga begränsningar:

**Lärdomar kan vara felaktiga.** Claude reflekterar baserat på sin förståelse, som ibland är ofullständig. En lärdom om att "EBITDA-marginalen ska beräknas exklusive engångsposter" kanske är korrekt i ett sammanhang men inte i ett annat. Mänsklig granskning är inte valfritt.

**Instruktionsbloat.** Varje lärdom som inarbetas i CLAUDE.md gör filen längre. Med tiden kan instruktionerna bli så omfattande att de skymmer de viktigaste reglerna. Var disciplinerad — inarbeta bara det som verkligen förbättrar konsistensen, och arkivera det som inte längre behövs.

**Dåliga mönster kan förstärkas.** Om en felaktig lärdom inarbetas i en CLAUDE.md fortsätter Claude att följa den i framtida sessioner. Det är därför granskningssteget är avgörande — det är ditt skydd mot att dåliga mönster cementeras.

**Det är ett komplement, inte en ersättning.** Självinlärning gör Claude mer konsekvent och sparar tid på upprepade misstag. Men det ersätter inte professionellt omdöme. Du behöver fortfarande granska, ifrågasätta och verifiera.

---

## Kom igång — steg för steg

Du behöver inte implementera allt ovan på en gång. Här är en pragmatisk plan för att komma igång, anpassad för en analytiker eller VP som vill testa.

### Vecka 1: Grunden

**Steg 1: Skapa mappstrukturen**

Börja med det enklaste som ger effekt — en firmamapp med en CLAUDE.md och ett portföljbolag:

```bash
mkdir -p min-firma
mkdir -p min-firma/portfoljbolag/bolag-x/bolagsdata
mkdir -p min-firma/portfoljbolag/bolag-x/analys
mkdir -p min-firma/portfoljbolag/bolag-x/styrelsearbete
mkdir -p min-firma/portfoljbolag/bolag-x/output
mkdir -p min-firma/gemensamt/skills
mkdir -p min-firma/gemensamt/learnings
```

**Steg 2: Skriv din första CLAUDE.md**

Skapa en rot-CLAUDE.md med grunderna — det tar 10 minuter:

```markdown
# CLAUDE.md — [Din firma]

## Roll
Du är en erfaren PE-analytiker på [din firma] med fokus på
nordiska mid-market-investeringar.

## Regler
- Skriv på svenska
- Siffror i MSEK, en decimal
- Börja alltid med Executive Summary
- Avsluta med rekommendation och nästa steg
- Spekulera inte — markera saknad data med [DATA SAKNAS]

## Filstruktur
- portfoljbolag/[bolag]/bolagsdata/ — Finansiell rådata
- portfoljbolag/[bolag]/analys/ — Bearbetade analyser
- portfoljbolag/[bolag]/output/ — Färdiga leveranser
- gemensamt/skills/ — Återanvändbara arbetsflöden
```

**Steg 3: Testa med en riktig uppgift**

Kopiera finansiell data för ett portföljbolag till `bolagsdata/`. Starta Claude Code i mappen och be om en konkret analys:

```
> Läs filerna i bolagsdata/ och sammanfatta nyckeltal för de senaste
> tre åren: omsättning, EBITDA, kassaflöde. Presentera som tabell.
```

### Vecka 2–3: Bygg ut

**Steg 4: Lägg till en bolagsspecifik CLAUDE.md**

När du märker att du upprepar samma kontext om bolaget — skriv en CLAUDE.md i bolagsmappen med affärsmodell, KPI:er och investeringstes.

**Steg 5: Skapa din första skill**

Ta den uppgift du gör oftast — kanske en kvartalsrapport eller screening — och gör den till en skill-fil i `gemensamt/skills/`. Se exemplen i `templates/private-equity/firma-exempel/gemensamt/skills/` för format och inspiration.

**Steg 6: Starta lärdomsfilen**

Skapa `gemensamt/learnings/LEARNINGS.md` med den mall som beskrivs ovan. Lägg till instruktioner om reflektion i din rot-CLAUDE.md.

### Vecka 4+: Iterera

**Steg 7: Lägg till fler bolag och pipeline**

Skapa mappar för fler portföljbolag. Lägg till en `pipeline/`-mapp om du aktivt screener nya möjligheter.

**Steg 8: Granska lärdomar**

Gå igenom LEARNINGS.md. Inarbeta det som ger mest värde. Arkivera det som inte längre är relevant.

**Steg 9: Kopiera exempelstrukturen**

När du är redo att bygga ut på allvar, kopiera `templates/private-equity/firma-exempel/` och byt ut Norvik Capitals data mot din egen.

### Vad ger mest effekt snabbast?

| Åtgärd | Tidsinsats | Effekt |
|--------|------------|--------|
| Skriv en rot-CLAUDE.md med grundregler | 10 minuter | Du slipper förklara format och ton varje session |
| Lägg bolagsdata i en strukturerad mapp | 30 minuter | Claude hittar rätt data utan att du pekar |
| Skapa en skill för din vanligaste uppgift | 20 minuter | Samma kvalitet varje gång, noll upprepning |
| Lägg till bolagsspecifik CLAUDE.md | 15 minuter | Claude förstår bolaget utan att du förklarar |
| Starta en lärdomsfil | 5 minuter | Systemet börjar bli bättre över tid |

Börja uppifrån i tabellen. Varje steg ger effekt i sig självt — du behöver inte implementera allt för att se skillnad.

---

## Avslutning

Det här kapitlet har visat hur verktygen du lärt dig i kapitel 00–04 hänger ihop i praktiken:

- **Mappstruktur** ger AI rätt kontext utan att du behöver förklara — filer och mappar *är* instruktioner
- **CLAUDE.md-hierarkin** gör att regler ärvs nedåt: skriv en gång, gäller överallt
- **Skills** automatiserar återkommande arbetsflöden med konsekvent kvalitet
- **Rätt verktyg för rätt uppgift** innebär att du kombinerar Chat, Excel, PowerPoint, Code och Cowork efter behov
- **Självinlärning** gör systemet bättre för varje session — utan att AI-modellen i sig förändras

Norvik Capital är ett fiktivt exempel. Men strukturen, principerna och arbetsflödena är byggda för att vara direkt användbara. Kopiera det som passar. Anpassa det som behöver justeras. Och börja enkelt — en CLAUDE.md och en mapp med data räcker för att se skillnaden.

Det viktigaste är inte att strukturen är perfekt från dag ett. Det viktigaste är att du **börjar** — och låter systemet växa med dig.

---

> *Föregående kapitel: [04 — Mappstruktur och kontext](04-mappstruktur-och-kontext.md)*
>
> *Tillbaka till [startsidan](index.md)*
