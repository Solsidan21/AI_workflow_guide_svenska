# Skill: Kampanjanalys

## Beskrivning

Denna skill aktiveras när användaren vill analysera resultatet av en marknadsföringskampanj, jämföra kampanjer mot varandra eller mot branschbenchmarks, och få rekommendationer för optimering.

**Triggers:** "kampanjanalys", "analysera kampanjen", "kampanjresultat", "hur gick kampanjen", "kampanjrapport", "ROI-analys"

---

## Steg-för-steg-instruktioner

### Steg 1: Samla in kampanjdata

Be användaren om följande data (om det inte redan angivits):

**Kampanjöversikt:**
- Kampanjnamn och syfte
- Tidsperiod
- Kanaler
- Målgrupp
- Budget (total och per kanal)

**Räckviddsdata:**
- Visningar/impressioner
- Räckvidd (unika personer)
- Frekvens (antal visningar per person)

**Engagemangsdata:**
- Klick (CTR)
- Likes, kommentarer, delningar
- Videovisningar (om relevant)
- Tid på landningssida

**Konverteringsdata:**
- Konverteringar (leads, köp, registreringar)
- Konverteringsgrad
- Kostnad per konvertering (CPA)
- Kostnad per klick (CPC)

**Resultatdata (om tillgängligt):**
- Genererad pipeline/omsättning
- ROI eller ROAS

### Steg 2: Analysera kampanjresultat

Analysera data genom fyra perspektiv:

**Räckvidd (Reach):**
- Nådde kampanjen tillräckligt många i målgruppen?
- Var frekvensen lagom (inte för hög/låg)?
- Vilken kanal genererade mest räckvidd per krona?

**Engagemang (Engagement):**
- Var CTR och engagemang över eller under branschsnitt?
- Vilket innehåll/annonser presterade bäst respektive sämst?
- Var det skillnad mellan kanaler?

**Konvertering (Conversion):**
- Uppnåddes konverteringsmålen?
- Hur ser funnel-konverteringen ut steg för steg?
- Var tappar vi flest — visning till klick, klick till konvertering?

**ROI (Return on Investment):**
- Vad var total ROI/ROAS?
- Vilken kanal hade bäst respektive sämst ROI?
- Hur förhåller sig CPA till kundens livstidsvärde (LTV)?

### Steg 3: Benchmarking

Jämför resultat mot:

| Kanal | KPI | Typiskt branschsnitt (B2B) | Typiskt branschsnitt (B2C) |
|-------|-----|---------------------------|---------------------------|
| LinkedIn Ads | CTR | 0,4–0,6% | — |
| LinkedIn Ads | CPC | 30–80 SEK | — |
| Google Search | CTR | 3–5% | 3–5% |
| Google Search | CPC | 10–40 SEK | 5–20 SEK |
| Meta (Facebook/Instagram) | CTR | 0,5–1,5% | 1–2% |
| Meta | CPC | 5–15 SEK | 3–10 SEK |
| E-post | Öppningsfrekvens | 20–25% | 15–20% |
| E-post | Klickfrekvens | 2–5% | 2–4% |

Notera: Benchmarks varierar kraftigt beroende på bransch, målgrupp och kampanjtyp. Använd som riktmärke, inte absolut sanning.

### Steg 4: Identifiera insikter och mönster

- Vilka kreativa element (rubriker, bilder, CTA) fungerade bäst?
- Fanns det skillnader mellan målgruppssegment?
- Hur presterade kampanjen över tid (start vs slut)?
- Fanns det skillnader mellan enheter (mobil vs desktop)?
- Vilka dagar/tider var mest effektiva?

### Steg 5: Formulera rekommendationer

Ge konkreta, prioriterade rekommendationer:
1. **Omedelbart:** Vad bör ändras nu (pausa underpresterande, skala upp bästa)
2. **Nästa kampanj:** Vad bör justeras i nästa iteration
3. **Strategiskt:** Långsiktiga lärdomar för kanalval, budgetfördelning och målgrupp

---

## Outputformat

```markdown
# Kampanjanalys — [Kampanjnamn]

## Sammanfattning
- **Period:** [Start–Slut]
- **Budget:** [Total budget]
- **Helhetsbedömning:** [Bra/Godkänd/Under förväntan]
- **Viktigaste insikten:** [En mening]

## Nyckeltal

| KPI | Resultat | Mål | vs Mål | vs Branschsnitt |
|-----|----------|-----|--------|-----------------|
| Räckvidd | | | | |
| Klick (CTR) | | | | |
| Konverteringar | | | | |
| CPA | | | | |
| ROAS/ROI | | | | |

## Kanaluppföljning

### [Kanal 1]
| KPI | Resultat | Budget | CPA | Bedömning |
|-----|----------|--------|-----|-----------|
| | | | | |

**Insikter:** [Vad fungerade, vad fungerade inte]

### [Kanal 2]
[Samma format]

## Bäst presterande innehåll
1. [Annons/innehåll 1] — [Varför det fungerade]
2. [Annons/innehåll 2] — [Varför det fungerade]

## Sämst presterande innehåll
1. [Annons/innehåll 1] — [Trolig orsak]
2. [Annons/innehåll 2] — [Trolig orsak]

## Funnel-analys
| Steg | Antal | Konverteringsgrad | Kommentar |
|------|-------|-------------------|-----------|
| Visningar | | — | |
| Klick | | [X%] | |
| Landningssida → Lead | | [X%] | |
| Lead → SQL | | [X%] | |
| SQL → Kund | | [X%] | |

## Rekommendationer

### Omedelbart (denna vecka)
1. [Åtgärd med förväntad effekt]

### Inför nästa kampanj
1. [Åtgärd med motivering]
2. [Åtgärd med motivering]

### Strategiska insikter
1. [Lärdom för långsiktig strategi]

## Föreslagna visualiseringar
- [Diagramtyp 1: Vad det visar]
- [Diagramtyp 2: Vad det visar]
```

---

## Exempelprompt

> "Kan du analysera vår senaste LinkedIn-kampanj? Vi körde under 4 veckor med en budget på 50 000 SEK. Målet var att generera leads till en webinar-registrering. Vi fick 120 000 visningar, 850 klick (CTR 0,7%), 45 registreringar och 12 deltagare som blev kvalificerade leads. Var det bra? Vad bör vi göra annorlunda nästa gång?"
