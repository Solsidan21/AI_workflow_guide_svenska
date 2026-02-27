# Exempel: Studier — Hela kursen som AI-system

> *Du förstår inte matte genom att läsa facit. Men du lär dig snabbare med en studiekamrat som läst hela kursboken.*

---

De tidigare kapitlen har gått igenom koncepten: kontext, mappstruktur, CLAUDE.md och skills. Det här kapitlet visar hur jag, Arvid, som skrivit den här guiden, använder samma principer för mina egna studier. Inte för att memorera lösningar, utan för att klara tentan genom att faktiskt kunna materialet.

Jag läser ekonomie kandidatprogrammet och är inte programmerare. Men jag har byggt hela det system som beskrivs här, och det har förändrat hur jag pluggar. Arbetsflödet fungerar för vilken kurs som helst. Du ska kunna ta det och anpassa till dina egna.

---

## Min situation

| | |
|---|---|
| **Program** | Ekonomie kandidatprogrammet |
| **Termin** | Valfri termin, VT 2026 |
| **Kurser** | Algebra & vektorgeometri, Envariabelsanalys |
| **Verktyg** | Claude Chat med projekt + Claude Code |
| **Mål** | Klara tentan genom att faktiskt kunna materialet |
| **Teknisk nivå** | Inte programmerare |

Jag läser två mattekurser parallellt. Jag har föreläsningsanteckningar, kursplaner, formelsamlingar och gamla tentor som PDF:er. Jag vill kunna ställa frågor mot kursmaterialet, få förklaringar med kursens metoder och öva inför tenta, utan att börja om från noll varje gång.

---

## Problemet: Screenshot-cirkusen

Jag sitter med en uppgift i algebra. Tar en screenshot, skickar till Claude. Claude löser uppgiften, snabbt och korrekt. Men med Gauss-eliminering. Min kurs har inte gått igenom Gauss-eliminering ännu. Vi använder ekvivalenta ekvationer och substitution.

Jag tar en ny screenshot, den här gången på facit, och skriver: "Lös som de gör här istället." Claude anpassar sig halvvägs, men blandar fortfarande in notation som inte matchar kursen.

Tredje försöket: jag tvingar Claude att läsa igenom en hel föreläsnings-PDF. Claude processar 40 sidor, hittar till slut rätt avsnitt, och svarar: "Ah, ni använder den metoden. Då kan jag förklara det så här."

Femton minuter. Varje gång.

Nästa dag, ny uppgift. Samma kurs. Samma problem: Claude har glömt allt.

Det här är exakt det problem som [kapitel 04](04-strukturerad-kontext.md) beskriver: ostrukturerad kontext kostar tid och ger sämre svar. Jag ger Claude rätt information, men i fel format, utan regler, och utan minne mellan sessioner.

---

## Lösningen steg för steg

Min lösning följer arbetsflödet från [kapitel 03](03-mappstruktur-och-arbetssatt.md): samla, extrahera, publicera, koppla. Anpassat för studier.

### Steg 1 — Samla kursmaterial

Jag samlade allt jag redan hade:

- Föreläsningsanteckningar (PDF:er eller handskrivna → fotograferade)
- Kursplan med lärandemål och examination
- Formelsamling
- Övningsuppgifter med facit
- Gamla tentor med lösningsförslag

Det mesta fanns redan som PDF på kurshemsidan. Jag laddade ner allt och la det i en mapp.

### Steg 2 — Claude Code extraherar till Markdown

Jag öppnade Claude Code i kursmappen och skrev:

```
Jag har lagt kursens föreläsningsanteckningar som PDF:er i pdf-original/.
Varje PDF är en föreläsning.

Läs igenom dem och extrahera innehållet till Markdown-filer i forelasningar/.
Behåll all matematik, alla definitioner och alla exempel.
Namnge filerna 01-[ämne].md, 02-[ämne].md osv baserat på
föreläsningens huvudtema.
```

Claude Code läser varje PDF och skapar strukturerade Markdown-filer. En 40-sidig PDF med tabeller, formler och figurbeskrivningar blir en ren textfil med rubriker, definitioner markerade som definitioner, och exempel tydligt avgränsade.

Samma sak för kursplanen, formelsamlingen och tentorna.

### Steg 3 — Mappstruktur

Resultatet ser ut så här:

```
mattekurser/
├── CLAUDE.md
├── algebra-vektorgeometri/
│   ├── CLAUDE.md
│   ├── kursplan.md
│   ├── formelsamling.md
│   ├── forelasningar/
│   │   ├── 01-vektorer-i-planet.md
│   │   ├── 02-linjara-ekvationssystem.md
│   │   ├── 03-matriser-och-determinanter.md
│   │   └── ...
│   ├── ovningsuppgifter/
│   │   ├── ovning-01-vektorer.md
│   │   └── ...
│   └── tentor/
│       ├── tenta-2024-01.md
│       ├── tenta-2024-08.md
│       └── ...
├── envariabelsanalys/
│   ├── CLAUDE.md
│   ├── kursplan.md
│   ├── formelsamling.md
│   ├── forelasningar/
│   │   ├── 01-gransvardesbegrepp.md
│   │   ├── 02-derivata.md
│   │   └── ...
│   ├── ovningsuppgifter/
│   └── tentor/
└── pdf-original/
    ├── algebra/
    └── envariabel/
```

Notera: `pdf-original/` behålls som arkiv. Jag arbetar aldrig direkt mot PDF:erna efter extraktion.

### Steg 4 — Publicera och koppla

Jag bad Claude Code initiera ett Git-repo och pusha till GitHub. Sedan skapade jag ett projekt i Claude Chat kopplat till repot. Nu har jag samma kursmaterial tillgängligt i både Claude Code och Claude Chat, på bussen, i biblioteket, vid skrivbordet.

---

## CLAUDE.md — kursens regelverk

### Rot-nivå: mattekurser/CLAUDE.md

Min övergripande CLAUDE.md sätter regler som gäller för alla kurser:

```markdown
## Roll
Du är en tålmodig och pedagogisk studiekamrat som hjälper mig förstå
universitetsmatte. Du är duktig på att förklara steg för steg.

## Regler

### Pedagogiskt förhållningssätt
- Lös ALDRIG uppgifter direkt. Vägled mig genom lösningen steg för steg.
- Fråga mig vad jag tror nästa steg är innan du visar det.
- Om jag kör fast — ge en ledtråd, inte svaret.
- Om jag ber om en fullständig lösning uttryckligen, visa den med
  förklaring av varje steg.

### Metoder och notation
- Använd BARA metoder och notation som gåtts igenom i kursens
  föreläsningar. Läs föreläsningsfilerna för att veta vad som är
  tillåtet.
- Om en uppgift kan lösas med en metod som inte gåtts igenom — lös
  den ändå med kursens metoder. Nämn gärna att det finns andra sätt,
  men visa kursens sätt.

### Format
- Skriv matematik med tydlig notation
- Numrera varje steg i en lösning
- Markera definitioner och satser tydligt
- Använd svenska termer med engelska i parentes vid första
  förekomsten, t.ex. "egenvektor (eigenvector)"
```

### Kursnivå: algebra-vektorgeometri/CLAUDE.md

Den kursspecifika CLAUDE.md lägger till det som är unikt för just den kursen:

```markdown
## Kursöversikt
| | |
|---|---|
| **Kurs** | Algebra och vektorgeometri |
| **Omfattning** | 7,5 hp |
| **Läsperiod** | VT 2026, period 3 |
| **Examination** | Skriftlig tentamen |

## Kursens progression
Föreläsningarna bygger på varandra i denna ordning:
1. Vektorer i planet och rummet
2. Linjära ekvationssystem
3. Matriser och determinanter
4. Linjära avbildningar
5. Egenvärden och egenvektorer
6. Ortogonalitet och projektion

## Viktigt för den här kursen
- Ekvationssystem löses med EKVIVALENTA OPERATIONER, inte med
  Gauss-eliminering (det kommer i senare kurs)
- Determinanter beräknas med kofaktorutveckling
- Notation: vektorer skrivs med pil ovanför (ā), inte fetstil
```

Det här löser inte allt. Claude missar fortfarande ibland. Men istället för femton minuter av screenshots och "nej, inte den metoden" handlar det om en snabb korrigering. Claude är redan i rätt spår.

---

## Rätt verktyg för rätt uppgift

### Claude Code — bygga och underhålla systemet

Claude Code använder jag för att bygga och underhålla studiesystemet:

- Extrahera PDF:er till Markdown
- Skapa och uppdatera CLAUDE.md-filer
- Lägga till nytt kursmaterial
- Pusha ändringar till GitHub

När en föreläsning är klar och jag har nya anteckningar öppnar jag Code:

```
Jag har lagt nya föreläsningsanteckningar i pdf-original/algebra/.
Extrahera dem till Markdown i forelasningar/ och uppdatera
CLAUDE.md om det tillkommit nya metoder eller notation.
```

Code hanterar filerna, jag pushar, och nästa gång jag öppnar Chat har projektet uppdaterat material.

### Claude Chat — dagligt pluggande

Allt faktiskt pluggande gör jag i Claude Chat. Projektet är kopplat till GitHub-repot, så Chat har tillgång till alla föreläsningar, regler och kursmaterial, utan att jag behöver sitta i terminalen.

**Snabba frågor — på bussen, i biblioteket:**

> *"Förklara vad en linjär avbildning är, med ett enkelt exempel."*

Claude svarar med kursens terminologi och refererar till föreläsning 04, utan att jag behöver peka ut vilken fil som är relevant.

> *"Jag fattar inte beviset för att determinanten av en produkt är produkten av determinanterna. Kan du gå igenom det steg för steg?"*

Claude hittar beviset i föreläsning 03 och bryter ner det.

**Övning och vägledning:**

> *"Jag vill öva på linjära ekvationssystem. Ge mig en uppgift på samma nivå som övning 2, uppgift 3–5. Vägled mig genom lösningen utan att ge svaret direkt."*

Claude läser övningsfilerna, förstår svårighetsgraden, och skapar en liknande uppgift. Om jag tyckte en uppgift var svår och vill göra en till, men det inte finns fler i kursmaterialet, skapar Chat en ny direkt.

**Förklara på djupet:**

> *"Jag förstår mekaniskt hur man beräknar egenvärden, men jag fattar inte vad de BETYDER geometriskt. Förklara intuitivt, med koppling till det vi gått igenom om linjära avbildningar."*

Claude kopplar ihop föreläsning 04 (linjära avbildningar) med föreläsning 05 (egenvärden) och förklarar med kursens egna exempel.

**Tentaförberedelse:**

> *"Analysera tentorna i tentor/. Vilka ämnen kommer alltid? Vilka typer av uppgifter är vanligast? Ge mig en prioriteringslista för vad jag borde öva mest på."*

Claude läser samtliga tentor, identifierar mönster, och ger en datadriven studieplan.

### Varför Chat för pluggande?

Chat-UI:t är bättre för det som pluggande faktiskt är: konversation. Jag ställer en fråga, får ett svar, följer upp, ber om ett till exempel. Det flödet funkar sämre i en terminal. Och eftersom Chat-projektet är syncat med GitHub har det exakt samma kontext som Code byggde: CLAUDE.md-regler, kursmaterial, allt.

### Typisk vecka

| Steg | Verktyg | Uppgift |
|------|---------|---------|
| 1 | **Chat** (telefon) | Läsa sammanfattning av nästa föreläsning på bussen |
| 2 | **Föreläsning** | Lyssna, anteckna, ställa frågor |
| 3 | **Code** | Extrahera nya anteckningar till Markdown, pusha till GitHub |
| 4 | **Chat** | Öva på uppgifter med vägledning |
| 5 | **Chat** | Snabba frågor när något är oklart |
| 6 | **Chat** | Tentaförberedelse: analysera gamla tentor, generera övningsuppgifter |

---

## Skills — strukturerade arbetssätt

Skills är en Claude Code-funktion: Markdown-filer i `.claude/skills/` som definierar steg-för-steg-arbetssätt. I Code triggar du dem med `/forklara` eller `/ova`. Men i praktiken behöver jag dem sällan direkt, eftersom Chat-projektet är syncat med GitHub har Claude redan tillgång till samma filer, och CLAUDE.md-reglerna ser till att Claude följer rätt approach oavsett. Jag skriver bara "skapa en övningsuppgift om determinanter" i Chat och det funkar.

Skills är ändå värda att skapa. De tvingar dig att tänka igenom *hur* du vill att Claude ska arbeta, och det gör både Code och Chat bättre.

### /forklara — Förklara ett begrepp

```markdown
# Förklara begrepp

1. Identifiera vilken kurs och vilket ämnesområde begreppet tillhör
2. Läs relevanta föreläsningsfiler för att hitta hur kursen definierar det
3. Ge definitionen med kursens notation
4. Förklara intuitivt — vad BETYDER det?
5. Ge ett konkret exempel från kursens material
6. Koppla till närliggande begrepp som redan gåtts igenom
```

### /ova — Skapa övningsuppgift

```markdown
# Skapa övningsuppgift

1. Fråga: vilket ämne och vilken svårighetsgrad?
2. Läs relevanta övningsuppgifter för att matcha nivån
3. Skapa en ny uppgift (inte en kopia)
4. Vägled genom lösningen steg för steg — ge INTE svaret direkt
5. Om jag kör fast efter två försök — ge en ledtråd
6. Om jag kör fast efter ledtråden — visa nästa steg med förklaring
7. När uppgiften är löst — sammanfatta vilken metod vi använde och varför
```

### /tentaanalys — Analysera gamla tentor

```markdown
# Tentaanalys

1. Läs alla tentor i tentor/
2. Kategorisera varje uppgift efter ämne och typ
3. Skapa en frekvenstabell: vilka ämnen kommer alltid, ofta, ibland?
4. Identifiera uppgiftstyper som återkommer
5. Ge en prioriterad studielista baserad på frekvens och poängvikt
6. Flagga ämnen som ökat i frekvens de senaste tentorna
```

---

## Självinlärning — systemet som lär sig med mig

Precis som i [kapitel 06](06-exempel-private-equity.md) går det att bygga ett lärdomssystem. För studier ser det lite annorlunda ut.

### Vad jag trackar

```markdown
## Lärdomar

### Notation skiljer sig mellan kurser
- **Datum:** 2026-02-10
- **Situation:** Claude använde transponat-notation från envariabel
  i en algebrauppgift. Kurserna använder olika notation.
- **Lärdom:** Varje kurs-CLAUDE.md behöver en egen notationssektion.
- **Status:** [INARBETAD] — lagt till i båda kursernas CLAUDE.md

### Övningsuppgifter behöver anpassad svårighetsgrad
- **Datum:** 2026-02-15
- **Situation:** /ova genererade uppgifter som var svårare än
  kursens övningar. Bra för utmaning, men inte för grundträning.
- **Lärdom:** Skillen behöver fråga om nivå: grundnivå (som
  övningarna) eller utmaningsnivå (som tentauppgifterna).
- **Status:** [INARBETAD] — uppdaterat /ova-skillen
```

Varje lärdom gör systemet bättre. Efter några veckor vet Claude exakt vilken notation, vilka metoder och vilken svårighetsgrad som gäller, utan att jag förklarar det.

---

## Kom igång — så här beskriver du det för Claude Code

### Börja i chatten

Öppna Claude Chat och beskriv din situation:

> *"Jag läser [kurs 1] och [kurs 2] på universitet. Jag har föreläsningsanteckningar, kursplaner, formelsamlingar och gamla tentor som PDF:er. Jag vill bygga ett AI-system som hjälper mig plugga, med fokus på att faktiskt kunna materialet, inte bara memorera lösningar. Hjälp mig tänka igenom hur det borde se ut."*

Diskutera och iterera. Be sedan chatten ta fram en terminalredo prompt.

### En exempelprompt för Claude Code

```
Skapa ett kursprojekt med följande struktur:

- En rotmapp med CLAUDE.md som sätter pedagogiska regler
- En mapp per kurs med egen CLAUDE.md, kursplan, föreläsningar,
  övningsuppgifter och tentor
- En pdf-original/ mapp för arkivering av original-PDF:er

Skapa en rot-CLAUDE.md med:
- Roll: tålmodig studiekamrat som förklarar steg för steg
- Regel: lös aldrig uppgifter direkt — vägled istället
- Regel: använd bara metoder och notation från kursens föreläsningar
- Format: stegnumrerade lösningar, svenska termer med engelska
  i parentes

Skapa kursspecifika CLAUDE.md-filer med:
- Kursöversikt (namn, hp, period)
- Kursens progression (vilka ämnen i vilken ordning)
- Kursspecifika regler för metoder och notation

Skapa skills för:
- /forklara — förklara ett begrepp med kursens definition och intuition
- /ova — skapa övningsuppgift och vägled genom lösningen
- /tentaanalys — analysera gamla tentor och ge studieprioriteringar

Initiera ett Git-repo.
```

### Nästa steg

1. **Lägg in dina PDF:er:** kopiera föreläsningar, kursplan, formelsamling och tentor till rätt mappar
2. **Extrahera till Markdown:** be Claude Code läsa PDF:erna och skapa Markdown-versioner
3. **Testa i Chat med en riktig uppgift:** till exempel: *"Jag fattar inte det här med linjärt beroende, förklara"*
4. **Iterera:** justera CLAUDE.md när Claude använder fel metod eller notation, lägg till fler skills

### Vad ger mest effekt snabbast?

| Åtgärd | Effekt |
|--------|--------|
| Extrahera föreläsningar till Markdown | Claude kan referera till exakt rätt material |
| Skriva kursspecifika CLAUDE.md med metoder och notation | Slut på "fel metod"-problemet |
| Skapa /ova-skillen | Obegränsat med övningsuppgifter på rätt nivå |
| Analysera gamla tentor | Datadriven studieplan istället för gissningar |

Börja med en kurs. Lägg in föreläsningarna. Testa att fråga något. Systemet blir bättre för varje session.

---

## Avslutning

Det här kapitlet har visat hur koncepten från Del 1 hänger ihop för studier:

- **Mappstruktur** som speglar kurserna: en mapp per kurs med föreläsningar, övningar och tentor
- **CLAUDE.md-hierarki** med pedagogiska regler på rotnivå och kursspecifika metoder och notation per kurs
- **Rätt verktyg för rätt uppgift:** Code bygger systemet, Chat är den dagliga studiepartnern
- **Skills** som gör vanliga studiemoment repeterbara: förklara, öva, analysera tentor
- **Självinlärning** som gör systemet bättre för varje vecka

Arbetsflödet fungerar för vilken kurs som helst: juridik, ekonomi, naturvetenskap, språk. Principen är densamma: ge AI rätt material i rätt format med regler som hjälper den fokusera.

Femton minuter per screenshot, eller femton minuter en gång för att bygga systemet. Jag valde det andra.

---

> *Föregående kapitel: [04 — Strukturerad kontext](04-strukturerad-kontext.md)*
>
> *Nästa kapitel: [06 — Exempel: Private Equity](06-exempel-private-equity.md)*
