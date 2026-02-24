# Gemensamt — Delade resurser

Mallar, skills, ramverk och referensdata som används på flera ställen i firman. Samlas här för att undvika duplicering och säkerställa konsistens.

## Undermappar

### `mallar/`
Dokumentmallar som återanvänds regelbundet:
- IC-memo-mall
- Styrelsepaketsmall (board pack)
- Kvartalsrapportmall till LP:er
- Screeningmall (one-pager)
- 100-dagarsplan-mall
- Exit-analysmall

### `skills/`
Claude-skills som används firmabrett:
- Kassaflödesanalys
- Värdering (DCF + multipelanalys)
- Due diligence-checklista
- Styrelserapportering
- LP-rapportering
- Scenarioanalys

Skills är detaljerade instruktioner som säger åt Claude *hur* en specifik uppgift ska utföras. De refereras från CLAUDE.md-filer i relevanta mappar.

### `ramverk/`
Analysramverk och checklistor:
- DD-ramverk (kommersiell, finansiell, legal, operativ)
- Värderingsramverk med standardantaganden
- ESG-utvärderingsramverk
- Integrationsramverk (post-acquisition)
- Riskbedömningsmatris

### `branschdata/`
Branschreferenser och benchmarks:
- Multipeldata per sektor (EV/EBITDA, EV/Revenue)
- Nordiska PE-benchmarks (IRR, MOIC per vintage)
- Sektorspecifika KPI-benchmarks
- Makroekonomiska referenspunkter

## Princip

**En källa, många användare.** När en mall eller ett ramverk uppdateras här gäller det överallt. CLAUDE.md-filer i andra mappar refererar till filer i `gemensamt/` istället för att duplicera innehållet.
