# Kapitel 01 — Från chatt till system

*Du chattar redan med AI och får bra svar. Det här kapitlet visar stegen från en vanlig chatt till ett system som minns, följer dina regler och arbetar åt dig medan du gör annat.*

!!! abstract "Kort version"
    - Samma modell ger olika resultat beroende på vilka filer, regler och verktyg den får arbeta med.
    - Trappan går från chatt via projekt och Claude-appen på datorn till Claude Code, och varje steg lägger till något nytt.
    - Rollerna är olika: chatten för svar och diskussion, Claude Code för att bygga och ändra saker i en mapp. Hos mig är chatten där jag är mest, och Claude Code används för att utveckla systemet, inte för att plugga.
    - Samma funktioner finns under olika namn hos Claude och ChatGPT, så upplägget går att flytta mellan dem.
    - Du behöver inte ta alla steg, utan väljer det steg som löser ditt nuvarande problem.

---

## Samma modell, olika förutsättningar

När du öppnar Claude eller ChatGPT pratar du med en modell från ett av de stora labben. Modellen är densamma för alla som betalar för samma plan. Ändå får en person ut mycket mer av den än en annan, och skillnaden ligger nästan alltid i vad modellen får att arbeta med: vilka filer den ser, vilka regler den följer, vilka verktyg den får använda.

Det här kapitlet går igenom byggstenarna, i den ordning de blir användbara. Exemplen kommer från mina kurser, men plugget är bara ett fall. Samma steg fungerar i ett jobb, i en hobby eller när du ska hålla ordning på vardagen.

## Problemet du redan känner till

Tre saker gnager när du bara chattar. Du upprepar dig: vem du är, hur du vill ha svaret, vad som gäller. Varje samtal börjar från noll, så det du lade en timme på igår är borta idag. Och du kopierar material fram och tillbaka mellan dokument och chattfönster.

Det är inget fel på dina prompter. Det är arbetsflödet som saknar något, och det kan byggas.

## Trappan

Verktygen kan ses som fyra steg. Varje steg löser en begränsning i det förra. Du behöver inte ta alla, men det hjälper att veta vilka som finns.

```
  Chatt  ->  Projekt  ->  Claude-appen på datorn  ->  Claude Code
  (flyktig)  (delad       (lokala mappar,             (full kontroll,
             kontext)     schemalagda uppgifter)      regelfiler, skills)
```

### Steg 1: Chatten

Du skriver, du får svar. Kontexten är konversationen och de filer du laddat upp, och den finns bara i just det samtalet. Det räcker för en snabb fråga eller ett bollplank. Det är här jag är mest av tiden, till exempel när jag pluggar: jag ber om en förklaring, ställer följdfrågor och bollar fram och tillbaka tills jag förstår, helst inne i ett projekt (nästa steg). Claude och ChatGPT har dessutom ett minne som sparar saker mellan samtal, vilket kapitel 02 går igenom, men det är en sammanfattning som modellen själv väljer, inte något du styr fullt ut.

### Steg 2: Projekt

Ett projekt är ett arbetsrum med egna instruktioner och egna filer, där alla samtal delar samma utgångsläge. Claude har projekt på alla planer, även gratisplanen, där man kan ha upp till fem. ChatGPT har också projekt, och dessutom Custom GPTs om du vill paketera instruktioner och filer som en egen assistent.

??? begrepp "Begrepp: Projekt"
    --8<-- "projekt.md"

    [Se alla begrepp i ordlistan](ordlista.md#projekt)

Jag har ett projekt per kurs. Projektinstruktionerna är en kort version av reglerna jag vill att Claude följer, och kursmaterialet ligger i projektets kontext (rutan Kontext på projektsidan, Project knowledge på engelska). Det går att lägga till filer direkt, och i mitt fall kopplar jag in ett GitHub-repo med kursens material så att projektet ser ändringarna jag gör. Hur det hänger ihop går vi igenom i kapitel 03 och 04.

En chatt kan flyttas in i ett projekt i efterhand, via menyn vid chattens namn. Det är så setup-sessionen på sidan [Kom igång](kom-igang.md) slutar: du skapar projektet och flyttar dit chatten där det planerades.

Projekt är ett bra mellansteg när du har ett avgränsat uppdrag och vill slippa upprepa dig. Gränsen går där du vill att Claude ska skriva tillbaka till filer, köra något på egen hand eller arbeta utan att du sitter där.

### Steg 3: Claude-appen på datorn

Claude finns som app för datorn, och där får du något som webbläsaren inte ger. Du kan koppla lokala mappar, och Claude kan då läsa och skriva filer i just de mapparna och inga andra. Du kan ge ett längre uppdrag och låta Claude arbeta medan du är borta. Du kan också skapa schemalagda uppgifter, som körs i molnet utan att din dator är påslagen. Funktionerna kräver en betalplan.

Den här delen av appen hette tidigare Cowork. Anthropic släppte Cowork som förhandsversion i januari 2026, och enligt min bedömning var tanken att ge den som inte vill använda en terminal det som Claude Code kan. Sedan september 2026 är Cowork inte längre en separat produkt utan en del av Claude-appen. Resonemanget om tröskeln står i [kapitel 09](09-troskeln.md).

??? begrepp "Begrepp: Schemalagd uppgift"
    --8<-- "schemalagd-uppgift.md"

    [Se alla begrepp i ordlistan](ordlista.md#schemalagd-uppgift)

Jag använder schemalagda uppgifter för tre saker: ett morgonbrev som sammanfattar läget, en kort koll på eftermiddagen och en nattlig synk av ett hobbyprojekt. De läser dokument och kalender och skickar ett meddelande. Kapitel 06 visar hur det är uppbyggt.

Här gäller samma regel som för allt Claude levererar: läs resultatet som ett utkast från en snabb medarbetare. Tydliga uppdrag ger bättre resultat än vaga, och det är värt att vara noga med vad som får ändras och vad som bara får läsas.

ChatGPT har motsvarigheter: ett agentläge som kan utföra uppgifter åt dig, och Tasks för uppgifter som körs vid bestämda tider. Vilka som ingår i vilken plan ändras, så titta på [chatgpt.com/pricing](https://chatgpt.com/pricing).

### Steg 4: Claude Code

Claude Code är det mest kraftfulla steget. Du ger Claude tillgång till en mapp på din dator, styr den med text, och den kan skapa, ändra och köra saker direkt i mappen. I min egen setup använder jag den för att utveckla systemet: bygga repon, skript och regler. Jag pluggar inte i den, det gör jag i chatten. Den kan läsa hela mappstrukturen, skapa och redigera filer, köra skript och följa regler som du skrivit ned i en fil.

??? begrepp "Begrepp: Claude Code"
    --8<-- "claude-code.md"

    [Se alla begrepp i ordlistan](ordlista.md#claude-code)

Du behöver inte kunna programmera. Du beskriver vad du vill ha, och Claude Code skapar mappar, regelfiler och skript. Ett bra sätt att börja är att först prata ut ditt projekt i en vanlig chatt, tills du har en tydlig bild, och sedan be chatten sammanfatta det som en färdig beskrivning som du klistrar in i Claude Code. Det enda du gör för hand är att skapa en tom mapp.

Regelfilen heter CLAUDE.md och läses i början av varje session. Den är skillnaden mellan en assistent som börjar om varje dag och en som känner projektet. Dessutom kan du lägga upp återanvändbara arbetssätt som skills, och även det tar kapitel 03 upp.

OpenAI har en motsvarighet som heter Codex, med regelfilen AGENTS.md.

??? begrepp "Begrepp: Codex"
    --8<-- "codex.md"

    [Se alla begrepp i ordlistan](ordlista.md#codex)

Jag började faktiskt med Codex och bytte senare till Claude Code. Jag kan inte säga att den ena är bäst, och landskapet ändras ofta. Jag använder Claude som huvudspår här eftersom det är det jag kan bäst, och för att jag kan lägga mina GitHub-repon i ett Claude-projekts kontext, vilket gör att kursprojektet alltid ser senaste versionen.

## Samma ting under olika namn

| Det du vill ha | Claude | ChatGPT |
|---|---|---|
| Samlad kontext för ett uppdrag | Projekt | Projekt, Custom GPTs |
| Minne mellan samtal | Minne och sökning i tidigare chattar | Minne |
| Regelfil i en mapp | CLAUDE.md | AGENTS.md |
| Agent som arbetar med kod och filer | Claude Code | Codex |
| Uppgifter vid bestämda tider | Schemalagda uppgifter | Tasks |
| Återanvändbara arbetssätt | Skills | Custom GPTs |

Tabellen är en förenkling. Funktionerna är inte identiska, men de löser samma problem, och det du lär dig av ett verktyg går att överföra till det andra.

## Planer och priser

Priser och gränser ändras ofta, så läs alltid av leverantörens egen sida innan du bestämmer dig. Det här är läget när guiden skrevs.

Claude har en gratisplan med begränsad användning. Pro kostar 20 dollar i månaden, eller 17 dollar i månaden om du betalar för ett år i förväg, och ger mer användning, Claude Code och fler modeller. Max börjar på 100 dollar i månaden och ger fem gånger så mycket användning som Pro. Källa: [claude.com/pricing](https://claude.com/pricing). Anthropic har ingen egen studentrabatt på prissidan, men ditt lärosäte kan ha ett avtal, så fråga.

ChatGPT har också en gratisnivå och flera betalnivåer, med bland annat Plus och Pro, där de högre nivåerna ger mer av agentläge, Codex och djup research. Exakta priser står på [chatgpt.com/pricing](https://chatgpt.com/pricing).

Min egen bedömning är att Claude Pro räcker långt för det som beskrivs i guiden. Du kan börja på gratisplanen med projekt och chatt och uppgradera när du märker att du vill ha lokala mappar, schemalagda uppgifter eller Claude Code.

## Vilket steg ska du välja?

Börja där ditt problem finns. Vet du inte var, låt setup-sessionen på sidan [Kom igång](kom-igang.md) ta reda på det tillsammans med dig. Om du upprepar dig, skapa ett projekt. Om du vill att Claude ska arbeta direkt med filer på din dator, prova appen eller Claude Code. Om du vill att något ska ske utan att du ber om det, skapa en schemalagd uppgift.

Det viktigaste i kapitlet är att modellen inte blir smartare på vägen uppför trappan. Det som förändras är vad den har att jobba med: egna filer, egna regler, egna rutiner. Nästa kapitel handlar om hur du ger den det på bästa sätt.

---

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny chatt i ditt Hjärnan-projekt, eller i det projekt som kapitlet gäller. Har du inget projekt än, börja med [setup-sessionen](kom-igang.md).

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/01-fran-chatt-till-system.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Utgå från det du redan vet om mig i det här projektet och fråga bara om det som saknas.
    Fråga vad jag använder AI till idag och vad som skaver mest.
    Hjälp mig sedan att välja vilket steg i trappan som passar mig och att ta det första konkreta steget i min egen vardag.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 02: Kontext i stället för långa prompter](02-kontext.md)
