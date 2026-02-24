# Kapitel 02 — Claude Code

> *Verktyget som tar dig fran engangsprompts till ett system dar AI arbetar med dina filer, foljer dina regler och gor sig smartare over tid.*

---

## Vad ar Claude Code?

Claude Code ar ett CLI-verktyg (Command Line Interface) fran Anthropic. Du startar det i terminalen, och darifran kan Claude:

- **Lasa filer** pa din dator — PDF:er, Excel-exporter, textfiler, CSV
- **Skriva och redigera filer** — rapporter, analyser, sammanstallningar
- **Kora kommandon** — organisera mappar, bearbeta data, automatisera uppgifter
- **Folja regler** — genom CLAUDE.md och skills som du definierar

**Tanksatt:** Forestall dig en extremt kompetent assistent som sitter bredvid dig vid datorn. Du pekar pa en mapp med finansiella data och sager "analysera kassaflodet och skriv en sammanfattning." Assistenten laser filerna, gor berakningarna, skriver rapporten och sparar den pa ratt stalle.

---

## Varfor det ar ett sprang jamfort med chatten

Du ar van vid att chatta med AI. Claude Code ger dig tre saker som chatten inte har:

| Chatt | Claude Code |
|-------|-------------|
| Du kopierar in text manuellt | Claude laser dina filer direkt |
| Du far svar i chattfonster att kopiera | Claude skriver filer pa din dator |
| Du forklarar regler varje session | CLAUDE.md gor att reglerna alltid galler |
| Samma prompt varje gang | Skills automatiserar ateranvandbara arbetsfloden |
| Kontextfonstret ar allt som finns | Hela mappstrukturen ar kontext |

Skillnaden ar inte att Claude Code ar "smartare" — det ar samma AI-modell. Skillnaden ar att du ger den **battre forutsattningar** att gora ett bra jobb.

---

## Installation steg for steg

### 1. Installera Node.js

Ga till [nodejs.org](https://nodejs.org) och ladda ner LTS-versionen. Klicka dig genom installationen med standardinstallningar.

Node.js ar en "motor" som Claude Code behover for att fungera. Du anvander den aldrig direkt.

### 2. Oppna terminalen

- **Mac:** Sok efter "Terminal" i Spotlight (Cmd + Mellanslag)
- **Windows:** Sok efter "PowerShell"

### 3. Installera Claude Code

Skriv foljande och tryck Enter:

```
npm install -g @anthropic-ai/claude-code
```

(`npm` ar en pakethanterare som foljde med Node.js — tank pa det som en appbutik for verktyg.)

### 4. Starta Claude Code

```
claude
```

### 5. Logga in

Forsta gangen ombeds du logga in med ditt Anthropic-konto. Folj instruktionerna pa skarmen.

> **Tips:** Om du aldrig har oppnat en terminal forut, be en teknisk kollega hjalpa dig med installationen. Det tar 5-10 minuter. Nar det ar gjort ar allt enkelt.

---

## Grundlaggande anvandning

### Starta en session

Navigera till din projektmapp och starta Claude Code:

```
cd ~/Dokument/portfoljbolag-x
claude
```

Nu ser Claude alla filer i mappen och kan arbeta med dem. **Var du star nar du startar spelar roll** — Claude arbetar i den mapp du befinner dig i.

### Interaktiv konversation

Skriv fragor och instruktioner precis som i en chatt:

```
> Visa mig alla filer i det har projektet
> Las arsredovisningen i data/finansiellt/ och sammanfatta nyckeltal
> Skapa en kassaflodesanalys och spara som analys/kassaflode.md
```

Claude minns hela konversationen sa lange sessionen pagar.

### Snabbfraga (utan session)

```
claude "Sammanfatta alla textfiler i den har mappen"
```

Claude svarar och avslutar. Perfekt for snabba uppgifter.

### Viktiga kommandon

| Kommando | Vad det gor |
|----------|-------------|
| `/compact` | Sammanfattar konversationen for att frigora kontext. **Anvand regelbundet** vid langre sessioner. |
| `/clear` | Rensar konversationen — borjar om fran noll |
| `/cost` | Visar hur manga tokens du forbrukat |
| `/help` | Visar hjalptext |
| `/exit` | Avslutar sessionen (eller Ctrl+C) |

**Specialtips — `/compact`:** Claudes kontextfonster ar stort men inte oandligt. Nar du arbetat lange kan Claude borja tappa trad fran borjan av sessionen. `/compact` sammanfattar allt hittills till en kortare version sa du kan fortsatta arbeta.

---

## CLAUDE.md — Det viktigaste verktyget

Om du bara tar med dig en sak fran hela den har guiden: **skapa en CLAUDE.md-fil.**

### Vad ar det?

En Markdown-fil som du placerar i roten av din projektmapp. Nar Claude Code startar laser den automatiskt CLAUDE.md och foljer instruktionerna. Varje session, utan att du behover saga nagot.

**Det ar skillnaden mellan en assistent som borjar fran noll varje dag och en som kanner projektet.**

### Var placeras den?

Direkt i projektmappens rot:

```
mitt-projekt/
├── CLAUDE.md          <-- Har
├── data/
├── analys/
└── output/
```

### Vad ska sta i den?

En bra CLAUDE.md tacker fem saker:

**1. Roll och kontext**
```markdown
## Roll
Du ar en erfaren PE-analytiker med fokus pa nordiska SaaS-bolag.
Var noggrann med siffror, koncis i formuleringar och fokuserad pa
det som ar relevant for investeringsbeslutet.

## Projektkontext
Vi utvardelar Bolag X, ett svenskt HR-tech SaaS-bolag med ~150 MSEK
i intakter. Vi befinner oss i tidig evaluering.
```

**2. Regler och format**
```markdown
## Regler
- Skriv alltid pa svenska
- Alla finansiella siffror i MSEK
- Tusentalsavgransare med mellanslag: 1 000
- Procent med en decimal: 12,3%
- Tabeller for all jamforande data
- Borja rapporter med sammanfattning (3-5 meningar)
- Avsluta med "Nasta steg" eller "Rekommendation"
- Spekulera inte — om data saknas, ange det tydligt
```

**3. Vanliga uppgifter**
```markdown
## Vanliga uppgifter

### Kassaflodesanalys
1. Las data fran data/finansiellt/
2. Berakna Revenue, EBITDA, Capex, delta rorelsekapital, FCF
3. Presentera i tabell med arlig jamforelse
4. Kommentera trender (3-5 meningar)
5. Spara i analys/kassaflode/
```

**4. Filstruktur**
```markdown
## Filstruktur
- data/finansiellt/ — Arsredovisningar, kvartalsdata
- data/marknad/ — Branschrapporter, konkurrentinfo
- analys/ — Bearbetade analyser (skapa har)
- output/ — Fardiga leveranser
- mallar/ — Mallar for formatering
```

**5. Mallar och referenser**
```markdown
## Mallar
- Investment memo: se mallar/investment-memo-mall.md
- Kvartalsrapport: se mallar/kvartalsrapport-mall.md
Folj mallen exakt vad galler struktur.
```

### Praktiskt PE-exempel (komplett)

```markdown
# CLAUDE.md — Portfoljbolag X

## Roll
Du ar en erfaren PE-analytiker med fokus pa nordiska SaaS-bolag.
Noggrann med siffror, koncis i formuleringar, fokuserad pa
investeringsbeslutet.

## Projektkontext
Bolag X ar ett svenskt HR-tech SaaS-bolag, grundat 2015.
Cirka 200 anstallda, ~150 MSEK i intakter (2024).
Vi befinner oss i initial evaluering.

## Regler
- Sprak: svenska
- Ton: formell men tillganglig
- Siffror: MSEK, en decimal, mellanslag som tusentalsavgransare
- Datum: YYYY-MM-DD
- Tabeller for jamforande data
- Borja rapporter med sammanfattning (3-5 meningar)
- Avsluta analyser med rekommendation eller nasta steg
- Spekulera inte — markera saknad data med [DATA SAKNAS]

## Vanliga uppgifter

### Kassaflodesanalys
1. Las data/finansiellt/
2. Berakna Revenue, EBITDA, Capex, delta rorelsekapital, FCF
3. Tabell med arlig jamforelse + tillvaxt
4. FCF-konvertering (FCF/EBITDA)
5. Trendkommentar (3-5 meningar)
6. Spara: analys/kassaflode/kassaflode-YYYY-MM-DD.md

### Investment memo
1. Anvand mallar/investment-memo-mall.md
2. Fyll i alla sektioner baserat pa tillganglig data
3. Markera sektioner dar data saknas
4. Spara: output/memos/

## Filstruktur
- data/finansiellt/ — Arsredovisningar, kvartalsdata
- data/marknad/ — Branschrapporter, konkurrentinfo
- data/operativt/ — KPI:er, organisation
- analys/ — Bearbetade analyser
- output/ — Fardiga leveranser
- mallar/ — Rapportmallar
```

> For en djupare genomgang av CLAUDE.md med hierarkisk placering och avancerade tekniker, se **[kapitel 04](04-mappstruktur-och-kontext.md)**.

---

## Skills — egna kommandon

Skills ar ateranvandbara arbetsfloden. Du skapar en Markdown-fil med instruktioner, och sedan kan du aktivera den med ett enda kommando.

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
# Kassaflodesanalys

Nar den har skillen aktiveras:

1. Las alla finansiella filer i data/finansiellt/
2. Identifiera revenue, EBITDA, Capex och forandring i rorelsekapital
3. Berakna fritt kassaflode (FCF) for varje period
4. Skapa en tabell med:
   - Revenue och tillvaxt (%)
   - EBITDA och EBITDA-marginal (%)
   - Capex
   - Forandring rorelsekapital
   - Fritt kassaflode
   - FCF-konvertering (FCF/EBITDA)
5. Skriv kort kommentar (3-5 meningar) om trender
6. Spara som analys/kassaflode/kassaflode-YYYY-MM-DD.md
```

### Hur anvander du den?

I en Claude Code-session:

```
/kassaflodesanalys
```

Claude laser instruktionsfilen och utfor alla stegen. Samma resultat varje gang, utan att du behover skriva om instruktionerna.

### Fler skill-ideer

- `/investment-memo` — Komplett memo baserat pa tillganglig data
- `/konkurrentanalys` — Kartlagg och jamfor konkurrenter
- `/due-diligence` — Checklista anpassad efter bolagets profil
- `/manadsbrev` — Utkast fran KPI-data
- `/presentationsunderlag` — Struktur for styrelsepresentation

---

## MCP-servrar (kort)

MCP (Model Context Protocol) ar utokningar som ger Claude Code tillgang till externa datakallor och verktyg — till exempel databaser, webb-API:er eller filsystem utanfor projektet.

Det ar ett kraftfullt verktyg for avancerade anvandare men inget du behover bry dig om nar du borjar. Parkera det och kom tillbaka till det nar du kant dig hemma i grunderna.

Det viktiga: Claude Code ar byggt for att vaxa med dig.

---

## Praktiska tips

### Nar du borjar

1. **Skriv en CLAUDE.md forst.** Even en kort version med roll, regler och filstruktur gor enorm skillnad. Det ar den basta tidsinsatsen du kan gora.

2. **Testa med en riktig uppgift.** Ta nagot du brukar gora manuellt — sammanfatta en rapport, jamfora tva kvartal — och lat Claude gora det.

3. **Be Claude visa filstrukturen forst.** "Visa mig alla filer i projektet" satter kontexten for bade dig och Claude.

### Nar du vill bli effektivare

4. **Spara bra prompts som skills.** Nar du hittar en formulering som ger bra resultat, gor den till en skill. Det ar sa systemet vaxer.

5. **Anvand `/compact` regelbundet.** Nar svaren borjar tappa koppling till det ni diskuterat, kor `/compact` for att frigora kontext.

6. **Iterera.** Det basta med Code ar att ni kan arbeta fram och tillbaka. "Bra, men andrar tonen. Lagg till en tabell." Claude gor andringen direkt i filen.

### Vanliga misstag

- **For vaga instruktioner.** "Gor en analys" ar for vagt. "Analysera kassaflodet baserat pa data i data/finansiellt/ och presentera som tabell" ar bra.

- **Ingen CLAUDE.md.** Utan instruktionsfil maste du upprepa samma saker i varje session. Det ar exakt det problem vi forsoker losa.

- **Fel mapp.** Claude arbetar i den mapp du startar det i. Dubbelkolla att du ar i ratt mapp innan du borjar.

- **For stora forsta steg.** Borja inte med att delegera en hel due diligence. Borja med en kassaflodessammanfattning. Bygg upp fortroendet.

---

> *Foregaende kapitel: [01 — Fran chatt till system](01-fran-chatt-till-system.md)*
>
> *Nasta kapitel: [03 — Claude Cowork](03-claude-cowork.md)*
