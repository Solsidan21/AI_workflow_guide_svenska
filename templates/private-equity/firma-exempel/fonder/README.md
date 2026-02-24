# Fonder

En mapp per fond. Varje fond har sin egen kontext: LP-bas, villkor, portfölj och prestanda.

## Nuvarande fonder

### `fond-I/` — Norvik Capital Fund I
- **Vintage:** 2020
- **Committed capital:** 500 MSEK
- **Status:** Fullinvesterad (4 portföljbolag)
- **Strategi:** Nordisk mid-market, majoritets- och betydande minoritetsinvesteringar

## Struktur per fond

Varje fond har tre undermappar:

| Mapp | Innehåll |
|------|----------|
| `fonddata/` | Fondvillkor, LPA-sammanfattning, LP-commitments, cap table |
| `rapportering/` | Kvartals- och årsrapporter till LP:er, NAV-beräkningar |
| `prestanda/` | IRR, MOIC, PME-benchmarking, attribution per bolag |

## Framtida fonder

När Norvik startar Fund II skapas en ny mapp `fond-II/` med samma struktur. Historiken för Fund I bevaras intakt.
