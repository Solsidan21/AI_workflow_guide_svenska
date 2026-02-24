# Kapitel 02 — Claude Code

> *Verktyget som tar dig från engångsprompts till ett system där AI arbetar med dina filer, följer dina regler och gör sig smartare över tid.*

!!! note "Det här kapitlet är Claude-specifikt"
    Claude Code är Anthropics verktyg och har ingen direkt motsvarighet hos andra leverantörer. Liknande koncept finns dock i **Cursor** (AI-editor med filåtkomst och regler), **GitHub Copilot Workspace** och **Windsurf**. Principerna — persistent kontext, instruktionsfiler, återanvändbara arbetsflöden — går att tillämpa oavsett verktyg.

---

## Vad är Claude Code?

Claude Code är ett CLI-verktyg (Command Line Interface) från Anthropic. Du startar det i terminalen, och därifrån kan Claude:

- **Läsa filer** på din dator — PDF:er, Excel-exporter, textfiler, CSV
- **Skriva och redigera filer** — rapporter, analyser, sammanställningar
- **Köra kommandon** — organisera mappar, bearbeta data, automatisera uppgifter
- **Följa regler** — genom CLAUDE.md och skills som du definierar

**Tänksätt:** Föreställ dig en extremt kompetent assistent som sitter bredvid dig vid datorn. Du pekar på en mapp med finansiella data och säger "analysera kassaflödet och skriv en sammanfattning." Assistenten läser filerna, gör beräkningarna, skriver rapporten och sparar den på rätt ställe.

---

## Varför det är ett språng jämfört med chatten

Du är van vid att chatta med AI. Claude Code ger dig tre saker som chatten inte har:

| Chatt | Claude Code |
|-------|-------------|
| Du kopierar in text manuellt | Claude läser dina filer direkt |
| Du får svar i chattfönster att kopiera | Claude skriver filer på din dator |
| Du förklarar regler varje session | CLAUDE.md gör att reglerna alltid gäller |
| Samma prompt varje gång | Skills automatiserar återanvändbara arbetsflöden |
| Kontextfönstret är allt som finns | Hela mappstrukturen är kontext |

Skillnaden är inte att Claude Code är "smartare" — det är samma AI-modell. Skillnaden är att du ger den **bättre förutsättningar** att göra ett bra jobb.

---

## Installation steg för steg

### 1. Installera Node.js

Gå till [nodejs.org](https://nodejs.org) och ladda ner LTS-versionen. Klicka dig genom installationen med standardinställningar.

Node.js är en "motor" som Claude Code behöver för att fungera. Du använder den aldrig direkt.

### 2. Öppna terminalen

- **Mac:** Sök efter "Terminal" i Spotlight (Cmd + Mellanslag)
- **Windows:** Sök efter "PowerShell"

### 3. Installera Claude Code

Skriv följande och tryck Enter:

```
npm install -g @anthropic-ai/claude-code
```

(`npm` är en pakethanterare som följde med Node.js — tänk på det som en appbutik för verktyg.)

### 4. Starta Claude Code

```
claude
```

### 5. Logga in

Första gången ombeds du logga in med ditt Anthropic-konto. Följ instruktionerna på skärmen.

> **Tips:** Om du aldrig har öppnat en terminal förut, be en teknisk kollega hjälpa dig med installationen. Det tar 5-10 minuter. När det är gjort är allt enkelt.

---

## Grundläggande användning

### Starta en session

Navigera till din projektmapp och starta Claude Code:

```
cd ~/Dokument/portfoljbolag-x
claude
```

Nu ser Claude alla filer i mappen och kan arbeta med dem. **Var du står när du startar spelar roll** — Claude arbetar i den mapp du befinner dig i.

### Interaktiv konversation

Skriv frågor och instruktioner precis som i en chatt:

```
> Visa mig alla filer i det här projektet
> Läs årsredovisningen i data/finansiellt/ och sammanfatta nyckeltal
> Skapa en kassaflödesanalys och spara som analys/kassaflode.md
```

Claude minns hela konversationen så länge sessionen pågår.

### Snabbfråga (utan session)

```
claude "Sammanfatta alla textfiler i den här mappen"
```

Claude svarar och avslutar. Perfekt för snabba uppgifter.

### Viktiga kommandon

| Kommando | Vad det gör |
|----------|-------------|
| `/compact` | Sammanfattar konversationen för att frigöra kontext. **Använd regelbundet** vid längre sessioner. |
| `/clear` | Rensar konversationen — börjar om från noll |
| `/cost` | Visar hur många tokens du förbrukat |
| `/help` | Visar hjälptext |
| `/exit` | Avslutar sessionen (eller Ctrl+C) |

**Specialtips — `/compact`:** Claudes kontextfönster är stort men inte oändligt. När du arbetat länge kan Claude börja tappa tråd från början av sessionen. `/compact` sammanfattar allt hittills till en kortare version så du kan fortsätta arbeta.

---

## CLAUDE.md — Det viktigaste verktyget

Om du bara tar med dig en sak från hela den här guiden: **skapa en CLAUDE.md-fil.**

### Vad är det?

En Markdown-fil som du placerar i roten av din projektmapp. När Claude Code startar läser den automatiskt CLAUDE.md och följer instruktionerna. Varje session, utan att du behöver säga något.

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

### Vad ska stå i den?

En bra CLAUDE.md täcker fem saker:

**1. Roll och kontext**
```markdown
## Roll
Du är en erfaren PE-analytiker med fokus på nordiska SaaS-bolag.
Var noggrann med siffror, koncis i formuleringar och fokuserad på
det som är relevant för investeringsbeslutet.

## Projektkontext
Vi utvärderar Bolag X, ett svenskt HR-tech SaaS-bolag med ~150 MSEK
i intäkter. Vi befinner oss i tidig evaluering.
```

**2. Regler och format**
```markdown
## Regler
- Skriv alltid på svenska
- Alla finansiella siffror i MSEK
- Tusentalsavgränsare med mellanslag: 1 000
- Procent med en decimal: 12,3%
- Tabeller för all jämförande data
- Börja rapporter med sammanfattning (3-5 meningar)
- Avsluta med "Nästa steg" eller "Rekommendation"
- Spekulera inte — om data saknas, ange det tydligt
```

**3. Vanliga uppgifter**
```markdown
## Vanliga uppgifter

### Kassaflödesanalys
1. Läs data från data/finansiellt/
2. Beräkna Revenue, EBITDA, Capex, delta rörelsekapital, FCF
3. Presentera i tabell med årlig jämförelse
4. Kommentera trender (3-5 meningar)
5. Spara i analys/kassaflode/
```

**4. Filstruktur**
```markdown
## Filstruktur
- data/finansiellt/ — Årsredovisningar, kvartalsdata
- data/marknad/ — Branschrapporter, konkurrentinfo
- analys/ — Bearbetade analyser (skapa här)
- output/ — Färdiga leveranser
- mallar/ — Mallar för formatering
```

**5. Mallar och referenser**
```markdown
## Mallar
- Investment memo: se mallar/investment-memo-mall.md
- Kvartalsrapport: se mallar/kvartalsrapport-mall.md
Följ mallen exakt vad gäller struktur.
```

### Praktiskt PE-exempel (komplett)

```markdown
# CLAUDE.md — Portföljbolag X

## Roll
Du är en erfaren PE-analytiker med fokus på nordiska SaaS-bolag.
Noggrann med siffror, koncis i formuleringar, fokuserad på
investeringsbeslutet.

## Projektkontext
Bolag X är ett svenskt HR-tech SaaS-bolag, grundat 2015.
Cirka 200 anställda, ~150 MSEK i intäkter (2024).
Vi befinner oss i initial evaluering.

## Regler
- Språk: svenska
- Ton: formell men tillgänglig
- Siffror: MSEK, en decimal, mellanslag som tusentalsavgränsare
- Datum: YYYY-MM-DD
- Tabeller för jämförande data
- Börja rapporter med sammanfattning (3-5 meningar)
- Avsluta analyser med rekommendation eller nästa steg
- Spekulera inte — markera saknad data med [DATA SAKNAS]

## Vanliga uppgifter

### Kassaflödesanalys
1. Läs data/finansiellt/
2. Beräkna Revenue, EBITDA, Capex, delta rörelsekapital, FCF
3. Tabell med årlig jämförelse + tillväxt
4. FCF-konvertering (FCF/EBITDA)
5. Trendkommentar (3-5 meningar)
6. Spara: analys/kassaflode/kassaflode-YYYY-MM-DD.md

### Investment memo
1. Använd mallar/investment-memo-mall.md
2. Fyll i alla sektioner baserat på tillgänglig data
3. Markera sektioner där data saknas
4. Spara: output/memos/

## Filstruktur
- data/finansiellt/ — Årsredovisningar, kvartalsdata
- data/marknad/ — Branschrapporter, konkurrentinfo
- data/operativt/ — KPI:er, organisation
- analys/ — Bearbetade analyser
- output/ — Färdiga leveranser
- mallar/ — Rapportmallar
```

> För en djupare genomgång av CLAUDE.md med hierarkisk placering och avancerade tekniker, se **[kapitel 04](04-mappstruktur-och-kontext.md)**.

---

## Skills — egna kommandon

Skills är återanvändbara arbetsflöden. Du skapar en Markdown-fil med instruktioner, och sedan kan du aktivera den med ett enda kommando.

### Var placeras de?

I mappen `.claude/skills/` i ditt projekt:

```
mitt-projekt/
├── CLAUDE.md
├── .claude/
│   └── skills/
│       ├── kassaflodesanalys.md
│       ├── investment-memo.md
│       └── due-diligence.md
└── ...
```

### Hur skapar du en skill?

Skapa en Markdown-fil med instruktioner:

**`.claude/skills/kassaflodesanalys.md`**
```markdown
# Kassaflödesanalys

När den här skillen aktiveras:

1. Läs alla finansiella filer i data/finansiellt/
2. Identifiera revenue, EBITDA, Capex och förändring i rörelsekapital
3. Beräkna fritt kassaflöde (FCF) för varje period
4. Skapa en tabell med:
   - Revenue och tillväxt (%)
   - EBITDA och EBITDA-marginal (%)
   - Capex
   - Förändring rörelsekapital
   - Fritt kassaflöde
   - FCF-konvertering (FCF/EBITDA)
5. Skriv kort kommentar (3-5 meningar) om trender
6. Spara som analys/kassaflode/kassaflode-YYYY-MM-DD.md
```

### Hur använder du den?

I en Claude Code-session:

```
/kassaflodesanalys
```

Claude läser instruktionsfilen och utför alla stegen. Samma resultat varje gång, utan att du behöver skriva om instruktionerna.

### Fler skill-idéer

- `/investment-memo` — Komplett memo baserat på tillgänglig data
- `/konkurrentanalys` — Kartlägg och jämför konkurrenter
- `/due-diligence` — Checklista anpassad efter bolagets profil
- `/manadsbrev` — Utkast från KPI-data
- `/presentationsunderlag` — Struktur för styrelsepresentation

---

## MCP-servrar (kort)

MCP (Model Context Protocol) är utökningar som ger Claude Code tillgång till externa datakällor och verktyg — till exempel databaser, webb-API:er eller filsystem utanför projektet.

Det är ett kraftfullt verktyg för avancerade användare men inget du behöver bry dig om när du börjar. Parkera det och kom tillbaka till det när du känt dig hemma i grunderna.

Det viktiga: Claude Code är byggt för att växa med dig.

---

## Praktiska tips

### När du börjar

1. **Skriv en CLAUDE.md först.** Även en kort version med roll, regler och filstruktur gör enorm skillnad. Det är den bästa tidsinsatsen du kan göra.

2. **Testa med en riktig uppgift.** Ta något du brukar göra manuellt — sammanfatta en rapport, jämföra två kvartal — och låt Claude göra det.

3. **Be Claude visa filstrukturen först.** "Visa mig alla filer i projektet" sätter kontexten för både dig och Claude.

### När du vill bli effektivare

4. **Spara bra prompts som skills.** När du hittar en formulering som ger bra resultat, gör den till en skill. Det är så systemet växer.

5. **Använd `/compact` regelbundet.** När svaren börjar tappa koppling till det ni diskuterat, kör `/compact` för att frigöra kontext.

6. **Iterera.** Det bästa med Code är att ni kan arbeta fram och tillbaka. "Bra, men ändrar tonen. Lägg till en tabell." Claude gör ändringen direkt i filen.

### Vanliga misstag

- **För vaga instruktioner.** "Gör en analys" är för vagt. "Analysera kassaflödet baserat på data i data/finansiellt/ och presentera som tabell" är bra.

- **Ingen CLAUDE.md.** Utan instruktionsfil måste du upprepa samma saker i varje session. Det är exakt det problem vi försöker lösa.

- **Fel mapp.** Claude arbetar i den mapp du startar det i. Dubbelkolla att du är i rätt mapp innan du börjar.

- **För stora första steg.** Börja inte med att delegera en hel due diligence. Börja med en kassaflödessammanfattning. Bygg upp förtroendet.

---

> *Föregående kapitel: [01 — Från chatt till system](01-fran-chatt-till-system.md)*
>
> *Nästa kapitel: [03 — Claude Cowork](03-claude-cowork.md)*
