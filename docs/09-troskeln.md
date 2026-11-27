# Kapitel 09 — Tröskeln, inte förmågan

*Mycket av det som väcker förvåning med AI i år gick att göra redan förra året. Kapitlet går först igenom vad som går att belägga om utvecklingen, och lägger sedan fram min egen tolkning av varför det först nu når så många.*

!!! abstract "Kort version"
    **Fakta (med källor):**

    - Modellerna och kodningsverktygen används i utvecklingen av sig själva och nästa modell. Hos Anthropic syns det från 2025, och OpenAI beskriver detsamma för en modell som släpptes i februari 2026. Anthropic uppger att Claude skrev över 80 procent av den kod som slogs ihop i maj 2026.
    - Anthropics släpp av modeller och funktioner har blivit tätare sedan Claude Code kom. Orsaken är omstridd.
    - Modellerna har också blivit klart bättre, särskilt på långa, självständiga uppgifter.

    **Min tes (min egen bedömning):**

    - Förutsättningarna för de nya produkterna fanns redan i en vanlig prenumeration. Produkterna sänker den tekniska tröskeln, så att fler kommer åt det som redan gick att göra. Cowork är det tydligaste exemplet.
    - Anthropic skriver inte själva att syftet är att sänka en tröskel. Tesen är en medveten förenkling.

---

## Vad som har kommit

Claude började som en chattbot, och chatten är kvar. Listan handlar om det som har byggts ut runt den. Datumen kommer från Anthropics nyhetsinlägg och supportsidor.

- 25 november 2024: Anthropic [lanserar MCP](https://www.anthropic.com/news/model-context-protocol), en öppen standard för att koppla AI-assistenter till de system där data finns.
- 24 februari 2025: Claude Code visas som en [begränsad förhandsvisning](https://www.anthropic.com/news/claude-3-7-sonnet), ett verktyg för utvecklare att styra från terminalen.
- 22 maj 2025: Claude Code blir [allmänt tillgängligt](https://www.anthropic.com/news/claude-4).
- 14 juli 2025: [Katalogen över connectors](https://claude.com/blog/connectors-directory) öppnas i Claude, så att du kopplar en tjänst med ett klick.
- 25 augusti 2025: [Claude in Chrome](https://claude.com/blog/claude-for-chrome) börjar testas med ett begränsat antal användare.
- 16 oktober 2025: [Skills](https://claude.com/blog/skills) kommer, mappar med instruktioner och skript som Claude hämtar vid behov.
- 12 januari 2026: Cowork släpps som förhandsversion i Claude-appen på datorn, först för Max på Mac och några dagar senare för Pro. Källa: [Anthropics versionsanteckningar](https://support.claude.com/en/articles/12138966-release-notes).
- 25 februari 2026: Schemalagda uppgifter kommer till Cowork, enligt samma [versionsanteckningar](https://support.claude.com/en/articles/12138966-release-notes), och [hjälpsidan](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) beskriver hur de fungerar.
- 9 april 2026: Cowork blir allmänt tillgängligt på Mac och Windows, enligt versionsanteckningarna.
- 16 september 2026: Cowork och chatten slås ihop till en och samma Claude. Enligt [inlägget](https://claude.com/blog/cowork-is-now-claude) var det frustrerande att behöva avgöra var en uppgift hörde hemma.

??? begrepp "Begrepp: Claude Code"
    --8<-- "claude-code.md"

    [Se alla begrepp i ordlistan](ordlista.md#claude-code)

??? begrepp "Begrepp: MCP"
    --8<-- "mcp.md"

    [Se alla begrepp i ordlistan](ordlista.md#mcp)

??? begrepp "Begrepp: Connector"
    --8<-- "connector.md"

    [Se alla begrepp i ordlistan](ordlista.md#connector)

## Används modellerna för att bygga sig själva?

Ja, det uppger både Anthropic och OpenAI.

**Anthropic.** Boris Cherny, som leder utvecklingen av Claude Code, sa i [podcasten Latent Space](https://officechai.com/ai/80-of-claude-codes-code-is-written-by-claude-code-anthropic-lead-engineer/) våren 2025 att ungefär 80 procent av Claude Code skrevs av Claude Code. Människor granskar koden. När Cowork kom i januari 2026 [rapporterade Axios](https://axios.com/2026/01/13/anthropic-claude-code-cowork-vibe-coding) att Cherny skrev att hela Cowork byggdes med Claude Code, och att Felix Rieseberg i Anthropics tekniska personal sa att bygget tog ungefär en och en halv vecka.

Mest heltäckande är Anthropic Institutes inlägg [When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement). Där står att Claude i maj 2026 skrev över 80 procent av koden som slogs ihop i Anthropics kodbas, mot låga ensiffriga procent före Claude Code i februari 2025. Enligt en fotnot har Anthropics ledning offentligt uppskattat att 90 procent eller mer skrivs av Claude när man räknar in skript och experimentell kod. Mängden kod som en ingenjör slog ihop per dag låg ungefär still från 2021 till 2024 och var runt åtta gånger högre andra kvartalet 2026.

Anthropic är själva försiktiga. Kodrader är ett ofullkomligt mått och åttafaldigandet är nästan säkert en överdrift av den verkliga produktivitetsvinsten. Att Claude skriver koden är dessutom något annat än att Claude bygger nästa modell på egen hand.

**OpenAI.** När OpenAI [släppte GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/) den 5 februari 2026 skrev de att det var deras första modell som varit avgörande i att skapa sig själv. Codex-teamet använde tidiga versioner för att felsöka modellens egen träning, hantera utrullningen och analysera test- och utvärderingsresultat. Det är OpenAI:s egen beskrivning av hur arbetet gick till, och det är ett smalare påstående än Anthropics siffror om hur stor del av koden som skrivs av modellen. Någon motsvarande procentsiffra från OpenAI själva har jag inte hittat.

## Har takten ökat?

Det finns belägg för att släppen blivit tätare. [Fast Company](https://fastcompany.com/91611158/why-ai-model-releases-feel-nonstop) räknar att tiden mellan Anthropics modellsläpp krympte från ungefär 46 dagar första halvåret 2026 till ungefär 26 dagar andra halvåret. Tidslinjen ovan pekar åt samma håll, med många nya produkter och funktioner på kort tid efter att Claude Code kom.

Artikeln är dock skeptisk till orsaken. Tiden mellan helt nya flaggskepp har ändrats lite för både Anthropic och OpenAI, och många släpp är omprissatta eller ompaketerade versioner av äldre modeller. En analytiker på IDC tvivlar på att självförbättrande system ligger bakom och pekar på konkurrens och bättre förståelse för vad marknaden efterfrågar. En analytiker på Gartner menar att bolagen tajmar släpp för att försvara marknadsandelar och binda kunder. Att takten ökat är alltså belagt, men varför är det inte.

## Hur Anthropic beskriver Cowork och skills

När Cowork släpptes hette inlägget [Cowork: Claude Code for the rest of your work](https://claude.com/blog/cowork-research-preview). Anthropic skriver där att Cowork är byggt för kunskapsarbete som inte är kodning, och att det använder samma agentiska arbetssätt som Claude Code. [TechCrunch](https://www.techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/) skrev att verktyget delvis byggde på att allt fler prenumeranter redan använde Claude Code till annat än kod, och att Cowork inte kräver kommandorad eller virtuella miljöer. Enligt tidningen gör det verktyget mindre avskräckande för icke-tekniska användare.

Skills är ett exempel på hur Anthropic själva arbetar. De skriver att de [använder skills i Claude Code i stor utsträckning internt](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills), med hundratals i aktiv användning, och att nyttiga skills sprids organiskt mellan kollegor innan de blir en del av ett gemensamt galleri. I [lanseringsinlägget](https://claude.com/blog/skills) står att Claude redan använde skills för att skapa filer som kalkylblad och presentationer i Claude-apparna.

## Modellerna har också blivit bättre

Utvecklingen handlar inte bara om produkter. Det bästa måttet jag hittat kommer från forskningsorganisationen METR. De mäter hur långa uppgifter en modell klarar, mätt i hur lång tid de tar för en människa. Längden där modellen lyckas ungefär varannan gång kallas tidshorisont.

Enligt METR:s [uppdaterade mätning](https://metr.org/blog/2026-01-29-time-horizon-1-1/) har tidshorisonten fördubblats ungefär var sjunde månad sedan 2019. Sedan 2024 går det snabbare, med en fördubbling ungefär var tredje månad. Claude Opus 4 från våren 2025 hamnar kring 100 minuter och Claude Opus 4.5 hösten 2025 kring 320 minuter.

METR påpekar själva att osäkerhetsintervallen är breda och att uppgifterna mest rör programmering, maskininlärning och säkerhet. [Sidan om tidshorisonter](https://metr.org/time-horizons/) uppdateras dessutom inte längre aktivt. Ett test på väldefinierade uppgifter säger inte hur modellen klarar en rörig vardag.

??? begrepp "Begrepp: Benchmark"
    --8<-- "benchmark.md"

    [Se alla begrepp i ordlistan](ordlista.md#benchmark)

Särskilt för långa, självständiga uppgifter är modellerna alltså märkbart bättre än när Claude Code lanserades.

## Min tes

Det här avsnittet är min egen bedömning, inte fakta. Jag är student och har ingen insyn i hur Anthropic resonerar. Anthropic skriver inte själva att syftet med produkterna är att sänka en tröskel.

- AI-stödd utveckling gör att Anthropic hinner bygga mycket mer produkt.
- Förutsättningarna för de nya produkterna fanns redan i en vanlig prenumeration. Produkterna fanns inte, men allt som behövdes för att bygga motsvarande själv fanns. Tröskeln var terminalen, att ge Claude rätt mappar och att skapa egna MCP-kopplingar. Effekten av produkterna blir att tröskeln sänks och att fler kommer åt det som redan gick att göra.
- Det Anthropic släpper har troligen hög korrelation med hur användare och Anthropic själva använder Claude. De ser vad som fungerar och gör en färdig mall av det. Skills är ett exempel, se [hur de används internt](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) och [lanseringsinlägget](https://claude.com/blog/skills).
- Det är en medveten förenkling av något mer komplext. Modellerna har blivit bättre, och konkurrens och marknad spelar också roll.

## Förmågeöverhäng

Det finns ett begrepp för glappet mellan vad en modell kan och vad folk har kommit på att göra med den: förmågeöverhäng, på engelska capability overhang. Grundtanken är en latent förmåga som är betydligt större än den som används i praktiken. [AI Wiki](https://aiwiki.ai/wiki/capability_overhang) går igenom hur termen används. Den moderna betydelsen brukar kopplas till Jack Clark, som i nyhetsbrevet [Import AI 321](https://jack-clark.net/2023/03/21/import-ai-321-open-source-gpt3-giving-away-democracy-to-agi-companies-gpt-4-is-a-political-artifact/) i mars 2023 skrev att varken OpenAI eller deras partner visste hur stor GPT-4:s förmåga egentligen var, och att de användningar man såg då var de förhållandevis enkla.

Med det som bakgrund kan min tes sägas så här: en del av förmågeöverhänget har suttit i tröskeln. Förmågan fanns, men den som inte ville använda en terminal kom aldrig åt den. När tröskeln sänks syns överhänget som nya användningar, och det ser ut som att modellerna plötsligt blivit smartare. Ibland har de det. Ibland har bara fler fått tillgång till det som redan fanns.

## Vad det betyder för dig

Tröskeln är lägre än många tror. Du behöver inte kunna programmera. Mycket av det som för två år sedan krävde en terminal går i dag att göra i Claude-appen, med en mapp du väljer och en uppgift du beskriver.

Den som går ett steg upp i trappan, från chatt till projekt, till appen på datorn eller vidare till Claude Code, får tillgång till sådant som modellen redan kan. Trappan beskrivs i [kapitel 01](01-fran-chatt-till-system.md). Du får fler saker att ge modellen att arbeta med. Ju mer självständigt Claude arbetar, desto viktigare är det att du säger vad den får ändra och läser resultatet som ett utkast.

En ironisk slutpoäng: med den här guiden arbetar jag på sätt och vis gratis som säljare åt Claude. Någon provision har jag inte sett röken av, men jag får åtminstone använda produkten för att skriva reklamen.

---

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny chatt i det projekt som kapitlet gäller, eller i ett projekt som håller koll på helheten om du har ett. Har du inget projekt än, börja med [setup-sessionen](kom-igang.md).

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/09-troskeln.md
    Guiden beskriver en persons upplägg och är inget facit. Kapitlet skiljer fakta med källor från författarens egen tes, så behandla tesen som hans bedömning och ta den med en nypa salt.
    Utgå från det du redan vet om mig i det här projektet och fråga bara om det som saknas.
    Fråga vad jag använder AI till i dag och vad som hindrar mig från nästa steg.
    Föreslå sedan ett första steg som passar mig.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 10: Därför slår du i taket](10-anvandningsgransen.md)
