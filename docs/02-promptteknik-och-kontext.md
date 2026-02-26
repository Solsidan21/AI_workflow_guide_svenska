# Kapitel 02 — Promptteknik och kontext

> *Skillnaden mellan ett okej svar och ett briljant svar handlar sällan om prompten — det handlar om kontexten runtomkring.*

Du vet redan hur man skriver en prompt. Det här kapitlet handlar om allt det andra: vad kontext egentligen är, varför det avgör kvaliteten på svaren, och vilka tekniker som gör störst skillnad i praktiken.

Promptteknik handlar inte bara om att formulera frågor i en chatt. Det handlar om att kunna **beskriva vad du vill ha** — tillräckligt tydligt för att Claude Code ska kunna bygga det åt dig. Samma tekniker som gör en chattfråga bättre gör också en projektbeskrivning bättre.

---

## Vad är kontext — och varför det avgör allt

När Claude svarar på en fråga baseras svaret på **all information som finns tillgänglig** i det ögonblicket:

- Din aktuella prompt
- Hela konversationshistoriken
- Uppladdade filer
- Projektinstruktioner (om du använder Projects)
- CLAUDE.md och skills (om du använder Claude Code)

Allt detta kallas **kontext**. Och det är kontexten — inte bara prompten — som avgör kvaliteten på svaret.

**Analogi:** Tänk dig att du ber en konsult analysera ett bolag. Om du bara säger "analysera bolaget" får du ett generiskt svar. Men om du ger konsulten årsredovisningen, branschrapporter, en briefing om vad ni letar efter och en mall för hur rapporten ska se ut — då får du ett helt annat resultat. Inte för att konsulten plötsligt blev smartare, utan för att kontexten gav bättre förutsättningar.

---

## Kontextfönstret — AI:ns arbetsminne

### Vad det är

Varje AI-modell har ett **kontextfönster** — en maximal mängd information den kan ha "i huvudet" samtidigt. Det mäts i tokens (du lärde dig om tokens i [kapitel 00](00-grundbegrepp.md)).

**Analogi:** Tänk på kontextfönstret som ett skrivbord. Det rymmer en viss mängd papper. Du kan lägga dit din fråga, konversationshistoriken, uppladdade filer och instruktioner. Men om du lägger dit en hel bokhylla med dokument blir skrivbordet fullt — och en del trillar ner på golvet.

### Vad som händer i praktiken

Moderna modeller som Claude har stora kontextfönster — nog för att hantera långa dokument och komplexa konversationer. Men kontexten är inte oändlig. I en lång konversation kan Claude börja tappa de tidigaste detaljerna. Det är inte ett fel — det är en fysisk begränsning.

**Praktiskt tips:** I Claude Code kan du köra `/compact` för att sammanfatta konversationen hittills och frigöra plats i kontextfönstret. I Claude Chat kan du starta en ny konversation inom samma projekt — projektinstruktionerna och filerna finns kvar, men konversationshistoriken börjar om.

### Varför filformat spelar roll

Inte all information kostar lika mycket kontext. En 50-sidig PDF förbrukar enormt med tokens varje gång den läses — även om du bara behöver tre rader. Samma information i Markdown kostar en bråkdel. Se [PDF-problemet](#pdf-problemet-den-vanligaste-flaskhalsen) nedan och [kapitel 03](03-mappstruktur-och-arbetssatt.md) för hur du löser det.

---

## Prompttekniker som gör skillnad

### 1. Var specifik

**Inte så här:** "Gör en analys av det här bolaget."

**Utan så här:** "Analysera kassaflödet baserat på bifogad årsredovisning. Presentera revenue, EBITDA, capex och fritt kassaflöde i en tabell per år. Kommentera trender i 3–5 meningar."

Specificitet gör att AI:n inte behöver gissa vad du menar. Ju mer du specificerar format, innehåll och struktur, desto närmare ditt förväntade resultat hamnar svaret.

### 2. Ge kontext

Berätta inte bara *vad* du vill ha — berätta *varför* och *för vem*.

**Utan kontext:** "Sammanfatta den här rapporten."

**Med kontext:** "Sammanfatta den här rapporten i 5 punkter för en styrelseledamot som behöver förstå de viktigaste riskerna. Fokusera på finansiella avvikelser och operativa utmaningar."

Kontexten styr tonläget, detaljnivån och vinkeln.

### 3. Be om steg-för-steg

För komplexa uppgifter, be AI:n arbeta steg för steg:

"Analysera det här bolagets finansiella utveckling:
1. Sammanfatta nyckeltal (revenue, EBITDA, nettoresultat) per år
2. Beräkna tillväxttakt (CAGR) över perioden
3. Identifiera de tre viktigaste trenderna
4. Ge en bedömning av finansiell hälsa"

Steg-för-steg-instruktioner minskar risken att AI:n hoppar över delmoment eller blandar ihop resultat.

### 4. Iterera

Det bästa sättet att arbeta med AI är **iterativt**. Börja brett, förfina, rikta om.

```
Du: "Sammanfatta årsredovisningen."
Claude: [Sammanfattning]
Du: "Bra, men fokusera mer på kassaflödet. Lägg till en tabell."
Claude: [Uppdaterad sammanfattning med tabell]
Du: "Perfekt. Lägg till en kort risksektion."
Claude: [Slutgiltig version]
```

Tre korta iterationer ger ofta bättre resultat än en lång, perfekt formulerad prompt.

### 5. Berätta vad du INTE vill ha

AI:n kan vara för hjälpsam — den lägger till information, gör antaganden eller skriver i en ton du inte bad om. Negativa instruktioner hjälper:

- "Spekulera inte — om data saknas, ange det tydligt"
- "Inga buzzwords eller säljspråk"
- "Inkludera inte information som inte finns i de bifogade filerna"
- "Max 500 ord"

### 6. Ge exempel

Om du vill ha ett specifikt format, visa ett exempel:

"Sammanfatta varje bolag enligt detta format:

**Bolagsnamn** — Kort beskrivning (1 mening)
- Omsättning: X MSEK
- Tillväxt: X%
- Noterbart: [En viktig observation]"

Exempel kommunicerar format snabbare och tydligare än långa beskrivningar.

---

## Från chatt till Code — promptteknik i praktiken

Alla teknikerna ovan fungerar utmärkt i en vanlig AI-chatt. Men de blir ännu kraftfullare när du använder dem för att **beskriva ett helt projekt** för Claude Code.

Workflowet ser ut så här:

1. **Börja i chatten.** Öppna Claude Chat (eller ChatGPT, Gemini) och beskriv vad du vill skapa. Använd teknikerna ovan — var specifik, ge kontext, ge exempel.
2. **Iterera.** Diskutera med chatten. Förfina din bild av projektet, strukturen och reglerna.
3. **Be om en terminalredo prompt.** När bilden är tydlig, be chatten sammanfatta allt som en prompt du kan ge till Claude Code.
4. **Ge prompten till Claude Code.** Claude Code bygger hela strukturen — mappar, CLAUDE.md, skills — baserat på din beskrivning.

Det här är kärnan i guiden: **du beskriver, Claude bygger.** Och ju bättre du är på att beskriva — med kontext, specificitet och struktur — desto bättre blir resultatet.

---

## Projekt — persistent kunskap i chatten

Claude Projects (och ChatGPT Custom GPTs) löser ett av chattens största problem: att varje session börjar från noll.

### Vad det är

Ett projekt i Claude Chat är en arbetsyta med:

- **Projektinstruktioner** — regler och kontext som gäller för alla konversationer inom projektet
- **Projektkunskap** — uppladdade filer som Claude kan referera till
- **Flera konversationer** — du kan starta nya chattar utan att förlora kontext

### Hur du tänker kring det

Skapa ett projekt per avgränsad arbetskontext. Exempel:

- "Kvartalsrapportering — Bolag X" med årsredovisningar och rapportmallar
- "Marknadskartläggning — Norden" med branschrapporter
- "Kursmaterial — Finansiell analys" med kursböcker och föreläsningsanteckningar

### Projektinstruktioner — chattens version av CLAUDE.md

Skriv projektinstruktioner som ger Claude rätt kontext från start:

```
Du analyserar finansiell data för bolag X, ett svenskt SaaS-bolag.
Svara alltid på svenska. Siffror i MSEK med en decimal.
Börja alltid med en sammanfattning i 3–5 punkter.
Fokusera på: revenue, EBITDA, kassaflöde och tillväxt.
```

Med bra projektinstruktioner slipper du upprepa samma kontext i varje ny konversation.

---

## Filhantering — vad fungerar och hur du tänker

### Vilka filtyper fungerar?

Claude kan arbeta med de flesta vanliga filtyper:

| Filtyp | Fungerar i Chat | Fungerar i Code | Kommentar |
|--------|----------------|----------------|-----------|
| **PDF** | Ja | Ja | Bra men kontextkrävande |
| **Word (.docx)** | Ja | Ja | God texttolkning |
| **Excel (.xlsx, .csv)** | Ja | Ja | CSV är mest effektivt |
| **Bilder (.png, .jpg)** | Ja | Ja | Claude kan läsa och tolka bilder |
| **Markdown (.md)** | Ja | Ja | Det mest effektiva formatet |
| **Text (.txt)** | Ja | Ja | Ren text, inga formateringsproblem |
| **PowerPoint (.pptx)** | Ja | Ja | Textinnehåll extraheras |
| **Kod** | Ja | Ja | Alla vanliga programmeringsspråk |

---

## PDF-problemet — den vanligaste flaskhalsen

De flesta kunskapsarbetare har sina viktigaste dokument som PDF:er — årsredovisningar, rapporter, kursböcker, avtal. Och PDF:er fungerar i alla AI-verktyg. Så vad är problemet?

PDF:er är byggda för människor att läsa på skärm. De är **inte byggda för AI att arbeta med.** Tre saker gör dem problematiska:

**1. AI:n måste tolka hela dokumentet.** Den kan inte "bläddra" till rätt sida — den processar allt från framsida till appendix, varje gång.

**2. Det förbrukar enormt med kontext.** En 50-sidig årsredovisning äter tusentals tokens varje gång den läses in. Samma information i Markdown kostar en bråkdel.

**3. Formatering tolkas ofta fel.** Tabeller, kolumner och sidbrytningar i PDF:er översätts dåligt till text. Siffror hamnar i fel kolumn. Formler försvinner.

| Format | Kontextkostnad | Precision |
|--------|---------------|-----------|
| **Markdown** | Låg — ren text, minimal overhead | Hög — AI läser exakt det som står |
| **CSV** | Låg — strukturerad data | Hög — tydliga kolumner och rader |
| **PDF** | Hög — AI måste tolka hela dokumentet | Varierande — tabeller kan feltolkas |

**Lösningen** är inte att sluta använda PDF:er — de är ofta det enda formatet du får. Lösningen är att bearbeta dem till Markdown *en gång*, och sedan arbeta mot den bearbetade versionen. Originalet behåller du som källa. Exakt hur du gör det beskrivs i [kapitel 03](03-mappstruktur-och-arbetssatt.md).

---

## Artifacts — Claude skapar saker åt dig

### Vad det är

Artifacts är en funktion i Claude Chat där Claude skapar fristående innehåll som visas i ett eget fönster bredvid konversationen. Det kan vara:

- **Dokument** — rapporter, sammanfattningar, memos
- **Kod** — program, skript, webbsidor
- **Tabeller och diagram** — visualiseringar av data
- **Interaktiva element** — kalkylatorer, enkla verktyg

### När skapas de?

Claude skapar automatiskt en artifact när resultatet är tillräckligt substantiellt och fristående. En kort sammanfattning hamnar i chatten. En hel rapport, en tabell med 20 rader, eller ett kodblock hamnar som artifact.

### Varför det spelar roll

Artifacts gör att du kan:

- Kopiera resultatet enkelt (utan att leta i en lång konversation)
- Iterera på ett specifikt dokument ("Uppdatera artifact:en med en risksektion")
- Ladda ner eller dela resultatet

Du behöver inte be om artifacts — de skapas automatiskt. Men du kan styra formatet genom att be om till exempel "skapa en tabell" eller "skriv ett komplett memo".

---

## Minne — Claude som kommer ihåg

### Vad det är

Claude har en minnesfunktion som låter den komma ihåg saker mellan konversationer. Det är inte samma sak som projektinstruktioner (som du skriver manuellt) — minnet byggs upp automatiskt baserat på saker du berättar.

### Hur det fungerar

Under en konversation kan Claude spara information som du uttryckligen delar:

- "Jag jobbar på en konsultfirma med fokus på energisektorn"
- "Jag föredrar alltid svar på svenska med siffror i MSEK"
- "Jag använder alltid tabellformat för jämförelser"

Denna information finns sedan tillgänglig i framtida konversationer, även utanför projekt.

### Hur du hanterar det

Du kan se och redigera vad Claude kommer ihåg i inställningarna. Det är bra att då och då kontrollera att minnena är korrekta och relevanta.

**Viktigt:** Minne är ett komplement till projektinstruktioner — inte en ersättning. Minnet är personligt och generellt. Projektinstruktioner är specifika för en arbetskontext. Använd båda.

---

## Sammanfattning — så får du bättre svar

| Teknik | Effekt |
|--------|--------|
| **Ge kontext** (vem, varför, för vem) | AI:n förstår uppgiften bättre |
| **Var specifik** (format, struktur, längd) | Resultatet matchar dina förväntningar |
| **Steg-för-steg** | Komplexa uppgifter bryts ner korrekt |
| **Iterera** | Förfina successivt istället för att jaga den perfekta prompten |
| **Negativa instruktioner** | Undvik oönskat innehåll och ton |
| **Exempel** | Format kommuniceras direkt |
| **Projekt/CLAUDE.md** | Kontexten är redan på plats — du slipper upprepa dig |
| **Bearbeta filer** | Markdown istället för PDF sparar tokens och ökar precision |

Det viktigaste att ta med sig: **kontext slår promptkvalitet**. En medioker prompt med utmärkt kontext (rätt filer, bra instruktioner, tydlig mappstruktur) ger nästan alltid ett bättre resultat än en perfekt prompt utan kontext.

---

> *Föregående kapitel: [01 — AI-verktygslandskapet](01-verktygslandskapet.md)*
>
> *Nästa kapitel: [03 — Mappstruktur och arbetssätt](03-mappstruktur-och-arbetssatt.md)*
