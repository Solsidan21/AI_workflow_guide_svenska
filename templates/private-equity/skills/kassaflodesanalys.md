# Skill: Kassaflödesanalys

## Beskrivning

Denna skill aktiveras när användaren ber om en kassaflödesanalys, analys av fritt kassaflöde, cash conversion-analys eller liknande uppgifter kopplade till ett bolags kassaflöden.

**Triggers:** "kassaflödesanalys", "analysera kassaflödet", "FCF-analys", "cash conversion", "rörelsekapitalanalys", "likviditetsanalys"

---

## Steg-för-steg-instruktioner

### Steg 1: Identifiera och samla in relevant finansiell data

- Be användaren om resultaträkning, balansräkning och kassaflödesanalys (minst 3 historiska år)
- Om data saknas, specificera exakt vilka datapunkter som behövs
- Bekräfta vilken period som ska analyseras
- Kontrollera att data är konsekvent (samma redovisningsprinciper, räkenskapsår)

### Steg 2: Strukturera kassaflödesanalys

Dela upp kassaflödet i tre huvudkategorier:

**Operativt kassaflöde:**
- EBITDA (utgångspunkt)
- Förändringar i rörelsekapital (kundfordringar, lager, leverantörsskulder)
- Betald skatt
- Övriga operativa poster

**Investeringskassaflöde:**
- Underhållsinvesteringar (CapEx — maintenance)
- Tillväxtinvesteringar (CapEx — growth)
- Förvärv och avyttringar
- Övriga investeringar

**Finansieringskassaflöde:**
- Upptagna/amorterade lån
- Utdelningar
- Nyemissioner/återköp
- Räntebetalningar

### Steg 3: Beräkna nyckeltal

| Nyckeltal | Formel | Tolkning |
|-----------|--------|----------|
| Fritt kassaflöde (FCF) | EBITDA - skatt - CapEx ± rörelsekapitalförändring | Kassaflöde tillgängligt för skuld och ägare |
| Cash conversion | FCF / EBITDA | Hur väl vinsten konverteras till kassa (>80% = bra) |
| Rörelsekapital/omsättning | Rörelsekapital / nettoomsättning | Kapitaleffektivitet (<15% = effektivt) |
| DSO | Kundfordringar / (omsättning/365) | Dagar innan kunder betalar |
| DPO | Leverantörsskulder / (COGS/365) | Dagar innan bolaget betalar leverantörer |
| DIO | Lager / (COGS/365) | Dagar som lager hålls |
| Cash Conversion Cycle | DSO + DIO - DPO | Total tid kapital är bundet |
| CapEx/omsättning | Totalt CapEx / nettoomsättning | Investeringsintensitet |
| Maintenance CapEx/avskrivningar | Underhålls-CapEx / avskrivningar | Rimligt förhållande nära 1.0 |

### Steg 4: Identifiera trender och avvikelser

Analysera:
- **Trender:** Hur utvecklas kassaflödet över tid? Förbättras cash conversion?
- **Säsongsvariationer:** Finns det tydliga mönster under året?
- **Avvikelser:** Ovanliga poster, engångseffekter, stora rörelsekapitalsvängningar
- **Rörelsekapitaldynamik:** Växer rörelsekapitalet snabbare än omsättningen?
- **Investeringsmönster:** Är CapEx konsekvent eller cykliskt? Uppskjutna investeringar?
- **Kassaflödeskvalitet:** Hur stor andel av EBITDA blir faktisk kassa?

### Steg 5: Sammanfatta insikter och rekommendationer

Strukturera sammanfattningen så här:
1. **Helhetsbedömning** — Är kassaflödesprofilen attraktiv för en PE-investering?
2. **Styrkor** — Vad fungerar bra?
3. **Risker** — Var finns kassaflödesrisker?
4. **Förbättringsområden** — Konkreta åtgärder för att förbättra kassaflödet
5. **Påverkan på värdering** — Hur påverkar kassaflödesmönstret bolagsvärdet?

---

## Outputformat

```markdown
# Kassaflödesanalys — [Bolagsnamn]

## Executive Summary
- [Viktigaste insikt 1]
- [Viktigaste insikt 2]
- [Viktigaste insikt 3]

## Kassaflödesöversikt

| MSEK | 20XX | 20XX | 20XX | Snitt |
|------|------|------|------|-------|
| EBITDA | | | | |
| Rörelsekapitalförändring | | | | |
| Betald skatt | | | | |
| Operativt kassaflöde | | | | |
| CapEx (underhåll) | | | | |
| CapEx (tillväxt) | | | | |
| **Fritt kassaflöde** | | | | |
| Cash conversion | | | | |

## Nyckeltal och trender
[Analys av nyckeltal med trendkommentarer]

## Rörelsekapitalanalys
[Detaljerad genomgång av DSO, DPO, DIO, CCC]

## Avvikelser och engångsposter
[Lista med identifierade avvikelser]

## Rekommendationer
1. [Åtgärd 1 med kvantifierad effekt]
2. [Åtgärd 2 med kvantifierad effekt]
3. [Åtgärd 3 med kvantifierad effekt]
```

---

## Exempelprompt

> "Kan du göra en kassaflödesanalys för Bolag X? Här är resultaträkning och balansräkning för 2022–2024. Fokusera särskilt på rörelsekapitalutvecklingen och cash conversion. Vi utvärderar bolaget som ett potentiellt förvärv."
