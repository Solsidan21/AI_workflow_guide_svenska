# Kapitel 07 — Att bygga vidare på

*Ett system som fungerar är sällan färdigt. Här går jag igenom var mitt eget system har glapp och vilka sätt det finns att utveckla det, plus några idéer som inte alls handlar om plugg.*

!!! abstract "Kort version"
    - Kapitlet är en idébank över var systemet har glapp och hur det kan utvecklas.
    - Begrepp, misstag och repetition är de delar som oftast är minst strukturerade.
    - Lärdomar kan föras tillbaka till gemensamma mallar och mappar, så att nästa kurs eller projekt börjar starkare.
    - Det behöver finnas en tydlig gräns för vad som är offentligt och vad som är privat.
    - Du väljer det som passar dig och låter resten ligga.

Det som följer är inga löften om vad jag kommer att bygga. Det är en lista över möjligheter, hämtade från de ställen där jag själv märker friktion. Läs den som en idébank: välj det som passar ditt eget upplägg och låt resten ligga. Plugget är fortfarande exemplet. Varje punkt har en motsvarighet i ett jobb, en hobby eller en vardag med många bollar i luften, och jag pekar ut den där det är tydligt.

## Var friktionen sitter

I kapitel 05 beskrev jag hur jag läser en kurs nerifrån och upp, med förklaringar som utgår från varför. Det fungerar, men när jag letar efter svaga punkter i systemet hamnar jag nästan alltid hos begreppen. Kursmaterialet är stabilt och delat, och statusen är föränderlig och privat. Begreppen är det som binder ihop dem, och just de är den minst strukturerade delen.

Begrepp finns idag på tre ställen. Definitioner och satser ligger i kursens fulltext, med rubriker som går att länka till. Begrepp jag har haft svårt för dyker upp i loggen och under en rubrik för sådant som är osäkert. Och för en av mina andra kurser finns en separat begreppsöversikt med modeller, distinktioner och fällor från gamla duggor, men den är byggd för just den kursen. Fyra saker skaver:

- En förklaring som fungerade, som bilden av gradienten som berg och karta, står som en loggrad med datum. Loggen är kronologisk, så förklaringen hittas inte nästa gång begreppet dyker upp.
- Beroendena mellan begrepp är underförstådda. Att Hessianen bygger på Taylor framgår bara av studieplanens ordning och av löptexten i sammanfattningarna.
- Misstagen loggas, men de kopplas inte till ett begrepp. Jag kan inte fråga "vilka begrepp har jag oftast fel på?".
- Det jag lär mig i en konversation når inte kursens repo om jag inte aktivt för över det.

Allt nedan är olika sätt att möta de fyra punkterna.

## En begreppsmapp per kurs

Det mest närliggande draget är en mapp `begrepp/` i varje kursrepo, med en fil per begrepp och samma fyra fält i alla filer:

1. Definitionen, ordagrant ur kursens egen text, med länk till ankaret i fulltexten.
2. Varför den gäller, alltså den intuition som gör att regeln känns rimlig.
3. En konkret bild eller analogi som har fungerat.
4. Vanliga fel, helst hämtade från mina egna misstag och från gamla tentor.

Poängen är att en förklaring som en gång har fungerat får ett hem. I stället för att dö i en logg kan den hämtas av Claude nästa gång begreppet kommer upp, också i en annan kurs där samma idé återkommer. Rubrikerna i fulltexten ger redan färdiga ankare att länka till, så filerna behöver inte kopiera kursens text.

Samma tänk går att använda utanför studierna. En fil per återkommande begrepp i ett arbete, med definition, varför det spelar roll och typiska missförstånd, är en liten personlig ordlista som Claude kan läsa innan den svarar.

??? begrepp "Begrepp: Repo"
    --8<-- "repo.md"

    [Se alla begrepp i ordlistan](ordlista.md#repo)

## En översikt över hur begreppen beror av varandra

Den andra möjligheten är en liten fil per kurs som för varje begrepp anger vad det förutsätter och vad det behövs för. För flervariabelanalys skulle en rad kunna säga att Hessianen förutsätter Taylors formel och partiella derivator, och att den behövs för klassificering av kritiska punkter. Det är exakt den vy en läsare som går nerifrån och upp behöver, och idag finns den bara i mitt huvud.

Filen kan delvis genereras. Jag har redan ett skript som bygger ett uppgiftsindex ur fulltexten, och ett liknande skript skulle kunna plocka ut hänvisningar mellan definitioner och satser. Resten skriver Claude och jag tillsammans, och jag granskar. En färdig beroendeöversikt gör också studieplanen mer exakt: ordningen på veckorna kan kontrolleras mot den i stället för att bygga på min magkänsla.

Utanför plugget är motsvarigheten en översikt över vad som måste vara klart innan något annat kan börja. Det fungerar för ett projekt på jobbet lika väl som för en kurs.

## Taggade misstag

Om varje loggrad får en etikett med det begrepp den handlar om kan ett skript, eller Claude, sammanställa vilka begrepp som oftast går fel. Det räcker med en enkel konvention, till exempel att varje rad börjar med begreppets filnamn inom hakparenteser. Efter några veckor går det att fråga loggen vilka tre begrepp som har flest rader, och sedan lägga tiden där.

Det stänger också återkopplingsslingan. Ett misstag blir inte bara en notering utan en signal till begreppsmappen: den här filen behöver en bättre bild eller ett tydligare fel i fältet för vanliga fel.

## Repetition med ökande intervall

Mina schemalagda uppgifter styr redan efter närhet till tentan och antal timmar som är kvar. Nästa tänkbara steg är att de också föreslår repetition av sådant som loggats som osäkert, med växande avstånd mellan tillfällena: efter en dag, efter tre, efter en vecka, och så vidare tills begreppet har suttit några gånger i rad. Underlaget vore taggarna från förra avsnittet.

??? begrepp "Begrepp: Schemalagd uppgift"
    --8<-- "schemalagd-uppgift.md"

    [Se alla begrepp i ordlistan](ordlista.md#schemalagd-uppgift)

Det som skulle behövas är en datumkolumn per begrepp som uppdateras när jag svarar rätt eller fel, och en regel om att morgonbrevet bara föreslår det som är dags. Det är inte komplicerat, men det kräver att någon, antingen jag eller en uppgift med strikta regler, är ansvarig för att skriva till den kolumnen. Principen om en skrivare per dokument gäller även här.

Specialtjänster för flashcards gör just det här färdigt och snyggt, och jag återkommer till dem i nästa kapitel. Skälet att ändå bygga själv är att repetitionen då styrs av mina egna taggade misstag och av kursens begrepp, inte av ett generiskt kortset.

## Föra upp lärdomar till repot

Det som jag lär mig i ett kursprojekt hamnar i statusdokumenten på Drive, medan det varaktiga materialet bor i repot. Ett avslutande steg efter varje pass kunde knyta ihop dem: de begrepp som loggats som osäkra sammanställs och föreslås som ändringar i `begrepp/`. Kursprojektet föreslår, jag läser igenom och pushar med det skript jag redan använder. Då har ingen automatisk process rätt att skriva i det som är offentligt, och en människa har sista ordet.

Samma mönster är användbart i vilket system som helst med två lager. Det föränderliga får hållas lösligt, men det som ska bli bestående passerar en granskning på vägen.

## En gemensam mall för nya kursrepon

Skelettet i mina repon är redan likadant: ett index, kursmaterial, föreläsningar, studieplan, tentor, fulltext och skript. Det som skulle göra nästa kurs billigare är en kopierbar mall som även innehåller:

- en `CLAUDE.md` med grundreglerna, till exempel att motivera varje steg och definiera symboler
- en specifikation för hur fulltexten ska extraheras, med lärdomen att sidgränser tappar innehåll
- verifieringsskript som kontrollerar att ingen sats eller definition saknas
- en tom `begrepp/` med fältmallen

Med en sådan mall startar varje ny kurs med samma kvalitetskontroller, och jag slipper återupptäcka samma fällor.

??? begrepp "Begrepp: CLAUDE.md"
    --8<-- "claude-md.md"

    [Se alla begrepp i ordlistan](ordlista.md#claude-md)

Ett företag eller en förening med flera projekt har samma behov. En mall för nya projekt, med regelfil, mappskelett och kontrollskript, gör att kvaliteten inte beror på vem som startade just det här projektet. Bilagan om arbetslivet visar en större variant av det.

## Fler kvalitetskontroller

Idag kontrolleras fulltextens täckning av skript. Motsvarande kontroll saknas för resten. Några exempel på vad som går att kontrollera automatiskt:

- att varje avsnitt i studieplanen har minst en logg- eller testrad
- att varje begrepp som nämns i planen har en fil i `begrepp/`
- att länkarna från begreppsfilerna till fulltextens ankare leder någonstans
- att numreringen stämmer när kursboken finns i två upplagor, vilket just nu hålls i fas för hand

Kontrollerna behöver inte vara avancerade. Ett skript som skriver ut en lista över saknade rader är värt mycket, eftersom det ersätter en känsla av att allt nog är med av ett svar som går att lita på.

## Tydlig gräns för vad som är offentligt

Mina kursrepon är offentliga, medan Drive och minnet är privata. Den gränsen skyddas bäst av att den står skriven där arbetet sker. En kort regel i varje `CLAUDE.md` om vad som får skrivas i repot och vad som ska stanna på Drive är ett billigt skydd mot misstag. I praktiken kan regeln lyda ungefär så här:

```markdown
## Vad som får skrivas i repot
- Kursinnehåll, begrepp, förklaringar och studieplaner.
- Aldrig personuppgifter, resultat, ekonomi eller annat som rör privatlivet.
- Aldrig lösningar eller upplägg för inlämningsuppgifter.
- Osäker? Skriv det i Drive-dokumentet i stället och fråga mig.
```

Samma sorts regel behövs på varje ställe där ett privat och ett offentligt lager möts, som i ett jobb där en del av materialet är kundens och en del är ditt eget.

## Idéer utanför plugget

Det här är samma byggstenar i andra miljöer, utan att något av det är beslutat.

- Ett projekt för en hobby, där regelfilen beskriver hur du vill ha hjälp och en mapp samlar det du lärt dig och vill komma ihåg. Taggade misstag och intervallrepetition fungerar lika bra för en teknik i en sport eller ett instrument som för en sats i analys.
- Ett hushållsprojekt för sådant som återkommer, som inköp, matplanering eller en årlig deklaration. En schemalagd uppgift kan påminna i tid, och en regel om att aldrig hitta på hindrar att något påstås vara gjort när det inte syns i källorna.
- Ett arbetsprojekt för det du lär dig på ett nytt jobb: begrepp, förkortningar, interna processer. Begreppsmappen blir då en personlig introduktionsbok som växer av sig själv.
- En enkel loggrutin för ett eget byggprojekt, där Claude ställer samma tre frågor efter varje arbetspass och föreslår vad som ska föras in i regelfilen.

Gemensamt för alla fyra är att ingen av dem kräver mer än en vanlig prenumeration och en mapp. Börja med det som skaver mest i just din vardag, bygg det minsta som hjälper, och låt nästa steg komma ur det du märker.

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/07-bygga-vidare.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Fråga var jag själv märker friktion i mitt arbetssätt just nu.
    Hjälp mig sedan att välja en av idéerna i kapitlet och bygga den minsta versionen av den.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 08: Modellerna](08-modellerna.md)
