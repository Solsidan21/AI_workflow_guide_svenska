# Portföljbolag

En mapp per portföljbolag. Här sker det dagliga arbetet — analys, styrelsematerial, värdeskapande och uppföljning.

## Bolag i portföljen

| Bolag | Mapp | Sektor | Nyckeltal |
|-------|------|--------|-----------|
| CloudFlow AB | `cloudflow-ab/` | SaaS / logistik | 80 MSEK ARR |
| Nordisk Precision AB | `nordisk-precision-ab/` | Industri / CNC | 220 MSEK omsättning |
| Arbetslyft AB | `arbetslyft-ab/` | Bemanning & konsult | 150 MSEK omsättning |
| MedTech Nordic AB | `medtech-nordic-ab/` | Medicinsk teknik | 60 MSEK omsättning |

## Struktur per bolag

Varje portföljbolag har samma fem undermappar:

### `bolagsdata/`
Grundläggande data som Claude behöver för att förstå bolaget:
- Historisk finansiell data (resultat- och balansräkning, kassaflöde)
- Månads- och kvartals-KPI:er
- Budget och prognos
- Ägarstruktur och cap table

### `analys/`
Löpande och ad hoc-analyser:
- Värderingar och multipelanalyser
- Scenariomodeller
- Add-on-utvärderingar
- Marknads- och konkurrentanalys

### `styrelsearbete/`
Material kopplat till styrelsemöten:
- Styrelsepaket (board packs) — kvartalsvis
- Protokoll och beslutslogg
- Strategiska beslutsunderlag
- Kommittéarbete (ersättning, revision)

### `vardeskapande/`
Värdeskapande plan och uppföljning:
- 100-dagarsplan (post-investering)
- Operativa förbättringsinitiativ
- Kommersiella initiativ (prissättning, nya marknader)
- KPI-uppföljning mot plan

### `output/`
Färdiga leveranser och presentationer:
- Sammanställda rapporter
- Presentationer till IC eller LP:er
- Exit-material och informationsmemorandum
- Övriga slutprodukter

## Nytt portföljbolag

När en ny investering genomförs (från `pipeline/aktiva-processer/`):
1. Skapa en ny mapp med bolagsnamnet i kebab-case
2. Skapa de fem standardundermapparna
3. Flytta relevant DD-material från pipeline till `bolagsdata/` och `analys/`
4. Skapa en CLAUDE.md med bolagsspecifik kontext
