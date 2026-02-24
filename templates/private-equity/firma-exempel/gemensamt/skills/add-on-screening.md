# Skill: Add-on-screening

## Beskrivning

Denna skill aktiveras när teamet utvärderar potentiella tilläggsförvärv (add-on acquisitions) för befintliga portföljbolag. Analysen fokuserar på strategisk passform, synergier och en preliminär värdering — inte en fullständig DD utan ett beslutsunderlag för om processen ska drivas vidare.

**Triggers:** "add-on", "tilläggsförvärv", "bolt-on", "add-on-screening", "kompletteringsförvärv", "förvärvskandidat", "add-on-analys"

---

## Input som behövs

| Datapunkt | Beskrivning |
|-----------|-------------|
| **Portföljbolag (köpare)** | Vilket Norvik-bolag överväger add-on |
| **Målbolag** | Namn, bransch, geografi |
| **Finansiella data** | Omsättning, EBITDA, tillväxt, marginal |
| **Antal anställda** | Ungefärligt |
| **Strategisk rationale** | Varför detta förvärv? (kapacitet, geografi, kunder, kompetens, produkt) |
| **Indikativt pris / EV** | Om känt |
| **Källa** | Mäklare, proaktivt, via portföljbolaget |

---

## Steg-för-steg-instruktioner

### Steg 1: Fastställ strategisk rationale

Varför vill vi göra detta förvärv? Kategorisera motivet:

| Typ | Beskrivning | Exempel |
|-----|-------------|---------|
| **Kapacitetsförvärv** | Öka produktionskapacitet eller leveranskapacitet | Nordisk Precision förvärvar CNC-verkstad |
| **Geografisk expansion** | Etablera närvaro på ny marknad | Arbetslyft expanderar till Norge |
| **Kundbasförvärv** | Få tillgång till nya kundsegment eller kanaler | MedTech Nordic får tyska distributörer |
| **Produktkomplettering** | Bredda produktportföljen | CloudFlow adderar WMS-modul |
| **Kompetensförvärv** | Få tillgång till nyckelkompetens eller team | MedTech Nordic förvärvar R&D-team |
| **Konsolidering** | Marknadsledarskap genom konsolidering | Arbetslyft förvärvar mindre bemanningsbolag |

### Steg 2: Kvantifiera synergier

Identifiera och uppskatta synergier i tre kategorier:

**Intäktssynergier:**
- Cross-selling till varandras kunder
- Ny pricing power genom kompletterande erbjudande
- Tillgång till ny kanal eller geografi
- *Uppskatta konservativt — intäktssynergier realiseras sällan fullt ut*

**Kostnadssynergier:**
- Samordnad administration (ekonomi, HR, IT)
- Inköpsfördelar (volymrabatter)
- Eliminering av dubbla funktioner
- Gemensam infrastruktur/lokaler
- *Uppskatta realistiskt — brukar realiseras till 60–80% av plan*

**Strategiska synergier** (svårare att kvantifiera):
- Stärkt marknadsposition
- Ökad attraktivitet vid exit
- Diversifiering av kundbas/sektor

Presentera synergier i MSEK per år vid full realisering, med tidslinje (6/12/24 månader).

### Steg 3: Bedöm integrationsrisk

| Faktor | Bedömning | Kommentar |
|--------|-----------|-----------|
| **Kulturell passform** | Låg/Medel/Hög risk | Liknande företagskultur? Geografisk närhet? |
| **IT-integration** | Låg/Medel/Hög risk | Kompatibla system? Migrationsbehov? |
| **Nyckelmedarbetare** | Låg/Medel/Hög risk | Risk för personaltapp? Earn-out/retention-paket? |
| **Kundöverlapp** | Låg/Medel/Hög risk | Positiv eller negativ kunddynamik? |
| **Operativ integration** | Låg/Medel/Hög risk | Processer, leveranskedjor, kvalitetssystem |
| **Regulatorisk** | Låg/Medel/Hög risk | Konkurrensfrågor? Branschspecifika tillstånd? |

### Steg 4: Gör en preliminär värdering

Gör en indikativ värdering baserat på tillgänglig data:

**Multipelvärdering:**
- Applicera relevanta branschmultiplar (EV/EBITDA, EV/omsättning)
- Justera för storlek (small-cap discount för mindre bolag)
- Justera för synergier (vad är targetvärdet med synergier?)

**Synergivärde:**
- Beräkna nuvärdet av identifierade synergier
- Hur stor del av synergivärdet kan betalas till säljaren vs behållas?

**Indikativ prislapp:**

| Värdering | MSEK |
|-----------|------|
| EV baserat på standalone-multipel | |
| Synergivärde (diskonterat) | |
| Motiverat EV inklusive synergier | |
| Rimligt bud-intervall | |

### Steg 5: Ge rekommendation

Sammanfatta med en av tre:
- **GÅ VIDARE** — Inled diskussioner och eventuell DD
- **BEVAKA** — Intressant men timing/pris inte rätt (ange trigger)
- **AVBÖJ** — Strategisk passform eller värdering motiverar inte att gå vidare

---

## Outputformat

```markdown
# Add-on-screening: [Målbolag] → [Portföljbolag]

**Datum:** YYYY-MM-DD
**Upprättad av:** [Namn], Norvik Capital

## Executive Summary
- [Vad: vilken typ av add-on och strategisk rationale i en mening]
- [Synergier: uppskattad EBITDA-effekt vid full realisering]
- [Värdering: indikativ prislapp vs motiverat värde]
- [Rekommendation: go/no-go i en mening]

## Snapshot

| | Målbolag | Portföljbolag (köpare) | Kombinerat (proforma) |
|---|---------|----------------------|----------------------|
| **Omsättning** | | | |
| **EBITDA** | | | |
| **EBITDA-marginal** | | | |
| **Anställda** | | | |
| **Geografi** | | | |

## Strategisk rationale
[Varför detta förvärv — 3–5 punkter]

## Synergibedömning

| Synergi | Typ | MSEK/år | Tidslinje | Sannolikhet |
|---------|-----|---------|-----------|-------------|
| [Synergi 1] | Intäkt/Kostnad | | 6/12/24m | Hög/Medel/Låg |
| [Synergi 2] | | | | |
| **Totalt** | | **X** | | |

## Integrationsrisk

| Faktor | Risk | Kommentar |
|--------|------|-----------|
| Kulturell passform | 🟢/🟡/🔴 | |
| IT-integration | 🟢/🟡/🔴 | |
| Nyckelmedarbetare | 🟢/🟡/🔴 | |
| Kundöverlapp | 🟢/🟡/🔴 | |
| Operativ integration | 🟢/🟡/🔴 | |
| Regulatorisk | 🟢/🟡/🔴 | |

## Preliminär värdering

| | MSEK |
|---|------|
| EV (standalone-multipel) | |
| Synergivärde (diskonterat) | |
| Motiverat EV inkl synergier | |
| Indikativt pris / bud-intervall | |
| Implied multipel (EV/EBITDA) | |

## Nyckelfrågor att besvara vid DD
1. [Fråga 1]
2. [Fråga 2]
3. [Fråga 3]

## Rekommendation

**[GÅ VIDARE / BEVAKA / AVBÖJ]**

[Motivering i 2–3 meningar]

[Vid GÅ VIDARE: föreslagna nästa steg och tidsplan]
```

---

## Exempelprompt

> "Nordisk Precision tittar på ett mindre CNC-bolag i Linköping, Mekanik Partner AB. Ca 50 MSEK omsättning, 15% EBITDA-marginal, specialiserade på aluminium. Det skulle ge oss kapacitet inom lättviktsmaterial och 3 nya automotive-kunder. Kan du göra en add-on-screening?"

> "Arbetslyft har identifierat en bemanningsaktör i Oslo med 80 MSEK omsättning, fokus på bygg och anläggning. Gör en snabb add-on-bedömning."

---

## Dokumentation och lärdom

När add-on-screeningen är klar, reflektera:

- Var synergiuppskattningarna rimliga eller spekulativa? Fanns det data att stödja dem, eller är de antaganden som kräver verifiering i DD?
- Missade du någon väsentlig integrationsrisk som borde ha flaggats?
- Hade du tillräcklig kontext om portföljbolagets strategi och kapacitet för att bedöma passformen?

Dokumentera insikter i `gemensamt/learnings/LEARNINGS.md` som hjälper framtida add-on-bedömningar — särskilt kring synergirealism, integrationskomplexitet eller branschspecifika multiplar.
