# Kom igång

> *Du läser inte guiden först. Du klistrar in en prompt, och din egen Claude sätter upp ditt arbetssätt tillsammans med dig. Guiden finns sedan här när du vill förstå varför.*

!!! abstract "Kort version"
    - Klistra in prompten nedan i en helt ny chatt, utanför alla projekt.
    - Chatten är en setup-session och används bara till att sätta upp ditt upplägg, inte till att jobba med dina uppgifter.
    - Claude frågar hur du arbetar i dag och anpassar sig efter hur van du är.
    - Du skapar ett projekt som blir din "hjärna", med instruktioner som Claude skriver åt dig, och flyttar sedan in chatten dit.
    - Sessionen slutar med ett nästa steg. Upplägget växer med tiden, och ingen bygger allt i ett svep.

## Prompten

Öppna en ny chatt i Claude (eller ChatGPT), inte inne i något projekt, och klistra in det här:

```text
Det här är en setup-session. Läs och följ instruktionerna här:
https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/setup/setup-session.md

Använd den här chatten bara till att sätta upp mitt arbetssätt, inte till att jobba med mina uppgifter.
```

Om din AI säger att den inte kan öppna länken, fäll ut rutan längst ned och klistra in hela instruktionen i stället.

## Vad som händer

1. **Claude tar reda på var du står.** Den läser av det den kan själv, till exempel ditt minne, vilka tjänster som är kopplade och om den når din dator, och frågar sedan om resten: vad du använder AI till, vilken plan du har, vilka områden som tar din tid och om du jobbar med andra.
2. **Claude föreslår ett upplägg.** Ett projekt för helheten, och kanske ett eget projekt för något stort som ett examensarbete. Den förklarar också vad som ska ligga på din dator, i Google Drive och i Claude.
3. **Ni skriver instruktionerna tillsammans.** Du får dem färdiga att klistra in.
4. **Du skapar projektet och flyttar dit chatten.** Claude läser då instruktionerna som en ny chatt i projektet skulle göra, ger återkoppling och testar att det fungerar.
5. **Ni avslutar.** Du får veta vad som finns var, ett första konkret steg i ett av projekten och hur du utvecklar upplägget vidare.

Räkna med 15 till 30 minuter för en första version.

## Varför en egen chatt för setupen?

Om du börjar jobba med en uppgift i samma chatt som du sätter upp ditt upplägg i, hamnar allt i en lång chatt utan instruktioner, och det är just det upplägget ska ersätta. Därför flyttas setupen in i projektet när den är klar, och det riktiga arbetet görs i nya chattar där. [Kapitel 01](01-fran-chatt-till-system.md#trappan) förklarar skillnaden mellan chatt och projekt, och [kapitel 10](10-anvandningsgransen.md#varfor-langa-chattar-blir-dyra) varför en lång chatt blir både sämre och dyrare än flera korta.

## Efter setupen

Hjärnan och dina projekt blir bättre av att användas. När du märker att något skaver, starta en ny chatt i Hjärnan och be om att bygga vidare. Kapitlen i guiden slutar med prompter som du klistrar in i ett av dina projekt för att ta nästa steg. Vill du se hur långt det går att ta, beskriver [kapitel 04](04-arkitekturen.md) och [kapitel 06](06-hjarnan.md) mitt eget upplägg.

??? note "Hela instruktionen, om din AI inte kan öppna länken"
    Kopiera allt i rutan och klistra in det i en ny chatt.

    ````text
    --8<-- "setup-session.md"
    ````
