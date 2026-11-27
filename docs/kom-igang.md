# Kom igång

> *Du läser inte guiden först. Du klistrar in en prompt, och din egen Claude sätter upp ditt arbetssätt tillsammans med dig. Guiden finns sedan här när du vill förstå varför.*

!!! abstract "Kort version"
    - Klistra in prompten nedan i en helt ny chatt, utanför alla projekt.
    - Chatten är en setup-session och används bara till att sätta upp ditt upplägg, inte till att jobba med dina uppgifter.
    - Claude frågar hur du arbetar i dag, vilka projekt du har och vad du främst vill få gjort, och anpassar sig efter det.
    - Grunden är projekt. Har du inga skapar du ett för det du främst vill göra. Har du redan projekt börjar ni med det viktigaste, och det utvärderas inifrån.
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

1. **Claude tar reda på var du står.** Först ber den dig öppna Claude-appen för datorn om du har den och skicka versionsnumret och en skärmdump, eftersom appen ser olika ut hos olika användare. Sedan läser den av det den kan själv, till exempel ditt minne, vilka tjänster som är kopplade och om den når din dator. Den frågar vilka projekt du har och vad du främst vill få gjort med Claude just nu, till exempel ett examensarbete.
2. **Claude förklarar vad du lägger grunden till.** Kort om du mest chattar, mer konkret om du redan har projekt. Grunden är projekt med materialet i en form som Claude läser bra och tydliga regler för hur Claude ska arbeta, regler som blir bra först när de justeras med användning.
3. **Du får en prompt till ett projekt.** Har du inga projekt skapar du ett och ger det ett namn, inget mer. Har du redan projekt väljer ni det viktigaste. I båda fallen klistrar du in prompten i en ny chatt i projektet.
4. **Projektet sätts upp inifrån.** Är projektet redan i bruk går Claude först igenom instruktionerna, materialet och hur projektet har använts, och frågar vad som skaver. Sedan tar ni materialet: Claude strukturerar det och skriver om det till Markdown i en egen mapp, utan att röra originalen. Filer du har laddat upp direkt i projektet tas via en mapp på datorn. Vill du nå materialet från mobilen läggs en kopia i molnet. Först därefter skrivs instruktionerna: mål, hur du vill ha hjälp, hur Claude ska hantera det den producerar och om du jobbar med andra.
5. **Du börjar arbeta.** När projektet är uppsatt startar du en ny chatt där och sätter igång.

Räkna med en kvart för setup-sessionen och 10 till 20 minuter för ett nytt projekt. Ett projekt som redan används kan ta längre tid, eftersom det finns mer att gå igenom. Det brukar också ge mer.

Ibland ber Claude dig ta ställning till något och föreslår ett avsnitt i guiden att läsa först. Det är inget måste, men det tar ett par minuter och gör att du förstår vad du väljer och vilket problem det löser.

## Om din app ser annorlunda ut

Claude-appen ser inte likadan ut för alla just nu. Anthropic rullar ut en ny projektvy gradvis, där ett projekt öppnas som en konversation med flikarna Threads och Context till höger. Nya projekt får den först, så ett nytt projekt kan se annorlunda ut än dina gamla. Appen på datorn kan dessutom se annorlunda ut än Claude i webbläsaren. Upplägget är detsamma, men knapparna sitter på olika ställen. Därför börjar setup-sessionen med att be dig öppna appen för datorn, skicka versionsnumret (Claude i menyraden, About Claude) och en skärmdump, och anpassar sedan stegen efter det du ser.

Varje prompt du får för en ny chatt börjar med samma text som prompten under "När du vill bygga vidare" nedan och på startsidan. Den har länken till guiden, så att varje ny chatt vet vad den bygger. [Kapitel 01](01-fran-chatt-till-system.md#projekten-ser-olika-ut-hos-olika-anvandare) förklarar skillnaden.

## Om du redan har ett upplägg

Har du redan flera projekt utgår sessionen från dem. Claude frågar vad de används till och var det skaver, och ger dig en prompt till det viktigaste. Utvärderingen görs sedan inne i projektet, eftersom det är där Claude ser instruktionerna, materialet och hur du har använt det. De andra projekten kan du ta ett i taget med samma prompt. Har du redan något som håller ihop dem, som ett centralt projekt eller ett morgonbrev, byggs det inte om. Jag kan inte lova stora förändringar, men det brukar finnas något att hämta.

## Varför en egen chatt för setupen?

Om du börjar jobba med en uppgift i samma chatt som du sätter upp ditt upplägg i, hamnar allt i en lång chatt utan instruktioner, och det är just det upplägget ska ersätta. Därför används setup-chatten bara till att komma fram till rätt projekt, och det riktiga arbetet görs i nya chattar i projektet. [Kapitel 01](01-fran-chatt-till-system.md#trappan) förklarar skillnaden mellan chatt och projekt, och [kapitel 10](10-anvandningsgransen.md#varfor-langa-chattar-blir-dyra) varför en lång chatt blir både sämre och dyrare än flera korta.

## Efter setupen

Dina projekt blir bättre av att användas och justeras. När du märker att något skaver, starta en ny chatt i det projekt det gäller och klistra in prompten nedan. Gäller det helheten, till exempel ett nytt projekt, en lista eller ett morgonbrev, starta en ny chatt utanför projekt, eller i ett projekt som håller koll på helheten om du har byggt ett.

```text
Jag vill bygga vidare på mitt upplägg. Läs AI-workflowguide på svenska:
https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/llms-full.txt
Guiden beskriver en persons upplägg och är inget facit.
Utgå från hur jag arbetar i dag, fråga var det skaver och föreslå ett nästa steg.
Ställ en fråga i taget.

Det här vill jag göra:
```

Samma prompt finns på startsidan, så att du hittar den när du behöver den. Kapitlen i guiden slutar med prompter som du klistrar in i ett av dina projekt för att ta nästa steg. Vill du se hur långt det går att ta, beskriver [kapitel 04](04-arkitekturen.md) och [kapitel 06](06-hjarnan.md) mitt eget upplägg. Det är ett exempel, inget facit.

??? note "Hela instruktionen, om din AI inte kan öppna länken"
    Kopiera allt i rutan och klistra in det i en ny chatt.

    ````text
    --8<-- "setup-session.md"
    ````
