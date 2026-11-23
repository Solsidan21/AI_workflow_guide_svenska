# Kapitel 09 — Tröskeln, inte förmågan

*Mycket av det som väcker förvåning med AI i år gick att göra redan förra året. Det här kapitlet är min bedömning av varför det först nu når så många, och vad det betyder för dig.*

!!! abstract "Kort version"
    - Min tes: runt 2024 och 2025 blev modellerna och kodningsverktygen så bra att de kunde användas i utvecklingen av sig själva. Det förklarar delvis det höga tempot efter att Claude Code kom.
    - AI-stödd utveckling gör att Anthropic hinner bygga mycket mer produkt. Förutsättningarna för produkterna fanns redan i en vanlig prenumeration, så effekten blir att fler kommer åt det som redan gick att göra. Cowork är det tydligaste exemplet.
    - Tesen är min tolkning och en medveten förenkling. Anthropic skriver inte själva att syftet var att sänka en tröskel.
    - Modellerna har också blivit klart bättre. Förmågeöverhäng är glappet mellan vad en modell kan och vad folk använder den till.
    - Steget upp i trappan ger dig förmågor som redan finns.

---

## Min tes

Resten av guiden beskriver hur jag arbetar. Här gör jag en bedömning av utvecklingen, och den ska du ta med en nypa salt. Jag är student, inte forskare, och jag har ingen insyn i hur Anthropic resonerar. Tesen har fyra steg, och den är en medveten förenkling av något mer komplext.

1. Någon gång runt 2024 och 2025 blev språkmodellerna och kodningsverktygen så bra att de kunde användas i utvecklingen av sig själva och nästa modell. Jag bedömer att det gäller Anthropic och på motsvarande sätt OpenAI.
2. Jag tror att det är en förklaring till att takten ökade kraftigt efter att Claude Code kom. Det kändes som en ny modell eller funktion varje vecka.
3. AI-stödd utveckling gör att de hinner bygga mycket mer produkt.
4. Förutsättningarna för de nya produkterna fanns redan i en vanlig prenumeration. Produkterna fanns inte, men allt som behövdes för att bygga motsvarande själv fanns. Syftet med en produkt är förstås bara att ge något som folk tycker är användbart, inte uttryckligen att sänka en tröskel. Men i praktiken blir effekten att fler kommer åt det som redan gick att göra.

Den tekniska tröskeln stoppade de flesta från att använda Claude Code. Du behövde ge Claude tillgång till rätt mappar, skapa en egen MCP-koppling till en tjänst som saknade färdig connector, och ha koll på terminal, filer och installationer. Modellen saknade sällan förmåga. Det som hindrade var vägen dit.

??? begrepp "Begrepp: Claude Code"
    --8<-- "claude-code.md"

    [Se alla begrepp i ordlistan](ordlista.md#claude-code)

??? begrepp "Begrepp: MCP"
    --8<-- "mcp.md"

    [Se alla begrepp i ordlistan](ordlista.md#mcp)

??? begrepp "Begrepp: Connector"
    --8<-- "connector.md"

    [Se alla begrepp i ordlistan](ordlista.md#connector)

Steg 1 och 2 har visst stöd i Anthropics egna uppgifter. Steg 3 och 4 är mer av min egen slutsats.

## Vad som har kommit

Claude började som en chattbot, och chatten är kvar. Listan handlar om det som har byggts ut runt den. Datumen kommer från Anthropics nyhetsinlägg och supportsidor.

- 25 november 2024: Anthropic [lanserar MCP](https://www.anthropic.com/news/model-context-protocol), en öppen standard för att koppla AI-assistenter till de system där data finns.
- 24 februari 2025: Claude Code visas som en [begränsad förhandsvisning](https://www.anthropic.com/news/claude-3-7-sonnet), ett verktyg för utvecklare att styra från terminalen.
- 22 maj 2025: Claude Code blir [allmänt tillgängligt](https://www.anthropic.com/news/claude-4).
- 14 juli 2025: [Katalogen över connectors](https://claude.com/blog/connectors-directory) öppnas i Claude, så att du kopplar en tjänst med ett klick.
- 25 augusti 2025: [Claude in Chrome](https://claude.com/blog/claude-for-chrome) börjar testas med ett begränsat antal användare.
- 16 oktober 2025: [Skills](https://claude.com/blog/skills) kommer, mappar med instruktioner och skript som Claude hämtar vid behov.
- 12 januari 2026: Cowork släpps som förhandsversion i Claude-appen på datorn, först för Max på Mac och strax därefter för Pro. Källa: [Anthropics versionsanteckningar](https://support.claude.com/en/articles/12138966-release-notes).
- 25 februari 2026: Schemalagda uppgifter kommer till Cowork, enligt samma [versionsanteckningar](https://support.claude.com/en/articles/12138966-release-notes), och [hjälpsidan](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) beskriver hur de fungerar.
- 9 april 2026: Cowork blir allmänt tillgängligt på Mac och Windows.
- 16 september 2026: Cowork och chatten slås ihop till en och samma Claude. Enligt [inlägget](https://claude.com/blog/cowork-is-now-claude) var det frustrerande att behöva avgöra var en uppgift hörde hemma.

Tempot och inriktningen mot att göra förmågor lättare att nå syns i listan: färdiga kopplingar i stället för egna, en app i stället för en terminal, ett gemensamt hem i stället för två.

## Modellen hjälper till att bygga sig själv

I en [intervju i podcasten Latent Space](https://officechai.com/ai/80-of-claude-codes-code-is-written-by-claude-code-anthropic-lead-engineer/) våren 2025 sa Boris Cherny, som leder utvecklingen av Claude Code, att ungefär 80 procent av Claude Code skrevs av Claude Code. Människor granskar koden.

När Cowork kom i januari 2026 [rapporterade Axios](https://axios.com/2026/01/13/anthropic-claude-code-cowork-vibe-coding) att Cherny skrev att hela Cowork byggdes med Claude Code. Felix Rieseberg i Anthropics tekniska personal sa att bygget tog ungefär en och en halv vecka och att teamet la mer tid på produkt och arkitektur än på kodrader.

Mest heltäckande är Anthropic Institutes inlägg [When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement). Där står att Claude i maj 2026 skrivit över 80 procent av koden som slogs ihop i Anthropics produktionskod, mot låga ensiffriga procent före Claude Code i februari 2025. Mängden kod som en ingenjör slog ihop per dag låg still till 2024 och var runt åtta gånger högre andra kvartalet 2026.

Anthropic är själva försiktiga. Kodrader är ett ofullkomligt mått och åttafaldigandet är nästan säkert en överdrift. Mänsklig granskning är redan en flaskhals, och Claude har stora brister i att välja mål för teknik och forskning. Att hjälpa till är något annat än att bygga nästa modell på egen hand.

Stämmer det att takten har ökat? [Fast Company](https://fastcompany.com/91611158/why-ai-model-releases-feel-nonstop) räknar att tiden mellan Anthropics modellsläpp krympte från ungefär 46 dagar första halvåret 2026 till ungefär 26 dagar andra halvåret. Artikeln är dock skeptisk. Tiden mellan helt nya flaggskepp har ändrats lite, och en IDC-analytiker tvivlar på att självförbättring ligger bakom och pekar på konkurrens. Min känsla av ett nytt släpp varje vecka har alltså visst stöd, men orsaken är inte bevisad. Uppgifterna är förenliga med min tes, mer än så kan jag inte säga.

## Vad Anthropic själva säger

Det som stöder steg 4 är för det första namnet. När Cowork släpptes hette inlägget [Cowork: Claude Code for the rest of your work](https://claude.com/blog/cowork-research-preview). Anthropic skriver där att Cowork är byggt för kunskapsarbete som inte är kodning, och att det använder samma agentiska arbetssätt som Claude Code. [TechCrunch](https://www.techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/) skrev att verktyget delvis var inspirerat av att allt fler prenumeranter redan använde Claude Code till annat än kod, och att det inte kräver kommandorad.

Nu kommer saltkornet. Det sista är reporterns beskrivning, inte ett citat. Så vitt jag kan se skriver Anthropic ingenstans att syftet var att sänka en teknisk tröskel, och ingenstans att AI-stödd utveckling var anledningen till att de prioriterade produkter. De beskriver en målgrupp och en produkt för den. Att det fungerar som en lägre tröskel är min slutsats av tidslinjen och rubriken.

Jag antar också att det Anthropic släpper har hög korrelation med hur användarna använder Claude och vad de bygger, och med hur Anthropic själva använder Claude internt. De ser vad som fungerar och gör en bättre, färdig mall av det. Det är mitt antagande och inget Anthropic har sagt. Skills är ett exempel. Anthropic skriver att de [använder skills i Claude Code i stor utsträckning internt](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills), med hundratals i aktiv användning. I [lanseringsinlägget](https://claude.com/blog/skills) står att Claude använder skills för att skapa filer som kalkylblad och presentationer. Att just skills för dokumentformat redan låg bakom filskapandet kunde jag inte belägga, så den delen är också mitt antagande.

## Modellerna har också blivit bättre

Det vore fel att stanna där, för modellerna har faktiskt utvecklats. Det bästa måttet jag hittat kommer från forskningsorganisationen METR. De mäter hur långa uppgifter en modell klarar, mätt i hur lång tid de tar för en människa. Längden där modellen lyckas ungefär varannan gång kallas tidshorisont.

Enligt METR:s [uppdaterade mätning](https://metr.org/blog/2026-01-29-time-horizon-1-1/) har tidshorisonten fördubblats ungefär var sjunde månad sedan 2019. Sedan 2024 går det snabbare, med en fördubbling ungefär var tredje månad. Claude Opus 4 från våren 2025 hamnar kring 100 minuter och Claude Opus 4.5 hösten 2025 kring 320 minuter.

Även det här tas med en nypa salt. METR påpekar själva att osäkerhetsintervallen är breda och att uppgifterna mest rör programmering, maskininlärning och säkerhet. [Sidan om tidshorisonter](https://metr.org/time-horizons/) uppdateras dessutom inte längre aktivt. Ett test på väldefinierade uppgifter säger inte hur modellen klarar en rörig vardag.

??? begrepp "Begrepp: Benchmark"
    --8<-- "benchmark.md"

    [Se alla begrepp i ordlistan](ordlista.md#benchmark)

Min tes är alltså för enkel i sin starkaste form. Om modellerna vore oförändrade skulle tröskeln förklara allt, men särskilt för långa, självständiga uppgifter är de märkbart bättre än när Claude Code lanserades. Båda förklaringarna gäller: modellerna har blivit bättre, och produkterna har gjort förmågan lättare att nå.

## Förmågeöverhäng

Det finns ett begrepp för glappet mellan vad en modell kan och vad folk har kommit på att göra med den: förmågeöverhäng, på engelska capability overhang. Grundtanken är en latent förmåga som är betydligt större än den som används i praktiken. [AI Wiki](https://aiwiki.ai/wiki/capability_overhang) går igenom hur termen används. Den moderna betydelsen brukar kopplas till Jack Clark, som i nyhetsbrevet [Import AI 321](https://jack-clark.net/2023/03/21/import-ai-321-open-source-gpt3-giving-away-democracy-to-agi-companies-gpt-4-is-a-political-artifact/) i mars 2023 skrev att varken OpenAI eller deras partner visste hur stor GPT-4:s förmåga egentligen var, och att de användningar man såg då var de förhållandevis enkla.

Med det som bakgrund kan min tes sägas så här: en del av förmågeöverhänget har suttit i tröskeln. Förmågan fanns, men den som inte ville använda en terminal kom aldrig åt den. När tröskeln sänks syns överhänget som nya användningar, och det ser ut som att modellerna plötsligt blivit smartare. Ibland har de det. Ibland har bara fler fått tillgång till det som redan fanns.

## Vad det betyder för dig

Tröskeln är lägre än många tror. Du behöver inte kunna programmera. Mycket av det som för två år sedan krävde en terminal går i dag att göra i Claude-appen, med en mapp du väljer och en uppgift du beskriver.

Förmågorna finns redan. Den som går ett steg upp i trappan, från chatt till projekt, till appen på datorn eller vidare till Claude Code, får tillgång till sådant som modellen redan kan. Trappan beskrivs i [kapitel 01](01-fran-chatt-till-system.md). Du får inte en smartare modell av att klättra. Du får fler saker att ge den att arbeta med.

Räkna ändå med att den lägre tröskeln inte tar bort ditt ansvar. Ju mer självständigt Claude arbetar, desto viktigare är det att du säger vad den får ändra och läser resultatet som ett utkast.

En ironisk slutpoäng: med den här guiden arbetar jag på sätt och vis gratis som säljare åt Claude. Någon provision har jag inte sett röken av, men jag får åtminstone använda produkten för att skriva reklamen.

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
