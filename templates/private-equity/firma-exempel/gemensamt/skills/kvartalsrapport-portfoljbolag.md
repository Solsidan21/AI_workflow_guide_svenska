# Skill: Kvartalsrapport — Portföljbolag

## Beskrivning

Denna skill aktiveras när teamet behöver sammanställa en kvartalsrapport för ett portföljbolag inför styrelsemöte. Rapporten ger styrelsen en tydlig bild av bolagets utveckling med trafikljusbedömning per KPI, statusuppdatering på strategiska initiativ och rekommenderade åtgärder.

**Triggers:** "kvartalsrapport", "styrelsepaket", "board pack", "styrelsemöte", "kvartals-KPI", "portföljbolagsrapport", "quarterly report"

---

## Input som behövs

| Datapunkt | Beskrivning |
|-----------|-------------|
| **Bolagsnamn** | Vilket portföljbolag gäller rapporten |
| **Period** | Kvartal och år (t.ex. Q3 2025) |
| **Finansiella siffror** | Omsättning, EBITDA, resultat, kassaflöde — faktiskt utfall och budget/föregående år |
| **KPI-data** | Bolagsspecifika nyckeltal (se KPI-set nedan) |
| **Statusuppdatering** | Initiativ i värdeskapandeplanen — vad har hänt under kvartalet |
| **Väsentliga händelser** | Nya kunder, förlorade kunder, personalförändringar, marknadshändelser etc. |

---

## Steg-för-steg-instruktioner

### Steg 1: Identifiera rätt KPI-set

Norvik Capital anpassar KPI-uppföljningen efter bolagstyp. Välj rätt set baserat på portföljbolaget:

#### SaaS-bolag (CloudFlow)

| KPI | Mål | Trafikljus |
|-----|-----|------------|
| ARR | Budget ±5% | 🟢 ±5% / 🟡 ±10% / 🔴 >10% avvikelse |
| ARR-tillväxt YoY | >30% | 🟢 >30% / 🟡 20–30% / 🔴 <20% |
| MRR-bridge | Positiv netto new | 🟢 / 🟡 / 🔴 per komponent |
| NRR (Net Revenue Retention) | >110% | 🟢 >110% / 🟡 100–110% / 🔴 <100% |
| GRR (Gross Revenue Retention) | >90% | 🟢 >90% / 🟡 85–90% / 🔴 <85% |
| Churn rate | <1,5% månadsvis | 🟢 <1,5% / 🟡 1,5–2,5% / 🔴 >2,5% |
| CAC Payback | <18 månader | 🟢 <18m / 🟡 18–24m / 🔴 >24m |
| LTV/CAC | >3x | 🟢 >3x / 🟡 2–3x / 🔴 <2x |
| Bruttomarginal | >75% | 🟢 >75% / 🟡 70–75% / 🔴 <70% |
| Rule of 40 | >40 | 🟢 >40 / 🟡 30–40 / 🔴 <30 |
| Burn rate / runway | >12 månader | 🟢 >12m / 🟡 6–12m / 🔴 <6m |

#### Industribolag (Nordisk Precision)

| KPI | Mål | Trafikljus |
|-----|-----|------------|
| Omsättning | Budget ±5% | 🟢 ±5% / 🟡 ±10% / 🔴 >10% avvikelse |
| Orderbok | Book-to-bill >1,0x | 🟢 >1,0x / 🟡 0,9–1,0x / 🔴 <0,9x |
| EBITDA-marginal | >18% | 🟢 >18% / 🟡 15–18% / 🔴 <15% |
| Bruttomarginal | Stabil/ökande | 🟢 ökande / 🟡 stabil / 🔴 sjunkande |
| OEE (Overall Equipment Effectiveness) | >75% | 🟢 >75% / 🟡 65–75% / 🔴 <65% |
| Kapacitetsutnyttjande | 80–85% | 🟢 80–85% / 🟡 70–80% / 🔴 <70% eller >90% |
| Kasskonvertering (FCF/EBITDA) | >70% | 🟢 >70% / 🟡 50–70% / 🔴 <50% |
| Leveransprecision | >95% | 🟢 >95% / 🟡 90–95% / 🔴 <90% |
| Kassationsprocent | <2% | 🟢 <2% / 🟡 2–4% / 🔴 >4% |
| Kundkoncentration (topp 5) | <45% | 🟢 <45% / 🟡 45–55% / 🔴 >55% |

#### Tjänstebolag (Arbetslyft)

| KPI | Mål | Trafikljus |
|-----|-----|------------|
| Omsättning | Budget ±5% | 🟢 ±5% / 🟡 ±10% / 🔴 >10% avvikelse |
| Antal uthyrda (FTE) | Enligt plan | 🟢 ±5% / 🟡 ±10% / 🔴 >10% avvikelse |
| Beläggningsgrad | >92% | 🟢 >92% / 🟡 88–92% / 🔴 <88% |
| Intäkt per FTE | Ökande | 🟢 ökande / 🟡 stabil / 🔴 sjunkande |
| Bruttomarginal per segment | >20% totalt | 🟢 >20% / 🟡 17–20% / 🔴 <17% |
| EBITDA-marginal | >12% | 🟢 >12% / 🟡 10–12% / 🔴 <10% |
| Konsultandel av omsättning | Mål: 40% | 🟢 >35% / 🟡 30–35% / 🔴 <30% |
| Personalomsättning (intern) | <15% | 🟢 <15% / 🟡 15–20% / 🔴 >20% |
| Time-to-fill | <15 dagar | 🟢 <15d / 🟡 15–25d / 🔴 >25d |
| NPS | >40 | 🟢 >40 / 🟡 25–40 / 🔴 <25 |
| DSO | <45 dagar | 🟢 <45d / 🟡 45–60d / 🔴 >60d |

#### Medtech-bolag (MedTech Nordic)

| KPI | Mål | Trafikljus |
|-----|-----|------------|
| Omsättning | Budget ±5% | 🟢 ±5% / 🟡 ±10% / 🔴 >10% avvikelse |
| Omsättningstillväxt YoY | >15% | 🟢 >15% / 🟡 10–15% / 🔴 <10% |
| Bruttomarginal | >65% | 🟢 >65% / 🟡 60–65% / 🔴 <60% |
| EBITDA-marginal | >18% | 🟢 >18% / 🟡 12–18% / 🔴 <12% |
| R&D-andel av omsättning | 10–15% | 🟢 10–15% / 🟡 ±3pp / 🔴 >18% eller <7% |
| Regulatorisk status | MDR-compliant | 🟢 tidplan / 🟡 försenad <3m / 🔴 försenad >3m |
| Produktpipeline | Enligt roadmap | 🟢 tidplan / 🟡 försenad <1 kvartal / 🔴 försenad >1 kvartal |
| Distributörsintäkter | Ökande | 🟢 >10% tillväxt / 🟡 0–10% / 🔴 sjunkande |
| Kundretention | >90% | 🟢 >90% / 🟡 85–90% / 🔴 <85% |
| Lageromlopp | Förbättring | 🟢 förbättring / 🟡 stabilt / 🔴 försämring |
| FCF-konvertering | >50% | 🟢 >50% / 🟡 30–50% / 🔴 <50% |

### Steg 2: Sammanställ finansiell översikt

Skapa en tabell med:
- Aktuellt kvartal: utfall vs budget vs föregående år
- YTD: utfall vs budget vs föregående år
- Beräkna avvikelser i % och absolutbelopp
- Kommentera väsentliga avvikelser (>5%)

### Steg 3: Bedöm KPI:er med trafikljus

För varje KPI:
1. Fyll i aktuellt värde
2. Jämför mot mål och föregående period
3. Sätt trafikljus (🟢 / 🟡 / 🔴)
4. Skriv en kort kommentar vid gul eller röd — vad orsakar avvikelsen och vad görs åt det?

**Regel:** Alla röda KPI:er kräver en åtgärdsplan med ansvarig och tidslinje.

### Steg 4: Uppdatera status på värdeskapandeinitiativ

Gå igenom varje initiativ i värdeskapandeplanen:
- Status: 🟢 Enligt plan / 🟡 Försenad men hanteras / 🔴 Väsentligt avvikande
- Vad har uppnåtts under kvartalet (konkreta milstolpar)
- Vad är planerat nästa kvartal
- Eventuella hinder eller resursbrister

### Steg 5: Formulera rekommendationer

Avsluta med 3–5 konkreta rekommendationer till styrelsen:
- Beslutspunkter (kräver styrelsebeslut)
- Informationspunkter (styrelsen bör känna till)
- Förslag på fokusområden till nästa kvartal

---

## Outputformat

```markdown
# Kvartalsrapport — [Bolagsnamn] [Kvartal År]

**Rapportdatum:** YYYY-MM-DD
**Styrelsemöte:** YYYY-MM-DD
**Upprättad av:** [Namn], Norvik Capital

## Executive Summary
- [Övergripande bedömning av kvartalet — en mening]
- [Viktigaste positiva trenden]
- [Största utmaningen]
- [Viktigaste beslutspunkten för styrelsen]

## Finansiell översikt

| MSEK | Q[X] Utfall | Q[X] Budget | Avvikelse | FY Utfall YTD | FY Budget YTD | FÅ-1 Q[X] |
|------|-------------|-------------|-----------|---------------|---------------|------------|
| Omsättning | | | | | | |
| Bruttoresultat | | | | | | |
| Bruttomarginal | | | | | | |
| EBITDA | | | | | | |
| EBITDA-marginal | | | | | | |
| Operativt kassaflöde | | | | | | |
| Fritt kassaflöde | | | | | | |

**Kommentar:** [Kort analys av avvikelser]

## KPI-uppföljning

| KPI | Utfall | Mål | Föreg. kvartal | Trend | Status |
|-----|--------|-----|----------------|-------|--------|
| [KPI 1] | | | | ↑/→/↓ | 🟢/🟡/🔴 |
| [KPI 2] | | | | ↑/→/↓ | 🟢/🟡/🔴 |
| ... | | | | | |

### Kommentarer till gula och röda KPI:er

**🔴 [KPI-namn]:**
- Orsak: [Förklaring]
- Åtgärd: [Vad görs]
- Ansvarig: [Vem]
- Förväntad normalisering: [När]

**🟡 [KPI-namn]:**
- Orsak: [Förklaring]
- Bevakning: [Vad följer vi]

## Värdeskapande — initiativstatus

| # | Initiativ | Status | Kommentar |
|---|-----------|--------|-----------|
| 1 | [Initiativ 1] | 🟢/🟡/🔴 | [Kort status] |
| 2 | [Initiativ 2] | 🟢/🟡/🔴 | [Kort status] |
| ... | | | |

### Detaljerad uppföljning per initiativ
[Kort beskrivning av framsteg, milstolpar och nästa steg per initiativ]

## Väsentliga händelser under kvartalet
- [Händelse 1]
- [Händelse 2]

## Prognos och utsikter
[Kort bedömning av resterande år / kommande kvartal]

## Rekommendationer och beslutspunkter

### Beslutspunkter (kräver styrelsebeslut)
1. [Beslutspunkt med bakgrund och rekommendation]

### Informationspunkter
1. [Informationspunkt]

### Förslag på fokusområden nästa kvartal
1. [Fokusområde]
```

---

## Exempelprompt

> "Sammanställ kvartalsrapporten för CloudFlow Q3 2025 inför styrelsemötet den 28 oktober. Här är KPI-data och finansiella siffror. ARR landade på 92 MSEK mot budget 95 MSEK, NRR föll till 108%, men vi fick tre nya enterprise-kunder."

> "Gör board pack för Nordisk Precision Q2 2025. Orderingången var stark (book-to-bill 1,2x) men EBITDA-marginalen dippade till 16% pga ökade materialpriser. OEE förbättrades till 72%."

---

## Dokumentation och lärdom

När kvartalsrapporten är klar, reflektera:

- Saknades det KPI-data som hade gett styrelsen en bättre bild? Behöver KPI-setet justeras för detta bolag?
- Var trafikljuströsklarna relevanta eller behöver de kalibreras baserat på bolagets mognad och marknadssituation?
- Blev rapporten lagom detaljerad — eller behövde du korta ner/bygga ut någon sektion?

Om du identifierar en generaliserbar insikt, skriv en kort lärdom till `gemensamt/learnings/LEARNINGS.md` — det hjälper nästa kvartals rapportering att bli ännu skarpare.
