# Kapitel 08 — Modellen och skalet

*Företag som Legora och Lovable bygger sina produkter på modeller från de stora AI-labben. Skillnaden mellan dem och en privatperson med en prenumeration är mindre än den ser ut, men den finns, och den är värd att förstå.*

Hela guiden vilar på en tanke: modellen är densamma för alla, och det som skiljer olika användare åt är vad som finns runt den. Det här kapitlet prövar den tanken mot hur riktiga bolag arbetar, redogör för var den håller och var den förenklar, och slutar i vad du själv kan bygga med en vanlig prenumeration.

## Samma modeller, olika skal

Ordet för det som finns runt modellen är skal, på engelska harness. Det är verktygen modellen får använda, källorna den får läsa, instruktionerna den följer och arbetsflödena som styr i vilken ordning saker görs.

??? begrepp "Begrepp: Skal (harness)"
    --8<-- "skal.md"

    [Se alla begrepp i ordlistan](ordlista.md#skal)

??? begrepp "Begrepp: Modell"
    --8<-- "modell.md"

    [Se alla begrepp i ordlistan](ordlista.md#modell)

Juristplattformen Legora är ett tydligt exempel. De beskriver själva modellen som resonemangsmotorn, och i deras "harness" får modellen verktyg, skills, juridiska källor och arbetsflöden. I [sin benchmark](https://legora.com/wip-legal-benchmark-2) utvärderar de modeller från flera leverantörer, bland dem Claude, GPT och Grok, på riktiga juridiska fall i den egna miljön och väljer sedan per uppgift. OpenAI beskriver sig som [en nyckelleverantör av modeller till Legora](https://openai.com/index/legora), och samtidigt använder Legora Claude och [rullar ut nya modeller efter egen utvärdering](https://legora.com/blog/legora%E2%80%99s-performance-improvements-with-sonnet-4.6), något som även [Anthropic beskriver](https://www.anthropic.com/customers/legora). För att passa in i juristers vardag integrerar plattformen dessutom med Word och SharePoint, [via Azure OpenAI](https://www.microsoft.com/en/customers/story/23171-legora-azure-openai).

Lovable, som bygger appar ur en beskrivning, [säger att de kör på Claude](https://lovable.dev/id/guides/claude-vs-lovable-ai-platform-comparison) och att det som skiljer dem från att använda claude.ai direkt är plattformslagret runt samma intelligens: byggställning, infrastruktur och driftlager. Enligt [Anthropics kundberättelse](https://claude.com/customers/lovable) delar Lovables huvudagent ut deluppgifter till subagenter och matchar varje uppgift mot den modell som passar bäst.

??? begrepp "Begrepp: Subagent"
    --8<-- "subagent.md"

    [Se alla begrepp i ordlistan](ordlista.md#subagent)

Mönstret är alltså detsamma i båda fallen. Modellen hyrs, byts eller blandas efter behov, och produkten är det som byggts runt den. Det betyder att mycket av det som får Legora att vara användbart för en jurist går att förstå som val av verktyg, källor och instruktioner. Det är samma slags val som du gör när du skriver en `CLAUDE.md` eller lägger kursmaterial i ett projekt.

## Nyanserna

Tesen om att modellen är densamma för alla blir lätt för slät. Fyra invändningar är rimliga.

**Modellen går att anpassa.** Leverantörerna erbjuder finjustering via sina gränssnitt för utvecklare, där en modell tränas vidare på egna exempel. Det är en annan sak än att skriva instruktioner, och det kräver data, kunskap och pengar.

??? begrepp "Begrepp: Finjustering"
    --8<-- "finjustering.md"

    [Se alla begrepp i ordlistan](ordlista.md#finjustering)

**Att välja modell per uppgift är inte att ändra modellen.** När Lovables agent skickar en deluppgift till en viss modell, eller när Legora väljer den modell som presterar bäst på en typ av fall, är det routing. Modellernas vikter rörs inte. Det är ett skicklighetsarbete i att veta vilken modell som passar vad, och det bygger på utvärdering, men det är något annat än att träna något nytt.

??? begrepp "Begrepp: Routing"
    --8<-- "routing.md"

    [Se alla begrepp i ordlistan](ordlista.md#routing)

**Skalet har ett verkligt värde.** Att sammanfatta det som "bara en prompt runt någon annans modell" underskattar arbetet. Ett bolag som Legora eller Lovable har saker som en enskild användare inte har:

- Egen data och licensierade källor, till exempel juridiska databaser som inte finns på öppna nätet.
- Utvärdering i stor skala. De kan testa nya modeller mot hundratals riktiga fall innan de rullar ut dem, och märker när något försämras.
- Integrationer med de system kunderna redan använder, inklusive hanteringen av behörigheter.
- Säkerhet och efterlevnad, som avtal om hur kunddata får behandlas.
- Drift i skala: övervakning, kostnadskontroll och support för tusentals samtidiga användare.

**Modellerna skiljer sig åt.** Att man utvärderar flera modeller per uppgift är ett tecken på att de inte är utbytbara. Tesen gäller att alla med en prenumeration når samma nivå av modell, inte att alla modeller är lika bra på allt.

## Vad en privatperson kan bygga själv

Med en vanlig prenumeration går det att bygga en liten motsvarighet till de flesta delarna i ett skal, för eget bruk. I resten av guiden finns exemplen, och de är samma byggstenar som bolagen arbetar med, fast i liten skala.

| Del av ett skal | Din version |
|---|---|
| Instruktioner | Projektinstruktioner och en `CLAUDE.md` med dina egna regler (kapitel 03) |
| Egna källor | Kursmaterial, anteckningar och gamla tentor i en mapp, ett repo och ett projekt (kapitel 03 och 04) |
| Arbetsflöden | Skills och upprepbara rutiner, till exempel veckoplan och uppgiftsindex (kapitel 05) |
| Samordning | Ett centralt projekt som läser statusen från de andra (kapitel 06) |
| Drift | Schemalagda uppgifter som körs utan att du är på plats (kapitel 06) |
| Utvärdering | Gamla tentor som test och en logg över misstag (kapitel 05 och 07) |

Skalet för eget bruk behöver heller inte vara tekniskt avancerat. Det som ger mest är att du vet vad du vill uppnå och att det du skriver ned är tydligt.

Det som däremot inte går att kopiera är det som kräver skala, avtal eller licens: exklusiva datakällor, utvärdering mot tusentals fall, företagsintegrationer med behörighetsstyrning och drift för många användare. Det är rimligt att köpa en färdig produkt när man står inför ett sådant behov. Den som ska hantera kunders avtal på ett kontor har andra krav än den som läser en kurs.

## Studieappar som ett fall av samma sak

Ett närliggande exempel är de studietjänster som finns på marknaden, som NotebookLM, Quizlet, StudyFetch, Knowt och Mindgrasp. De är också skal runt modeller, riktade mot studenter. Det är sakligt att säga vad de gör bättre.

- NotebookLM från Google bygger svaren på de källor du laddat upp, och beteendet är inbyggt. Det minskar risken för påhittade fakta. Ett Claude- eller ChatGPT-projekt med kursmaterial kan ge liknande resultat om instruktionen säger att svaren bara ska bygga på materialet och ange var, men där måste du själv se till att regeln följs.
- Quizlet och flera andra tjänster har färdiga gränssnitt för flashcards och repetition med scheman. En vanlig chatt har inget inbyggt repetitionsschema, och det är en reell fördel för dem som bara vill plugga och inte bygga.
- StudyFetch, Knowt och Mindgrasp samlar anteckningar, kort och övningsfrågor, och gör om föreläsningar eller dokument till studiematerial i ett steg. Det sänker tröskeln. Innehållsarbetet går i stort sett att göra även med en allmän prenumeration, men upplägget får man bygga själv.

Tjänsternas priser varierar och ändras, och jag har inte kontrollerat dem mot leverantörerna, så titta på respektive sida. En sak gäller oavsett verktyg: kort och förklaringar som en AI har skapat kan innehålla fel och behöver granskas.

De allmänna verktygen har en motsvarande svaghet. Disciplinen är ditt ansvar. ChatGPT har ett studieläge som är en genväg till ett förklarande arbetssätt, men det går enligt de källor jag har sett lätt att stänga av. Specialtjänsterna kan tvinga fram ett arbetssätt som du själv ibland väljer bort.

??? begrepp "Begrepp: RAG"
    --8<-- "rag.md"

    [Se alla begrepp i ordlistan](ordlista.md#rag)

Valet beror alltså på vad du vill ha. Vill du ha ett färdigt gränssnitt som kräver lite, kan en specialtjänst vara rätt. Vill du att systemet ska följa just din kurs, dina misstag och din dag, är det värt att bygga själv.

## Möjligheterna i en vanlig prenumeration

Det som kostar pengar i det här upplägget är prenumerationen. Hos Claude kostar Pro 20 dollar i månaden, eller 17 dollar per månad vid årsbetalning, och Max börjar på 100 dollar i månaden med fem gånger så mycket användning. Priserna står på [claude.com/pricing](https://claude.com/pricing) och kan ändras. Pro innehåller bland annat projekt och Claude Code, och på en betalplan går det att arbeta i Claude-appen på datorn med lokala mappar och schemalagda uppgifter. Hos OpenAI finns planer på flera nivåer, från gratis till dyrare varianter, och exakta priser och vad som ingår står på [chatgpt.com/pricing](https://chatgpt.com/pricing). Där finns också motsvarigheter som projekt, minne, Codex och uppgifter som körs på schema. Vilken funktion som ingår i vilken plan skiljer sig åt och ändras, så kontrollera innan du bestämmer dig. Kolla även om ditt lärosäte har avtal som ger rabatt.

Det avgörande är vad du gör med det. En prenumeration ger dig samma modeller som bolagen bygger på. Det som du lägger till är dina egna källor, dina egna regler och en rutin som får systemet att fortsätta fungera. Det är en begränsad version av det som ett skal är, men den är din, den anpassas efter hur du lär dig, och den kan flyttas mellan olika miljöer: studierna idag, ett jobb senare.

Nästa: [Bilaga: Samma upplägg i arbetslivet](bilaga-arbetsliv.md)
