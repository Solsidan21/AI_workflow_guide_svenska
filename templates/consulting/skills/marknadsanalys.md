# Skill: Marknadsanalys

## Beskrivning

Denna skill aktiveras när användaren behöver en strukturerad marknadsanalys — oavsett om det handlar om att bedöma en ny marknad, förstå konkurrenslandskapet eller identifiera tillväxtmöjligheter.

**Triggers:** "marknadsanalys", "marknadsstorlek", "TAM SAM SOM", "konkurrensanalys", "marknadsstudie", "branschanalys", "Porter", "tillväxtdrivare"

---

## Steg-för-steg-instruktioner

### Steg 1: Definiera scope

Klargör med användaren:
- Vilken marknad/bransch ska analyseras?
- Geografiskt scope (Sverige, Norden, Europa)
- Tidshorisont (nuläge + prognos, typiskt 3–5 år)
- Syfte (investeringsbeslut, strategibeslut, marknadsinträde)
- Perspektiv (vilken aktör analyserar vi marknaden utifrån?)

### Steg 2: Marknadsstorlek och tillväxt

Strukturera marknadsstorleken i tre nivåer:

| Nivå | Definition | Metod |
|------|-----------|-------|
| **TAM** (Total Addressable Market) | Hela den potentiella marknaden globalt/regionalt | Top-down: branschrapporter, statistik |
| **SAM** (Serviceable Addressable Market) | Den del av marknaden som kunden kan adressera | Geografisk och segmentfiltrering |
| **SOM** (Serviceable Obtainable Market) | Realistisk marknadsandel att uppnå | Bottom-up: kapacitet, säljresurser, tillväxttakt |

Beräkningsmetodik:
- **Top-down:** Använd branschdata och bryt ned per segment/geografi
- **Bottom-up:** Räkna från antal potentiella kunder x genomsnittligt ordervärde
- **Triangulera:** Använd båda metoderna och jämför

Inkludera alltid:
- Historisk tillväxttakt (CAGR senaste 3–5 åren)
- Prognostiserad tillväxttakt (CAGR kommande 3–5 åren)
- Tillväxtdrivare och bromsklossar

### Steg 3: Tillväxtdrivare och trender

Identifiera och prioritera de viktigaste drivkrafterna:

**Strukturella drivkrafter:**
- Demografiska förändringar
- Teknologisk utveckling och digitalisering
- Regulatoriska förändringar
- Hållbarhetskrav och ESG

**Cykliska faktorer:**
- Konjunkturläge
- Investerings- och budgetcykler
- Säsongsvariationer

**Disruption och risker:**
- Nya affärsmodeller
- Substitut och nya teknologier
- Geopolitiska risker

### Steg 4: Konkurrenslandskap (Porter's Five Forces)

Analysera marknadens attraktivitet genom fem krafter:

**1. Konkurrens mellan befintliga aktörer**
- Antal och storlek på konkurrenter
- Marknadens tillväxttakt (hög tillväxt = lägre rivalitet)
- Differentiering vs priskonkurrens
- Utträdesbarriärer

**2. Hot från nya aktörer**
- Inträdesbarriärer (kapital, kompetens, regleringar, varumärke)
- Skalfördelar bland befintliga aktörer
- Nätverkseffekter
- Switching costs för kunder

**3. Hot från substitut**
- Alternativa lösningar på kundens problem
- Pris-/prestandaförhållande jämfört med substitut
- Kundens benägenhet att byta

**4. Leverantörernas förhandlingsstyrka**
- Antal leverantörer och koncentration
- Switching costs
- Leverantörernas möjlighet till framåtintegration

**5. Kundernas förhandlingsstyrka**
- Kundkoncentration
- Switching costs
- Prismedvetenhet och transparens
- Kundens möjlighet till bakåtintegration

Sammanfatta i en tabell:

| Kraft | Styrka (1–5) | Kommentar | Implikation |
|-------|-------------|-----------|-------------|
| Befintlig konkurrens | | | |
| Nya aktörer | | | |
| Substitut | | | |
| Leverantörsmakt | | | |
| Kundmakt | | | |

### Steg 5: Konkurrentanalys

Kartlägg de 5–10 viktigaste konkurrenterna:

| Konkurrent | Omsättning | Marknadsandel | Positionering | Styrkor | Svagheter |
|-----------|-----------|--------------|--------------|---------|-----------|
| | | | | | |

Analysera:
- Konkurrensdynamik och trender
- Strategiska grupper
- White spaces (obemannade positioner i marknaden)
- Potentiella framtida konkurrenter

### Steg 6: Sammanfatta med implikationer

Koppla varje insikt till en implikation och potentiell handling:

| Insikt | So what? | Rekommendation |
|--------|----------|---------------|
| Marknaden växer X% | [Implikation] | [Handling] |
| Konkurrent Y expanderar | [Implikation] | [Handling] |

---

## Datakällor att referera

Ange alltid vilka källor analysen baseras på. Vanliga källor:
- SCB (Statistiska centralbyrån) — svensk statistik
- Eurostat — europeisk statistik
- Branschorganisationer (Teknikföretagen, Almega, etc.)
- Branschrapporter (McKinsey, BCG, Bain, m.fl.)
- Företags årsredovisningar och kvartalsrapporter
- Allabolag.se, Retriever, Bisnode — bolagsdata
- Google Trends — sökintresse och trender
- Om data saknas, ange tydligt att uppskattningar används och beskriv metodik

---

## Outputformat

```markdown
# Marknadsanalys — [Marknad/Bransch]

## Executive Summary
- [Marknadsstorlek och tillväxt — en rad]
- [Viktigaste trenden — en rad]
- [Konkurrensläge — en rad]
- [Huvudrekommendation — en rad]

## Marknadsstorlek och tillväxt

| | Värde (MSEK/MDSEK) | Tillväxt (CAGR) |
|---|---|---|
| TAM | | |
| SAM | | |
| SOM | | |

### Tillväxtdrivare
1. [Drivkraft 1 — kvantifierad om möjligt]
2. [Drivkraft 2]
3. [Drivkraft 3]

## Konkurrensdynamik (Porter's Five Forces)

[Sammanfattningstabell + analys per kraft]

## Konkurrentkartläggning

[Tabell med de viktigaste konkurrenterna + analys]

## Trender och framtidsutsikter

[Strukturerade trender med implikationer]

## Implikationer och rekommendationer

| Insikt | Implikation | Rekommenderad handling |
|--------|------------|----------------------|
| | | |
```

---

## Exempelprompt

> "Vi behöver en marknadsanalys av den svenska marknaden för HR-tech SaaS-lösningar. Vår klient överväger att lansera en ny produkt för digital onboarding riktad mot företag med 50–500 anställda. Vi behöver förstå marknadsstorlek, tillväxt, konkurrenter och vilka möjligheter som finns. Fokusera på Sverige men nämn även nordisk potential."
