# Pipeline — Deal Flow

Nya investeringsmöjligheter, från första kontakt till investeringsbeslut (eller avböjning).

## Arbetsflöde

```
Ny möjlighet → Screening → Aktiv process (DD) → IC-beslut → Investering/Avböjning
                  ↓              ↓                              ↓
              screening/    aktiva-processer/                avslutade/
                                                      eller portfoljbolag/
```

## Undermappar

### `screening/`
Initiala bedömningar av nya möjligheter:
- Teasers och CIM-sammanfattningar
- Snabbanalyser (one-pagers)
- Strategisk passform-bedömning
- Go/no-go-underlag

Typiskt utvärderar Norvik 2–3 nya möjligheter parallellt i denna fas.

### `aktiva-processer/`
Möjligheter som gått vidare till fördjupad analys:
- Due diligence-material (kommersiell, finansiell, legal, teknisk)
- Värderingsmodeller och budanalys
- Investment Committee-memo (IC-memo)
- Förhandlingsunderlag (SPA-utkast, indikativa bud)

Varje aktiv process får typiskt en egen undermapp med bolagets namn.

### `avslutade/`
Arkiv för processer som inte ledde till investering:
- Avböjda möjligheter med kortfattad motivering
- Processer som avbröts av säljaren
- Referensmaterial för framtida liknande möjligheter

Att behålla avslutade processer ger värdefull historik: varför tackade vi nej? Vad lärde vi oss?

## Tips

- Använd konsekvent namngivning: `bolagsnamn-ab/` i kebab-case
- Dokumentera alltid varför en process avslutades — det sparar tid vid framtida liknande möjligheter
- Flytta relevant material till `portfoljbolag/` vid genomförd investering, men behåll en referens i `avslutade/`
