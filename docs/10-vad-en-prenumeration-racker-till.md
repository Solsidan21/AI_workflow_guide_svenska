# Kapitel 10 — Vad en prenumeration räcker till

*Du betalar redan för en av de bästa modellerna som finns. Det här kapitlet handlar om hur långt den räcker när du bygger ditt eget system, och när det ändå kan vara värt att betala för något mer.*

!!! abstract "Kort version"
    - En vanlig prenumeration på Claude eller ChatGPT räcker långt för ett eget system.
    - Projekt, lokala mappar och schemalagda uppgifter finns redan på betalplanerna, men innehållet skiljer sig åt mellan planer, så kontrollera själv.
    - Färdiga AI-tjänster kan vara värda pengarna i vissa fall, men de bygger på samma modeller.
    - Det du själv tillför är källor, regler och en rutin som håller systemet igång.

## Vad du redan betalar för

Hos Claude kostar Pro 20 dollar i månaden, eller 17 dollar per månad vid årsbetalning, och Max börjar på 100 dollar i månaden med fem gånger så mycket användning. Priserna står på [claude.com/pricing](https://claude.com/pricing) och kan ändras. Pro innehåller bland annat projekt och Claude Code, och på en betalplan kan du arbeta i Claude-appen på datorn med lokala mappar och schemalagda uppgifter.

Hos OpenAI finns planer på flera nivåer, från gratis till betydligt dyrare. Exakta priser och vad som ingår står på [chatgpt.com/pricing](https://chatgpt.com/pricing). Där finns motsvarigheter som projekt, minne, Codex och uppgifter som körs på schema. Vilken funktion som ingår i vilken plan skiljer sig åt och ändras, så kontrollera innan du bestämmer dig. Kolla även om ditt lärosäte eller din arbetsgivare har ett avtal.

??? begrepp "Begrepp: Modell"
    --8<-- "modell.md"

    [Se alla begrepp i ordlistan](ordlista.md#modell)

## Vad ditt eget system täcker

Resten av guiden visar byggstenarna. Tillsammans täcker de det mesta som en betald AI-tjänst brukar erbjuda:

| Behov | Så löser du det själv |
|---|---|
| Svar som utgår från ditt material | Kursmaterial, anteckningar och gamla tentor i en mapp, ett repo och ett projekt (kapitel 03 och 04) |
| Svar på ditt sätt | Projektinstruktioner och en `CLAUDE.md` med dina egna regler (kapitel 03 och 05) |
| Övning och test | Gamla tentor, uppgifter med ankare och en logg över misstag (kapitel 05) |
| Planering och påminnelser | Ett centralt projekt, en lista och schemalagda uppgifter (kapitel 06) |
| Återkommande arbetsflöden | Skills och skript, till exempel ett uppgiftsindex som genereras automatiskt (kapitel 03 och 05) |

??? begrepp "Begrepp: RAG"
    --8<-- "rag.md"

    [Se alla begrepp i ordlistan](ordlista.md#rag)

Inget av det kräver att du kan programmera. Claude skriver skripten och regelfilerna tillsammans med dig. Det som krävs är att du vet vad du vill uppnå och att det du skriver ned är tydligt.

## Om färdiga AI-tjänster

Det finns gott om AI-tjänster för studier och för olika yrken: appar som gör flashcards och quiz av dina anteckningar, tjänster som sammanfattar föreläsningar, verktyg för jurister, säljare och utvecklare. Väldigt många av dem bygger på samma modeller som du redan har tillgång till. Det de lägger till är i grunden det den här guiden beskriver, alltså ordnade källor, instruktioner, några skript och arbetsflöden, förpackat i ett snyggare gränssnitt som är bekvämare att använda. För eget bruk kan du bygga mycket av det själv, och då blir det dessutom format efter just dig.

Det finns ändå lägen där en färdig tjänst är rätt val:

- Du vill inte bygga något alls och hellre betala för att slippa.
- Du behöver något en chatt saknar, till exempel ett färdigt schema för repetition av flashcards eller en mobilapp för just det.
- Du arbetar med data eller källor som du inte själv har tillgång till, eller med krav på säkerhet och avtal som en privat prenumeration inte uppfyller. Det gäller oftare på jobbet än i plugget.

En sak gäller oavsett verktyg: förklaringar, kort och sammanfattningar som en AI har skapat kan innehålla fel och behöver granskas.

## Disciplinen är din

Den verkliga skillnaden mellan ett eget system och en färdig tjänst är inte tekniken utan vem som håller i det. En färdig tjänst tvingar fram ett arbetssätt. I ditt eget system är det du som bestämmer att Claude ska visa stegen i stället för att ge svaret, att misstagen loggas och att du testar dig mot gamla tentor. Det är mer frihet och mer ansvar.

Det avgörande är alltså vad du gör med prenumerationen. Du har redan samma modeller som tjänsterna bygger på. Det du lägger till är dina egna källor, dina egna regler och en rutin som får systemet att fortsätta fungera. Det går att börja på en eftermiddag, det blir bättre för varje vecka, och det följer med dig från studierna till ett jobb.

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/10-vad-en-prenumeration-racker-till.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Fråga vilken plan jag har idag, vad jag vill använda den till och vad jag tycker saknas.
    Hjälp mig sedan att bedöma om min nuvarande plan räcker och vad jag kan bygga först utan att betala för mer.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Bilaga: Samma upplägg i arbetslivet](bilaga-arbetsliv.md)
