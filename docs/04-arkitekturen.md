# Kapitel 04 — Arkitekturen

> *Några mappar, några projekt och ett kalkylark räcker långt, så länge det är tydligt vem som skriver vad och var saker bor. Här visar jag hur delarna hänger ihop i min egen setup.*

!!! abstract "Kort version"
    - Tumregeln för var något ska ligga är vem som läser det, inte hur ofta det ändras.
    - Det ger tre lager: maskinlagret som Claude läser, människolagret som du och andra läser, och kunskapslagret som talar om för Claude vad den vet och hur den ska arbeta.
    - Ett projekt per område ger ren kontext. Projekt fungerar ungefär som mappar, men de kan inte ligga i varandra och ser inte varandra.
    - Därför speglar varje projekt sitt läge till ett delat kalkylark, som Hjärnan och de schemalagda uppgifterna läser.
    - Varje dokument har en enda skrivare men många läsare, vilket förhindrar dubbletter och inaktuell information.
    - Du bygger delarna i den takt behovet uppstår, och inget av dem måste göras om i efterhand.

Hittills har guiden handlat om enskilda delar: hur du skriver prompter, hur du ordnar material i mappar och hur CLAUDE.md styr arbetet. Det här kapitlet handlar om helheten. När du har fler än ett område, till exempel flera kurser samtidigt, behöver delarna ett gemensamt upplägg. Annars börjar information ligga på fel ställen, bli inaktuell eller dupliceras.

Jag använder mina kurser som exempel eftersom det är där jag byggt mest. Upplägget är inte bundet till plugg. Mot slutet av kapitlet visar jag hur exakt samma arkitektur ser ut i ett jobb.

## Tumregeln: vem läser?

Den vanligaste frågan när man bygger sitt upplägg är var saker ska ligga. Tidigare gav jag tumregeln att det som ändras ofta hör hemma i Drive. Den är inte fel, men den leder lätt fel. En bättre fråga är vem som läser. Då faller innehållet i tre lager.

| Lager | Vad det är | Var det hör hemma |
|---|---|---|
| Maskinlagret | Det som främst Claude läser och skriver: att göra-listan, läget per område, loggar och speglingar mellan projekt | Där det är billigast och tydligast för Claude, och där dina schemalagda uppgifter når det |
| Människolagret | Det du och andra läser: en affärsplan, ett CV, en text ni skriver tillsammans | Drive eller motsvarande, eftersom delning och mobilen spelar roll |
| Kunskapslagret | Det som talar om för Claude vad den vet och hur den ska arbeta: kursmaterial, regelfiler, projektinstruktioner och minne | Repon, projektinstruktioner, projektkunskap och minnet |

Lagren går in i varandra. Även maskinlagret bör gå att läsa för en människa ibland. Jag öppnar sällan min att göra-lista, eftersom morgonbrevet berättar det jag behöver veta. Men när jag blir klar med något mellan två brev vill jag kunna se allt på en gång. Därför ligger listan i ett kalkylark med flikar för Claude och en flik för mig, som [avsnittet om arket](#ett-ark-som-delat-skikt) visar. Frågan om vem som läser avgör alltså inte bara var något ska ligga, utan också vilket format det ska ha.

## Fem delar

Min setup består av fem delar. Det enklaste sättet att se dem är en skiss där information rör sig från sådant som sällan ändras till sådant som ändras varje dag.

```
  LOKALT (~/Projects/Plugg)             GITHUB
  en mapp = ett repo per kurs   --->    samma repo, pushas med ett skript
  (kursmaterial, fulltext, tentor)            |
                                              | läggs till som kunskap
                                              v
                             CLAUDE-PROJEKT, ett per kurs
                             (+ ett centralt projekt för helheten)
                                   |                       ^
                  skriver status   |                       | läser
                                   v                       |
                    GOOGLE-ARKET "HJÄRNAN" I DRIVE
                    Att göra + en rad per kurs + logg + Översikt
                                   |
                  läses av         v
                    SCHEMALAGDA UPPGIFTER (morgon, eftermiddag, natt)
                    + GOOGLE KALENDER (allt som har en fast tid)
```

Gå igenom skissen uppifrån och ned. Det som ligger högst upp är stabilt och delat. Det som ligger längst ned är föränderligt och personligt. Den fördelningen är hela poängen med arkitekturen, och jag återkommer till den.

## Lokala mappar och GitHub

Alla mina kursmappar ligger på samma ställe på datorn, och varje kurs är ett eget repo. Alla repon har samma skelett: en mapp för översikt och index, en för kursmaterial, en för föreläsningar, en för studieplan, en för gamla tentor, en för bokens innehåll, en för fulltext och en för skript. Att skelettet är detsamma gör att Claude hittar rätt oavsett kurs. Kapitel 03 går igenom varför.

??? begrepp "Begrepp: Repo"
    --8<-- "repo.md"

    [Se alla begrepp i ordlistan](ordlista.md#repo)

Repona synkas till GitHub. Där kan de läggas till som kunskap i ett Claude-projekt, vilket är kopplingen mellan filerna på min dator och det Claude faktiskt har framför sig när jag pratar med den.

??? begrepp "Begrepp: GitHub"
    --8<-- "github.md"

    [Se alla begrepp i ordlistan](ordlista.md#github)

Själva pushandet sköter jag med ett litet skript som pushar alla kursrepon i ett svep. Det går att dubbelklicka på i filhanteraren, så att synken inte kräver att jag öppnar en terminal. Det är en detalj som låter obetydlig, men en rutin som är besvärlig att köra är en rutin som slutar köras.

Vem skriver här? Jag och Claude Code bygger repona tillsammans. Efter att en kurs är uppsatt är innehållet i huvudsak statiskt. Claude i kursprojektet läser repot men skriver aldrig till det.

## Ett projekt per område

Varje kurs har ett eget Claude-projekt med kursens repo som kunskap. Projektinstruktionerna är en kortversion av CLAUDE.md i repot. Anledningen är praktisk: instruktionerna i projektet är det första Claude ser, så de viktigaste reglerna ska stå där utan att Claude först behöver läsa hela filträdet.

??? begrepp "Begrepp: Projekt"
    --8<-- "projekt.md"

    [Se alla begrepp i ordlistan](ordlista.md#projekt)

Att ha ett projekt per område och inte ett enda stort projekt för allt har två fördelar. Kontexten blir ren, så Claude blandar inte ihop reglerna för en kurs med en annans. Och det går att ge varje projekt just de regler som passar området. En kurs där matematisk kommunikation examineras kräver andra instruktioner än en kurs som bygger på modeller och begreppsdistinktioner.

Utöver kursprojekten har jag ett centralt projekt som håller koll på helheten. Det får ett eget kapitel, kapitel 06.

## Hur projekten hänger ihop

Ett projekt kan liknas vid en mapp. Det som finns i den är det Claude har att arbeta med när du startar en chatt där. Det mesta i ditt Claude-konto går att tänka på som textfiler i sådana mappar:

- *Projektinstruktionerna* är en regelfil som läses först i varje chatt i projektet.
- *Projektkunskapen* är filerna i mappen.
- *Minnet* är korta anteckningar som Claude själv för om dig. Kontots minne gäller överallt. Varje projekt har dessutom ett eget minne som bara gäller där, och i projektets inställningar väljer du om det ska vara kopplat till kontots minne eller hållas helt för sig. [Kapitel 02](02-kontext.md#minne-vad-claude-kommer-ihag-mellan-samtal) går igenom minnet närmare.
- *Chattar och projektdokument* stannar i sitt projekt.
- *Artifacts*, alltså de dokument och sidor Claude gör åt dig, ligger på kontot och kan nås från alla projekt.

Det betyder att projekten inte ser varandra. Ett kursprojekt vet inte vad som händer i ett annat, och ett centralt projekt ser inte in i kursprojekten av sig självt. Det är en fördel, eftersom kontexten blir ren, men det lämnar frågan om vem som ser helheten.

Lösningen i min setup kallar jag speglingsmönstret. Varje projekt skriver en kort status till ett delat ställe som det centrala projektet och de schemalagda uppgifterna läser. Hos mig är det en rad per kurs i ett kalkylark, plus en loggrad efter varje pass. Kursens egen plan bor kvar i kursprojektet. Det som speglas är bara det helheten behöver veta: nästa examination, läget och nästa steg.

??? note "För dig som kan Claude Code: samma byggstenar med lägre tröskel"
    Har du använt Claude Code finns det en liknelse som gör hela upplägget lättare att förstå.

    Tänk dig att du utvecklar tre appar. I Claude Code får varje app en egen mapp med en egen CLAUDE.md, och de tre mapparna kan ligga i en gemensam övermapp som också har en CLAUDE.md. I den övre står det som gäller allt: vem du är, hur du vill arbeta och hur apparna hänger ihop. I varje undermapp står bara det som gäller just den appen.

    Du utvecklar inte apparna från övermappen. Startar du en session där ser Claude allt på en gång, och då ökar risken att den arbetar i fel app eller blandar ihop reglerna. När du bygger en viss app öppnar du sessionen i dess mapp. Övermappen använder du till annat: att se helheten, planera mellan apparna och ändra det som gäller alla.

    Översatt till Claude är varje projekt en sådan undermapp. Projektinstruktionerna motsvarar undermappens CLAUDE.md, projektkunskapen motsvarar filerna i mappen och projektets minne motsvarar en anteckningsfil som Claude själv för. Kontots minne och dina allmänna inställningar motsvarar övermappens CLAUDE.md, som gäller överallt. Varje chatt motsvarar en session.

    Skillnaden är att Claude inte låter dig lägga projekt i projekt. Det finns ingen övermapp som ser in i undermapparna. Hjärnan i [kapitel 06](06-hjarnan.md) är mitt sätt att gå runt det: ett vanligt projekt som spelar övermappens roll och som ser vad som händer i de andra projekten genom att de speglar sitt läge till ett delat ark.

    Jag ser därför Claude som en tillämpning av samma byggstenar som Claude Code, paketerade för att sänka den tekniska tröskeln. I Claude Code behöver du hålla ordning på mappar, filer och en terminal. I Claude får du ett bekvämare gränssnitt och mobilen, men byggstenarna är i grunden desamma. Det hänger ihop med min tes i [kapitel 09](09-troskeln.md#min-tes), att mycket av Anthropics produktutveckling handlar om att sänka tröskeln till det som redan gick att göra. Anthropic presenterade själva Cowork, som numera är en del av Claude-appen, som Claude Code för resten av ditt arbete.

    Liknelsen är en tankemodell, inte en beskrivning av hur produkterna byggdes. Projekt fanns i Claude innan Claude Code släpptes, och allt motsvarar inte varandra exakt. I Claude Code kan Claude själv ändra sin CLAUDE.md, medan du i Claude klistrar in ändringar i projektinstruktionerna själv. Som karta tycker jag ändå att den stämmer, och den förklarar varför samma principer fungerar i båda. Anthropic har dessutom börjat föra in projekt i Claude Code, i beta när det här skrevs, vilket pekar åt samma håll. Ser du det annorlunda vill jag gärna höra det.

## Ett ark som delat skikt

Kursprojekten behöver ett sätt att berätta för det centrala projektet och för mina schemalagda uppgifter hur det går, och jag behöver ett ställe där allt jag ska göra står. Båda bor i ett och samma Google-ark som heter Hjärnan, med fyra flikar:

- **Att göra:** en rad per sak, med kolumner för område, vad det är, när det lades till, när jag vill bli påmind, status, när det blev klart och en kommentar.
- **Plugg:** en rad per kurs med nästa examination, läget och nästa pass. Varje rad skrivs av sitt eget kursprojekt.
- **Plugglogg:** en rad per pass, också skriven av kursprojekten.
- **Översikt:** min dashboard. Den består bara av formler som läser de andra flikarna, och ingen skriver där.

Arket fyller alltså två lager på en gång. Dataflikarna är maskinlager som Claude läser och skriver rad för rad, och Översikt är människolagret som jag kan öppna i mobilen när jag vill se allt på en gång.

Anslutningen mellan Claude och Drive sker via en connector.

??? begrepp "Begrepp: Connector"
    --8<-- "connector.md"

    [Se alla begrepp i ordlistan](ordlista.md#connector)

### Varför ett ark och inte ett dokument

Jag började med vanliga Google-dokument: en att göra-lista med rubriker och ett statusdokument per kurs. Det fungerade, men det var dyrt och klumpigt för Claude. Att göra-listan var drygt 5 kB text, men när Claude läste den via kopplingen till Google Docs blev det ungefär 186 000 tecken, eftersom hela dokumentets struktur och formatering följer med. För att ändra en rad behövde Claude dessutom räkna ut var i dokumentet texten stod. I ett ark läser Claude bara de kolumner den behöver och skriver en rad i taget. Det blir snabbare, billigare och svårare att göra fel, och det är ett bra exempel på varför formatet spelar lika stor roll som platsen.

### Varför inte GitHub

Tidigare skrev jag att jag valde Drive för att slippa pusha manuellt. Det argumentet håller inte. Claude kan pusha själv, och min nattliga synk klonar redan ett repo varje natt.

GitHub är ändå fel ställe för just det här, av ett annat skäl. GitHub är byggt för filer och versionshantering, inte för en lista som en människa vill öppna och överblicka. Även om jag oftast bara läser morgonbrevet vill jag kunna gå in i listan och se varje sak, till exempel när jag blivit klar med något mellan två brev. Det gör jag enkelt i ett ark i mobilen, men inte i en datafil i ett repo. Till det kommer att varje session måste klona repot innan den kan läsa, och att två skrivare som ändrar samtidigt kan krocka.

### Om du börjar från noll

Drive är inte det enda svaret. Välj i första hand det du redan har. Nästan alla har ett Google- eller Microsoft-konto genom sin mejl, och då ligger Google Drive eller OneDrive nära till hands. Använder du redan Notion fungerar det lika bra, och Notion har en connector där Claude kan läsa och skriva sidor och databaser. GitHub har färre konto på, och det passar bättre för material som ska versionshanteras än för listor du vill överblicka.

Det viktiga är att listan finns där Claude, dina schemalagda uppgifter och du själv når den. För min del tillför Notion inget, eftersom Drive, GitHub och mina lokala filer redan täcker samma behov. Det säger mer om min setup än om Notion. För den som jobbar i ett team ser frågan annorlunda ut, vilket [bilagan om arbetslivet](bilaga-arbetsliv.md#nar-hjarnorna-ska-prata-med-varandra) tar upp.

Allt som har en fast tid bor i kalendern. Det som saknar tid bor i arket. Det går att tycka att det är en liten sak, men regeln gör att jag aldrig behöver fundera på var en uppgift hör hemma.

## Schemalagda uppgifter

Ovanpå Drive och kalendern ligger schemalagda uppgifter, alltså instruktioner som Claude kör på bestämda tider utan att jag är inblandad.

??? begrepp "Begrepp: Schemalagd uppgift"
    --8<-- "schemalagd-uppgift.md"

    [Se alla begrepp i ordlistan](ordlista.md#schemalagd-uppgift)

Jag har tre. En körs på morgonen och sammanfattar läget, en körs på eftermiddagen och gör en kort avstämning, och en körs på natten och synkar ett hobbyprojekts statusfiler till ett eget kalkylark. Två av dem läser bara. Den tredje skriver, men bara i ett enda ark och enligt strikta regler: aldrig ta bort något, alltid logga ändringen. De två första beskrivs i kapitel 06.

## Principen: en skrivare per dokument, många läsare

Det som håller ihop arkitekturen är en enda regel. Varje dokument har exakt en skrivare. Alla andra får läsa.

| Vad | Vem skriver | Vem läser |
|---|---|---|
| Kursrepot | jag och Claude Code, vid uppsättning | kursprojektet |
| Kursens rad i fliken Plugg och dess loggrader | kursprojektet | det centrala projektet och de schemalagda uppgifterna |
| Fliken Att göra | det centrala projektet, när jag nämner något | de schemalagda uppgifterna och jag |
| Fliken Översikt | ingen, bara formler | jag |
| Kalendern | det centrala projektet, för sådant med fast tid | alla |
| Speglingsarket för hobbyprojektet | bara den nattliga uppgiften | jag |

Regeln löser ett problem som annars dyker upp snabbt. Om två projekt kan skriva i samma dokument skriver de över varandra, eller så uppstår två versioner av sanningen och ingen vet vilken som gäller. Med en skrivare per dokument finns alltid ett svar på frågan "var ska jag titta?", och ett fel går att spåra till en enda källa.

Det betyder också att det centrala projektet aldrig ändrar i kursernas rader, hur frestande det än är när det ser att något är fel. Det rätta är att rapportera felet och låta kursprojektet rätta det. Ett litet extra steg, men det gör att jag kan lita på att varje dokument speglar vad dess ägare faktiskt vet.

## Stabilt och delat, föränderligt och privat

Arkitekturen delar upp information efter två egenskaper på samma gång.

Kursmaterial är stabilt. Det ändras sällan, det är detsamma för alla som läser kursen och det är ofta redan offentligt. Det passar i ett repo på GitHub, där det är versionshanterat och där flera verktyg kan läsa det.

Status är föränderlig och personlig. Hur långt jag har kommit, vad jag är osäker på och vad jag ska göra i morgon ändras varje dag och angår ingen annan. Det passar i arket i Drive, där en rad kan skrivas om utan att något behöver versioneras, och där jag själv kan läsa den.

En praktisk konsekvens är att gränsen mellan offentligt och privat följer lagren. Det som ligger i repona kan jag visa upp. Det som ligger i Drive är mitt. Därför skriver jag i varje CLAUDE.md en kort regel om vad som får hamna i repot, så att inget privat av misstag följer med vid nästa push.

??? begrepp "Begrepp: CLAUDE.md"
    --8<-- "claude-md.md"

    [Se alla begrepp i ordlistan](ordlista.md#claude-md)

## Lokalt, i Drive eller i Claudes moln

Tumregeln om vem som läser säger vilket lager något hör till. Här är platserna, och vad var och en är bra på.

**Claudes moln** är allt som ligger i ditt Claude-konto. Det består av fyra delar som ofta blandas ihop:

- *Projektinstruktioner* är reglerna för hur Claude ska arbeta i projektet. De läses i början av varje chatt i projektet, så det som måste gälla varje gång hör hemma här.
- *Projektkunskap* är referensmaterial som Claude kan läsa i alla chattar i projektet: en kursplan, riktlinjer, en mall, en beskrivning av dig. En uppladdad fil är en ögonblicksbild och uppdateras inte av sig själv. En kopplad källa, som mina GitHub-repon, följer med när källan ändras.
- *Minne* är det Claude själv väljer att spara om dig mellan chattar. Det är bra för bestående fakta men går inte att styra exakt, vilket [kapitel 02](02-kontext.md#minne-vad-claude-kommer-ihag-mellan-samtal) går igenom.
- *Chatthistorik och artifacts* är samtalen och de dokument eller sidor Claude har gjort, som du kan gå tillbaka till.

**Google Drive** (eller OneDrive, Notion och liknande, via en connector) är platsen för det som människor ska läsa och dela, och för maskinlager som du själv också vill kunna öppna, som min att göra-lista. Schemalagda uppgifter körs i molnet utan att din dator är på, så de når det som ligger där, alltså Drive, GitHub och ditt Claude-konto, men inte filer på datorn.

**Lokalt på datorn** kräver Claude-appen med kopplade mappar eller Claude Code. Här ligger det som är stort, det som ska bearbetas med verktyg och det som ska versionshanteras: mina kursrepon med fulltext och skript, regelfiler som CLAUDE.md och material som jag gör om från PDF till Markdown.

| Vad det är | Var det hör hemma |
|---|---|
| Regler för hur Claude ska arbeta i ett område | Projektinstruktioner |
| Stabilt material som ska läsas, till exempel en kursplan | Projektkunskap |
| Fakta om dig som är bra att Claude minns | Minne |
| Listor och status som Claude skriver och du vill kunna läsa | Ett ark i Drive |
| Det som bara Claude läser | Där det är billigast för Claude, till exempel ett repo eller en fil i projektet |
| Det du delar med andra människor | Drive, i en delad mapp |
| Stora mängder rådata, skript och sådant som versionshanteras | Lokalt, och vid behov GitHub |

Du behöver inte alla tre från början. Med bara projekt och Drive kommer man långt, och det fungerar på alla enheter. Den lokala delen blir intressant först när du vill att Claude ska arbeta med många filer på en gång eller bygga saker åt dig. Setup-sessionen på sidan [Kom igång](kom-igang.md) går igenom fördelningen utifrån vad du har.

## Samma arkitektur i ett jobb

Inget i det här är specifikt för kurser. Byt ut orden så ser det ut så här.

| I mitt plugg | I ett jobb |
|---|---|
| Ett repo per kurs | En mapp per kund, projekt eller affär med avtal, underlag och mallar |
| Kursprojekt med repot som kunskap | Ett Claude-projekt per kund eller team med mappen som kunskap |
| En rad per kurs i fliken Plugg | Ett statusdokument eller en rad per kund: läget, nästa steg, öppna frågor |
| Att göra-listan | En gemensam lista över åtaganden |
| Kalender | Kalender, precis som förut |
| Morgon och eftermiddag | En sammanfattning inför dagens möten och en avstämning på eftermiddagen |

Stabilt och delat blir kundens underlag, era mallar och policyer. Föränderligt och privat blir status, anteckningar och bedömningar. Principen om en skrivare per dokument gäller oförändrad: den som äger kundrelationen skriver statusdokumentet, andra läser. Samma upplägg fungerar för en hobby med flera delprojekt, för ett föreningsuppdrag eller för ett litet företag. Hur flera personers upplägg kan prata med varandra tar [bilagan om arbetslivet](bilaga-arbetsliv.md#nar-hjarnorna-ska-prata-med-varandra) upp.

Du behöver inte bygga allt på en gång. Börja med en mapp och ett projekt för det område där du tillbringar mest tid. Lägg till en statusrad när du märker att du förklarar läget för Claude om och om igen. Lägg till schemalagda uppgifter först när du har något som är värt att sammanfatta varje dag. Arkitekturen växer med behovet, och varje lager går att lägga till i efterhand utan att det som redan finns behöver göras om.

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny chatt i ditt Hjärnan-projekt, eller i det projekt som kapitlet gäller. Har du inget projekt än, börja med [setup-sessionen](kom-igang.md).

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/04-arkitekturen.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Utgå från det du redan vet om mig i det här projektet och fråga bara om det som saknas.
    Fråga vilka områden jag har parallellt och var information hamnar fel eller blir inaktuell.
    Hjälp mig sedan att rita upp vilka lager jag behöver nu och vilket som är det första jag ska skapa.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 05: Individanpassad inlärning](05-individanpassad-inlarning.md)
