# Mappstruktur och kontext — Grunden for effektivt AI-arbete

> *Det har kapitlet handlar om det som skiljer anvandare som far "okej"-resultat fran de som far "fantastiska" resultat. Hemligheten ar inte battre prompts — det ar battre struktur.*

---

## Varfor mappstruktur spelar roll

Nar du arbetar med Claude Code laser AI:n inte bara dina fragor — den laser ocksa **filnamn, mappnamn och filstruktur**. Allt detta ger kontext som paverkar kvaliteten pa svaren.

**Analogi:** Tankt pa skillnaden mellan tva skrivbord.

Det ena ar valorganiserat: pappersbuntar med etiketter, mappar med tydliga namn, en hylla med ordnade parmar. Om du ber nagon hjalpa dig hitta "Q3-kassaflodet for Bolag X" pa det skribordet tar det sekunder.

Det andra ar kaotiskt: papper overallt, oklara filnamn, ingen logisk ordning. Samma fraga tar minuter — och svaret kanske inte ens ar korrekt.

AI fungerar pa exakt samma satt. **Bra struktur = battre svar.**

### Filnamn och mappnamn AR instruktioner

Nar Claude Code ser foljande stiger:

```
data/finansiellt/arsredovisning-2024.pdf
```

...forstar den automatiskt att det ar en arsredovisning fran 2024, att den innehaller finansiell data, och att den ligger i projektets datasamling. Du behover inte forklara nagot — strukturen gor jobbet.

Jamfor med:

```
dokument/fil3.pdf
```

Har forstar Claude ingenting. Du maste forklara allt i din prompt.

---

## Principer for bra mappstruktur

### 1. Beskrivande namn

**Gor sa har:**
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

**Tumregel:** Skulle en kollega forsta vad filen innehaller bara genom att se filnamnet? Om ja — bra namn. Om nej — byt namn.

### 2. Logisk hierarki

Organisera filer i en tradstruktur som speglar hur du tanker om arbetet.

**Gor sa har:**
```
projekt/bolag-x/
├── data/
│   ├── finansiellt/
│   └── marknad/
├── analys/
└── output/
```

**Inte sa har:**
```
projekt/
├── bolag-x-arsredovisning.pdf
├── bolag-x-kassaflode.md
├── bolag-x-konkurrenter.md
├── bolag-y-arsredovisning.pdf
├── bolag-y-kassaflode.md
└── ... (50 filer i en platt lista)
```

**Tumregel:** Om en mapp har fler an 10-15 filer, overvagg att bryta ut undermappar.

### 3. Konsistens

Anvand samma monster genom hela projektet. Om du anvander `kebab-case` (ord-separerade-med-bindestreck) for filnamn, gor det overallt. Om du anvander datum i formatet YYYY-MM-DD, gor det overallt.

**Konsistent:**
```
kassaflode-2024-Q1.md
kassaflode-2024-Q2.md
kassaflode-2024-Q3.md
kassaflode-2024-Q4.md
```

**Inkonsistent:**
```
kassaflode Q1 2024.md
kassaflöde-2024-q2.md
KF_Q3_24.md
analys kassaflode kvartal 4.md
```

### 4. Separation av data, analys och output

Hall tre typer av material atskillt:

| Mapp | Innehall | Exempel |
|------|---------|---------|
| `data/` | Radata och kallmaterial som du **fatt** | Arsredovisningar, CSV-exporter, rapporter |
| `analys/` | Material du **skapat** genom bearbetning | Kassaflodesberakningar, jamforelser, modeller |
| `output/` | **Fardigt** material for leverans | Rapporter, presentationer, memos |

Varfor? For att du alltid kan ga tillbaka till radata om nagot ar fel i analysen. Och du blandar aldrig ihop arbetsunderlag med fardiga leveranser.

### 5. README-filer i varje mapp

En liten `README.md` i varje mapp hjalper bade dig och Claude att forsta vad mappen innehaller.

**Exempel — `data/finansiellt/README.md`:**
```markdown
# Finansiell data

Innehaller arsredovisningar och kvartalsdata for Bolag X.

## Filer
- arsredovisning-YYYY.pdf — Officiella arsredovisningar
- kvartalsdata-YYYY.csv — Exporterad fran ekonomisystem, innehaller
  revenue, EBITDA, nettoresultat per kvartal

## Kallor
- Arsredovisningar: Bolagsverket / bolaget direkt
- Kvartalsdata: CFO-rapportering via e-post
```

---

## CLAUDE.md — Djupdykning

I kapitel 04 introducerade vi CLAUDE.md. Har gar vi pa djupet.

### Placering och hierarki

Claude Code laser **alla** CLAUDE.md-filer den stoter pa i mappstrukturen. Det innebar att du kan ha en hierarki av instruktioner:

```
mitt-projekt/
├── CLAUDE.md                    # Overgripande regler for hela projektet
├── data/
│   └── CLAUDE.md                # Regler for hur data ska hanteras
├── analys/
│   └── CLAUDE.md                # Regler for hur analyser ska goras
└── output/
    └── CLAUDE.md                # Regler for hur output ska formateras
```

**Hur det fungerar:**

- **Rot-CLAUDE.md** galler for allt arbete i projektet. Har placerar du overgripande regler: sprak, tonalitet, projektbeskrivning, generella riktlinjer.

- **Mapp-specifika CLAUDE.md** galler utover rot-reglerna nar Claude arbetar i den mappen. Har placerar du specialiserade instruktioner.

Claude laser **alla** CLAUDE.md-filer uppat i hierarkin fran den mapp den arbetar i. Sa om Claude arbetar i `analys/kassaflode/` laser den:
1. `analys/kassaflode/CLAUDE.md` (om den finns)
2. `analys/CLAUDE.md` (om den finns)
3. `CLAUDE.md` (i roten)

Det innebar att du inte behover upprepa generella regler i varje CLAUDE.md — bara det som ar specifikt for den mappen.

### Vad en bra CLAUDE.md innehaller

Har ar en komplett checklista:

#### 1. Rollbeskrivning

Borja med att definiera vem Claude "ar" i det har projektet. Det satter tonen for allt som foljer.

```markdown
## Roll
Du ar en erfaren PE-analytiker med 10 ars erfarenhet av nordiska
techbolag. Du arbetar med investeringsanalys for en medelstor PE-fond
med fokus pa SaaS och techbolag i Norden.
```

#### 2. Projektkontext

Beskriv vad projektet handlar om. Ju mer kontext, desto battre resultat.

```markdown
## Projektkontext
Vi utvardelar Bolag X for potentiell investering. Bolaget ar ett
svenskt SaaS-bolag inom HR-tech grundat 2015. De har cirka 200 anstallda
och intakter runt 150 MSEK (2024). Vi befinner oss i en tidig fas av
evaluering — fokus ar pa att forsta marknad, tillvaxt och finansiell
profil innan vi gar vidare till due diligence.
```

#### 3. Regler och format

Var tydlig med hur du vill att saker ska se ut.

```markdown
## Regler

### Sprak och format
- Skriv alltid pa svenska
- Anvand formell men tillganglig ton
- Alla finansiella siffror i MSEK om inget annat anges
- Tusentalsavgransare med mellanslag: 1 000 (inte 1,000 eller 1000)
- Procent med en decimal: 12,3%
- Datum i formatet YYYY-MM-DD

### Struktur
- Anvand tydliga rubriker (##) for varje sektion
- Inkludera alltid en sammanfattning (3-5 meningar) i borjan av rapporter
- Anvand tabeller for jamforelser och oversikter
- Avsluta analyser med "Nasta steg" eller "Rekommendation"

### Vad som ska undvikas
- Spekulera inte — om data saknas, ange det tydligt
- Anvand inte buzzwords ("paradigmskifte", "game-changer")
- Ge inte investeringsrekommendationer utan tydlig analysgrund
- Blanda inte svenska och engelska i lopande text (engelska facktermer ok)
```

#### 4. Vanliga uppgifter med instruktioner

Beskriv hur specifika uppgifter ska utforas.

```markdown
## Vanliga uppgifter

### Kassaflodesanalys
1. Las data fran data/finansiellt/
2. Berakna: Revenue, EBITDA, Capex, forandring rorelsekapital, FCF
3. Presentera i tabell med arlig jamforelse
4. Berakna FCF-konvertering (FCF/EBITDA)
5. Kommentera trender i 3-5 meningar
6. Spara i analys/kassaflode/

### Konkurrentoversikt
1. Las data fran data/marknad/
2. Identifiera 5-10 relevanta konkurrenter
3. For varje: namn, land, intakter, tillvaxt, huvudprodukt, agare
4. Presentera som tabell sorterad efter intakter
5. Skriv kort jamforande analys
6. Spara i analys/konkurrenter/
```

#### 5. Filstruktur-guide

Beskriv var Claude hittar vad.

```markdown
## Filstruktur

### Var hittar du vad
- data/finansiellt/ — Arsredovisningar och kvartalsdata
- data/marknad/ — Branschrapporter och konkurrentdata
- data/operativt/ — KPI:er, organisationsdata
- analys/ — Bearbetade analyser (skapa nya har)
- output/ — Fardiga leveranser (rapporter, presentationer)
- mallar/ — Mallar som ska anvandas for formatering

### Viktiga filer
- mallar/investment-memo-mall.md — Anvand for investment memos
- mallar/kvartalsrapport-mall.md — Anvand for kvartalsrapporter
- data/finansiellt/kvartalsdata-2024.csv — Senaste finansiella data
```

#### 6. Referenser till mallar

Peka Claude mot specifika mallar och exempel.

```markdown
## Mallar och referenser
Nar du skapar rapporter, anvand alltid mallen fran mallar/-mappen.
- Investment memo: se mallar/investment-memo-mall.md
- Kvartalsrapport: se mallar/kvartalsrapport-mall.md
- Styrelsepresentation: se mallar/styrelsepresentation-struktur.md

Foljt mallen exakt vad galler struktur. Du kan anpassa innehallet men inte rubrikerna.
```

### Fullstandigt CLAUDE.md-exempel

Har ar ett komplett exempel for ett PE-projekt. Anvand det som utgangspunkt och anpassa.

```markdown
# CLAUDE.md — Portfoljbolag X

## Roll
Du ar en erfaren PE-analytiker med fokus pa nordiska SaaS-bolag.
Du ar noggrann med siffror, koncis i dina formuleringar och
fokuserad pa det som ar relevant for investeringsbeslutet.

## Projektkontext
Bolag X ar ett svenskt HR-tech SaaS-bolag som vi utvardelar for
investering. Grundat 2015, cirka 200 anstallda, ~150 MSEK i
intakter (2024). Vi befinner oss i initial evaluering.

## Regler

### Format
- Sprak: svenska
- Ton: formell men tillganglig
- Siffror: MSEK, en decimal, mellanslag som tusentalsavgransare
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
- Buzzwords och overdriven positivitet
- Investeringsrekommendationer utan tydlig analys
- Blandning av svenska och engelska i lopande text

## Vanliga uppgifter

### Kassaflodesanalys
1. Las data/finansiellt/
2. Berakna Revenue, EBITDA, Capex, delta rorelsekapital, FCF
3. Tabell med arlig jamforelse + tillvaxt
4. Berakna FCF-konvertering
5. 3-5 meningar om trender
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
3. Markera sektioner dar data saknas med [DATA SAKNAS]
4. Spara: output/memos/

## Filstruktur
- data/finansiellt/ — Arsredovisningar, kvartalsdata
- data/marknad/ — Branschrapporter, konkurrentinfo
- data/operativt/ — KPI:er, organisation
- analys/ — Bearbetade analyser (skapa har)
- output/ — Fardiga leveranser
- mallar/ — Mallar for formatering

## Mallar
- mallar/investment-memo-mall.md
- mallar/kvartalsrapport-mall.md
```

---

## Exempelmappstruktur — PE-bolag

Har ar en komplett, beprövad mappstruktur for PE-arbete med Claude Code:

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
│       ├── kundlista-top20.csv
│       └── churn-data-2022-2024.csv
│
├── analys/
│   ├── CLAUDE.md                      # Regler for hur analyser ska goras
│   ├── kassaflode/
│   │   ├── kassaflode-2025-01-15.md
│   │   └── kassaflode-2025-02-20.md
│   ├── vardering/
│   │   ├── dcf-modell.md
│   │   └── multipelvaardering.md
│   └── scenarioanalys/
│       ├── bas-scenario.md
│       ├── optimistiskt-scenario.md
│       └── pessimistiskt-scenario.md
│
├── output/
│   ├── CLAUDE.md                      # Regler for output-format
│   ├── rapporter/
│   │   └── initial-evaluering-2025-01.md
│   ├── presentationer/
│   │   └── ic-presentation-2025-02.md
│   └── memos/
│       └── investment-memo-v1.md
│
├── mallar/
│   ├── investment-memo-mall.md
│   ├── kvartalsrapport-mall.md
│   └── styrelsepresentation-struktur.md
│
└── .claude/
    └── skills/
        ├── kassaflodesanalys.md
        ├── konkurrentrapport.md
        ├── investment-memo.md
        └── manadsbrev.md
```

### Anvandning i praktiken

Med den har strukturen pa plats kan du ge Claude Code instruktioner som:

```
"Gor en kassaflodesanalys baserat pa senaste kvartalsdata"
```

Claude vet automatiskt:
- Var data finns (tack vare CLAUDE.md och filstrukturen)
- Hur analysen ska goras (tack vare CLAUDE.md och skill-filen)
- Var resultatet ska sparas (tack vare instruktionerna)
- Vilket format som galler (tack vare mallarna)

---

## Praktisk ovning — Skapa din forsta AI-projektstruktur

Har ar en steg-for-steg-guide for att komma igang. Du behover inte ha alla filer pa plats — borja med strukturen och fyll pa efterhand.

### Steg 1: Skapa grundstrukturen

Oppna terminalen och navigera till var du vill ha projektet:

```bash
mkdir mitt-forsta-ai-projekt
cd mitt-forsta-ai-projekt
mkdir -p data analys output mallar .claude/skills
```

### Steg 2: Skapa din CLAUDE.md

Skapa filen `CLAUDE.md` i rotmappen. Du kan gora det i valfri texteditor. Borja enkelt:

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
- mallar/ — Mallar for formatering
```

### Steg 3: Lagg in dina filer

Kopiera relevant material till `data/`-mappen. Dopp om filer sa de har beskrivande namn.

### Steg 4: Starta Claude Code

```bash
cd mitt-forsta-ai-projekt
claude
```

### Steg 5: Testa

Borja med nagot enkelt:

```
"Visa mig alla filer i det har projektet och beskriv vad du ser."
```

Sedan nagot mer substansiellt:

```
"Las filerna i data/ och skapa en sammanfattning. Spara som analys/initial-sammanfattning.md"
```

### Steg 6: Bygg ut efterhand

Lagg till fler filer i `data/`. Gor CLAUDE.md mer detaljerad. Skapa skills for uppgifter du gor ofta. Over tid vaxer projektet organiskt och Claude blir allt battre pa att hjalpa dig.

---

## Avslutning — Du har nu verktygen

Gratulerar. Du har tagit dig igenom hela guiden — fran grundlaggande begrepp och chattanvandning till Claude Code, Cowork, och avancerad mappstruktur.

### Vad du har lart dig

- **Claudes ekosystem** — Chat, Code och Cowork, och nar du ska anvanda vad
- **Promptteknik** — hur du formulerar instruktioner som ger bra resultat
- **Claude Code** — praktisk anvandning av AI direkt pa din dator
- **Claude Cowork** — autonom AI for langre uppgifter
- **Mappstruktur och CLAUDE.md** — grunden som gor allt annat battre

### Vad du bor gora nu

1. **Skapa ett testprojekt.** Anvand steg-for-steg-guiden ovan. Det behover inte vara perfekt — det viktigaste ar att borja.

2. **Skriv en CLAUDE.md.** Even en kort version gor skillnad. Du kan alltid forbattra den over tid.

3. **Prova en riktig uppgift.** Ta nagot fran ditt faktiska arbete — en rapport, en analys, en sammanstallning — och lat Claude hjalpa dig.

4. **Utforska templates/-mappen.** I det har repots [`templates/`](../templates/)-mapp hittar du fardiga mallar, CLAUDE.md-exempel och skill-filer for PE, consulting och marknadsarbete. Anvand dem som utgangspunkt.

5. **Experimentera.** Det basta sattet att lara sig ar att prova. Claude ar talmodig, aldrig otrevlig, och tillganglig dygnet runt.

### En sista tanke

AI-verktygen vi gatt igenom ar kraftfulla, men de ar just verktyg. Din expertis — din formaoga att stalla ratt fragor, bedoma svar kritiskt, och fatta beslut baserat pa ofullstandig information — ar det som gor skillnaden. Claude gor dig snabbare och mer effektiv. Men det ar du som styr.

Lycka till.

---

*Det har ar det sista kapitlet i guiden. Ga tillbaka till [Innehallsforteckningen](../README.md) for att utforska mallar och andra resurser.*
