# Kapitel 04 — Mappstruktur och kontext

> *Det har ar kapitlet som binder ihop allt. Struktur ar inte administration — det ar det som gor AI bra.*

---

## Varfor mappstruktur spelar roll

Nar Claude Code startar laser den inte bara din prompt. Den ser **filnamn, mappnamn och hela projektstrukturen**. Allt detta ar kontext som paverkar kvaliteten pa svaren.

**Analogi:** Tva skrivbord. Det ena ar valorganiserat — mappar med etiketter, tydliga namn, logisk ordning. Om du ber nagon hitta "Q3-kassaflodet for Bolag X" tar det sekunder.

Det andra ar kaotiskt — papper overallt, oklara filnamn. Samma fraga tar minuter, och svaret kanske inte ens ar korrekt.

AI fungerar pa exakt samma satt. **Bra struktur = battre svar.**

### Filnamn och mappnamn AR instruktioner

Nar Claude ser:

```
data/finansiellt/arsredovisning-2024.pdf
```

...forstar den automatiskt vad filen ar, vilket ar, och var den passar in. Utan att du behover forklara nagot.

Jamfor med:

```
dokument/fil3.pdf
```

Har forstar Claude ingenting. Du maste forklara allt i din prompt — varje gang.

---

## Principer

### 1. Beskrivande namn

**Sa har:**
```
kassaflodesanalys-2024-Q3.md
konkurrentoversikt-nordisk-hr-tech.md
styrelsepresentation-2024-12.pptx
```

**Inte sa har:**
```
analys1.md
rapport-final-v2-SISTA.md
dok.pptx
```

**Tumregel:** Skulle en kollega forsta vad filen innehaller bara genom att se filnamnet? Om ja — bra namn.

### 2. Logisk hierarki

Organisera filer i en tradstruktur som speglar hur du tanker om arbetet.

```
projekt/bolag-x/
├── data/
│   ├── finansiellt/
│   └── marknad/
├── analys/
└── output/
```

Inte 50 filer i en platt lista. **Tumregel:** Om en mapp har fler an 10-15 filer, bryt ut undermappar.

### 3. Konsistens

Anvand samma monster overallt. Om du anvander `kebab-case` (ord-med-bindestreck) for filnamn, gor det konsekvent. Om du anvander YYYY-MM-DD for datum, gor det overallt.

**Konsistent:**
```
kassaflode-2024-Q1.md
kassaflode-2024-Q2.md
kassaflode-2024-Q3.md
```

**Inkonsistent:**
```
kassaflode Q1 2024.md
kassaflöde-2024-q2.md
KF_Q3_24.md
```

### 4. Separation av data, analys och output

Hall tre typer av material atskillt:

| Mapp | Innehall | Exempel |
|------|---------|---------|
| `data/` | Radata som du **fatt** | Arsredovisningar, CSV-exporter, rapporter |
| `analys/` | Material du **skapat** genom bearbetning | Kassaflodesberakningar, modeller |
| `output/` | **Fardigt** material for leverans | Rapporter, presentationer, memos |

Varfor? Du kan alltid ga tillbaka till radata om nagot ar fel. Och du blandar aldrig ihop arbetsunderlag med fardiga leveranser.

### 5. README-filer

En kort `README.md` i varje mapp hjalper bade dig och Claude att forsta vad mappen innehaller.

**Exempel — `data/finansiellt/README.md`:**
```markdown
# Finansiell data

Arsredovisningar och kvartalsdata for Bolag X.

## Filer
- arsredovisning-YYYY.pdf — Officiella arsredovisningar
- kvartalsdata-YYYY.csv — Revenue, EBITDA, nettoresultat per kvartal

## Kallor
- Arsredovisningar: Bolagsverket / bolaget direkt
- Kvartalsdata: CFO-rapportering
```

---

## CLAUDE.md pa djupet

I kapitel 02 gick vi igenom grunderna. Har gar vi djupare.

### Placering och hierarki

Claude Code laser **alla** CLAUDE.md-filer den stoter pa i mappstrukturen. Det innebar att du kan ha en hierarki av instruktioner:

```
mitt-projekt/
├── CLAUDE.md                    # Overgripande regler
├── data/
│   └── CLAUDE.md                # Regler for datahantering
├── analys/
│   └── CLAUDE.md                # Regler for analyser
└── output/
    └── CLAUDE.md                # Regler for output-format
```

**Hur det fungerar:**

- **Rot-CLAUDE.md** galler for allt arbete. Har placerar du: sprak, ton, projektbeskrivning, generella riktlinjer.
- **Mapp-specifika CLAUDE.md** galler *utover* rot-reglerna nar Claude arbetar i den mappen.

Claude laser alla CLAUDE.md-filer uppat i hierarkin fran den mapp den arbetar i. Sa om Claude arbetar i `analys/kassaflode/` laser den:

1. `analys/kassaflode/CLAUDE.md` (om den finns)
2. `analys/CLAUDE.md` (om den finns)
3. `CLAUDE.md` (i roten)

Du behover inte upprepa generella regler i varje CLAUDE.md — bara det som ar specifikt for just den mappen.

### Vad en bra CLAUDE.md innehaller

**Komplett checklista:**

| Sektion | Syfte | Exempel |
|---------|-------|---------|
| **Roll** | Vem Claude "ar" i projektet | "Erfaren PE-analytiker med fokus pa nordiska SaaS-bolag" |
| **Projektkontext** | Vad projektet handlar om | Bolag, storlek, fas, syfte |
| **Regler** | Format, sprak, stil | MSEK, svenska, tabeller for jamforelser |
| **Vanliga uppgifter** | Steg-for-steg for aterkommande arbete | Kassaflodesanalys, konkurrentoversikt |
| **Filstruktur** | Var Claude hittar vad | data/finansiellt/, analys/, output/ |
| **Mallar** | Vilka mallar som ska anvandas | mallar/investment-memo-mall.md |

### Fullstandigt exempel

```markdown
# CLAUDE.md — Portfoljbolag X

## Roll
Du ar en erfaren PE-analytiker med fokus pa nordiska SaaS-bolag.
Noggrann med siffror, koncis i formuleringar, fokuserad pa
investeringsbeslutet.

## Projektkontext
Bolag X ar ett svenskt HR-tech SaaS-bolag, grundat 2015.
Cirka 200 anstallda, ~150 MSEK i intakter (2024).
Vi befinner oss i initial evaluering — fokus pa att forsta
marknad, tillvaxt och finansiell profil.

## Regler

### Format
- Sprak: svenska
- Ton: formell men tillganglig
- Siffror: MSEK, en decimal, mellanslag som tusentalsavgransare (1 000)
- Procent: en decimal (12,3%)
- Datum: YYYY-MM-DD
- Tabeller for all jamforande data

### Struktur for rapporter
1. Sammanfattning (3-5 meningar)
2. Bakgrund / kontext
3. Analys med data och tabeller
4. Slutsatser
5. Nasta steg / rekommendation

### Undvik
- Spekulationer utan datagrund
- Buzzwords ("paradigmskifte", "game-changer")
- Blandning av svenska och engelska i lopande text
- Investeringsrekommendationer utan tydlig analys

## Vanliga uppgifter

### Kassaflodesanalys
1. Las data/finansiellt/
2. Berakna Revenue, EBITDA, Capex, delta rorelsekapital, FCF
3. Tabell med arlig jamforelse + tillvaxt
4. FCF-konvertering (FCF/EBITDA)
5. Trendkommentar (3-5 meningar)
6. Spara: analys/kassaflode/kassaflode-YYYY-MM-DD.md

### Konkurrentoversikt
1. Las data/marknad/
2. 5-10 konkurrenter: namn, land, intakter, tillvaxt, produkt, agare
3. Tabell sorterad efter intakter
4. Kort jamforande analys
5. Spara: analys/konkurrenter/

### Investment memo
1. Anvand mallar/investment-memo-mall.md
2. Fyll i alla sektioner baserat pa tillganglig data
3. Markera saknad data med [DATA SAKNAS]
4. Spara: output/memos/

## Filstruktur
- data/finansiellt/ — Arsredovisningar, kvartalsdata
- data/marknad/ — Branschrapporter, konkurrentinfo
- data/operativt/ — KPI:er, organisation
- analys/ — Bearbetade analyser (skapa har)
- output/ — Fardiga leveranser
- mallar/ — Rapportmallar

## Mallar
- mallar/investment-memo-mall.md
- mallar/kvartalsrapport-mall.md
Folj mallen exakt vad galler struktur. Anpassa innehallet.
```

---

## Exempelmappstruktur for PE-arbete

Har ar en komplett, beprövad struktur:

```
portfoljbolag-x/
├── CLAUDE.md                          # Overgripande instruktioner
│
├── data/
│   ├── README.md                      # Beskrivning av datakallor
│   ├── finansiellt/
│   │   ├── arsredovisning-2022.pdf
│   │   ├── arsredovisning-2023.pdf
│   │   ├── arsredovisning-2024.pdf
│   │   ├── kvartalsdata-2024.csv
│   │   └── budget-2025.xlsx
│   ├── marknad/
│   │   ├── branschrapport-hr-tech-2024.pdf
│   │   ├── konkurrentoversikt.md
│   │   └── marknadsstorlek-norden.csv
│   └── operativt/
│       ├── kpi-dashboard-2024.csv
│       ├── organisationsstruktur.md
│       └── churn-data-2022-2024.csv
│
├── analys/
│   ├── CLAUDE.md                      # Regler for analyser
│   ├── kassaflode/
│   ├── vardering/
│   └── scenarioanalys/
│
├── output/
│   ├── CLAUDE.md                      # Regler for output-format
│   ├── rapporter/
│   ├── presentationer/
│   └── memos/
│
├── mallar/
│   ├── investment-memo-mall.md
│   └── kvartalsrapport-mall.md
│
└── .claude/
    └── skills/
        ├── kassaflodesanalys.md
        ├── investment-memo.md
        └── due-diligence.md
```

Med den har strukturen kan du skriva:

```
/kassaflodesanalys
```

Och Claude vet automatiskt: var data finns, hur analysen ska goras, var resultatet ska sparas, och vilket format som galler. Noll upprepning.

---

## Praktisk ovning — Skapa din forsta AI-projektstruktur

### Steg 1: Skapa mappstrukturen

Oppna terminalen:

```bash
mkdir mitt-forsta-ai-projekt
cd mitt-forsta-ai-projekt
mkdir -p data analys output mallar .claude/skills
```

### Steg 2: Skriv din CLAUDE.md

Skapa filen `CLAUDE.md` i rotmappen. Borja enkelt:

```markdown
# CLAUDE.md

## Roll
Du ar min assistent for [beskriv projektet].

## Regler
- Skriv pa svenska
- Var koncis och faktadriven
- Anvand tabeller for jamforelser

## Filstruktur
- data/ — Kallmaterial och radata
- analys/ — Bearbetade analyser
- output/ — Fardiga leveranser
- mallar/ — Rapportmallar
```

### Steg 3: Lagg in dina filer

Kopiera relevant material till `data/`. Ge filerna beskrivande namn.

### Steg 4: Starta Claude Code

```bash
cd mitt-forsta-ai-projekt
claude
```

### Steg 5: Testa

```
> Visa mig alla filer i projektet och beskriv vad du ser
> Las filerna i data/ och skapa en sammanfattning. Spara som analys/initial-sammanfattning.md
```

### Steg 6: Bygg ut

Gor CLAUDE.md mer detaljerad. Skapa skills for uppgifter du gor ofta. Over tid vaxer projektet och Claude blir battre och battre pa att hjalpa dig.

---

## Fardiga startpunkter

I det har repots [`templates/`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates)-mapp hittar du fardiga mallar — CLAUDE.md-exempel, skill-filer och projektstrukturer for:

- **Private Equity** — investeringsanalys, kassaflode, due diligence
- **Konsulting** — marknadsanalys, strategisk rekommendation
- **Marknadsforing** — innehallsplanering, kampanjanalys

Anvand dem som utgangspunkt och anpassa till ditt arbete.

---

## Avslutning

Du har nu hela bilden:

- **Kapitel 00** gav dig ordforradet
- **Kapitel 01** forklarade varfor du ska sluta upprepa dig
- **Kapitel 02** visade hur Claude Code fungerar i praktiken
- **Kapitel 03** oppnade dorren till autonom AI med Cowork
- **Kapitel 04** band ihop allt med struktur, CLAUDE.md och kontext

Det viktigaste ar inte att du implementerar allt pa en gang. Borja med en CLAUDE.md och en mapp med data. Testa en riktig uppgift. Lagg till en skill nar du marke att du upprepar dig. Over tid vaxer systemet — och varje session blir battre an den foregaende.

AI-verktygen ar kraftfulla, men de ar just verktyg. Din expertis — formagan att stalla ratt fragor, bedoma svar kritiskt och fatta beslut — ar det som gor skillnaden. Claude gor dig snabbare. Men det ar du som styr.

---

*Det har ar det sista kapitlet. Ga tillbaka till [startsidan](index.md) for att utforska mallar och andra resurser.*
