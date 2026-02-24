# Skill: LP-rapportering

## Beskrivning

Denna skill aktiveras när teamet behöver sammanställa kvartalsvis rapportering till LP:er (Limited Partners) i Norvik Capital Fund I. LP-rapporten ger investerarna en balanserad bild av fondens utveckling, portföljbolagens status och fondnyckeltal — utan att röja operativ bolagsdetalj som är konfidentiell.

**Triggers:** "LP-rapport", "LP-brev", "LP-rapportering", "kvartalsrapport LP", "investor report", "fondrapport", "limited partner", "LP quarterly"

---

## Input som behövs

| Datapunkt | Beskrivning |
|-----------|-------------|
| **Period** | Kvartal och år (t.ex. Q3 2025) |
| **Fondnyckeltal** | Brutto-IRR, Netto-IRR, MOIC, DPI, TVPI, NAV, RVPI |
| **Portföljbolagens kvartalsdata** | Omsättning, EBITDA, tillväxt, strategisk status — per bolag |
| **Kassaposition** | Oinvesterat kapital, management fee, follow-on-reserv |
| **Capital calls / distributions** | Under perioden |
| **Pipeline-status** | Antal möjligheter under utvärdering (ej bolagsnamn) |
| **Väsentliga händelser** | Förvärv, avyttringar, add-ons, organisationsförändringar |

---

## Steg-för-steg-instruktioner

### Steg 1: Kontrollera konfidentialitetsregler

**KRITISKT** — Innan du skriver ett enda ord, verifiera:

- ❌ **Aldrig** inkludera LP-namn eller commitment-belopp
- ❌ **Aldrig** inkludera detaljerade bolagsspecifika KPI:er (churn, NPS, OEE per maskin, kundnamn, leverantörsnamn)
- ❌ **Aldrig** nämna pipeline-bolags namn eller identifierbar information
- ✅ **Alltid** rapportera fondnyckeltal enligt IPEV-riktlinjer
- ✅ **Alltid** använda aggregerade siffror per portföljbolag (omsättning, EBITDA, tillväxt, strategisk status)
- ✅ **Alltid** inkludera disclaimers och hänvisning till fondavtal

### Steg 2: Sammanställ fondöversikt

Presentera fondens övergripande status:

| Nyckeltal | Definition | Källa |
|-----------|-----------|-------|
| **Brutto-IRR** | Avkastning före avgifter och carried interest | fonder/fond-I/prestanda/ |
| **Netto-IRR** | Avkastning efter avgifter och carried interest | fonder/fond-I/prestanda/ |
| **MOIC (brutto)** | Multiple on Invested Capital, före avgifter | fonder/fond-I/prestanda/ |
| **MOIC (netto)** | Multiple on Invested Capital, efter avgifter | fonder/fond-I/prestanda/ |
| **DPI** | Distributions to Paid-In capital | fonder/fond-I/prestanda/ |
| **TVPI** | Total Value to Paid-In capital | fonder/fond-I/prestanda/ |
| **RVPI** | Residual Value to Paid-In capital | fonder/fond-I/prestanda/ |
| **NAV** | Net Asset Value av fonden | fonder/fond-I/prestanda/ |

Inkludera utveckling över tid (minst senaste 4 kvartal) för att visa trend.

### Steg 3: Skriv portföljöversikt per bolag

Per portföljbolag, presentera på **aggregerad hög nivå**:

- Bolagsnamn och branschbeskrivning (en mening)
- Omsättning och EBITDA (aktuellt kvartal och YoY-utveckling)
- Strategisk status i en mening (t.ex. "Stark orderingång driven av ny automotive-kund")
- Bedömning: 🟢 Utvecklas enligt eller bättre än plan / 🟡 Avviker men hanteras / 🔴 Kräver uppmärksamhet

**Regel:** Tänk "vad behöver en LP veta för att bedöma fondens utveckling?" — inte "vad behöver en styrelseledamot veta för att styra bolaget?"

### Steg 4: Rapportera kassaposition och kapitalanvändning

| Post | MSEK |
|------|------|
| Committed capital | 500,0 |
| Drawn capital | [X] |
| Remaining commitment | [X] |
| Invested in portfolio | [X] |
| Management fee (kumulativt) | [X] |
| Follow-on reserve | [X] |
| Oinvesterat / dry powder | [X] |

Inkludera kapitalanrop och utdelningar under perioden.

### Steg 5: Pipeline och utsikter

Beskriv pipeline på aggregerad nivå:
- Antal möjligheter under aktiv utvärdering (t.ex. "2 processer i screening-fas")
- Fokussektorer utan att namnge specifika bolag
- Generell syn på marknaden och deal flow

### Steg 6: Skriv LP-brevet

Inled med ett personligt brev från Managing Partner som sammanfattar kvartalet i 3–4 stycken:
1. Övergripande marknad och kontext
2. Fondens utveckling och nyckeltal
3. Portföljhöjdpunkter
4. Utsikter och prioriteringar

Tonen ska vara: **transparent, balanserad, professionell**. Flagga risker proaktivt — LP:er uppskattar ärlighet mer än polerad optimism.

---

## Outputformat

```markdown
# Norvik Capital Fund I — LP-rapport [Kvartal År]

**Rapportdatum:** YYYY-MM-DD
**Period:** [Kvartal År]
**Fond:** Norvik Capital Fund I (vintage 2020)

---

## Brev från Managing Partner

Bästa investerare,

[Stycke 1: Marknad och kontext]

[Stycke 2: Fondutveckling]

[Stycke 3: Portföljhöjdpunkter]

[Stycke 4: Utsikter]

Med vänliga hälsningar,
[Managing Partner], Norvik Capital

---

## Fondöversikt

| Nyckeltal | Q[X] [År] | Q[X-1] [År] | Förändring |
|-----------|-----------|-------------|------------|
| Brutto-IRR | | | |
| Netto-IRR | | | |
| MOIC (brutto) | | | |
| MOIC (netto) | | | |
| DPI | | | |
| TVPI | | | |
| NAV (MSEK) | | | |

## Kapitalanvändning

| Post | MSEK |
|------|------|
| Committed capital | 500,0 |
| Drawn capital | |
| Remaining commitment | |
| Invested in portfolio | |
| Follow-on reserve | |
| Dry powder | |

**Kapitalanrop under perioden:** [Belopp och syfte]
**Utdelningar under perioden:** [Belopp och källa]

## Portföljöversikt

| Bolag | Bransch | Omsättning (MSEK) | EBITDA (MSEK) | Tillväxt YoY | Status |
|-------|---------|-------------------|---------------|--------------|--------|
| CloudFlow AB | SaaS / Logistik | | | | 🟢/🟡/🔴 |
| Nordisk Precision AB | Industri / CNC | | | | 🟢/🟡/🔴 |
| Arbetslyft AB | Bemanning / Konsult | | | | 🟢/🟡/🔴 |
| MedTech Nordic AB | Medicinteknik | | | | 🟢/🟡/🔴 |

### CloudFlow AB
[2–3 meningar: verksamhetsbeskrivning, kvartalsutfall, strategisk status]

### Nordisk Precision AB
[2–3 meningar]

### Arbetslyft AB
[2–3 meningar]

### MedTech Nordic AB
[2–3 meningar]

## Pipeline och nya investeringar
[Aggregerad pipeline-status, inga bolagsnamn]

## Utsikter
[Kort bedömning av kommande kvartal]

---

*Denna rapport är konfidentiell och avsedd enbart för Limited Partners i Norvik Capital Fund I. Fondnyckeltal beräknas i enlighet med IPEV Valuation Guidelines. Historisk avkastning är ingen garanti för framtida resultat.*
```

---

## Tidsramar

Norvik Capital Fund I:s LP-rapporteringsschema:

| Rapport | Deadline |
|---------|----------|
| Kvartalsrapport | 45 dagar efter kvartalets slut |
| Årsrapport | 90 dagar efter räkenskapsårets slut |
| Kapitalanrop | 10 bankdagar i förväg |
| Utdelningsnotiser | Utan dröjsmål |
| LPAC-underlag | 15 dagar före möte |

---

## Exempelprompt

> "Sammanställ LP-rapporten för Q3 2025. Här är fondnyckeltalen och portföljbolagens kvartalsdata. Netto-IRR har förbättrats till 18%, TVPI 1,4x. CloudFlow hade ett starkt kvartal med 35% ARR-tillväxt. Nordisk Precision hade svagare marginal pga materialpriser."

> "Skriv LP-brevet för Q4 2025 med fokus på att vi gjort vår första exit (partiell) och att fonden nu har en DPI >0."

---

## Dokumentation och lärdom

När LP-rapporten är klar, reflektera:

- Var informationsnivån rätt — aggregerad nog för LP-nivå utan att tappa substans?
- Behövde du göra bedömningar av fair value eller avkastningssiffror som kräver verifiering mot fondadministratör?
- Flaggade du risker tillräckligt transparent, eller fanns det en tendens att tona ner negativa trender?

Dokumentera lärdomar i `gemensamt/learnings/LEARNINGS.md` om du identifierar mönster som förbättrar framtida LP-rapportering — särskilt kring dataaggregering, konfidentialitetsgränser eller tonläge.
