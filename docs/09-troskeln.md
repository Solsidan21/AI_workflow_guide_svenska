# Kapitel 09 — Tröskeln, inte förmågan

*Mycket av det som väcker förvåning med AI i år gick att göra redan förra året. Det här kapitlet är min bedömning av varför det först nu når så många, och vad det betyder för dig.*

!!! abstract "Kort version"
    - Min tes: modellerna har kunnat mycket av det folk fascineras av i över ett år, via Claude Code. Det som stoppade de flesta var en teknisk tröskel.
    - Anthropics produkter det senaste året kan till stor del ses som sätt att sänka tröskeln. Cowork är det tydligaste exemplet.
    - Tesen är min tolkning. Anthropic skriver själva inte att syftet var att sänka en tröskel, och modellerna har också blivit klart bättre, särskilt på långa uppgifter.
    - Båda förklaringarna gäller samtidigt. Begreppet förmågeöverhäng beskriver glappet mellan vad en modell kan och vad folk faktiskt använder den till.
    - Tröskeln är lägre än många tror, och steget upp i trappan ger dig förmågor som redan finns.

---

## Min tes

Det här kapitlet skiljer sig från de andra. Resten av guiden beskriver hur jag arbetar. Här gör jag en bedömning av utvecklingen, och den ska du ta med en nypa salt. Jag är student, inte forskare, och jag har inte insyn i hur Anthropic resonerar.

Så här ser tesen ut. Mycket av det som folk har fascinerats av under det senaste året har modellerna kunnat i över ett år, genom Claude Code. Modellen saknade sällan förmåga. Det som hindrade de flesta var en teknisk tröskel. Du behövde ge Claude tillgång till rätt mappar på datorn. Du behövde skapa en egen MCP-koppling till en tjänst som saknade färdig connector. Och du behövde ha allmän koll på hur en dator fungerar, med terminal, filer och installationer.

??? begrepp "Begrepp: Claude Code"
    --8<-- "claude-code.md"

    [Se alla begrepp i ordlistan](ordlista.md#claude-code)

??? begrepp "Begrepp: MCP"
    --8<-- "mcp.md"

    [Se alla begrepp i ordlistan](ordlista.md#mcp)

??? begrepp "Begrepp: Connector"
    --8<-- "connector.md"

    [Se alla begrepp i ordlistan](ordlista.md#connector)

Anthropics produkter det senaste året kan enligt mig till stor del ses som sätt att sänka just den tröskeln. Cowork är det tydligaste exemplet. Resten av kapitlet prövar om tesen håller.

## Vad tidslinjen visar

Datumen nedan kommer från Anthropics egna nyhetsinlägg och supportsidor.

- 25 november 2024: Anthropic [lanserar MCP](https://www.anthropic.com/news/model-context-protocol), som de beskriver som en öppen standard för att koppla AI-assistenter till de system där data finns. Motivet är att modeller annars sitter fast bakom informationssilos, och att varje ny datakälla kräver en egen anpassning.
- 24 februari 2025: Claude Code visas som en [begränsad förhandsvisning](https://www.anthropic.com/news/claude-3-7-sonnet), som ett verktyg för utvecklare att styra från terminalen.
- 22 maj 2025: Claude Code blir [allmänt tillgängligt](https://www.anthropic.com/news/claude-4).
- 14 juli 2025: [Katalogen över connectors](https://claude.com/blog/connectors-directory) öppnas i Claude, så att du kan koppla en tjänst med ett klick i stället för att sätta upp den själv.
- 25 augusti 2025: [Claude in Chrome](https://claude.com/blog/claude-for-chrome) börjar testas med ett begränsat antal användare.
- 16 oktober 2025: [Skills](https://claude.com/blog/skills) kommer, som mappar med instruktioner, skript och resurser som Claude hämtar när de behövs.
- 12 januari 2026: Cowork släpps som förhandsversion i Claude-appen på datorn, först för Max-planen på Mac och några dagar senare för Pro. Källa: [Anthropics versionsanteckningar](https://support.claude.com/en/articles/12138966-release-notes).
- 25 februari 2026: Schemalagda uppgifter kommer till Cowork, enligt samma [versionsanteckningar](https://support.claude.com/en/articles/12138966-release-notes). Hjälpsidan [beskriver hur de fungerar](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork).
- 9 april 2026: Cowork blir allmänt tillgängligt på Mac och Windows.
- 16 september 2026: Cowork och chatten slås ihop till en och samma Claude. Anthropic skriver i [sitt inlägg](https://claude.com/blog/cowork-is-now-claude) att användarna tyckte det var frustrerande att behöva avgöra var en uppgift hörde hemma.

Mönstret är tydligt. Claude Code fanns först, och nästan allt som kom efter handlar om att göra liknande saker lättare att nå: färdiga kopplingar i stället för egna, en app i stället för en terminal, ett gemensamt hem i stället för två.

## Vad Anthropic själva säger

Det som stöder tesen är för det första namnet. När Cowork släpptes hette inlägget [Cowork: Claude Code for the rest of your work](https://claude.com/blog/cowork-research-preview). Anthropic skriver där att Cowork är byggt för kunskapsarbete som inte är kodning, och att det använder samma agentiska arbetssätt som Claude Code. Teknikpressen beskrev det som en version av Claude Code utan koden. [TechCrunch](https://www.techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/) skrev att verktyget delvis var inspirerat av att allt fler prenumeranter redan använde Claude Code till uppgifter som inte handlade om kod, och att det inte kräver kommandorad.

Nu kommer saltkornet. Det sista är reporterns beskrivning och inte ett citat från Anthropic. Så vitt jag kan se skriver Anthropic ingenstans att syftet var att sänka en teknisk tröskel. De beskriver en målgrupp, kunskapsarbetare, och en produkt för den. Att det i praktiken fungerar som en lägre tröskel är min slutsats av tidslinjen och rubriken, inte något de har sagt rakt ut.

## Modellerna har också blivit bättre

Det vore ändå fel att stanna där, för modellerna har faktiskt utvecklats. Det bästa måttet jag hittat kommer från forskningsorganisationen METR. De mäter hur långa uppgifter en modell klarar, mätt i hur lång tid uppgiften tar för en människa, och räknar ut den längd där modellen lyckas ungefär varannan gång. Det kallas modellens tidshorisont.

Enligt METR:s [uppdaterade mätning](https://metr.org/blog/2026-01-29-time-horizon-1-1/) har tidshorisonten fördubblats ungefär var sjunde månad sedan 2019. Sedan 2024 går det snabbare, med en fördubbling ungefär var tredje månad. Claude Opus 4 från våren 2025 hamnar kring 100 minuter, och Claude Opus 4.5 hösten 2025 kring 320 minuter. Det är ungefär en tredubbling på ett halvår.

Även det här tas med en nypa salt. METR själva påpekar att resultaten är känsliga för vilka uppgifter som ingår, att osäkerhetsintervallen är breda och att uppgifterna mest rör programmering, maskininlärning och säkerhet. De varnar också för att mätningar över 16 timmar inte går att lita på med deras nuvarande uppgiftsuppsättning. På [METR:s sida om tidshorisonter](https://metr.org/time-horizons/) står dessutom att den inte längre uppdateras aktivt. Ett test på självständiga, väldefinierade uppgifter säger inte hur modellen klarar en rörig vardag.

??? begrepp "Begrepp: Benchmark"
    --8<-- "benchmark.md"

    [Se alla begrepp i ordlistan](ordlista.md#benchmark)

Slutsatsen blir att min tes är för enkel i sin starkaste form. Om modellerna vore oförändrade sedan förra året skulle tröskeln förklara allt. Det är de inte. Särskilt för långa, självständiga uppgifter, den sortens arbete där Claude får gå iväg och återkomma med ett resultat, är modellerna i slutet av 2026 märkbart bättre än de var när Claude Code lanserades. Båda förklaringarna gäller samtidigt: modellerna har blivit bättre, och produkterna har gjort förmågan lättare att nå.

## Förmågeöverhäng

Det finns ett begrepp för glappet mellan vad en modell kan och vad folk har kommit på att göra med den: förmågeöverhäng, på engelska capability overhang. Det finns ingen allmänt vedertagen definition, men grundtanken är en latent förmåga som är betydligt större än den som används i praktiken. En [sammanställning på AI Wiki](https://aiwiki.ai/wiki/capability_overhang) går igenom hur termen används. Den moderna betydelsen brukar kopplas till Jack Clark, som i nyhetsbrevet [Import AI 321](https://jack-clark.net/2023/03/21/import-ai-321-open-source-gpt3-giving-away-democracy-to-agi-companies-gpt-4-is-a-political-artifact/) i mars 2023 skrev att varken OpenAI eller deras partner visste hur stor GPT-4:s förmåga egentligen var, och att de användningar man såg då var de förhållandevis enkla.

Med det som bakgrund kan min tes sägas så här: en del av förmågeöverhänget har suttit i tröskeln. Förmågan fanns, men den som inte kunde eller ville använda en terminal kom aldrig åt den. När tröskeln sänks syns överhänget som nya användningar, och det kan se ut som att modellerna plötsligt har blivit smartare. Ibland har de det. Ibland har bara fler fått tillgång till det som redan fanns.

## Vad det betyder för dig

Det praktiska är det som är mest användbart, oavsett vem som har rätt om orsakerna.

Tröskeln är lägre än många tror. Du behöver inte kunna programmera eller förstå hur en MCP-server är uppbyggd. Mycket av det som för två år sedan krävde en terminal går i dag att göra i Claude-appen, med en mapp du väljer och en uppgift du beskriver.

Förmågorna finns redan. Den som går ett steg upp i trappan, från chatt till projekt, från projekt till appen på datorn, eller vidare till Claude Code, får tillgång till sådant som modellen redan kan. Trappan beskrivs i [kapitel 01](01-fran-chatt-till-system.md). Du får inte en smartare modell av att klättra. Du får fler saker att ge den att arbeta med.

Räkna ändå med att den lägre tröskeln inte tar bort ditt ansvar. Ju mer självständigt Claude arbetar, desto viktigare är det att du är tydlig med vad den får ändra, och att du läser resultatet som ett utkast.

---

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/09-troskeln.md
    Guiden beskriver en persons upplägg och är inget facit. Författarens tes är hans egen bedömning, så ta den med en nypa salt.
    Fråga vad jag använder AI till i dag och vad som hindrar mig från nästa steg.
    Föreslå sedan ett första steg som passar mig.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 10: Därför slår du i taket](10-anvandningsgransen.md)
