# Skill: Screening-memo

## Beskrivning

Denna skill aktiveras när teamet vill göra en snabb genomlysning av en ny investeringsmöjlighet. Screening-memot (one-pager) ger Investment Committee en komprimerad bild av bolaget och en go/no-go-rekommendation — innan tid läggs på djupare analys.

**Triggers:** "screening", "screena bolaget", "screening-memo", "one-pager", "ny deal", "ny investeringsmöjlighet", "first look", "initial bedömning"

---

## Input som behövs

Be användaren om följande grunddata. Alla fält behöver inte vara kända — markera okända fält med ❓ i output.

| Datapunkt | Beskrivning |
|-----------|-------------|
| **Bolagsnamn** | Formellt namn |
| **Bransch** | Sektor och undersegment |
| **Omsättning** | Senaste helår (MSEK) |
| **EBITDA / EBITDA-marginal** | Senaste helår |
| **Omsättningstillväxt** | YoY eller CAGR senaste 3 år |
| **Geografi** | Huvudkontor och primära marknader |
| **Antal anställda** | Ungefärligt |
| **Ägarbild** | Nuvarande ägare, anledning till försäljning |
| **Indikativt EV** | Om känt, annars estimera utifrån branschmultiplar |
| **Källa** | Hur vi hittade bolaget (mäklare, nätverk, proaktivt) |

---

## Steg-för-steg-instruktioner

### Steg 1: Verifiera mot hårda kriterier

Kontrollera omedelbart mot Norviks hårda screeningkriterier:

| Kriterium | Krav |
|-----------|------|
| **Enterprise value** | 100–500 MSEK |
| **Geografi** | Norden (huvudkontor och primär verksamhet) |
| **Ägarform** | Majoritet eller betydande minoritet med styrelseinflytande möjlig |
| **Lönsamhet** | Positiv EBITDA (undantag möjligt för SaaS med stark unit economics) |
| **Storlek** | Minst 30 MSEK i omsättning |

Om något hårt kriterium **inte** uppfylls — flagga det tydligt och ange om det finns rimlig grund för undantag. Om flera hårda kriterier brister, rekommendera AVBÖJ direkt.

### Steg 2: Bedöm mjuka kriterier

Utvärdera och gradera (✅ Stark / 🟡 Okej / ❌ Svag / ❓ Okänt):

| Kriterium | Vad vi letar efter |
|-----------|-------------------|
| **Tillväxt** | Organisk omsättningstillväxt >5% eller tydlig tillväxtpotential |
| **EBITDA-marginal** | >10% (eller trovärdig plan att nå dit) |
| **Marknadsutsikter** | Stabil eller växande marknad med strukturell medvind |
| **Ägarhistorik** | Grundarlett eller bolag med etablerad ledning som vill fortsätta |
| **Add-on-potential** | Fragmenterad marknad som möjliggör tilläggsförvärv |
| **ESG-profil** | Inga fundamentala ESG-risker |
| **Exit-möjligheter** | Realistiska exitvägar inom 3–7 år |
| **Passform med portföljen** | Komplementärt till befintlig portfölj, ingen överexponering mot samma sektor |

### Steg 3: Formulera investeringslogik

Besvara frågan: **varför skulle Norvik Capital vilja äga detta bolag?**

Identifiera 3–5 punkter som gör investeringen attraktiv. Fokusera på:
- Strukturell tillväxt i marknaden
- Operativ förbättringspotential (marginalexpansion, effektivisering)
- Add-on-möjligheter (fragmenterad marknad)
- Starka marknadspositioner eller konkurrensfördelar
- Potentiella exitvägar och förväntad avkastning

### Steg 4: Identifiera nyckelfrågor och risker

Lista de 3–5 viktigaste frågorna som måste besvaras om vi går vidare. Var specifik:
- Inte "marknadsrisk" utan "hur känsligt är bolaget för konjunkturnedgång — vad hände 2020?"
- Inte "kundkoncentration" utan "topp 3 kunder står för X% — hur ser avtalssituationen ut?"

### Steg 5: Ge en tydlig rekommendation

Välj en av tre:
- **GÅ VIDARE** — Initiera djupare analys och kontakta bolaget/rådgivaren
- **BEVAKA** — Intressant men inte nu (ange specifik trigger för att ta upp igen)
- **AVBÖJ** — Passar inte Norviks profil (ange huvudskäl)

Motivera rekommendationen i 2–3 meningar.

---

## Outputformat

```markdown
# Screening: [Bolagsnamn] — [Datum]

## Executive Summary
- [Viktigaste insikten — vad gör detta intressant eller ointressant]
- [Passform mot Norviks profil]
- [Rekommendation i en mening]

## Snapshot

| | |
|---|---|
| **Bolag** | |
| **Bransch** | |
| **Omsättning** | X MSEK |
| **EBITDA / EBITDA-marginal** | X MSEK / X% |
| **Omsättningstillväxt** | X% YoY |
| **Enterprise value (indikativt)** | X MSEK |
| **Geografi** | |
| **Antal anställda** | |
| **Ägarsituation** | |
| **Källa** | |

## Verksamhetsbeskrivning
[3–5 meningar: Vad gör bolaget? Kunder? Affärsmodell? Vad är unikt?]

## Investeringslogik — varför är detta intressant?
1. [Argument 1]
2. [Argument 2]
3. [Argument 3]

## Nyckelfrågor och risker
1. [Specifik fråga/risk 1]
2. [Specifik fråga/risk 2]
3. [Specifik fråga/risk 3]

## Passform mot Norviks kriterier

### Hårda kriterier

| Kriterium | Uppfyllt? | Kommentar |
|-----------|-----------|-----------|
| EV 100–500 MSEK | ✅ / ❌ / ❓ | |
| Nordisk | ✅ / ❌ / ❓ | |
| Majoritet/minoritet möjlig | ✅ / ❌ / ❓ | |
| Positiv EBITDA | ✅ / ❌ / ❓ | |
| Omsättning >30 MSEK | ✅ / ❌ / ❓ | |

### Mjuka kriterier

| Kriterium | Bedömning | Kommentar |
|-----------|-----------|-----------|
| Tillväxt >5% | ✅ / 🟡 / ❌ / ❓ | |
| EBITDA-marginal >10% | ✅ / 🟡 / ❌ / ❓ | |
| Marknadsutsikter | ✅ / 🟡 / ❌ / ❓ | |
| Ägarhistorik | ✅ / 🟡 / ❌ / ❓ | |
| Add-on-potential | ✅ / 🟡 / ❌ / ❓ | |
| ESG-profil | ✅ / 🟡 / ❌ / ❓ | |
| Exit-möjligheter | ✅ / 🟡 / ❌ / ❓ | |

## Rekommendation

**[GÅ VIDARE / BEVAKA / AVBÖJ]**

[2–3 meningar med motivering]

[Vid BEVAKA: ange trigger — "Ta upp igen när/om..."]
[Vid GÅ VIDARE: ange förslag på nästa steg]
```

---

## Exempelprompt

> "Vi har fått en teaser på ett svenskt industribolag, Precisionslösningar AB, som tillverkar hydraulikkomponenter i Jönköping. Omsättning ~180 MSEK, EBITDA ~25 MSEK, tillväxt 8% YoY. Ägaren (grundare, 62 år) vill trappa ner. Indikativt EV runt 200 MSEK. Kan du göra en snabb screening?"

> "Mäklaren skickade info om ett danskt SaaS-bolag inom fastighetsförvaltning, 45 MSEK ARR, 30% tillväxt men negativt EBITDA (-5 MSEK). Gör en screening-one-pager."

---

## Dokumentation och lärdom

När du slutfört screening-memot, reflektera kort:

- Var datakvaliteten tillräcklig för att göra en meningsfull bedömning, eller behövde du göra antaganden som borde flaggas?
- Saknades det data som hade förändrat rekommendationen?
- Finns det en lärdom om processen (t.ex. branschspecifik insikt, ny typ av källa, formatjustering)?

Skriv en kort lärdom till `gemensamt/learnings/LEARNINGS.md` enligt den etablerade mallen om du identifierar något som är generaliserbart och värdefullt för framtida screeningar.
