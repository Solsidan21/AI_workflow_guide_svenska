# Skills — Norvik Capital

## Vad är skills?

Skills är detaljerade instruktioner som guidar Claude genom specifika arbetsuppgifter. Varje skill definierar input, steg-för-steg-process, outputformat och exempelpromptar. De säkerställer att analyser och dokument håller konsekvent kvalitet oavsett vem i teamet som ger uppdraget.

## Tillgängliga skills

| Skill | Fil | Användning |
|-------|-----|------------|
| **Screening-memo** | `screening-memo.md` | Snabb genomlysning av ny investeringsmöjlighet (one-pager med go/no-go) |
| **Kvartalsrapport portföljbolag** | `kvartalsrapport-portfoljbolag.md` | Styrelsepaket med trafikljus-KPI:er, anpassat per bolagstyp (SaaS/industri/tjänster/medtech) |
| **LP-rapportering** | `lp-rapportering.md` | Kvartalsvis rapportering till Limited Partners med fondnyckeltal och portföljöversikt |
| **Add-on-screening** | `add-on-screening.md` | Utvärdering av potentiella tilläggsförvärv med synergibedömning och preliminär värdering |
| **Årlig värdeskapande-review** | `arlig-vardeskapande-review.md` | Årsgenomgång av värdeskapandeplanen med avvikelser, EBITDA-brygga och uppdaterade prioriteringar |

## Hur du använder en skill

Referera till uppgiften naturligt — Claude identifierar rätt skill via triggers. Exempel:

- *"Gör en screening av det här bolaget"* → `screening-memo.md`
- *"Sammanställ board pack för CloudFlow Q3"* → `kvartalsrapport-portfoljbolag.md`
- *"Skriv LP-rapporten för Q2"* → `lp-rapportering.md`
- *"Nordisk Precision tittar på ett add-on, kan du screena det?"* → `add-on-screening.md`
- *"Vi behöver göra årlig review för Arbetslyft"* → `arlig-vardeskapande-review.md`

Du kan också referera till en skill explicit: *"Använd skill screening-memo.md för att..."*

## Relation till andra resurser

Skills bygger på och refererar till:

- **Ramverk** (`gemensamt/ramverk/`) — Analytiska ramverk som DD-ramverk, värderingsramverk, ESG-ramverk
- **Mallar** (`gemensamt/mallar/`) — Dokumentmallar som IC-memo, styrelsepaket, kvartalsrapport
- **Branschdata** (`gemensamt/branschdata/`) — Multipeldata, KPI-benchmarks, makrodata
- **Lärdomar** (`gemensamt/learnings/LEARNINGS.md`) — Ackumulerade insikter som förbättrar arbetet

Se även generiska PE-skills i `../../skills/` (kassaflödesanalys, investment memo, due diligence) som kompletterar dessa firmspecifika skills.

## Lärdomar och förbättring

Varje skill inkluderar en sektion om dokumentation och lärdom. Efter utfört arbete reflekterar Claude och sparar generaliserbara insikter till `gemensamt/learnings/LEARNINGS.md`. Dessa lärdomar granskas av teamet och kan på sikt inarbetas i skills eller CLAUDE.md-filer.
