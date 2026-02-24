# Claude Code — AI i terminalen

> *Det har ar kapitlet dar det verkligen borjar handa saker. Claude Code ar verktyget som tar dig fran att chatta med AI till att samarbeta med AI — direkt pa din dator, med dina filer, i realtid.*

---

## Vad ar Claude Code?

Claude Code ar ett **CLI-verktyg** (Command Line Interface) fran Anthropic. "CLI" betyder helt enkelt att du interagerar med programmet genom att skriva textkommandon i terminalen — det svarta (eller vita) fonstret som utvecklare anvander.

Men lat inte det skramma dig. Du behover inte vara programmerare for att anvanda det.

**Vad Claude Code kan gora:**

- **Lasa filer** pa din dator — till exempel Excel-exporter, textfiler, analysunderlag
- **Skriva och redigera filer** — skapa rapporter, uppdatera dokument, bygga mallar
- **Kora kommandon** — organisera mappar, soka i filer, automatisera uppgifter
- **Navigera i hela ditt projekt** — forsta hur dina filer hanger ihop

**Tanksatt**: forestall dig en extremt kompetent assistent som sitter bredvid dig vid datorn. Du pekar pa en mapp med finansiella data och sager "analysera kassaflodet for de senaste tre aren och skriv en sammanfattning". Assistenten lagger till och gor det — laser filerna, gor berakningarna, skriver rapporten och sparar den pa ratt stalle. Det ar Claude Code.

### Varfor ar detta viktigare an Claude Chat?

| Claude Chat | Claude Code |
|-------------|-------------|
| Du kopierar in text manuellt | Claude laser dina filer direkt |
| Du far svar i chattfonster | Claude skriver resultatet som filer pa din dator |
| Begransat kontextfonster | Kan arbeta med hela projekt |
| En fraga i taget | Kan utfora flerasteguppgifter |

---

## Installation

### Vad du behover

For att installera Claude Code behover du **Node.js** — en programvara som gor det mojligt att kora JavaScript-baserade verktyg pa din dator. Tankt pa det som en "motor" som Claude Code behover for att fungera. Du anvander den aldrig direkt — den maste bara finnas installerad.

### Steg for steg

1. **Installera Node.js** — ga till [nodejs.org](https://nodejs.org) och ladda ner LTS-versionen (Long Term Support). Klistra bara genom installationen med standardinstallningar.

2. **Oppna terminalen:**
   - **Mac**: sok efter "Terminal" i Spotlight (Cmd + Mellanslag)
   - **Windows**: sok efter "Command Prompt" eller "PowerShell"

3. **Installera Claude Code** — skriv foljande kommando och tryck Enter:
   ```
   npm install -g @anthropic-ai/claude-code
   ```
   (`npm` ar en pakethanterare som foljde med Node.js. Tankt pa det som en "app store" for programmeringsverktyg.)

4. **Starta Claude Code** — skriv:
   ```
   claude
   ```

5. **Logga in** — forsta gangen ombeds du logga in med ditt Anthropic-konto. Folj instruktionerna pa skarmen.

> **Tips:** Om du aldrig har oppnat en terminal forut, be en teknisk kollega hjalpa dig med installationen. Det tar 5-10 minuter. Nar det valf ar gjort ar allt enkelt.

---

## Grundlaggande anvandning

### Starta en interaktiv session

```
claude
```

Det har oppnar en konversation dar du kan stalla fragor och ge instruktioner. Claude ser alla filer i den mapp du star i och kan arbeta med dem.

### Snabbfraga

```
claude "Sammanfatta alla textfiler i den har mappen"
```

Perfekt for snabba uppgifter. Claude svarar och avslutar sedan.

### Print mode — for skript och automation

```
claude -p "Lista alla filer i data/-mappen sorterade efter storlek"
```

Flaggan `-p` (print mode) innebar att Claude skriver ut svaret direkt utan interaktion. Anvandbart om du vill koppla ihop flera kommandon.

### Navigering i konversationen

Nar du ar i en interaktiv session:

- **Skriv din fraga** och tryck Enter — precis som en chatt
- **Flerra fragor i rad** — Claude minns hela konversationen
- **Avsluta sessionen**: tryck `Ctrl+C` eller skriv `/exit`

### Viktigt: var du star spelar roll

Claude Code arbetar i den mapp du befinner dig i nar du startar det. Om du vill att Claude ska arbeta med ett specifikt projekt, navigera till den mappen forst:

```
cd ~/Dokument/portfoljbolag-x
claude
```

Nu ser Claude alla filer i `portfoljbolag-x/` och kan arbeta med dem.

---

## CLAUDE.md — Ditt viktigaste verktyg

Om du bara tar med dig en sak fran hela den har guiden, lat det vara detta: **skapa en CLAUDE.md-fil**.

### Vad ar CLAUDE.md?

Det ar en vanlig textfil (i Markdown-format) som du placerar i roten av din projektmapp. Nar Claude Code startar i den mappen laser den automatiskt CLAUDE.md och foljer instruktionerna.

**Analogi:** Tankt dig att du anstaller en ny medarbetare. Forsta dagen ger du dem en introduktionsmanual: "Sa har jobbar vi. Det har ar projektet. De har reglerna galler. Sa har vill vi att rapporter ser ut." CLAUDE.md ar exakt den manualen — fast for din AI-assistent.

### Var placeras den?

I **roten** av din projektmapp — det vill saga direkt i huvudmappen, inte i nagon undermapp.

```
mitt-projekt/
├── CLAUDE.md          <-- Har!
├── data/
├── analys/
└── output/
```

### Vad ska sta i din CLAUDE.md?

Har ar en praktisk checklista:

**1. Projektbeskrivning och syfte**
```markdown
# Projektinstruktioner

## Om det har projektet
Det har ar analysunderlaget for portfoljbolag X, ett nordiskt SaaS-bolag
inom HR-tech. Vi utvardelar bolaget for potentiell investering.
```

**2. Regler och riktlinjer**
```markdown
## Regler
- Skriv alltid pa svenska
- Anvand formell men tillganglig ton
- Alla finansiella siffror i MSEK om inget annat anges
- Anvand tusentalsavgransare med mellanslag (1 000, inte 1000)
- Ange alltid kallor nar du refererar till data
```

**3. Vanliga uppgifter**
```markdown
## Vanliga uppgifter

### Kassaflodesanalys
Nar jag ber om kassaflodesanalys:
1. Las data fran data/finansiellt/
2. Berakna fritt kassaflode (EBITDA - Capex - forandring rorelsekaptial)
3. Presentera i tabell med arlig jamforelse
4. Spara resultat i analys/kassaflode/

### Konkurrentoversikt
Nar jag ber om konkurrentanalys:
1. Las data fran data/marknad/
2. Jamfor mot vara interna KPI:er i data/operativt/
3. Skapa sammanfattning med styrkor/svagheter
```

**4. Filstruktur-oversikt**
```markdown
## Filstruktur
- data/ — All radata och kallmaterial
- analys/ — Bearbetade analyser och berakningar
- output/ — Fardiga rapporter och presentationer
- mallar/ — Ateranvandbara mallar for rapporter
```

**5. Tonalitet och sprak**
```markdown
## Tonalitet
Skriv som en erfaren PE-analytiker. Var koncis och faktadriven.
Undvik buzzwords. Anvand konkreta siffror framfor vaga formuleringar.
Malgrupppen ar investeringskommitten — de vill ha substans, inte fyllnad.
```

> For en fullstandig djupdykning i CLAUDE.md, inklusive avancerade tekniker som hierarkiska instruktionsfiler, se **kapitel 06**.

---

## Slash-kommandon och Skills

Claude Code har inbyggda kommandon som borjar med `/` (snedstreck). De ar genvagar for vanliga operationer.

### Inbyggda kommandon

| Kommando | Vad det gor |
|----------|-------------|
| `/help` | Visar hjalptext och tillgangliga kommandon |
| `/clear` | Rensar konversationen — borjar om fran noll |
| `/compact` | Sammanfattar konversationen for att spara kontext |
| `/cost` | Visar hur manga tokens (AI-"ord") du forbrukat |
| `/exit` | Avslutar sessionen |

**Specialtips — `/compact`:** Claude har ett begransat "minne" (kontextfonster). Nar du arbetat lange i en session kan Claude borja "glomma" det ni pratade om i borjan. `/compact` later Claude sammanfatta konversationen hittills till en kortare version, vilket frigort utrymme for mer arbete. Anvand det regelbundet vid langre sessioner.

### Custom Skills — Egna kommandon

Har blir det riktigt kraftfullt. Du kan skapa **egna kommandon** som kallas "skills". En skill ar helt enkelt en Markdown-fil med instruktioner som Claude foljer nar du aktiverar den.

**Var placeras skills?**

I mappen `.claude/skills/` i ditt projekt:

```
mitt-projekt/
├── CLAUDE.md
├── .claude/
│   └── skills/
│       ├── kassaflodesanalys.md
│       ├── konkurrentrapport.md
│       └── manadsbrev.md
└── ...
```

**Hur skapar du en skill?**

Skapa en Markdown-fil i `.claude/skills/`. Har ar ett exempel:

**`.claude/skills/kassaflodesanalys.md`**
```markdown
# Kassaflodesanalys

Nar den har skillen aktiveras, gor foljande:

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
5. Skriv en kort kommentar (3-5 meningar) om trender
6. Spara resultat som analys/kassaflode/kassaflode-YYYY-MM-DD.md
```

**Hur anvander du skillen?**

I en Claude Code-session skriver du:

```
/kassaflodesanalys
```

Claude laser instruktionsfilen och utfor alla stegen automatiskt. Det ar som att ha en makro — fast intelligent.

**Fler skill-ideer for kunskapsarbete:**

- `/investmentmemo` — Skapar ett komplett investment memo baserat pa tillganglig data
- `/konkurrentanalys` — Kartlagger och jamfor konkurrenter
- `/manadsbrev` — Genererar utkast till manadsbrev fran KPI-data
- `/due-diligence-checklista` — Skapar och bockar av DD-punkter
- `/presentationsunderlag` — Bygger struktur for styrelsepresentation

---

## Mappstruktur for kunskapsarbete

Claude Code ar inte bara for programmerare. Det fungerar utmarkt for analys, rapporter och presentationsunderlag — forutsatt att du organiserar dina filer smart.

### Varfor struktur spelar roll

Claude anvander **filnamn och mappnamn** for att forsta vad saker ar. En fil som heter `kassaflodesanalys-2024-Q3.md` i mappen `analys/kassaflode/` ger Claude all kontext den behover. En fil som heter `dok1.xlsx` i en mapp full med andra `dok`-filer ger nastan ingenting.

### Exempelstruktur for PE-arbete

```
portfoljbolag-x/
├── CLAUDE.md                    # Instruktioner for AI
├── data/
│   ├── finansiellt/
│   │   ├── arsredovisning-2023.pdf
│   │   ├── arsredovisning-2024.pdf
│   │   └── kvartalsdata-2024.csv
│   ├── marknad/
│   │   ├── branschrapport-hr-tech-2024.pdf
│   │   └── konkurrentoversikt.md
│   └── operativt/
│       ├── kpi-dashboard-2024.csv
│       └── organisationsstruktur.md
├── analys/
│   ├── kassaflode/
│   ├── vardering/
│   └── scenarioanalys/
├── output/
│   ├── rapporter/
│   ├── presentationer/
│   └── memos/
├── mallar/
│   ├── investment-memo-mall.md
│   └── kvartalsrapport-mall.md
└── .claude/
    └── skills/
        ├── kassaflodesanalys.md
        └── investment-memo.md
```

**Principerna bakom strukturen:**

1. **Separera radata fran analys** — `data/` ar det du har fatt, `analys/` ar det du skapat
2. **Separera analys fran output** — `analys/` ar arbetsunderlag, `output/` ar det som skickas vidare
3. **Beskrivande filnamn** — datum, typ och format framgar av namnet
4. **Mallar for atervandning** — spara bra format sa slipper du borja fran noll

> For en grundlig genomgang av mappstruktur och CLAUDE.md, se **kapitel 06**.

---

## MCP-servrar (Model Context Protocol)

For den som vill ga annu langre finns nagot som kallas **MCP-servrar**. Det ar utokningar som ger Claude Code tillgang till externa verktyg och datakallor.

**Exempel pa vad MCP kan gora:**

- **Filesystem-server** — ger Claude tillgang till filer utanfor den aktuella mappen
- **GitHub-server** — later Claude arbeta direkt mot kodforvar och versionskontroll
- **Databasserver** — Claude kan stalla fragor mot databaser

**For vem ar det?** MCP ar framst for avancerade anvandare och tekniska team. Om du just har borjat med Claude Code, parkera det har och kom tillbaka till det langre fram.

Det viktiga att veta: Claude Code ar designat for att vaxa med dig. Du kan borja enkelt och lagga till mer kapacitet efterhand.

---

## Praktiska tips

### For dig som precis borjar

1. **Borja med filorganisering.** Anvand Claude Code for att sortera och strukturera dina filer. Det ar ett bra satt att lara sig verktyget utan risk.

2. **Skriv en CLAUDE.md.** Even en enkel version med projektbeskrivning och nagra regler gor enorm skillnad. Det ar den enskilt basta investeringen du kan gora.

3. **Testa med en riktig uppgift.** Ta nagot du brukar gora manuellt — till exempel sammanfatta en rapport eller jamfora tva kvartal — och lat Claude gora det.

### For dig som vill bli effektivare

4. **Spara bra prompts som skills.** Nar du hittar ett satt att formulera en uppgift som ger bra resultat, spara det som en skill sa slipper du skriva om det varje gang.

5. **Anvand `/compact` regelbundet.** Nar du marker att Claude borjar ge svar som inte riktigt hanger ihop med det ni pratade om tidigare, kor `/compact` for att frigora kontext.

6. **Iterera med Claude.** Det basta med Code jamfort med Chat ar att ni kan arbeta fram och tillbaka. "Bra, men andrar tonen till mer formell. Och lagg till en tabell." Claude gor andringen direkt i filen.

7. **Anvand projekttrad.** Nar du startar en session, be Claude lista filstrukturen forst: "Visa mig alla filer i det har projektet." Det satter kontexten for bade dig och Claude.

### Vanliga misstag att undvika

- **For vaga instruktioner.** "Gor en analys" ar for vagt. "Analysera kassaflodet for 2022-2024 baserat pa data i data/finansiellt/ och presentera som tabell" ar bra.
- **Att inte anvanda CLAUDE.md.** Utan instruktionsfil maste du upprepa samma saker i varje session.
- **Att glomma var du star.** Claude Code arbetar i den mapp du startar det i. Dubbelkolla att du ar i ratt mapp innan du borjar.

---

## Sammanfattning

| Begrepp | Vad det ar |
|---------|-----------|
| Claude Code | CLI-verktyg som later Claude arbeta direkt med dina filer |
| CLAUDE.md | Instruktionsfil som Claude laser automatiskt |
| Skills | Egna kommandon for ateranvandbara arbetsfloden |
| `/compact` | Sammanfattar konversationen for att spara kontext |
| MCP | Utokningar for att koppla Claude till externa verktyg |

---

## Nasta steg

Nu nar du forstar hur Claude Code fungerar och hur du strukturerar ditt arbete ar det dags att titta pa nasta niva: **Claude Cowork** — en autonom AI-agent som kan arbeta sjalvstandigt med langre uppgifter medan du gor annat.

**Fortsatt till [Kapitel 05 — Claude Cowork: Autonom AI-agent](05-claude-cowork.md)**
