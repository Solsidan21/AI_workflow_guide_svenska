# Kapitel 03 — Mappstruktur och arbetssätt

> *Det här är kapitlet som binder ihop allt. Struktur är inte administration — det är det som gör AI bra.*

Det här är guidens viktigaste kapitel. Inte för att det är det mest tekniska, utan för att det beskriver **arbetssättet** som gör allt annat möjligt. Mappstruktur, CLAUDE.md, skills, och framför allt: det grundläggande arbetsflödet som förvandlar dina dokument till ett AI-system.

---

## Varför mappstruktur spelar roll

När Claude Code startar läser den inte bara din prompt. Den ser **filnamn, mappnamn och hela projektstrukturen**. Allt detta är kontext som påverkar kvaliteten på svaren.

**Analogi:** Två skrivbord. Det ena är välorganiserat — mappar med etiketter, tydliga namn, logisk ordning. Om du ber någon hitta "Q3-rapporten" tar det sekunder.

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

## Principer för bra struktur

### 1. Beskrivande namn

**Så här:**
```
kassaflodesanalys-2024-Q3.md
konkurrentoversikt-nordisk-marknad.md
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

Organisera filer i en trädstruktur som speglar hur du tänker om arbetet:

```
mitt-projekt/
├── data/
│   ├── finansiellt/
│   └── marknad/
├── analys/
└── output/
```

Inte 50 filer i en platt lista. **Tumregel:** Om en mapp har fler än 10–15 filer, bryt ut undermappar.

### 3. Konsistens

Använd samma mönster överallt. Om du använder `kebab-case` (ord-med-bindestreck) för filnamn, gör det konsekvent. Om du använder YYYY-MM-DD för datum, gör det överallt.

**Konsistent:**
```
kvartalsrapport-2024-Q1.md
kvartalsrapport-2024-Q2.md
kvartalsrapport-2024-Q3.md
```

**Inkonsistent:**
```
kvartalsrapport Q1 2024.md
kvartalsrapp-2024-q2.md
KR_Q3_24.md
```

### 4. Separation av data, analys och output

Håll tre typer av material åtskilt:

| Mapp | Innehåll | Exempel |
|------|---------|---------|
| `data/` | Rådata som du **fått** | Rapporter, CSV-exporter, dokument |
| `analys/` | Material du **skapat** genom bearbetning | Sammanfattningar, beräkningar, modeller |
| `output/` | **Färdigt** material för leverans | Rapporter, presentationer, memos |

Varför? Du kan alltid gå tillbaka till rådata om något är fel. Och du blandar aldrig ihop arbetsunderlag med färdiga leveranser.

### 5. README-filer

En kort `README.md` i varje mapp hjälper både dig och Claude att förstå vad mappen innehåller:

**Exempel — `data/finansiellt/README.md`:**
```markdown
# Finansiell data

Årsredovisningar och kvartalsdata.

## Filer
- arsredovisning-YYYY.pdf — Officiella årsredovisningar
- kvartalsdata-YYYY.csv — Revenue, EBITDA, nettoresultat per kvartal

## Källor
- Årsredovisningar: Bolagsverket / bolaget direkt
- Kvartalsdata: Intern rapportering
```

---

## Det centrala arbetsflödet — PDF till system

Det här avsnittet beskriver det grundläggande arbetssätt som gör allt annat möjligt. Det är enkelt, men det förändrar allt.

### Problemet

Du har dokument — PDF:er, rapporter, kursböcker, branschdata. Du vill att AI ska kunna arbeta med dem intelligent, konsekvent och utan att du behöver kopiera text varje gång.

### Lösningen: fyra steg

```
   PDF:er och dokument
          │
          ▼
   ┌─────────────────┐
   │  1. SAMLA       │  Lägg dokument i data/
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │  2. EXTRAHERA   │  Claude Code → Markdown
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │  3. PUBLICERA   │  Push till GitHub
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │  4. KOPPLA      │  Repo som Claude-projekt
   └─────────────────┘
```

### Steg 1: Samla dina dokument

Skapa en projektmapp med logisk struktur och lägg in dina dokument:

```
mitt-projekt/
├── data/
│   ├── rapporter/
│   │   ├── arsredovisning-2024.pdf
│   │   └── branschrapport-2024.pdf
│   └── underlag/
│       ├── kunddata-2024.csv
│       └── projektbeskrivning.docx
├── analys/
├── output/
└── CLAUDE.md
```

### Steg 2: Extrahera till Markdown

Det här är nyckelsteget. Istället för att mata AI med samma tunga PDF varje gång, bearbetar du dokumentet **en gång** och sparar det som lättläst Markdown.

I Claude Code:

```
> Läs arsredovisning-2024.pdf och extrahera:
> - Nyckeltal (revenue, EBITDA, nettoresultat) som tabell
> - Kassaflödesdata
> - Väsentliga risker
> Spara som separata Markdown-filer i data/rapporter/arsredovisning-2024/
```

**Före:**
```
data/rapporter/arsredovisning-2024.pdf    ← 50 sidor, tusentals tokens varje gång
```

**Efter:**
```
data/rapporter/arsredovisning-2024/
├── nyckeltal.md           # Revenue, EBITDA, nettoresultat i tabell
├── kassaflodesdata.md     # FCF, capex, rörelsekapital
└── risker.md              # Väsentliga risker och osäkerhetsfaktorer
```

**Skillnaden:**

| | PDF varje gång | Markdown (bearbetad en gång) |
|--|---|---|
| **Tokens** | Tusentals per inläsning | Några hundra per fil |
| **Precision** | AI läser allt, hittar kanske rätt | AI läser exakt rätt fil |
| **Hastighet** | Långsamt | Snabbt |
| **Återanvändning** | Samma kostnad varje session | Gratis efter första gången |

**Viktigt:** Behåll alltid original-PDF:en — den är din källa och ditt kvitto. Men låt Claude arbeta mot Markdown-versionerna.

### Steg 3: Publicera till GitHub

Initiera ett Git-repo och pusha till GitHub:

```
git init
git add -A
git commit -m "Initial projektstruktur med extraherade data"
git push
```

Nu finns ditt projekt versionshanterat och tillgängligt. Varje ändring loggas. Du kan alltid gå tillbaka.

### Steg 4: Koppla repot som Claude-projekt

Här händer magin. I Claude Chat:

1. Skapa ett nytt projekt
2. Koppla ditt GitHub-repo som kunskapskälla
3. Skriv projektinstruktioner (baserade på din CLAUDE.md)

Nu har du **samma kunskap tillgänglig i både Claude Code och Claude Chat**. Du arbetar i Code när du behöver automation och filhantering. Du arbetar i Chat när du behöver snabba frågor och bollplank. Båda delar samma kunskapsbas.

### Varför det här förändrar allt

- **Dokument bearbetas en gång** — inte varje session
- **Markdown är billigt** — mer plats i kontextfönstret för din fråga
- **GitHub ger versionshantering** — du kan alltid gå tillbaka
- **Samma kunskap överallt** — Code och Chat delar samma data
- **Teamet kan samarbeta** — alla har tillgång till samma repo

Det här är inte ett avancerat arbetsflöde. Det är **grundflödet** som gör allt annat möjligt.

---

## Från analys till färdigt dokument

Du har nu lärt dig att Markdown är det bästa arbetsformatet för AI. Men till slut behöver du ofta leverera ett dokument som kollegor eller kunder vill öppna: en PDF eller ett Word-dokument.

Lösningen: låt Claude arbeta i Markdown genom hela processen och konvertera till rätt format **i sista steget**.

```
data/ (råmaterial)  →  analys/ (Markdown)  →  output/ (PDF/Word)
                    Claude analyserar          Claude formaterar
```

Claude Code kan skapa PDF- och Word-filer genom verktyg som `pandoc` eller Python-bibliotek. Du behöver inte kunna dessa verktyg själv — Claude hanterar det. Det enda du behöver göra är att beskriva formatet.

---

## CLAUDE.md — ditt projekts regelverk

### Vad är det?

En Markdown-fil som du placerar i roten av din projektmapp. När Claude Code startar läser den CLAUDE.md automatiskt och följer instruktionerna. Varje session, utan att du behöver säga något.

**Det är skillnaden mellan en assistent som börjar från noll varje dag och en som känner projektet.**

### Var placeras den?

Direkt i projektmappens rot:

```
mitt-projekt/
├── CLAUDE.md          <-- Här
├── data/
├── analys/
└── output/
```

### Vad en bra CLAUDE.md innehåller

| Sektion | Syfte | Exempel |
|---------|-------|---------|
| **Roll** | Vem Claude "är" i projektet | "Erfaren analytiker med fokus på nordiska marknaden" |
| **Projektkontext** | Vad projektet handlar om | Kort beskrivning, fas, syfte |
| **Regler** | Format, språk, stil | MSEK, svenska, tabeller för jämförelser |
| **Vanliga uppgifter** | Steg-för-steg för återkommande arbete | Sammanfattning, analys, rapportgenerering |
| **Filstruktur** | Var Claude hittar vad | data/, analys/, output/ |
| **Mallar** | Vilka mallar som ska användas | mallar/rapport-mall.md |

### Komplett generellt exempel

```markdown
# CLAUDE.md — Mitt projekt

## Roll
Du är en erfaren analytiker. Noggrann med siffror,
koncis i formuleringar, fokuserad på det väsentliga.

## Projektkontext
[Kort beskrivning av projektet — vad det handlar om,
vilken fas det befinner sig i, vad målet är.]

## Regler

### Format
- Språk: svenska
- Ton: formell men tillgänglig
- Siffror: MSEK, en decimal, mellanslag som tusentalsavgränsare (1 000)
- Datum: YYYY-MM-DD
- Tabeller för all jämförande data

### Struktur för rapporter
1. Sammanfattning (3–5 meningar)
2. Bakgrund / kontext
3. Analys med data och tabeller
4. Slutsatser
5. Nästa steg / rekommendation

### Undvik
- Spekulationer utan datagrund
- Buzzwords
- Blandning av svenska och engelska i löpande text

## Vanliga uppgifter

### Sammanfattning av rapport
1. Läs dokumentet i data/
2. Extrahera nyckeltal och huvudpunkter
3. Presentera som tabell + 5 punkter
4. Spara i analys/

## Filstruktur
- data/ — Källmaterial och rådata
- analys/ — Bearbetade analyser
- output/ — Färdiga leveranser
- mallar/ — Rapportmallar
```

### Placering och hierarki

Claude Code läser **alla** CLAUDE.md-filer den stöter på i mappstrukturen. Det innebär att du kan ha en hierarki:

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

Claude läser alla CLAUDE.md-filer uppåt i hierarkin. Om Claude arbetar i `analys/kvartalsrapport/` läser den:

1. `analys/kvartalsrapport/CLAUDE.md` (om den finns)
2. `analys/CLAUDE.md` (om den finns)
3. `CLAUDE.md` (i roten)

Du behöver inte upprepa generella regler i varje CLAUDE.md — bara det som är specifikt för just den mappen.

### Tumregler för placering

| Fråga att ställa | Svaret styr placeringen |
|-------------------|------------------------|
| "Gäller det oavsett var jag arbetar i projektet?" | → Rot-CLAUDE.md |
| "Gäller det bara för analyser / bara för output?" | → Mapp-specifik CLAUDE.md |
| "Gäller det bara för en specifik uppgift?" | → En skill-fil istället |

---

## Skills — återanvändbara arbetsflöden

### Vad är en skill?

En skill är en Markdown-fil med steg-för-steg-instruktioner för en återkommande uppgift. Istället för att skriva om instruktionerna varje gång, aktiverar du skillen med ett kommando.

### Var placeras de?

I mappen `.claude/skills/` i ditt projekt:

```
mitt-projekt/
├── CLAUDE.md
├── .claude/
│   └── skills/
│       ├── sammanfattning.md
│       ├── kvartalsrapport.md
│       └── konkurrentanalys.md
└── ...
```

### Hur skapar du en skill?

Skapa en Markdown-fil med instruktioner:

**`.claude/skills/sammanfattning.md`**
```markdown
# Sammanfatta rapport

När den här skillen aktiveras:

1. Fråga vilken fil som ska sammanfattas (om inte angiven)
2. Läs filen
3. Extrahera:
   - Nyckeltal i tabellform
   - Huvudsakliga slutsatser (max 5 punkter)
   - Risker eller svagheter (om tillämpligt)
4. Presentera med sammanfattning först, sedan tabell, sedan punktlista
5. Spara som analys/sammanfattning-[filnamn]-YYYY-MM-DD.md
```

### Hur använder du den?

I en Claude Code-session:

```
/sammanfattning
```

Claude läser instruktionsfilen och utför alla stegen. Samma resultat varje gång, utan att du behöver skriva om instruktionerna.

### Skill-idéer för olika roller

- `/sammanfattning` — Sammanfatta valfritt dokument enligt fast format
- `/kvartalsrapport` — Skapa rapport baserat på data i projektet
- `/konkurrentanalys` — Kartlägg och jämför aktörer
- `/motesforberedelse` — Sammanställ underlag inför möte
- `/presentationsunderlag` — Struktur för presentation
- `/dataextraktion` — Extrahera nyckeltal från PDF till Markdown

---

## Exempelmappstruktur

Här är en komplett startpunkt som fungerar för de flesta projekt:

```
mitt-projekt/
├── CLAUDE.md                          # Övergripande instruktioner
│
├── data/
│   ├── README.md                      # Beskrivning av datakällor
│   ├── rapporter/                     # PDF:er och originaldokument
│   ├── extraherat/                    # Bearbetade Markdown-versioner
│   └── underlag/                      # Övriga dokument, CSV:er
│
├── analys/                            # Bearbetade analyser
│   └── CLAUDE.md                      # Regler för analyser
│
├── output/                            # Färdiga leveranser
│   ├── CLAUDE.md                      # Regler för output-format
│   ├── rapporter/
│   └── presentationer/
│
├── mallar/                            # Dokumentmallar
│
└── .claude/
    └── skills/                        # Återanvändbara arbetsflöden
```

Med den här strukturen kan du skriva:

```
> Sammanfatta alla rapporter i data/rapporter/ och spara i analys/
```

Och Claude vet automatiskt: var data finns, hur analysen ska göras, var resultatet ska sparas, och vilket format som gäller.

---

## Praktisk övning — skapa din första projektstruktur

### Steg 1: Skapa mappstrukturen

```bash
mkdir mitt-projekt
cd mitt-projekt
mkdir -p data/rapporter data/extraherat analys output mallar .claude/skills
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

### Steg 4: Starta Claude Code och extrahera

```bash
cd mitt-projekt
claude
```

```
> Läs alla PDF:er i data/rapporter/ och extrahera nyckeltal och
> sammanfattningar till Markdown-filer i data/extraherat/
```

### Steg 5: Initiera Git och pusha

```bash
git init
git add -A
git commit -m "Initial projektstruktur"
git push
```

### Steg 6: Koppla som Claude-projekt

Skapa ett projekt i Claude Chat, koppla repot, och skriv projektinstruktioner baserade på din CLAUDE.md.

### Steg 7: Bygg ut

Gör CLAUDE.md mer detaljerad. Skapa skills för uppgifter du gör ofta. Över tid växer projektet och Claude blir bättre och bättre på att hjälpa dig.

---

## Färdiga startpunkter

I det här repots [`templates/`](../templates/)-mapp hittar du färdiga mallar — CLAUDE.md-exempel, skill-filer och projektstrukturer för olika roller och branscher.

Använd dem som utgångspunkt och anpassa till ditt arbete.

---

## Sammanfattning

Det här kapitlet har täckt tre saker:

1. **Mappstruktur** — Beskrivande namn, logisk hierarki, separation av data/analys/output. Struktur *är* kontext.

2. **Det centrala arbetsflödet** — Samla dokument → Extrahera till Markdown → Pusha till GitHub → Koppla som Claude-projekt. Det här är grundflödet som gör allt annat möjligt.

3. **CLAUDE.md och skills** — Regler som alltid gäller och arbetsflöden som kan återanvändas. Systemet som gör att AI blir bättre på just ditt jobb.

Det viktigaste är inte att strukturen är perfekt från dag ett. Det viktigaste är att du **börjar** — och låter systemet växa med dig.

---

> *Föregående kapitel: [02 — Promptteknik och kontext](02-promptteknik-och-kontext.md)*
>
> *Nästa kapitel: [04 — Exempel: Studier](04-exempel-studier.md)*
