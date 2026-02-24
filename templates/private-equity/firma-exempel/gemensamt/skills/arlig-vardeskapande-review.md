# Skill: Årlig värdeskapande-review

## Beskrivning

Denna skill aktiveras vid den årliga genomgången av värdeskapandeplanen per portföljbolag. Syftet är att stämma av utfall mot ursprunglig plan, identifiera avvikelser, uppdatera prioriteringar och säkerställa att bolagets utveckling ligger i linje med Norviks investeringstes och avkastningsförväntningar.

**Triggers:** "värdeskapande-review", "årlig review", "value creation review", "värdeskapandeplan uppföljning", "VCP-genomgång", "årlig genomgång portföljbolag"

---

## Input som behövs

| Datapunkt | Beskrivning |
|-----------|-------------|
| **Bolagsnamn** | Vilket portföljbolag |
| **Period** | Vilket år som avslutas (t.ex. 2025) |
| **Ursprunglig värdeskapandeplan** | Initiativen som definierades vid investering eller senaste revidering |
| **Utfall per initiativ** | Vad har uppnåtts — kvantitativt och kvalitativt |
| **Finansiellt utfall** | Omsättning, EBITDA, FCF — utfall vs plan vid investering |
| **Nya initiativ** | Tillkommande möjligheter som inte fanns i ursprunglig plan |
| **Marknadsutveckling** | Förändrad kontext som påverkar planen |

---

## Steg-för-steg-instruktioner

### Steg 1: Rekonstruera ursprunglig investeringstes

Sammanfatta den ursprungliga investeringstesen i 3–5 punkter:
- Varför investerade Norvik?
- Vilken avkastning förväntades (IRR/MOIC)?
- Vilka var de centrala antagandena?
- Vilka var de identifierade riskerna?

Detta ger en fast referenspunkt att mäta mot.

### Steg 2: Stäm av finansiellt utfall mot investeringscase

Skapa en brygga mellan investerings-case och faktiskt utfall:

| MSEK | Vid investering (plan) | Aktuellt utfall | Avvikelse | Kommentar |
|------|----------------------|-----------------|-----------|-----------|
| Omsättning | | | | |
| Omsättningstillväxt | | | | |
| EBITDA | | | | |
| EBITDA-marginal | | | | |
| FCF | | | | |
| Nettoskuld/EBITDA | | | | |

Beräkna:
- **Nuvarande implied value** baserat på aktuell EBITDA × relevant multipel
- **Nuvarande MOIC och IRR** baserat på investerat belopp och nuvarande NAV
- **Avvikelse mot plan** — ligger vi före, efter eller i linje?

### Steg 3: Gå igenom varje initiativ i värdeskapandeplanen

Per initiativ, dokumentera:

| Fält | Innehåll |
|------|----------|
| **Initiativ** | Namn och beskrivning |
| **Typ** | Organisk tillväxt / Marginalförbättring / Add-on / Organisation / Annat |
| **Mål (vid start)** | Kvantifierat mål (t.ex. "Öka EBITDA-marginal från 15% till 20%") |
| **Status** | ✅ Genomfört / 🔄 Pågår enligt plan / ⚠️ Försenat / ❌ Avbrutet / 🆕 Nytt |
| **Utfall** | Faktiskt resultat, kvantifierat |
| **EBITDA-effekt** | Uppskattad bidragande EBITDA-effekt (MSEK/år) |
| **Avvikelse** | Skillnad mot plan med förklaring |
| **Lärdomar** | Vad fungerade, vad fungerade inte |

### Steg 4: Bygg en EBITDA-brygga (värdeskapandebrygga)

Visualisera hur värde har skapats:

```
EBITDA vid investering
  + Organisk omsättningstillväxt × marginal
  + Marginalförbättring (operativa initiativ)
  + Add-on-förvärv (inkl synergier)
  ± Marknadseffekter (konjunktur, prisförändringar)
  ± Övriga effekter
  = Aktuell EBITDA
```

Kvantifiera varje komponent i MSEK. Detta visar tydligt **var** värdet har skapats och var det saknas.

### Steg 5: Uppdatera värdeskapandeplanen

Baserat på genomgången, uppdatera planen:

**Ta bort:**
- Initiativ som genomförts (markera som ✅)
- Initiativ som avbrutits med motivering

**Revidera:**
- Initiativ som försenats — ny tidslinje och åtgärder
- Initiativ vars mål behöver justeras (uppåt eller nedåt)

**Lägg till:**
- Nya initiativ som identifierats under året
- Nya möjligheter baserat på förändrad marknad

Per initiativ i den uppdaterade planen:

| Fält | Innehåll |
|------|----------|
| **Initiativ** | Namn |
| **Mål** | Kvantifierat slutmål |
| **Tidsplan** | Start → förväntad slutleverans |
| **Ansvarig** | Vem i bolaget/Norvik äger detta |
| **EBITDA-effekt** | Förväntad effekt (MSEK/år) |
| **Resurskrav** | Investering, rekrytering, extern hjälp |
| **Milstolpar** | 2–3 checkpoints för uppföljning |
| **Risk** | Huvudrisker och mitigerande åtgärder |

### Steg 6: Värdera portföljbolaget och beräkna avkastning

Uppdatera avkastningsprognosen:

| Scenario | EBITDA (exit) | Multipel | EV | Equity value | MOIC | IRR |
|----------|--------------|----------|-----|-------------|------|-----|
| **Bear** | | | | | | |
| **Bas** | | | | | | |
| **Bull** | | | | | | |

Jämför med ursprungligt investeringscase:
- Är vi på spåret mot target-avkastning?
- Vad behöver hända för att nå target?
- Har tidshorisonten förändrats?

### Steg 7: Formulera prioriteringar för kommande år

Lista de 3–5 viktigaste prioriteringarna, rangordnade:
1. Största värdedrivaren — vad ger mest EBITDA-effekt?
2. Största risken — vad hotar mest om det inte hanteras?
3. Lägst hängande frukt — vad kan realiseras snabbast?

---

## Outputformat

```markdown
# Årlig värdeskapande-review — [Bolagsnamn] [År]

**Datum:** YYYY-MM-DD
**Period:** Helår [År]
**Upprättad av:** [Namn], Norvik Capital

---

## Executive Summary
- [Övergripande bedömning: på spåret / försenat / bättre än plan]
- [Viktigaste framsteg under året]
- [Största avvikelse från plan]
- [Avkastningsstatus: aktuell IRR/MOIC vs target]
- [Viktigaste prioritering kommande år]

## 1. Investeringstes — påminnelse

| | |
|---|---|
| **Investerat** | [Datum], [belopp] MSEK |
| **Ägarandel** | X% |
| **Investeringstes** | [3–5 punkter] |
| **Target-avkastning** | IRR X%, MOIC X.Xx |

## 2. Finansiellt utfall vs plan

| MSEK | Plan (vid inv.) | [År-1] Utfall | [År] Utfall | Avvikelse vs plan |
|------|-----------------|---------------|-------------|-------------------|
| Omsättning | | | | |
| Omsättningstillväxt | | | | |
| EBITDA | | | | |
| EBITDA-marginal | | | | |
| FCF | | | | |
| Nettoskuld/EBITDA | | | | |

**Kommentar:** [Analys av avvikelser]

## 3. Värdeskapandebrygga (EBITDA)

| Komponent | MSEK | Kommentar |
|-----------|------|-----------|
| EBITDA vid investering | | |
| + Organisk tillväxt | | |
| + Marginalförbättring | | |
| + Add-on-förvärv | | |
| ± Marknadseffekter | | |
| ± Övrigt | | |
| **= Aktuell EBITDA** | **X** | |

## 4. Initiativuppföljning

| # | Initiativ | Typ | Mål | Status | Utfall | EBITDA-effekt |
|---|-----------|-----|-----|--------|--------|---------------|
| 1 | | | | ✅/🔄/⚠️/❌ | | |
| 2 | | | | | | |
| ... | | | | | | |

### Detaljerad uppföljning
[Per initiativ: vad hände, varför, lärdomar]

## 5. Uppdaterad värdeskapandeplan

### Pågående och nya initiativ

| # | Initiativ | Mål | Tidsplan | Ansvarig | EBITDA-effekt | Risk |
|---|-----------|-----|----------|----------|---------------|------|
| 1 | | | | | | |
| 2 | | | | | | |

### Avslutade och avbrutna initiativ
[Lista med motivering]

## 6. Avkastningsprognos

| Scenario | EBITDA (exit) | Multipel | EV (MSEK) | MOIC | IRR |
|----------|--------------|----------|-----------|------|-----|
| Bear | | | | | |
| Bas | | | | | |
| Bull | | | | | |

**Jämförelse mot investeringscase:**
[Ligger vi före, i linje eller efter? Vad driver skillnaden?]

## 7. Prioriteringar [Kommande år]

1. **[Prioritet 1]** — [Varför, vad, vem, när]
2. **[Prioritet 2]** — [Varför, vad, vem, när]
3. **[Prioritet 3]** — [Varför, vad, vem, när]

## 8. Beslutspunkter

- [ ] [Beslut som krävs från IC eller styrelse]
- [ ] [Resurstilldelning som behövs]
```

---

## Exempelprompt

> "Gör den årliga värdeskapande-reviewn för CloudFlow 2025. Vid investering var planen att nå 100 MSEK ARR och 15% EBITDA-marginal inom 3 år. Vi ligger nu på 92 MSEK ARR och 12% marginal. Internationaliseringen har försenats men NRR har överträffat målet. Gå igenom alla initiativ och uppdatera planen."

> "Årlig review för Nordisk Precision 2025. OEE har förbättrats från 68% till 73%, men add-on-förvärvet vi planerade föll igenom. Marginalen har förbättrats från 16% till 18,5%. Vad ska vi prioritera nu?"

---

## Dokumentation och lärdom

Den årliga reviewn är ett av de viktigaste tillfällena att lära sig. Reflektera efter genomgång:

- Vilka antaganden i det ursprungliga investment-caset visade sig vara korrekta, och vilka var felaktiga? Vad kan vi lära oss för framtida investeringar?
- Vilka typer av initiativ tenderar att levera bättre respektive sämre än plan — och varför?
- Finns det systematiska mönster i hur vi överestimerar eller underestimerar värdeskapande?

Skriv lärdomar till `gemensamt/learnings/LEARNINGS.md` — årliga reviews är den rikaste källan till lärdomar som förbättrar Norviks investeringsprocess och portföljförvaltning.
