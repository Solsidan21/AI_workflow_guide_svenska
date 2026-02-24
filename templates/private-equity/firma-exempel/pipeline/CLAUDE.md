# CLAUDE.md — Pipeline / Deal Flow

## Syfte

Denna mapp hanterar alla nya investeringsmöjligheter — från första screening till investeringsbeslut eller avböjning. All analys här görs utifrån frågan: **ska Norvik Capital investera i detta bolag?**

## Screeningkriterier

Alla nya möjligheter ska initialt utvärderas mot Norviks investeringskriterier. Ett bolag behöver inte uppfylla samtliga kriterier för att gå vidare, men avvikelser ska noteras och motiveras.

### Hårda kriterier (ska uppfyllas)

| Kriterium | Krav |
|-----------|------|
| **Enterprise value** | 100–500 MSEK |
| **Geografi** | Norden (Sverige, Norge, Danmark, Finland) — huvudkontor och primär verksamhet |
| **Ägarform** | Majoritet eller betydande minoritet med styrelseinflytande |
| **Lönsamhet** | Positiv EBITDA (undantag möjligt för SaaS med stark unit economics) |
| **Storlek** | Minst 30 MSEK i omsättning |

### Mjuka kriterier (utvärderas och graderas)

| Kriterium | Vad vi letar efter |
|-----------|-------------------|
| **Bransch** | Teknik/SaaS, industri, tjänster, hälsovård — undvik fastigheter, råvaror, early-stage biotech |
| **Tillväxt** | Organisk omsättningstillväxt >5% eller tydlig tillväxtpotential |
| **EBITDA-marginal** | >10% (eller trovärdig plan att nå dit) |
| **Marknadsutsikter** | Stabil eller växande marknad med strukturell medvind |
| **Ägarhistorik** | Grundarlett eller bolag med etablerad ledning som vill fortsätta |
| **Add-on-potential** | Fragmenterad marknad som möjliggör tilläggsförvärv |
| **ESG-profil** | Inga fundamentala ESG-risker — miljö, socialt, styrning |
| **Exit-möjligheter** | Realistiska exitvägar (strategisk köpare, PE, IPO) inom 3–7 år |

## Format för screening-memos

Varje ny möjlighet som utvärderas ska dokumenteras i ett screening-memo (one-pager) med följande struktur:

```markdown
# Screening: [Bolagsnamn] — [Datum]

## Snapshot

| | |
|---|---|
| Bolag | |
| Bransch | |
| Omsättning | |
| EBITDA / EBITDA-marginal | |
| Enterprise value (indikativt) | |
| Geografi | |
| Ägarsituation | |
| Källa / hur vi hittade bolaget | |

## Verksamhetsbeskrivning (3–5 meningar)
[Vad gör bolaget? Kunder? Affärsmodell?]

## Investeringslogik — varför är detta intressant?
1. [Argument 1]
2. [Argument 2]
3. [Argument 3]

## Nyckelfrågor och risker
1. [Risk/fråga 1]
2. [Risk/fråga 2]
3. [Risk/fråga 3]

## Passform mot Norviks kriterier

| Kriterium | Uppfyllt? | Kommentar |
|-----------|-----------|-----------|
| EV 100–500 MSEK | ✅ / ❌ / ❓ | |
| Nordisk | ✅ / ❌ / ❓ | |
| Majoritet/minoritet möjlig | ✅ / ❌ / ❓ | |
| Positiv EBITDA | ✅ / ❌ / ❓ | |
| Omsättning >30 MSEK | ✅ / ❌ / ❓ | |
| Tillväxt >5% | ✅ / ❌ / ❓ | |
| Add-on-potential | ✅ / ❌ / ❓ | |
| ESG-profil | ✅ / ❌ / ❓ | |

## Rekommendation
[ ] GÅ VIDARE — Initiera djupare analys
[ ] BEVAKA — Intressant men inte nu (ange varför och trigger)
[ ] AVBÖJ — Passar inte (ange huvudskäl)
```

## Processens faser och mappstruktur

| Fas | Mapp | Typiska filer |
|-----|------|---------------|
| **Screening** | `screening/[bolagsnamn-ab]/` | Screening-memo, teaser, initial data |
| **Aktiv process** | `aktiva-processer/[bolagsnamn-ab]/` | CIM, DD-material, värderingsmodell, IC-memo |
| **Avslutad** | `avslutade/[bolagsnamn-ab]/` | Sammanfattning + motivering till avböjning |

### Namnkonvention

- Mappnamn: `bolagsnamn-ab` i kebab-case
- Filnamn: `screening-[bolagsnamn]-YYYY-MM-DD.md`
- Vid statusbyte (screening → aktiv process): flytta mappen, uppdatera inte filnamn

## Regler för pipeline-arbete

- **Dokumentera alltid varför en process avslutades** — det sparar tid vid framtida liknande möjligheter
- **Vid aktiv DD-process:** Strukturera materialet enligt DD-ramverket i `../../gemensamt/ramverk/`
- **IC-memo:** Använd mallen i `../../gemensamt/mallar/` — avvik aldrig från standardstrukturen
- **Värdering i DD-fas:** Tillämpa alltid DCF + multipelanalys med scenarioanalys (bas, bull, bear)
- **Konfidentialitet:** Pipeline-bolag är strikt konfidentiella. Nämn aldrig bolagsnamn utanför pipeline-kontexten om inte bolaget blivit ett portföljbolag.
- **Vid genomförd investering:** Flytta relevant material till `../../portfoljbolag/[bolagsnamn-ab]/` och behåll en referenslänk i `avslutade/`
