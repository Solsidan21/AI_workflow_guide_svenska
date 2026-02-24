# CLAUDE.md — Norvik Capital Fund I

## Fondöversikt

| | |
|---|---|
| **Fond** | Norvik Capital Fund I |
| **Vintage** | 2020 |
| **Committed capital** | 500 MSEK |
| **Investeringsperiod** | 2020–2024 (avslutad) |
| **Status** | Fullinvesterad — 4 portföljbolag |
| **Fondlivslängd** | 10 år (med möjlighet till 2 x 1 års förlängning) |
| **Strategi** | Nordisk mid-market, majoritets- och betydande minoritetsinvesteringar |
| **Target EV** | 100–500 MSEK per investering |
| **Sektorfokus** | Teknik, industri, tjänster, hälsovård |

## Portföljsammansättning

| Bolag | Sektor | Investeringsår | EV vid entry | Ägarandel | Status |
|-------|--------|----------------|-------------|-----------|--------|
| CloudFlow AB | SaaS / logistik | 2021 | ~200 MSEK | Majoritet | Aktiv tillväxt |
| Nordisk Precision AB | Industri / CNC | 2021 | ~350 MSEK | Majoritet | Operativ förbättring |
| Arbetslyft AB | Bemanning & konsult | 2022 | ~250 MSEK | Betydande minoritet | Tillväxt + add-on |
| MedTech Nordic AB | Medicinsk teknik | 2023 | ~180 MSEK | Majoritet | Tidig värdeskapandefas |

Detaljerad information om varje bolag finns i `../../portfoljbolag/[bolagsnamn]/CLAUDE.md`.

## Fondnyckeltal — tracka alltid

Vid all fondrelaterad analys och rapportering, inkludera alltid dessa nyckeltal:

| Nyckeltal | Definition | Notering |
|-----------|-----------|----------|
| **Brutto-IRR** | Internränta före fondkostnader och carried interest | Beräkna på bolagsnivå och fondnivå |
| **Netto-IRR** | Internränta efter alla kostnader och carry | Det LP:erna faktiskt får |
| **MOIC (brutto)** | Total Value / Invested Capital | Före kostnader |
| **MOIC (netto)** | Total Value to LPs / Drawn Capital | Efter kostnader och carry |
| **DPI** | Distributions to Paid-In — realiserat värde / inbetalt kapital | Visar hur mycket som faktiskt betalats tillbaka |
| **TVPI** | Total Value to Paid-In — (realiserat + orealiserat) / inbetalt | DPI + orealiserat |
| **NAV** | Net Asset Value — fondportföljens marknadsvärde | Uppdateras kvartalsvis |
| **RVPI** | Residual Value to Paid-In — orealiserat / inbetalt kapital | TVPI minus DPI |

Presentera alltid fondnyckeltal i en sammanfattningstabell med jämförelse mot föregående kvartal och budget/target.

## LP-rapportering

### Rapporteringsschema

| Rapport | Frekvens | Deadline | Mottagare |
|---------|----------|----------|-----------|
| Kvartalsrapport | Kvartalsvis | 45 dagar efter kvartalets slut | Alla LP:er |
| Årsrapport | Årligen | 90 dagar efter årsslutet | Alla LP:er |
| Capital call notice | Vid behov | 10 bankdagar före dragning | Berörda LP:er |
| Distribution notice | Vid exit/utdelning | 10 bankdagar före utbetalning | Alla LP:er |
| LPAC-material | Halvårsvis | 2 veckor före mötet | LPAC-ledamöter |

### Format och regler för LP-rapporter

- **Kvartalsrapporter** ska alltid innehålla:
  1. Executive Summary med fondens utveckling
  2. Fondnyckeltal (IRR, MOIC, DPI, TVPI, NAV) — kvartalet och kumulativt
  3. Portföljöversikt med kortfattad statusuppdatering per bolag
  4. Bolagsdjupdyk: ett bolag per kvartal i mer detalj
  5. Pipeline-uppdatering (utan konfidentiella detaljer)
  6. Kassaposition och prognostiserade kapitalanrop

- **Ton i LP-rapporter:** Transparent, balanserad och professionell. Undvik att bara rapportera positiva nyheter — LP:er förväntar sig en ärlig bild. Flagga risker proaktivt.

- **Jämförelsedata:** Inkludera alltid jämförelse mot föregående kvartal, samma kvartal föregående år och fond-target.

- **NAV-metodik:** Fair value enligt IPEV-riktlinjer. Baseras primärt på multipelanalys mot jämförbara publika bolag och transaktioner. Dokumentera alltid NAV-antaganden och förändringar.

### Konfidentialitet

- LP-namn och commitment-belopp per LP är strikt konfidentiella
- Portföljbolags detaljerade finansiella data ska aggregeras i LP-rapporter — inte exponera bolagsinterna KPI:er i detalj
- Vid osäkerhet om vad som kan delas — fråga innan du skriver

## Undermappar

| Mapp | Innehåll |
|------|----------|
| `fonddata/` | Fondvillkor, LPA-sammanfattning, LP-commitments, cap table, avgiftsstruktur |
| `rapportering/` | Kvartals- och årsrapporter, NAV-beräkningar, capital calls och distributions |
| `prestanda/` | IRR-beräkningar, MOIC-analys, PME-benchmarking, attribution per bolag |
