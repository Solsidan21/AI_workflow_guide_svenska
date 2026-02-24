# Skill: Due Diligence

## Beskrivning

Denna skill aktiveras när användaren behöver stöd med due diligence-arbete — oavsett om det gäller att skapa en DD-checklista, analysera DD-fynd eller sammanställa en DD-rapport.

**Triggers:** "due diligence", "DD-checklista", "DD-analys", "DD-rapport", "genomlysning", "besiktning av bolag"

---

## Due Diligence-områden

### 1. Finansiell Due Diligence

**Syfte:** Verifiera bolagets finansiella ställning och historiska prestation.

**Checklista:**

- [ ] **Intäktskvalitet:** Är intäkterna återkommande, kontrakterade, diversifierade?
- [ ] **EBITDA-brygga:** Normaliserad EBITDA med tydliga justeringar (engångsposter, ägarlön, related-party-transaktioner)
- [ ] **Rörelsekapitalanalys:** Normaliserat rörelsekapital, säsongsmönster, trender
- [ ] **Nettoskuld:** Skuld- och skuldliknande poster, off-balance-sheet-åtaganden
- [ ] **CapEx-analys:** Underhåll vs tillväxt, uppskjutna investeringar
- [ ] **Kassaflödeskvalitet:** Cash conversion, avstämning resultat vs kassa
- [ ] **Skattesituation:** Uppskjutna skatter, skattetvister, transfer pricing
- [ ] **Redovisningsprinciper:** IFRS/K3, konsekvens, aggressiv/konservativ
- [ ] **Prognoser:** Rimlighet i bolagets affärsplan, track record av budgetuppfyllelse
- [ ] **Revisionsberättelser:** Anmärkningar, särskilda notiser

**Prioritet:** HÖG — Alltid genomföra

### 2. Kommersiell Due Diligence

**Syfte:** Validera bolagets marknadssituation och tillväxtmöjligheter.

**Checklista:**

- [ ] **Marknadsstorlek och tillväxt:** TAM/SAM/SOM med oberoende källor
- [ ] **Konkurrensdynamik:** Marknadsandelar, konkurrenternas styrkor/svagheter
- [ ] **Kundanalys:** Topp 10/20-kunder, koncentration, avtalslängd, churn
- [ ] **Kundreferenser:** Intervjuer med nyckelkunder (min 5–10)
- [ ] **Prisstrategi:** Prissättningsmodell, priselasticitet, marginalutveckling
- [ ] **Försäljningsprocess:** Pipeline, konverteringsgrad, säljcykel
- [ ] **Marknadstrender:** Strukturella förändringar, digitalisering, regulatoriska skiften
- [ ] **Tillväxtinitiativ:** Validering av bolagets tillväxtplan
- [ ] **Inträdesbarriärer:** Vad hindrar nya konkurrenter?

**Prioritet:** HÖG — Alltid genomföra

### 3. Legal Due Diligence

**Syfte:** Identifiera juridiska risker och säkerställa korrekt ägarstruktur.

**Checklista:**

- [ ] **Bolagsstruktur:** Ägarkedja, dotterbolag, styrelsens sammansättning
- [ ] **Väsentliga avtal:** Kundavtal, leverantörsavtal, change-of-control-klausuler
- [ ] **Anställningsavtal:** Nyckelanställda, konkurrensklausuler, pensionsåtaganden
- [ ] **IP och varumärken:** Patent, varumärkesregistreringar, licensavtal
- [ ] **Tvister:** Pågående och potentiella rättsprocesser
- [ ] **Regulatorisk compliance:** Branschspecifika tillstånd, myndighetskrav
- [ ] **Fastigheter:** Hyresavtal, äganderätt, miljöansvar
- [ ] **Dataskydd (GDPR):** Personuppgiftshantering, dataskyddsombud, incidenthistorik
- [ ] **Försäkringar:** Typ, omfattning, historiska skador

**Prioritet:** HÖG — Alltid genomföra

### 4. Operativ Due Diligence

**Syfte:** Bedöma bolagets operativa kapacitet och förbättringsmöjligheter.

**Checklista:**

- [ ] **Ledningsgrupp:** Kompetens, erfarenhet, track record, incitamentsstruktur
- [ ] **Organisation:** Struktur, nyckelroller, personalberoende
- [ ] **Personalfrågor:** Personalomsättning, rekryteringsutmaningar, arbetsgivarvarumärke
- [ ] **IT-infrastruktur:** System, teknikskuld, cybersäkerhet, IT-beroenden
- [ ] **Processer:** Kärnprocesser, automatiseringsgrad, flaskhalsar
- [ ] **Leveranskedja:** Leverantörsberoenden, alternativa källor, logistik
- [ ] **Skalbarhet:** Kan verksamheten växa utan proportionell kostnad?
- [ ] **Integrationsmöjligheter:** Synergier med befintlig portfölj
- [ ] **Operativa förbättringar:** Identifiera "lågt hängande frukt"

**Prioritet:** MEDEL-HÖG — Anpassa djup efter bolagstyp

### 5. ESG Due Diligence

**Syfte:** Bedöma miljö-, sociala och styrningsrelaterade risker och möjligheter.

**Checklista:**

- [ ] **Miljö:** Utsläpp, energiförbrukning, avfallshantering, miljötillstånd
- [ ] **Klimatrisk:** Fysisk risk (extremväder) och transitionsrisk (regleringar, koldioxidskatt)
- [ ] **Socialt:** Arbetsmiljö, mångfald och inkludering, leverantörskedjan
- [ ] **Styrning:** Bolagsstyrning, anti-korruption, visselblåsarfunktion
- [ ] **Regulatorisk:** EU-taxonomin, CSRD-krav, branschspecifika ESG-krav
- [ ] **ESG-möjligheter:** Hållbara produkter/tjänster, grön tillväxt
- [ ] **ESG-rapportering:** Nuvarande nivå, gap till best practice

**Prioritet:** MEDEL — Anpassa efter bransch och fondkrav

---

## Riskflaggning

Claude ska flagga risker med tydliga prioritetsnivåer:

### Hög prioritet (deal-breaker-potential)
Formatera med **FET STIL** och prefixet `[HÖG RISK]`:
- Exempel: **[HÖG RISK] Kundkoncentration — topp 3 kunder står för 65% av omsättningen**
- Kräver omedelbar utredning och eventuellt prisavdrag eller deal-structure-anpassning

### Medel prioritet (väsentlig men hanterbar)
Formatera med prefixet `[MEDEL RISK]`:
- Exempel: [MEDEL RISK] IT-system behöver uppgraderas inom 2 år — uppskattad kostnad 5–8 MSEK
- Bör adresseras i 100-dagarsplan eller värdeskapandeplan

### Låg prioritet (notera men inte avgörande)
Formatera med prefixet `[LÅG RISK]`:
- Exempel: [LÅG RISK] Hyresavtal för Göteborgskontoret löper ut 2026 — bör omförhandlas
- Hantera som del av normal portföljförvaltning

---

## Outputformat

```markdown
# Due Diligence-rapport — [Bolagsnamn]

## Executive Summary
- **Övergripande bedömning:** [Grön/Gul/Röd] — [Sammanfattning]
- **Kritiska fynd:** [Lista med de viktigaste fynden]
- **Rekommendation:** [Gå vidare / Pausa / Avbryt]

## Hög-risk-fynd
[Detaljerad beskrivning av varje hög-risk-fynd med mitigeringsplan]

## Finansiell DD — Sammanfattning
**Status:** [Genomförd / Pågående / Ej påbörjad]
[Fynd och kommentarer per checklistepunkt]

## Kommersiell DD — Sammanfattning
**Status:** [Genomförd / Pågående / Ej påbörjad]
[Fynd och kommentarer per checklistepunkt]

## Legal DD — Sammanfattning
**Status:** [Genomförd / Pågående / Ej påbörjad]
[Fynd och kommentarer per checklistepunkt]

## Operativ DD — Sammanfattning
**Status:** [Genomförd / Pågående / Ej påbörjad]
[Fynd och kommentarer per checklistepunkt]

## ESG DD — Sammanfattning
**Status:** [Genomförd / Pågående / Ej påbörjad]
[Fynd och kommentarer per checklistepunkt]

## Risköversikt

| # | Risk | Kategori | Prioritet | Påverkan (MSEK) | Mitigering | Ansvarig |
|---|------|----------|-----------|-----------------|------------|----------|
| 1 | | | | | | |

## Nästa steg och öppna frågor
1. [Åtgärd 1 — ansvarig — deadline]
2. [Åtgärd 2 — ansvarig — deadline]
```

---

## Exempelprompt

> "Vi är i DD-fas för ett förvärv av ett industribolag med 300 MSEK i omsättning. Kan du skapa en komplett DD-checklista anpassad för bolaget? Fokusera extra på operativa risker — bolaget har en komplex leveranskedja och är beroende av några få leverantörer. Vi behöver även en ESG-genomlysning då vår fond har strikta ESG-krav."
