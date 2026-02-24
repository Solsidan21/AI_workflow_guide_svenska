# Kapitel 04 — Mappstruktur och kontext

> *Det här är kapitlet som binder ihop allt. Struktur är inte administration — det är det som gör AI bra.*

---

## Varför mappstruktur spelar roll

När Claude Code startar läser den inte bara din prompt. Den ser **filnamn, mappnamn och hela projektstrukturen**. Allt detta är kontext som påverkar kvaliteten på svaren.

**Analogi:** Två skrivbord. Det ena är välorganiserat — mappar med etiketter, tydliga namn, logisk ordning. Om du ber någon hitta "Q3-kassaflödet för Bolag X" tar det sekunder.

Det andra är kaotiskt — papper överallt, oklara filnamn. Samma fråga tar minuter, och svaret kanske inte ens är korrekt.

AI fungerar på exakt samma sätt. **Bra struktur = bättre svar.**

### Filnamn och mappnamn ÄR instruktioner

När Claude ser:

```
data/finansiellt/arsredovisning-2024.pdf
```

...förstår den automatiskt vad filen är, vilket år, och var den passar in. Utan att du behöver förklara något.

Jämför med:

```
dokument/fil3.pdf
```

Här förstår Claude ingenting. Du måste förklara allt i din prompt — varje gång.

---

## Principer

### 1. Beskrivande namn

**Så här:**
```
kassaflodesanalys-2024-Q3.md
konkurrentoversikt-nordisk-hr-tech.md
styrelsepresentation-2024-12.pptx
```

**Inte så här:**
```
analys1.md
rapport-final-v2-SISTA.md
dok.pptx
```

**Tumregel:** Skulle en kollega förstå vad filen innehåller bara genom att se filnamnet? Om ja — bra namn.

### 2. Logisk hierarki

Organisera filer i en trädstruktur som speglar hur du tänker om arbetet.

```
projekt/bolag-x/
├── data/
│   ├── finansiellt/
│   └── marknad/
├── analys/
└── output/
```

Inte 50 filer i en platt lista. **Tumregel:** Om en mapp har fler än 10-15 filer, bryt ut undermappar.

### 3. Konsistens

Använd samma mönster överallt. Om du använder `kebab-case` (ord-med-bindestreck) för filnamn, gör det konsekvent. Om du använder YYYY-MM-DD för datum, gör det överallt.

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

Håll tre typer av material åtskilt:

| Mapp | Innehåll | Exempel |
|------|---------|---------|
| `data/` | Rådata som du **fått** | Årsredovisningar, CSV-exporter, rapporter |
| `analys/` | Material du **skapat** genom bearbetning | Kassaflödesberäkningar, modeller |
| `output/` | **Färdigt** material för leverans | Rapporter, presentationer, memos |

Varför? Du kan alltid gå tillbaka till rådata om något är fel. Och du blandar aldrig ihop arbetsunderlag med färdiga leveranser.

### 5. PDF-problemet — varför filformat spelar roll

Du har säkert PDF:er i din datamapp. Årsredovisningar, branschrapporter, avtal. Det är naturligt — PDF är branschstandard. Men för AI är PDF ett av de svåraste formaten att arbeta med.

**Tre saker gör PDF:er problematiska:**

1. **AI måste tolka hela dokumentet.** Den kan inte "bläddra" till rätt sida. Den processar allt från framsida till appendix, oavsett vad du frågar om.
2. **Det förbrukar enormt med tokens.** En 50-sidig årsredovisning kan äta upp tusentals tokens bara för att läsas in — även om du bara behöver tre rader.
3. **Formatering tolkas ofta fel.** Tabeller, kolumner och sidbrytningar i PDF:er översätts dåligt till text. Siffror som var tydliga i originalet kan bli röriga.

**Analogi:** Det är som att ge en konsult en hel bokhylla när du egentligen bara behöver ett kalkylblad. Konsulten klarar det — men det tar tid, kostar pengar och risken för missförstånd ökar.

Konsekvensen? Varje gång du ber AI "läs årsredovisningen och hitta EBITDA" använder den en stor del av sitt kontextfönster bara på att läsa in dokumentet. Det finns en bättre lösning.

### 6. Bearbeta en gång, skriv om till Markdown

Istället för att mata AI med samma PDF om och om igen, gör jobbet **en gång**. Du (eller Claude) läser PDF:en, extraherar det relevanta innehållet och skriver om det till välstrukturerade Markdown-filer.

**Före:**
```
data/finansiellt/arsredovisning-2024.pdf    ← 50 sidor, tusentals tokens varje gång
```

**Efter:**
```
data/finansiellt/arsredovisning-2024/
├── nyckeltal.md           # Revenue, EBITDA, nettoresultat i tabell
├── kassaflodesanalys.md   # FCF, capex, rörelsekapital
├── risker.md              # Väsentliga risker och osäkerhetsfaktorer
└── noter.md               # Relevanta noter (goodwill, avskrivningar)
```

**Skillnaden:**

| | PDF varje gång | Markdown (bearbetad en gång) |
|--|---|---|
| **Tokens** | Tusentals per inläsning | Några hundra per fil |
| **Precision** | AI läser allt, hittar kanske rätt | AI läser exakt rätt fil |
| **Hastighet** | Långsamt | Snabbt |
| **Återanvändning** | Samma kostnad varje session | Gratis efter första gången |

**Så här gör du i praktiken:**

1. Öppna en Claude Code-session i ditt projekt
2. Be Claude: *"Läs arsredovisning-2024.pdf och extrahera nyckeltal, kassaflödesdata, risker och relevanta noter. Spara som separata Markdown-filer i data/finansiellt/arsredovisning-2024/"*
3. Granska resultatet — kontrollera att siffrorna stämmer
4. Från och med nu använder alla analyser de bearbetade Markdown-filerna istället för PDF:en

**Tumregel:** Behåll alltid original-PDF:en — den är din källa och ditt kvitto. Men låt Claude arbeta mot Markdown-versionerna. Det är skillnaden mellan att kopiera samma bok varje gång och att ha bra anteckningar.

### 7. Från analys till färdigt dokument — PDF och Word som slutprodukt

Du har nu lärt dig att **Markdown är det bästa arbetsformatet** för AI — lätt att läsa, billigt i tokens, enkelt att strukturera. Men till slut behöver du ofta leverera ett dokument som kollegor, styrelser eller kunder faktiskt vill öppna: en PDF eller ett Word-dokument.

Lösningen är att låta Claude arbeta i Markdown genom hela processen — och konvertera till rätt format **i sista steget**.

**Arbetsflödet:**

```
data/ (råmaterial)  →  analys/ (Markdown)  →  output/ (PDF/Word)
                    Claude analyserar          Claude formaterar
                    enligt CLAUDE.md           enligt regler
```

Du kan styra det här direkt i din CLAUDE.md eller i en skill. Beskriv hur det färdiga dokumentet ska se ut — rubriker, sidbrytningar, typsnitt, marginaler — och be Claude generera filen som sista steg.

**Hur det fungerar i praktiken:**

Claude Code kan skapa PDF- och Word-filer genom verktyg som `pandoc` (gratis, installeras via terminalen) eller Python-bibliotek som `python-docx` och `reportlab`. Du behöver inte kunna dessa verktyg själv — Claude hanterar det åt dig. Det enda du behöver göra är att **beskriva formatet i dina regler**.

**Exempel — output-regler i CLAUDE.md:**

```markdown
## Output-format

### Rapporter
- Skapa alltid en Markdown-version först i analys/
- Konvertera sedan till PDF med pandoc
- Använd mallen i mallar/rapport-layout.yaml för sidmarginaler,
  typsnitt och sidhuvud/sidfot
- Filnamn: output/rapporter/[typ]-[datum].pdf

### Memos
- Skapa som Word-dokument (.docx) med python-docx
- Följ formatmallen i mallar/memo-format.md:
  - Typsnitt: Calibri 11pt
  - Rubriker: Calibri Bold 14pt
  - Marginaler: 2,5 cm
  - Sidhuvud: Bolagsnamn + datum
- Spara: output/memos/[namn]-[datum].docx
```

**Exempel — skill som avslutar med PDF:**

```markdown
# Skill: Kvartalsrapport

1. Läs data i data/finansiellt/ för aktuellt kvartal
2. Beräkna nyckeltal enligt CLAUDE.md
3. Skriv rapport i Markdown: analys/kvartalsrapport-YYYY-QX.md
4. Konvertera till PDF med layout från mallar/rapport-layout.yaml
5. Spara: output/rapporter/kvartalsrapport-YYYY-QX.pdf
```

**Poängen:** Markdown-filen i `analys/` är ditt arbetsdokument — lätt att redigera, billigt att läsa för AI. PDF:en eller Word-dokumentet i `output/` är din leverans — snyggt formaterad enligt de ramar du satt upp. Du får det bästa av båda världar: effektivt AI-arbete och professionella slutprodukter.

### 8. README-filer

En kort `README.md` i varje mapp hjälper både dig och Claude att förstå vad mappen innehåller.

**Exempel — `data/finansiellt/README.md`:**
```markdown
# Finansiell data

Årsredovisningar och kvartalsdata för Bolag X.

## Filer
- arsredovisning-YYYY.pdf — Officiella årsredovisningar
- kvartalsdata-YYYY.csv — Revenue, EBITDA, nettoresultat per kvartal

## Källor
- Årsredovisningar: Bolagsverket / bolaget direkt
- Kvartalsdata: CFO-rapportering
```

---

## CLAUDE.md på djupet

I kapitel 02 gick vi igenom grunderna. Här går vi djupare.

### Placering och hierarki

Claude Code läser **alla** CLAUDE.md-filer den stöter på i mappstrukturen. Det innebär att du kan ha en hierarki av instruktioner:

```
mitt-projekt/
├── CLAUDE.md                    # Övergripande regler
├── data/
│   └── CLAUDE.md                # Regler för datahantering
├── analys/
│   └── CLAUDE.md                # Regler för analyser
└── output/
    └── CLAUDE.md                # Regler för output-format
```

**Hur det fungerar:**

- **Rot-CLAUDE.md** gäller för allt arbete. Här placerar du: språk, ton, projektbeskrivning, generella riktlinjer.
- **Mapp-specifika CLAUDE.md** gäller *utöver* rot-reglerna när Claude arbetar i den mappen.

Claude läser alla CLAUDE.md-filer uppåt i hierarkin från den mapp den arbetar i. Så om Claude arbetar i `analys/kassaflode/` läser den:

1. `analys/kassaflode/CLAUDE.md` (om den finns)
2. `analys/CLAUDE.md` (om den finns)
3. `CLAUDE.md` (i roten)

Du behöver inte upprepa generella regler i varje CLAUDE.md — bara det som är specifikt för just den mappen.

### Vad en bra CLAUDE.md innehåller

**Komplett checklista:**

| Sektion | Syfte | Exempel |
|---------|-------|---------|
| **Roll** | Vem Claude "är" i projektet | "Erfaren PE-analytiker med fokus på nordiska SaaS-bolag" |
| **Projektkontext** | Vad projektet handlar om | Bolag, storlek, fas, syfte |
| **Regler** | Format, språk, stil | MSEK, svenska, tabeller för jämförelser |
| **Vanliga uppgifter** | Steg-för-steg för återkommande arbete | Kassaflödesanalys, konkurrentöversikt |
| **Filstruktur** | Var Claude hittar vad | data/finansiellt/, analys/, output/ |
| **Mallar** | Vilka mallar som ska användas | mallar/investment-memo-mall.md |

### Fullständigt exempel

```markdown
# CLAUDE.md — Portföljbolag X

## Roll
Du är en erfaren PE-analytiker med fokus på nordiska SaaS-bolag.
Noggrann med siffror, koncis i formuleringar, fokuserad på
investeringsbeslutet.

## Projektkontext
Bolag X är ett svenskt HR-tech SaaS-bolag, grundat 2015.
Cirka 200 anställda, ~150 MSEK i intäkter (2024).
Vi befinner oss i initial evaluering — fokus på att förstå
marknad, tillväxt och finansiell profil.

## Regler

### Format
- Språk: svenska
- Ton: formell men tillgänglig
- Siffror: MSEK, en decimal, mellanslag som tusentalsavgränsare (1 000)
- Procent: en decimal (12,3%)
- Datum: YYYY-MM-DD
- Tabeller för all jämförande data

### Struktur för rapporter
1. Sammanfattning (3-5 meningar)
2. Bakgrund / kontext
3. Analys med data och tabeller
4. Slutsatser
5. Nästa steg / rekommendation

### Undvik
- Spekulationer utan datagrund
- Buzzwords ("paradigmskifte", "game-changer")
- Blandning av svenska och engelska i löpande text
- Investeringsrekommendationer utan tydlig analys

## Vanliga uppgifter

### Kassaflödesanalys
1. Läs data/finansiellt/
2. Beräkna Revenue, EBITDA, Capex, delta rörelsekapital, FCF
3. Tabell med årlig jämförelse + tillväxt
4. FCF-konvertering (FCF/EBITDA)
5. Trendkommentar (3-5 meningar)
6. Spara: analys/kassaflode/kassaflode-YYYY-MM-DD.md

### Konkurrentöversikt
1. Läs data/marknad/
2. 5-10 konkurrenter: namn, land, intäkter, tillväxt, produkt, ägare
3. Tabell sorterad efter intäkter
4. Kort jämförande analys
5. Spara: analys/konkurrenter/

### Investment memo
1. Använd mallar/investment-memo-mall.md
2. Fyll i alla sektioner baserat på tillgänglig data
3. Markera saknad data med [DATA SAKNAS]
4. Spara: output/memos/

## Filstruktur
- data/finansiellt/ — Årsredovisningar, kvartalsdata
- data/marknad/ — Branschrapporter, konkurrentinfo
- data/operativt/ — KPI:er, organisation
- analys/ — Bearbetade analyser (skapa här)
- output/ — Färdiga leveranser
- mallar/ — Rapportmallar

## Mallar
- mallar/investment-memo-mall.md
- mallar/kvartalsrapport-mall.md
Följ mallen exakt vad gäller struktur. Anpassa innehållet.
```

---

## Exempelmappstruktur för PE-arbete

Här är en komplett, beprövad struktur:

```
portfoljbolag-x/
├── CLAUDE.md                          # Övergripande instruktioner
│
├── data/
│   ├── README.md                      # Beskrivning av datakällor
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
│   ├── CLAUDE.md                      # Regler för analyser
│   ├── kassaflode/
│   ├── vardering/
│   └── scenarioanalys/
│
├── output/
│   ├── CLAUDE.md                      # Regler för output-format
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

Med den här strukturen kan du skriva:

```
/kassaflodesanalys
```

Och Claude vet automatiskt: var data finns, hur analysen ska göras, var resultatet ska sparas, och vilket format som gäller. Noll upprepning.

---

## Praktisk övning — Skapa din första AI-projektstruktur

### Steg 1: Skapa mappstrukturen

Öppna terminalen:

```bash
mkdir mitt-forsta-ai-projekt
cd mitt-forsta-ai-projekt
mkdir -p data analys output mallar .claude/skills
```

### Steg 2: Skriv din CLAUDE.md

Skapa filen `CLAUDE.md` i rotmappen. Börja enkelt:

```markdown
# CLAUDE.md

## Roll
Du är min assistent för [beskriv projektet].

## Regler
- Skriv på svenska
- Var koncis och faktadriven
- Använd tabeller för jämförelser

## Filstruktur
- data/ — Källmaterial och rådata
- analys/ — Bearbetade analyser
- output/ — Färdiga leveranser
- mallar/ — Rapportmallar
```

### Steg 3: Lägg in dina filer

Kopiera relevant material till `data/`. Ge filerna beskrivande namn.

### Steg 4: Starta Claude Code

```bash
cd mitt-forsta-ai-projekt
claude
```

### Steg 5: Testa

```
> Visa mig alla filer i projektet och beskriv vad du ser
> Läs filerna i data/ och skapa en sammanfattning. Spara som analys/initial-sammanfattning.md
```

### Steg 6: Bygg ut

Gör CLAUDE.md mer detaljerad. Skapa skills för uppgifter du gör ofta. Över tid växer projektet och Claude blir bättre och bättre på att hjälpa dig.

---

## Färdiga startpunkter

I det här repots [`templates/`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates)-mapp hittar du färdiga mallar — CLAUDE.md-exempel, skill-filer och projektstrukturer för:

- **Private Equity** — investeringsanalys, kassaflöde, due diligence
- **Konsulting** — marknadsanalys, strategisk rekommendation
- **Marknadsföring** — innehållsplanering, kampanjanalys

Använd dem som utgångspunkt och anpassa till ditt arbete.

---

## Avslutning

Du har nu hela bilden:

- **Kapitel 00** gav dig ordförrådet
- **Kapitel 01** förklarade varför du ska sluta upprepa dig
- **Kapitel 02** visade hur Claude Code fungerar i praktiken
- **Kapitel 03** öppnade dörren till autonom AI med Cowork
- **Kapitel 04** band ihop allt med struktur, CLAUDE.md och kontext

Det viktigaste är inte att du implementerar allt på en gång. Börja med en CLAUDE.md och en mapp med data. Testa en riktig uppgift. Lägg till en skill när du märker att du upprepar dig. Över tid växer systemet — och varje session blir bättre än den föregående.

AI-verktygen är kraftfulla, men de är just verktyg. Din expertis — förmågan att ställa rätt frågor, bedöma svar kritiskt och fatta beslut — är det som gör skillnaden. AI:n gör dig snabbare. Men det är du som styr.

---

*Det här är det sista kapitlet. Gå tillbaka till [startsidan](index.md) för att utforska mallar och andra resurser.*
