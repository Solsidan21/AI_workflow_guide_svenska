# Norvik Capital — Exempelstruktur för PE-firma

> **Detta är ett fiktivt exempel.** Norvik Capital finns inte på riktigt. Strukturen är byggd för att visa hur en liten nordisk PE-firma kan organisera sitt arbete med Claude som AI-assistent.

---

## Om Norvik Capital

| | |
|---|---|
| **Namn** | Norvik Capital |
| **Grundat** | 2018 |
| **Kontor** | Stockholm |
| **Strategi** | Nordisk mid-market PE — majoritets- och betydande minoritetsinvesteringar |
| **Aktiv fond** | Norvik Capital Fund I (vintage 2020, 500 MSEK committed capital) |
| **Team** | 6 personer: 2 partners, 2 VP/directors, 1 analytiker, 1 IR/admin |

### Portföljbolag (Fund I)

| Bolag | Sektor | Nyckeltal | Investeringsår |
|-------|--------|-----------|----------------|
| **CloudFlow AB** | SaaS / logistik | 80 MSEK ARR | 2021 |
| **Nordisk Precision AB** | Industri / CNC-bearbetning | 220 MSEK omsättning | 2021 |
| **Arbetslyft AB** | Bemanning & konsult | 150 MSEK omsättning | 2022 |
| **MedTech Nordic AB** | Medicinsk teknik | 60 MSEK omsättning | 2023 |

### Deal pipeline

Norvik utvärderar löpande 2–3 nya investeringsmöjligheter parallellt, i olika stadier från initial screening till aktiv due diligence.

---

## Mappstruktur — Översikt

```
firma-exempel/
│
├── firma/                         ← Firmanivå: det som gäller hela Norvik Capital
│   ├── compliance/                   Regulatorisk, AML/KYC, policyer
│   ├── fundraising/                  Fundraising för nuvarande och framtida fonder
│   ├── investor-relations/           LP-kommunikation, kvartalsutskick, AGM
│   └── team/                         Organisation, kompetenser, onboarding
│
├── fonder/                        ← Fondnivå: en mapp per fond
│   └── fond-I/                       Norvik Capital Fund I
│       ├── fonddata/                 Fondvillkor, LPA, commitments, cap table
│       ├── rapportering/             Kvartals- och årsrapporter till LP:er
│       └── prestanda/                IRR, MOIC, benchmarking, attribution
│
├── portfoljbolag/                 ← Portföljbolag: en mapp per bolag
│   ├── cloudflow-ab/
│   ├── nordisk-precision-ab/
│   ├── arbetslyft-ab/
│   └── medtech-nordic-ab/
│       Varje bolag har samma undermappar:
│       ├── bolagsdata/               Finansiell data, KPI:er, budget
│       ├── analys/                   Löpande analyser, värderingar
│       ├── styrelsearbete/           Styrelsepaket, protokoll, beslut
│       ├── vardeskapande/            100-dagarsplan, initiativ, uppföljning
│       └── output/                   Färdiga leveranser, presentationer
│
├── pipeline/                      ← Deal flow: nya investeringsmöjligheter
│   ├── screening/                    Initiala screeningar och snabbanalyser
│   ├── aktiva-processer/             Pågående DD-processer och förhandlingar
│   └── avslutade/                    Avböjda eller avslutade processer (arkiv)
│
└── gemensamt/                     ← Delade resurser för hela firman
    ├── mallar/                       Dokumentmallar (IC-memo, styrelsepaket, etc.)
    ├── skills/                       Claude-skills som används firmabrett
    ├── ramverk/                      Analysramverk (DD-checklista, värdering, etc.)
    └── branschdata/                  Branschreferenser, multipeldata, benchmarks
```

---

## Varför ser strukturen ut så här?

### Tre separata nivåer speglar verkligheten

En PE-firma opererar på tre distinkta nivåer som har olika informationsbehov:

1. **Firmanivå** — saker som gäller oavsett fond eller bolag: compliance, team, fundraising. Förändras sällan.
2. **Fondnivå** — specifikt för en fond och dess LP:er: rapportering, prestanda, fondvillkor. En fond per vintage.
3. **Portföljbolagsnivå** — det dagliga arbetet: analys, styrelsematerial, värdeskapande. Här spenderas mest tid.

Denna separation gör att Claude får rätt kontext för rätt uppgift. När du arbetar i `portfoljbolag/cloudflow-ab/` behöver Claude inte veta om fundraising — men den behöver veta allt om CloudFlows affärsmodell och KPI:er.

### Pipeline är separat från portföljbolag

Innan ett bolag blir ett portföljbolag lever det i `pipeline/`. Det har en annan arbetsrytm (screening → DD → IC-beslut) och annan information (teaser, CIM, indikativa bud). När en investering genomförs flyttas relevant material till den nya portföljbolagsmappen.

### Gemensamma resurser undviker duplicering

Mallar, skills och ramverk som används på flera ställen samlas i `gemensamt/`. Det innebär att en uppdatering av exempelvis DD-checklistan sker på ett ställe och gäller överallt.

---

## Koppling till PE-arbetscykeln

Strukturen följer en investerings livscykel genom mapparna:

```
SOURCING          SCREENING         DUE DILIGENCE      INVESTERING
pipeline/         pipeline/         pipeline/           portfoljbolag/
screening/        screening/        aktiva-processer/   [nytt bolag]/
                                                        bolagsdata/

     ↓                 ↓                  ↓                   ↓

VÄRDESKAPANDE     RAPPORTERING      EXIT-FÖRBEREDELSE   EXIT
portfoljbolag/    fonder/fond-I/    portfoljbolag/      fonder/fond-I/
[bolag]/          rapportering/     [bolag]/            prestanda/
vardeskapande/                      analys/
styrelsearbete/                     output/
```

| Fas | Primär mapp | Typiska uppgifter |
|-----|-------------|-------------------|
| **Sourcing** | `pipeline/screening/` | Snabbanalys av nya möjligheter, marknadskartläggning |
| **Screening** | `pipeline/screening/` | Initial finansiell analys, strategisk passform |
| **Due diligence** | `pipeline/aktiva-processer/` | Fullständig DD, värdering, IC-memo |
| **Investering** | `portfoljbolag/[bolag]/` | Nytt bolag skapas, 100-dagarsplan |
| **Värdeskapande** | `portfoljbolag/[bolag]/vardeskapande/` | Operativa initiativ, KPI-uppföljning |
| **Styrelsemöten** | `portfoljbolag/[bolag]/styrelsearbete/` | Styrelsepaket, kvartalsrapporter |
| **LP-rapportering** | `fonder/fond-I/rapportering/` | Kvartals- och årsrapporter till LP:er |
| **Exit** | `portfoljbolag/[bolag]/analys/` + `output/` | Exit-analys, försäljningsmaterial |

---

## Var kommer CLAUDE.md-filer att placeras?

> **Obs:** CLAUDE.md-filer skapas i nästa steg. Nedan beskrivs planen.

CLAUDE.md-filer ger Claude kontext och regler för den nivå den arbetar på. Strukturen planerar för CLAUDE.md på flera nivåer:

```
firma-exempel/
├── CLAUDE.md                      ← Firmabrett: ton, språk, grundregler
│
├── firma/
│   └── CLAUDE.md                  ← Instruktioner för firmaoperationer
│
├── fonder/fond-I/
│   └── CLAUDE.md                  ← Fondspecifik kontext: LP:er, villkor, rapporteringsformat
│
├── portfoljbolag/
│   ├── CLAUDE.md                  ← Gemensamt för alla portföljbolag
│   ├── cloudflow-ab/
│   │   └── CLAUDE.md              ← CloudFlow-specifik: affärsmodell, KPI:er, strategi
│   ├── nordisk-precision-ab/
│   │   └── CLAUDE.md              ← Nordisk Precision-specifik
│   ├── arbetslyft-ab/
│   │   └── CLAUDE.md              ← Arbetslyft-specifik
│   └── medtech-nordic-ab/
│       └── CLAUDE.md              ← MedTech Nordic-specifik
│
├── pipeline/
│   └── CLAUDE.md                  ← Instruktioner för screening och DD
│
└── gemensamt/
    └── CLAUDE.md                  ← Beskrivning av delade resurser
```

Denna hierarki utnyttjar Claude Codes kontextkedja: Claude läser CLAUDE.md från rot och nedåt, så specifik kontext (t.ex. CloudFlows ARR-definition) bara laddas när du arbetar i den mappen.

---

## Hur du använder denna struktur

1. **Kopiera** hela `firma-exempel/`-mappen till ditt eget projekt
2. **Byt namn** på bolagen och fyllna i med er egen data
3. **Anpassa** undermapparna efter era behov (lägg till eller ta bort efter behov)
4. **Skapa CLAUDE.md-filer** i varje nivå (se nästa kapitel i instruktionsboken)
5. **Börja arbeta** — öppna en mapp i Claude Code och låt kontexten göra jobbet

---

## Datasekretess

**Denna exempelstruktur innehåller inga verkliga data.** När du fyller i med er egen data:

- Lägg aldrig känslig data i git utan kryptering eller anonymisering
- Använd `.gitignore` för att exkludera filer med reell bolagsdata
- Behandla allt som versionshanteras som potentiellt synligt
- Se `gemensamt/` för mallar på hur data kan anonymiseras för delning
