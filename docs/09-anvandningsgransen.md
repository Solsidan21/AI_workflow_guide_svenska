# Kapitel 09 — Därför slår du i taket

*Många når användningsgränsen utan att bygga något alls, bara genom att plugga eller jobba. Det beror oftast på några få vanor som går att ändra.*

!!! abstract "Kort version"
    - Vid varje nytt meddelande bearbetar modellen hela konversationen igen, så en lång chatt blir dyrare för varje meddelande.
    - Stora filer, särskilt PDF, och toppmodellen med mycket tänkande drar mest.
    - Ny chatt per uppgift, Markdown i stället för PDF, material i projektets kunskap och rätt modell för rätt uppgift ger störst effekt.
    - Vid större arbete kan huvudkonversationen delegera till subagenter som arbetar i egen kontext och bara skickar tillbaka en kort rapport.
    - Delegering har en egen kostnad och lönar sig för större uppgifter, inte för en snabb fråga.

---

När jag först fick en betald plan trodde jag att gränsen var till för dem som bygger program. Sedan nådde jag den mitt i en tentaperiod, med enbart förklaringar och övningsfrågor. Det är vanligt. Orsaken ligger sällan i att du frågar för mycket. Den ligger i hur mycket modellen måste läsa varje gång du frågar.

## Hur gränsen fungerar

Anthropic beskriver två slags gränser på betalplanerna: en sessionsgräns som återställs fem timmar efter ditt första meddelande, och veckogränser. Förbrukningen delas mellan claude.ai, Claude Code och Claude Desktop, så det är ett gemensamt förråd. Hur mycket som finns kvar ser du under Settings och Usage. Anthropic förbehåller sig dessutom rätten att justera gränserna, så exakta tal är det ingen idé att lära sig utantill. Det som däremot består är vad som driver förbrukningen.

## Varför långa chattar blir dyra

Det viktigaste att förstå är att modellen inte minns tidigare meddelanden på egen hand. Vid varje nytt meddelande skickas hela konversationen in igen: instruktioner, allt som sagts, bifogade filer. Allt det är kontext som bearbetas på nytt.

??? begrepp "Begrepp: Token"
    --8<-- "token.md"

    [Se alla begrepp i ordlistan](ordlista.md#token)

Ett exempel. Du har en chatt med femtio meddelanden och ställer nummer femtioett. Då bearbetas alla femtio tidigare meddelanden plus det nya, bara för att svara på en kort fråga. Varje meddelande kostar alltså mer än det förra. Tjugo korta frågor i en lång chatt kostar mycket mer än tjugo korta frågor i varsin ny chatt, trots att du skrivit exakt lika mycket.

Det finns en mildrande mekanism som heter caching: det som redan bearbetats och inte ändrats kan återanvändas till en bråkdel av priset. Men cachen är kortlivad. På API-nivå är standardlivslängden fem minuter, och den förlängs varje gång den används. Tar du en längre paus går den ut, och nästa meddelande bearbetar hela historiken till fullt pris igen. Anthropics supportsida säger själva att cachat innehåll i projekt förfaller efter inaktivitet. Hur länge det gäller i claude.ai specifikt har jag inte sett angivet, så siffran fem minuter är en indikation och inget löfte.

Filer gör det värre. En PDF läses som text plus en bild av varje sida. Det blir ungefär några tusen tokens per sida, och det är en uppskattning som varierar med hur tät sidan är. En kursbok på trehundra sidor kan då motsvara en miljon tokens, vilket är mer än en vanlig konversation rymmer. Det är där PDF-problemet från kapitel 02 blir en användningsfråga och inte bara en precisionsfråga.

Anthropics egen lista över vad som driver förbrukningen är i korthet: långa meddelanden, stora bifogade filer, lång pågående konversation, verktyg som Research och webbsökning, modellval, effort-nivån, artifacts och flerstegsuppgifter som att köra kod eller skapa filer. Toppmodellen och mycket tänkande drar mer än en mindre modell med lite tänkande, vilket också syns i priserna i kapitel 08.

## Vad du kan göra åt det

Det här är åtgärderna jag själv fått mest ut av, i ungefär den ordningen.

**Ny chatt per uppgift.** När ämnet byts, börja om. Historiken från en uppgift hjälper sällan nästa, men du betalar för den ändå. Inom ett projekt finns instruktioner och kunskap kvar, så du förlorar ingenting.

**Låt Claude sammanfatta läget innan du byter chatt.** Skriv något i stil med: "Sammanfatta var vi är, vad vi bestämt och vad som återstår, så att jag kan fortsätta i en ny chatt." Klistra in sammanfattningen i den nya. Du tar med dig det viktiga och lämnar tiotusentals tokens av omvägar.

**Markdown i stället för PDF.** Samma innehåll som Markdown är en bråkdel av kostnaden och läses exakt som det står. Hur du omvandlar dokument beskrivs i kapitel 03.

**Material i projektets kunskap, inte uppladdat i chatten.** Innehåll i ett projekt cachas, så det räknas mindre när det återanvänds. Dessutom slår RAG på automatiskt på betalplaner när innehållet blir stort, så Claude hämtar bara det som är relevant för frågan i stället för att läsa allt.

??? begrepp "Begrepp: RAG"
    --8<-- "rag.md"

    [Se alla begrepp i ordlistan](ordlista.md#rag)

En brasklapp: du styr inte själv när RAG används, och svaret blir beroende av vad sökningen hittar. Anthropic anger att noggrannheten ska vara jämförbar med att läsa allt, men det är deras eget påstående och jag har inte kunnat pröva det. Vid frågor där det är viktigt att inget missas kontrollerar jag därför mot källan.

**Rätt modell för rätt uppgift.** Kör vardagsfrågorna på en lägre nivå och spara toppmodellen till de tillfällen där den behövs. Bara det här kan märkas tydligt över en vecka.

**Samla frågor.** Tre relaterade frågor i ett komplett meddelande är billigare än tre separata, eftersom varje separat meddelande ger ett nytt varv över hela konversationen.

## Orkestrering: låt en agent delegera

När jag arbetar aktivt, alltså bygger om ett system, går igenom många filer eller skriver längre texter, räcker inte ovanstående. Då låter jag huvudkonversationen delegera till subagenter.

??? begrepp "Begrepp: Subagent"
    --8<-- "subagent.md"

    [Se alla begrepp i ordlistan](ordlista.md#subagent)

Så fungerar det. En subagent börjar med ren kontext, alltså utan historiken från din huvudkonversation. Den får en uppgift, gör jobbet och skickar tillbaka en kort rapport. Allt mellanarbete, som läsning av filer, sökningar och testkörningar, stannar i subagentens egen kontext och belastar inte din huvudchatt. Huvudkonversationen förblir kort, och därmed billig. Dessutom kan modell väljas per subagent, så att läsning och kontroller görs på den billigaste nivån.

Subagenter är väl dokumenterade i Claude Code. Jag använder dem även i Claude-appen när den arbetar agentiskt. Om du bara chattar i en vanlig konversation har du sannolikt inte tillgång till dem, och jag har inte kunnat bekräfta exakt vilka ytor som stöder det, så kolla i din egen app. OpenAIs Codex har en motsvarighet med samma princip.

Här är en projektinstruktion jag utgått från. Lägg den i projektets instruktioner och justera till din situation:

```text
När vi arbetar aktivt med något som består av flera delar ska du agera orkestrerare.
Dela upp arbetet och delegera avgränsade uppgifter till subagenter i stället för att göra allt i den här konversationen.
Välj den billigaste modell som inte försämrar resultatet:
Haiku för genomläsning och kontroller, Sonnet för skrivande och research, den högsta nivån bara för svåra avvägningar.
Skriv subagenternas prompter själv. Ge varje subagent ett tydligt mål, det underlag den behöver och vad den ska lämna tillbaka.
Be om korta rapporter och låt subagenterna spara sina resultat i filer, så att den här konversationen bara behöver läsa sammanfattningen.
Granska rapporterna innan du går vidare, och berätta för mig om något ser fel ut.
För små uppgifter och snabba frågor ska du svara direkt utan att delegera.
```

Den sista raden är viktig av skäl som jag kommer till strax.

## Låt AI skriva prompterna

En sak som förvånade mig: Claude skriver ofta bättre och mer fullständiga prompter till en subagent än jag själv gör. Skälet är enkelt. Claude har hela sammanhanget framför sig, med dina regler, filerna och vad som redan beslutats, och kan därför ta med det en subagent behöver veta. När jag skriver en prompt för hand glömmer jag halva sammanhanget, eftersom jag har det i huvudet och tar det för givet. Du behöver bara beskriva målet. Resten kan Claude formulera.

## Ett exempel: den här guiden

Den här guiden skrevs om på det sättet. Agenter på Haiku gick igenom befintliga kapitel och gjorde den tråkiga genomläsningen, Sonnet-agenter gjorde research och skrev utkast, och huvudkonversationen styrde arbetet och granskade det som kom tillbaka. Jag skrev inte prompterna till agenterna, det gjorde huvudkonversationen. Mitt jobb var att säga vad guiden skulle bli och att läsa resultatet kritiskt. Utan delegeringen hade huvudkonversationen fyllts av råtext från källor och gamla kapitel långt innan jag var klar.

## Avvägningen

Delegering är inte gratis. Varje subagent måste läsa in sitt eget underlag, och det kostar tokens. Har du tio subagenter som var och en läser samma tre filer har du betalat för de filerna tio gånger. Dessutom tillkommer kostnaden för att skriva uppdragen och läsa rapporterna.

Därför lönar det sig för större uppgifter: många filer, långa dokument, arbete som annars skulle fylla huvudkonversationen med mellanresultat. För en snabb fråga eller en liten ändring är det ofta billigare att fråga direkt. Tumregeln jag använder är att om jag ändå skulle behöva läsa tiotals sidor underlag för att svara, delegerar jag. Annars gör jag det inte.

Ett sista råd är att inte jaga det perfekta upplägget. Börja med att byta chatt oftare och lägga PDF-filerna i Markdown. Det räcker långt, och orkestrering är något du lägger till när du märker att de enkla greppen inte räcker.

---

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/09-anvandningsgransen.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Fråga hur jag brukar arbeta när jag når användningsgränsen och vilka filer och chattar som är längst.
    Hjälp mig sedan att ta ett konkret första steg för att dra ned förbrukningen.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 10: Vad en prenumeration räcker till](10-vad-en-prenumeration-racker-till.md)
