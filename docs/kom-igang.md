# Kom igång

> *Du läser inte guiden först. Du klistrar in en prompt, och din egen Claude sätter upp ditt arbetssätt tillsammans med dig. Guiden finns sedan här när du vill förstå varför.*

!!! abstract "Kort version"
    - Klistra in prompten nedan i en helt ny chatt, utanför alla projekt.
    - Chatten är en setup-session och används bara till att sätta upp ditt upplägg, inte till att jobba med dina uppgifter.
    - Claude frågar hur du arbetar i dag, vad du använder den till och vad du främst vill få gjort, och anpassar sig efter det.
    - Du får två projekt: Hjärnan, som håller koll på helheten och där setup-chatten bor kvar, och ett projekt för det du främst vill göra. Har du redan projekt kan de bli de två.
    - Sedan börjar du arbeta. Du har lagt grunden, och upplägget växer med tiden. Ingen bygger allt i ett svep.

## Prompten

Öppna en ny chatt i Claude (eller ChatGPT), inte inne i något projekt, och klistra in det här:

```text
Det här är en setup-session. Läs och följ instruktionerna här:
https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/setup/setup-session.md

Använd den här chatten bara till att sätta upp mitt arbetssätt, inte till att jobba med mina uppgifter.
```

Om din AI säger att den inte kan öppna länken, fäll ut rutan längst ned och klistra in hela instruktionen i stället.

## Vad som händer

1. **Claude tar reda på var du står.** Den läser av det den kan själv, till exempel ditt minne, vilka tjänster som är kopplade och om den når din dator, och frågar sedan vad du använder Claude till och vilka projekt du har. Den viktigaste frågan är vad du främst vill få gjort med Claude just nu, till exempel ett examensarbete. Det blir ditt fokusprojekt.
2. **Ni sätter upp Hjärnan.** Claude skriver instruktionerna med dig, du skapar projektet och flyttar in chatten dit. Där blir den kvar som din Setup-chatt. Går chatten inte att flytta i din app, ger Claude dig en kort överlämning att klistra in i Hjärnan i stället.
3. **Du skapar fokusprojektet.** Claude ger dig en prompt som du klistrar in i en ny chatt i det projektet. Där gör ni en kort setup för just ditt arbete: mål, material, hur du vill ha hjälp och om du jobbar med andra.
4. **Du börjar arbeta.** När fokusprojektet är uppsatt startar du en ny chatt där och sätter igång.
5. **Du kommer tillbaka när du vill.** Setup-chatten i Hjärnan finns kvar för när du vill utveckla upplägget, till exempel organisera vardagen, ta reda på hur du lär dig bäst eller lägga till fler projekt.

Räkna med 20 till 30 minuter för Hjärnan och 10 till 20 minuter för fokusprojektet. Har du redan många projekt kan det ta längre tid, eftersom ni då också går igenom vad som ska bli kvar, slås ihop eller kopplas till Hjärnan.

Ibland ber Claude dig ta ställning till något och föreslår ett avsnitt i guiden att läsa först. Det är inget måste, men det tar ett par minuter och gör att du förstår vad du väljer och vilket problem det löser.

## Om din app ser annorlunda ut

Claude-appen ser inte likadan ut för alla just nu. Anthropic rullar ut en ny projektvy gradvis, där ett projekt öppnas som en konversation med flikarna Threads och Context till höger. Har du fått den ser projekten annorlunda ut än i guidens beskrivningar, men upplägget är detsamma. Setup-sessionen frågar tidigt vilken vy du har, gärna med en skärmdump, och anpassar stegen efter den. [Kapitel 01](01-fran-chatt-till-system.md#projekten-ser-olika-ut-hos-olika-anvandare) förklarar skillnaden.

## Om du redan har ett upplägg

Har du redan flera projekt utgår sessionen från dem. Ni tar reda på om något av dem kan bli Hjärnan, om några mindre projekt hellre hör hemma i den och hur de projekt som blir kvar ska hänga ihop med den. Har du redan något som motsvarar Hjärnan blir sessionen mer av en utvärdering: Claude går igenom ditt upplägg och föreslår det som går att förbättra. Jag kan inte lova stora förändringar, men det brukar finnas något att hämta.

## Varför en egen chatt för setupen?

Om du börjar jobba med en uppgift i samma chatt som du sätter upp ditt upplägg i, hamnar allt i en lång chatt utan instruktioner, och det är just det upplägget ska ersätta. Därför blir det två projekt, setupen flyttas in i Hjärnan när den är klar, och det riktiga arbetet görs i nya chattar i fokusprojektet. [Kapitel 01](01-fran-chatt-till-system.md#trappan) förklarar skillnaden mellan chatt och projekt, och [kapitel 10](10-anvandningsgransen.md#varfor-langa-chattar-blir-dyra) varför en lång chatt blir både sämre och dyrare än flera korta.

## Efter setupen

Hjärnan och dina projekt blir bättre av att användas. När du märker att något skaver, gå tillbaka till Setup-chatten i Hjärnan, eller starta en ny chatt där och klistra in prompten nedan.

```text
Jag vill bygga vidare på mitt upplägg. Läs AI-workflowguide på svenska:
https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/llms-full.txt
Guiden beskriver en persons upplägg och är inget facit.
Utgå från hur jag arbetar i dag, fråga var det skaver och föreslå ett nästa steg.
Ställ en fråga i taget.

Det här vill jag göra:
```

Samma prompt finns på startsidan, så att du hittar den när du behöver den. Kapitlen i guiden slutar med prompter som du klistrar in i ett av dina projekt för att ta nästa steg. Vill du se hur långt det går att ta, beskriver [kapitel 04](04-arkitekturen.md) och [kapitel 06](06-hjarnan.md) mitt eget upplägg.

??? note "Hela instruktionen, om din AI inte kan öppna länken"
    Kopiera allt i rutan och klistra in det i en ny chatt.

    ````text
    --8<-- "setup-session.md"
    ````
