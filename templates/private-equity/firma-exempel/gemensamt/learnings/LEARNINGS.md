# Lärdomar — Norvik Capital

> **Vad är denna fil?**
> Här dokumenteras lärdomar från arbete med Claude. Syftet är att bygga upp en kunskapsbas som gör varje framtida session bättre. Lärdomar som godkänns kan på sikt inarbetas i relevanta CLAUDE.md- eller skill-filer.
>
> **Statusflöde:** [NY] → [GRANSKAD] → [INARBETAD] → [ARKIVERAD]
>
> Se `../../CLAUDE.md` (sektionen om självinlärning) för fullständiga instruktioner.

---

## Mall för nya lärdomar

```markdown
### [Kort rubrik som beskriver lärdomen]
- **Datum:** YYYY-MM-DD
- **Uppgift:** [Vad utfördes]
- **Fungerade bra:** [Vad gick bra]
- **Problematiskt:** [Vad var svårt eller gick fel]
- **Lärdom:** [Formulerad som en instruktion — "Gör X när Y" eller "Kontrollera alltid Z innan..."]
- **Status:** [NY]
```

---

## Lärdomar

### ARR-data ska alltid exkludera engångsintäkter vid CloudFlow-analys
- **Datum:** 2024-09-15
- **Uppgift:** Kvartalsanalys av CloudFlows finansiella utveckling Q3 2024
- **Fungerade bra:** Snabb sammanställning av alla SaaS-KPI:er från bolagsdata-mappen. MRR-bridgen gav tydlig bild av tillväxtdrivarna.
- **Problematiskt:** Första beräkningen av ARR inkluderade implementationsintäkter (engångsavgifter) som låg i samma datafil som abonnemangsintäkterna. Gav ett ARR som var ~5% för högt.
- **Lärdom:** Kontrollera alltid att ARR-data exkluderar engångsintäkter (implementation, konsulting, utbildning) vid analys av CloudFlow. Filtrera på intäktskategori "recurring" om det finns i datakällan, annars fråga efter uppdelningen.
- **Status:** [EXEMPEL]

### Nordisk Precisions orderbok kräver manuell verifiering
- **Datum:** 2024-10-22
- **Uppgift:** Uppdatering av orderboken inför styrelsemöte
- **Fungerade bra:** Sammanställningen av orderstatus per kund och produktkategori gav styrelsen en tydlig bild.
- **Problematiskt:** Orderboksfilen innehöll rader med status "tentativ" och "under förhandling" som inte borde räknas som fast orderbok. Dessa utgjorde ~12% av totalen och blåste upp book-to-bill-kvoten.
- **Lärdom:** Filtrera alltid orderboksdata på status "bekräftad" eller "kontrakterad" vid rapportering. Redovisa tentativa order separat som "pipeline" — blanda aldrig med fast orderbok.
- **Status:** [EXEMPEL]

### LP-rapporter kräver aggregerad data — inte bolagsspecifika detaljer
- **Datum:** 2024-11-08
- **Uppgift:** Kvartalsrapport till LP:er för Q3 2024
- **Fungerade bra:** Fondnyckeltalsberäkningen (IRR, MOIC, TVPI) gick smidigt med data från prestanda-mappen.
- **Problematiskt:** Första utkastet inkluderade detaljerade KPI:er per portföljbolag (exakta churn-siffror, kundnamn, marginaldata) som är för detaljerade för LP-rapportering. Behövde skriva om till aggregerad nivå.
- **Lärdom:** Vid LP-rapportering, börja alltid med att sammanfatta per bolag på hög nivå: omsättning, EBITDA, tillväxt, strategisk status. Inkludera aldrig bolagsinterna KPI:er (churn, NRR, kundnamn, OEE per maskin) utan explicit instruktion. LP:er vill se fondutveckling, inte operativa detaljer.
- **Status:** [EXEMPEL]

### Screening-memos ska skrivas innan djupanalys — inte efter
- **Datum:** 2024-12-03
- **Uppgift:** Initial screening av potentiellt förvärv inom IT-bemanning
- **Fungerade bra:** Den färdiga screening-memot var välstrukturerad och gav IC en snabb överblick.
- **Problematiskt:** Jag började med att göra djupare finansiell analys innan screening-memot var klart. Det visade sig att bolaget inte uppfyllde Norviks geografiska krav (huvudkontor utanför Norden). Analysen var onödig.
- **Lärdom:** Skriv alltid screening-memot först och verifiera passform mot hårda kriterier innan någon djupare analys påbörjas. Det tar 15 minuter att skriva en one-pager — det kan spara timmar om svaret är "avböj".
- **Status:** [EXEMPEL]
