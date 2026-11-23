# Kapitel 08 — Modellerna

*Claude, ChatGPT och Gemini erbjuder var sin trappa av modeller. Det mesta av det som skiljer dem märks i verktygen runt omkring, mindre i modellerna själva.*

!!! abstract "Kort version"
    - Anthropic har fyra nivåer: Haiku, Sonnet, Opus och Fable. Högre nivå betyder bättre förmåga, men också högre pris och snabbare förbrukning av användningsgränsen.
    - Välj den billigaste nivån som klarar uppgiften. Toppmodellen behövs sällan.
    - Benchmarks är användbara för att se grov skillnad, men små skillnader i toppen märks sällan i vardagsbruk.
    - Min tes är att toppmodellerna hos de stora bolagen är ungefär lika bra utanför avancerad kodning. Jämför därför produkterna: verktyg, integrationer och appar.
    - Välj produkt efter vad du ska göra och vilka verktyg du använder.

---

I de här kapitlen har jag mest skrivit "Claude" som om det vore en sak. I själva verket är det en familj av modeller, och valet mellan dem påverkar både kvalitet, hastighet och hur snabbt du når användningsgränsen som kapitel 09 handlar om. Det här kapitlet går igenom trappan och ger mig anledning att säga något om hur mycket modellvalet egentligen spelar roll.

## Vad en modell är

??? begrepp "Begrepp: Modell"
    --8<-- "modell.md"

    [Se alla begrepp i ordlistan](ordlista.md#modell)

Namnet du ser i appen, till exempel Claude, är en produkt. Under den ligger en eller flera modeller. Produkten är modellen plus allt som sitter runt den: projekt, minne, filhantering, kopplingar till andra tjänster och appar på mobil och dator. Skillnaden mellan modell och produkt är hela poängen med kapitlet.

## Anthropics trappa

Anthropic har fyra nivåer, från billig och snabb till kraftfull och dyr.

| Nivå | Typisk användning | API-pris per miljon tokens (indata / utdata) |
|---|---|---|
| Haiku | Genomläsning, sortering, kontroller, enkel extraktion | Klart billigast |
| Sonnet | Skrivande, research, vardaglig problemlösning | 2 / 10 dollar |
| Opus | Långa uppgifter, kodning, krävande kunskapsarbete | 4 / 20 dollar |
| Fable | De svåraste avvägningarna och längsta agentiska uppgifterna | 8 / 40 dollar |

Priserna kommer från Anthropics modellöversikt och gäller API:t, alltså det man betalar när man bygger egna program. Som privatperson med abonnemang betalar du inte per token, men siffrorna är ett bra relativt mått. Fable kostar fyra gånger så mycket som Sonnet. Det säger något om hur mycket mer beräkning som ligger bakom varje svar, och det är beräkningen som äter av din användningsgräns.

Den praktiska konsekvensen är att toppmodellen drar gränsen snabbare än de andra. Anthropic skriver det uttryckligen om Fable, och det stämmer med logiken i priserna. Vilka modeller som ingår i vilken plan ändras ofta, och det enda jag kunnat belägga är Fable: den finns på alla betalplaner men inte på gratisnivån. På Pro körs den mot usage credits, alltså extra betalning, medan den på Max och Ultra ingår i planen men förbrukar veckogränsen snabbare. Titta i appen eller på Anthropics sida om din plan innan du räknar med något.

Så här använder jag nivåerna:

- Haiku när jag vill att något ska läsas igenom eller kontrolleras, till exempel att gå igenom ett kapitel och lista vad som inte stämmer med reglerna.
- Sonnet till det mesta: förklaringar, research, skrivande och att bygga vidare på ett system.
- Opus när en uppgift är lång och har många delar som måste hänga ihop.
- Fable bara när jag fastnat på en svår avvägning och vill ha den bästa bedömningen, inte för rutinarbete.

Det är min egen tumregel. Anthropic själva rekommenderar Opus som standardval för de flesta arbetsbelastningar, så välj gärna högre än jag gör om du har gott om utrymme i din plan. Principen är densamma: börja på en lägre nivå och gå upp först när resultatet inte räcker.

## Motsvarigheter hos OpenAI och Google

OpenAI har en liknande trappa. I ChatGPT drivs de betalda planerna av GPT-6 Sol, medan gratisnivån och Go-nivån drivs av GPT-6 Luna. Det är alltså en enklare uppdelning för användaren, där nivån följer planen. Under GPT-5.6 fanns också en mellannivå som hette Terra. Jag har inte hittat några uppgifter om API-priser för GPT-6 och påstår därför inget om dem. Codex, OpenAIs verktyg för kodning och agentarbete, har precis som Claude Code stöd för subagenter med eget modellval.

Google har Gemini i två huvudspår, Pro och Flash, där Flash är den snabba och billiga och Pro den kraftfulla. Versionsnumren byts snabbt och jag har inte kunnat fastställa vilken som i dag är toppmodellen i Gemini-appen, så jag låter bli att ange någon. Allt jag skriver om konkreta modellnamn är dessutom en ögonblicksbild från november 2026 och kommer att vara förlegad snart. Trappstrukturen, med en billig, en mellan och en dyr nivå, är det som består.

## Vad benchmarks säger och inte säger

När en ny modell släpps följer en tabell med siffror. Några vanliga:

- SWE-bench Verified: riktiga felrapporter från öppna kodprojekt där modellen ska skriva en rättning som klarar projektets tester.
- GPQA Diamond: naturvetenskapliga frågor på forskarnivå. Testet är i princip mättat, och de bästa modellerna ligger kring 94 procent.
- Humanity's Last Exam: ungefär 2 500 mycket svåra frågor från experter, framtagna så att tidiga modeller skulle misslyckas.

??? begrepp "Begrepp: Benchmark"
    --8<-- "benchmark.md"

    [Se alla begrepp i ordlistan](ordlista.md#benchmark)

Det finns flera skäl att ta siffrorna med ro. När toppmodellerna närmar sig taket på ett test blir skillnaderna små och kan vara brus. Den som tränar en modell kan dessutom ha optimerat för just provet, och bland populära frågetester har granskningar hittat att en del frågor läckt in i träningsdata. Leverantörerna väljer också själva vilka siffror de visar, och det är rimligt att anta att de lyfter fram de där de står sig bäst. Det sista är mitt eget resonemang och inget jag funnit belagt, men det följer av incitamenten.

Rangordningen beror dessutom på hur man mäter. En sammanställning från Artificial Analysis i oktober 2026 hade de fyra främsta modellerna inom två poäng från varandra, där Opus låg på 58 och tre andra modeller på 56. I en annan sammanställning låg en av OpenAIs modeller på 58,9. Den som läser en enda tabell kan alltså få bilden att en modell vinner, och en annan tabell säger något annat. Glappet som verkligen var stort i den första sammanställningen låg mellan de slutna och de öppna modellerna, inte mellan de stora bolagens toppmodeller.

## Min tes: jämför produkterna

Det leder till det jag själv tror, och jag vill vara tydlig med att det är en bedömning och inte ett faktum. För de flesta uppgifter utanför avancerad kodning är toppmodellerna hos de stora bolagen ungefär lika bra. Förklara ett begrepp, sammanfatta en text, skriv ett utkast, hjälp mig tänka igenom ett problem: det klarar de alla, och skillnaden jag märker mellan dem är mindre än skillnaden mellan en bra och en dålig prompt. Det är också vad den som sammanställde siffrorna ovan landar i, men det är en tolkning och inget bevisat.

Det som skiljer sig mer är runt omkring: vilka verktyg som finns, hur väl de kopplas till dina andra tjänster och hur apparna fungerar.

??? begrepp "Begrepp: MCP"
    --8<-- "mcp.md"

    [Se alla begrepp i ordlistan](ordlista.md#mcp)

Jag valde Claude av just det skälet. Den ligger enligt min bedömning långt fram på verktyg och integrationer: projekt med egen kunskap, Claude Code med subagenter, och kopplingar till tjänster som mejl, kalender och dokument. Anthropic har också fokuserat på företag, vilket syns i vad de bygger. Det finns en siffra som pekar åt samma håll. Menlo Ventures angav i sin rapport från november 2026 att Anthropics andel av företagens utgifter för LLM-API:er steg från 40 till 55 procent, medan OpenAI gick från 27 till 31 och Google föll från 21 till 9. Läs den med försiktighet. Menlo Ventures är en riskkapitalfirma som själva är investerare i Anthropic, och siffran mäter företagens API-utgifter, inte vad en student har nytta av i vardagen.

ChatGPT har sina egna starka sidor, och de är inte små. Enligt Sensor Towers mätning från maj 2026 hade ChatGPT 46,4 procent av konsumentmarknaden, Gemini 27,7 och Claude 10,3. Antalet månadsanvändare låg på över 1,1 miljarder för ChatGPT mot 245 miljoner för Claude. OpenAI uppger själva över 1,2 miljarder veckoanvändare, men siffrorna mäter olika saker och går inte att jämföra rakt av. Många fler människor använder alltså ChatGPT, och bredden i erbjudandet är större på konsumentsidan: interaktiva element som diagram och formulär i svaren, och Codex i både skrivbordsapp, terminal och kodredigerare. Är det ChatGPT dina vänner, kurskamrater eller kollegor använder kan det i sig vara ett skäl att välja den, eftersom du då delar exempel och arbetssätt.

Det jag landar i är att frågan "vilken modell är bäst?" är mindre användbar än "vad ska jag göra, och vilka verktyg använder jag?". Använder du mest en chatt för frågor och förklaringar duger vilken som helst av de stora. Vill du bygga upp projekt med egen kunskap, koppla in dina tjänster och låta en agent arbeta i dina mappar, jämför då vad respektive produkt faktiskt kan göra, och prova gärna båda under en vecka med en riktig uppgift. Guiden är skriven med Claude eftersom det är vad jag använder, men upplägget går att flytta över.

---

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/08-modellerna.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Fråga vad jag mest använder AI till och vilken plan och vilka verktyg jag har i dag.
    Hjälp mig sedan att välja modellnivå för tre av mina vanligaste uppgifter och att ta ett konkret första steg.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 09: Därför slår du i taket](09-anvandningsgransen.md)
