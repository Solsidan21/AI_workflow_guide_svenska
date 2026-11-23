# Kapitel 03 — Struktur som kontext

*Du kan ge en modell hela kursboken och ändå få generiska svar. Skillnaden ligger oftare i hur materialet är ordnat än i hur mycket det är.*

!!! abstract "Kort version"
    - Hur materialet är ordnat spelar ofta större roll än hur mycket material modellen får.
    - Namn och mappar fungerar som instruktioner, så en tydlig mappstruktur ger bättre svar.
    - Dokument i Markdown är lättare för modellen att läsa än PDF:er.
    - En CLAUDE.md eller motsvarande regelfil följer med mappen och styr hur Claude arbetar.
    - Skills låter dig beskriva en återkommande uppgift en gång och återanvända den.

Det här kapitlet handlar om det som gör ett eget system värt att bygga: ordning. Jag använder en kursmapp som exempel, men samma tänk fungerar för en projektmapp på jobbet, en hobby eller en flytt. Där det finns material och återkommande uppgifter lönar sig struktur.

## Mer material ger inte automatiskt bättre svar

De flesta som börjar använda AI på allvar gör likadant. De laddar upp filer, skriver några rader instruktioner och lägger till mer material när svaren känns tunna. Det hjälper till en punkt, sedan planar det ut.

Modellen är redan tillräckligt smart för att förstå materialet. Den vet bara inte var den ska titta. Tänk dig en kompetent konsult som får 200 osorterade sidor och fem minuter. Hälften av tiden går åt till att sortera i stället för att tänka.

Två studenter inför en tenta visar skillnaden. Den ena har alla utskrivna föreläsningar och hela kursboken i en hög. Den andra har en pärm med flikar, en sammanfattning per kapitel och en innehållsförteckning. De har samma information, men den andra hittar svaret på tio sekunder.

Det jag har lärt mig sammanfattas så här: navigerbar kontext tillsammans med regler slår maxad kontext. Du gör inte modellen smartare. Du låter den använda det den kan.

## Namn och mappar är instruktioner

När Claude arbetar i en mapp ser den inte bara filernas innehåll. Den ser också filnamn, mappnamn och hur allt hänger ihop. Det är kontext som du inte behöver skriva i någon prompt.

Jämför `07_fulltext/kap_13/13.5.md` med `dokument/fil3.pdf`. Det första säger vad filen är, vilket kapitel och vilket avsnitt. Det andra tvingar dig att förklara allt, varje gång.

Några vanor som gör skillnad:

- Beskrivande namn. Skulle en kurskamrat förstå vad filen innehåller utifrån namnet?
- En logisk hierarki. Bryt ut undermappar när en mapp får fler än tio till femton filer.
- Samma mönster överallt, till exempel små bokstäver med bindestreck och datum som ÅÅÅÅ-MM-DD.
- Material du fått, material du gjort och färdiga leveranser i separata mappar, så att du alltid kan gå tillbaka till originalet.
- En kort README i mappar där det inte är självklart vad som ligger.

Du behöver inte skapa det här för hand. Beskriv vad du behöver, så bygger Claude Code strukturen åt dig. Kunskapen du behöver är varför den ser ut som den gör, så att du kan styra.

## Exempel: en kursmapp

Så här ser skelettet ut i mitt repo för en av mattekurserna. Alla mina kurser har samma upplägg, och du kan titta på det i det [offentliga repot för Flervariabelanalys](https://github.com/Solsidan21/Flervariabelanalys_ht26).

```
flervariabelanalys/
├── CLAUDE.md
├── 00_index/            översikt och uppgiftsindex
├── 01_kursmaterial/     kursplan, kapitelguide
├── 02_forelasningar/
├── 04_studieplan/       veckoplan
├── 05_tentor/           gamla tentor och lösningsförslag
├── 06_bokinnehall/      en sammanfattning per kapitel
├── 07_fulltext/         boken som Markdown, en fil per avsnitt
└── scripts/             skript som bygger index och kontrollerar täckning
```

Numreringen gör att mapparna hamnar i samma ordning överallt, och jag ser direkt var något ska ligga. Samma skelett i varje kurs betyder att Claude hittar rätt även i en kurs jag precis har startat. På jobbet vore motsvarigheten en mapp per kund eller per projekt med samma fasta delar.

## Från PDF till Markdown

Kursmaterial kommer oftast som PDF. Det är det sämsta formatet att ge en modell. En PDF är tung att läsa in, tabeller och formler tolkas ofta fel, och du betalar samma pris varje gång filen används.

??? begrepp "Begrepp: Token"
    --8<-- "token.md"

    [Se alla begrepp i ordlistan](ordlista.md#token)

Lösningen är att bearbeta dokumentet en gång och spara resultatet som Markdown.

??? begrepp "Begrepp: Markdown"
    --8<-- "markdown.md"

    [Se alla begrepp i ordlistan](ordlista.md#markdown)

Flödet har fyra steg:

1. Samla. Lägg originalen i en mapp. Behåll alltid PDF:en, den är din källa.
2. Extrahera. Be Claude Code läsa PDF:en och skriva den som Markdown, uppdelad i filer som följer materialets egen struktur.
3. Publicera. Lägg mappen i ett Git-repo och skicka det till GitHub.
4. Koppla. Lägg repot som kunskap i ett Claude-projekt.

??? begrepp "Begrepp: GitHub"
    --8<-- "github.md"

    [Se alla begrepp i ordlistan](ordlista.md#github)

Skillnaden märks tydligt. Hela kursboken som PDF kostar tusentals tokens för varje inläsning och modellen får leta själv. Som Markdown, en fil per avsnitt, läser den precis det avsnitt som frågan gäller och kostar en bråkdel. Dessutom går det att länka rakt in i texten. I mitt upplägg har varje definition och övning en egen rubrik, så att jag kan peka på ett exakt ställe. Hur jag använder det för att lära mig tar jag upp i [kapitel 05](05-individanpassad-inlarning.md).

Extraktionen är den del som är lätt att göra slarvigt. Min regel är att ingen definition eller sats får saknas, och jag har skript som kontrollerar täckningen. En tidig lärdom var att sidgränser kan tappa innehåll, så texten delas efter avsnitt och inte efter sida.

När du till slut behöver ett Word-dokument eller en PDF kan du arbeta i Markdown hela vägen och be Claude Code konvertera i sista steget, till exempel med verktyget pandoc. Arbetsformatet och leveransformatet behöver inte vara samma.

## CLAUDE.md: reglerna som följer med mappen

En mapp med bra struktur är en bra start, men modellen vet fortfarande inte hur du vill arbeta. Det är reglerfilens uppgift.

??? begrepp "Begrepp: CLAUDE.md"
    --8<-- "claude-md.md"

    [Se alla begrepp i ordlistan](ordlista.md#claude-md)

Filen ligger i projektets rot, och Claude Code skriver den gärna åt dig om du beskriver projektet. En bra fil har fyra delar: vad projektet är, vilka regler som gäller för format och språk, var saker ligger och hur återkommande uppgifter ska göras.

Ett utdrag ur en kursfil kan se ut så här:

```markdown
# CLAUDE.md

## Så här arbetar vi
- Visa fullständiga steg, inte bara svar.
- Motivera varje steg och definiera varje ny symbol.
- Läs teorin i 07_fulltext/ innan en uppgift löses.

## Var saker ligger
- 00_index/uppgiftsindex.md: vilken uppgift som finns var
- 05_tentor/: gamla tentor och lösningsförslag
```

Reglerna är kursspecifika, men formen går att kopiera. Ett projekt på jobbet skulle ha regler om språk, tonläge, hur siffror skrivs och vilka mallar som gäller.

OpenAI har en motsvarighet för sin kodagent Codex. Den heter AGENTS.md och är också en vanlig textfil i repot som agenten läser före arbetet. Idén är densamma, så en tydligt skriven regelfil går att flytta mellan verktygen.

### Flera nivåer

Du kan ha en CLAUDE.md i flera mappar. Den i roten gäller allt arbete. En fil i en undermapp gäller dessutom när Claude arbetar där, och du behöver bara skriva det som är specifikt för just den mappen. Som tumregel gäller att det som alltid ska gälla hör hemma i roten, det som bara gäller en typ av arbete hör hemma i en undermapp, och det som gäller en enskild uppgift passar bättre som en skill.

I Claude-projekten i appen finns ingen fil att lägga i mappen. Där fungerar projektinstruktionerna som motsvarighet. Jag håller dem som en kortversion av CLAUDE.md i repot, så att de viktigaste reglerna gäller direkt.

## Skills: uppgifter som du bara beskriver en gång

Vissa uppgifter återkommer. Att förklara ett begrepp i ett fast format, att gå igenom en gammal tenta eller att sammanfatta ett kapitel är exempel. Utan hjälp skriver du om instruktionen varje gång, och den blir lite annorlunda varje gång.

??? begrepp "Begrepp: Skill"
    --8<-- "skill.md"

    [Se alla begrepp i ordlistan](ordlista.md#skill)

En skill är alltså en mapp, till exempel `.claude/skills/forklara/`, med en fil `SKILL.md` i. Överst står ett namn och en kort beskrivning av när skillen ska användas. Därunder står stegen:

```markdown
---
name: forklara
description: Förklara ett begrepp utifrån varför det gäller, med en konkret bild.
---

1. Fråga vilket begrepp det gäller, om det inte är angivet.
2. Slå upp definitionen i 07_fulltext/ och ange avsnittet.
3. Förklara varför definitionen ser ut som den gör.
4. Ge en konkret bild och ett litet exempel.
```

Du kan skriva en skill själv, men det går snabbare att be Claude Code skapa den utifrån en beskrivning av vad du vill ha. Granska den sedan, eftersom det är du som vet hur resultatet ska se ut.

## Hur du kommer igång

Börja i en vanlig chatt och beskriv vad du arbetar med och vad du vill kunna göra. Be sedan chatten formulera en prompt som du kan ge till Claude Code, med mappstruktur, en första CLAUDE.md och en eller två skills. Skapa en tom mapp, starta Claude Code i den och klistra in prompten. Lägg in dina dokument, be Claude Code göra Markdown av dem och bygg ut över tid. Varje gång du märker att du förklarar samma sak två gånger är det ett tecken på att regeln ska in i en CLAUDE.md eller en skill.

Det viktigaste är inte att strukturen är perfekt från början. Den ska vara tillräckligt tydlig för att Claude ska hitta rätt, och den kan förbättras medan du använder den. I repots [`templates/`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates/)-mapp finns färdiga mallar för olika roller som du kan ge Claude Code som utgångspunkt.

Struktur är det som gör att en vanlig prenumeration börjar fungera som ett eget system. Nästa steg är att se hur flera sådana mappar hänger ihop.

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/03-struktur.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Fråga vilket område jag arbetar med mest och hur mitt material ser ut i dag.
    Hjälp mig sedan att föreslå en enkel mappstruktur och skriva ett första utkast till en regelfil för just det området.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 04: Arkitekturen](04-arkitekturen.md)
