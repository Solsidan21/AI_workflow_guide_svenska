# Kapitel 04 — Arkitekturen

> *Några mappar, några projekt och ett par dokument räcker långt, så länge det är tydligt vem som skriver vad och var saker bor. Här visar jag hur delarna hänger ihop i min egen setup.*

!!! abstract "Kort version"
    - Upplägget består av fem lager, från sådant som sällan ändras till sådant som ändras varje dag.
    - Ett projekt per område ger ren kontext, och Drive eller liknande fungerar som delat skikt.
    - Varje dokument har en enda skrivare men många läsare, vilket förhindrar dubbletter och inaktuell information.
    - Det stabila och delade hålls isär från det föränderliga och privata.
    - Du bygger lagren i den takt behovet uppstår, och inget av dem måste göras om i efterhand.

Hittills har guiden handlat om enskilda delar: hur du skriver prompter, hur du ordnar material i mappar och hur CLAUDE.md styr arbetet. Det här kapitlet handlar om helheten. När du har fler än ett område, till exempel flera kurser samtidigt, behöver delarna ett gemensamt upplägg. Annars börjar information ligga på fel ställen, bli inaktuell eller dupliceras.

Jag använder mina kurser som exempel eftersom det är där jag byggt mest. Upplägget är inte bundet till plugg. Mot slutet av kapitlet visar jag hur exakt samma arkitektur ser ut i ett jobb.

## Fem lager

Min setup består av fem lager. Det enklaste sättet att se dem är en skiss där information rör sig från sådant som sällan ändras till sådant som ändras varje dag.

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
                    GOOGLE DRIVE, en delad mapp
                    en att göra-lista + ett statusdokument per kurs
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

## Drive som delat skikt

Här kommer arkitekturens viktigaste beslut. Kursprojekten behöver ett sätt att berätta för varandra, och för mina schemalagda uppgifter, hur det går. Jag valde Google Drive för det. I en delad mapp finns två sorters dokument: en att göra-lista och ett statusdokument per kurs.

Statusdokumentet har samma sektioner i varje kurs: nästa examination, läget, vad som är kvar, nästa pass, vad jag är osäker på och en logg. Det skrivs av kursprojektet, i takt med att jag arbetar. Det är kort, daterat och handlar bara om nuläget.

Anslutningen mellan Claude och Drive sker via en connector.

??? begrepp "Begrepp: Connector"
    --8<-- "connector.md"

    [Se alla begrepp i ordlistan](ordlista.md#connector)

Varför Drive och inte GitHub? Två skäl. Jag ville inte behöva pusha något manuellt för att en plan ska uppdateras. Och de schemalagda uppgifterna körs i molnet, utan att min dator är påslagen, så de behöver komma åt statusen utan att något körs lokalt. Ett dokument i Drive uppfyller båda kraven.

Allt som har en fast tid bor i kalendern. Det som saknar tid bor i listan eller statusdokumenten. Det går att tycka att det är en liten sak, men regeln gör att jag aldrig behöver fundera på var en uppgift hör hemma.

## Schemalagda uppgifter

Ovanpå Drive och kalendern ligger schemalagda uppgifter, alltså instruktioner som Claude kör på bestämda tider utan att jag är inblandad.

??? begrepp "Begrepp: Schemalagd uppgift"
    --8<-- "schemalagd-uppgift.md"

    [Se alla begrepp i ordlistan](ordlista.md#schemalagd-uppgift)

Jag har tre. En körs på morgonen och sammanfattar läget, en körs på eftermiddagen och gör en kort avstämning, och en körs på natten och synkar ett hobbyprojekts statusfiler till ett kalkylark. Två av dem läser bara. Den tredje skriver, men bara i ett enda ark och enligt strikta regler: aldrig ta bort något, alltid logga ändringen. De två första beskrivs i kapitel 06.

## Principen: en skrivare per dokument, många läsare

Det som håller ihop arkitekturen är en enda regel. Varje dokument har exakt en skrivare. Alla andra får läsa.

| Vad | Vem skriver | Vem läser |
|---|---|---|
| Kursrepot | jag och Claude Code, vid uppsättning | kursprojektet |
| Statusdokument per kurs | kursprojektet | det centrala projektet och de schemalagda uppgifterna |
| Att göra-listan | det centrala projektet, när jag nämner något | de schemalagda uppgifterna |
| Kalendern | det centrala projektet, för sådant med fast tid | alla |
| Speglingsarket för hobbyprojektet | bara den nattliga uppgiften | jag |

Regeln löser ett problem som annars dyker upp snabbt. Om två projekt kan skriva i samma dokument skriver de över varandra, eller så uppstår två versioner av sanningen och ingen vet vilken som gäller. Med en skrivare per dokument finns alltid ett svar på frågan "var ska jag titta?", och ett fel går att spåra till en enda källa.

Det betyder också att det centrala projektet aldrig ändrar i kursernas statusdokument, hur frestande det än är när det ser att något är fel. Det rätta är att rapportera felet och låta kursprojektet rätta det. Ett litet extra steg, men det gör att jag kan lita på att varje dokument speglar vad dess ägare faktiskt vet.

## Stabilt och delat, föränderligt och privat

Arkitekturen delar upp information efter två egenskaper på samma gång.

Kursmaterial är stabilt. Det ändras sällan, det är detsamma för alla som läser kursen och det är ofta redan offentligt. Det passar i ett repo på GitHub, där det är versionshanterat och där flera verktyg kan läsa det.

Status är föränderlig och personlig. Hur långt jag har kommit, vad jag är osäker på och vad jag ska göra i morgon ändras varje dag och angår ingen annan. Det passar i Drive, där det kan skrivas om utan att något behöver versioneras eller pushas.

En praktisk konsekvens är att gränsen mellan offentligt och privat följer lagren. Det som ligger i repona kan jag visa upp. Det som ligger i Drive är mitt. Därför skriver jag i varje CLAUDE.md en kort regel om vad som får hamna i repot, så att inget privat av misstag följer med vid nästa push.

??? begrepp "Begrepp: CLAUDE.md"
    --8<-- "claude-md.md"

    [Se alla begrepp i ordlistan](ordlista.md#claude-md)

## Samma arkitektur i ett jobb

Inget i det här är specifikt för kurser. Byt ut orden så ser det ut så här.

| I mitt plugg | I ett jobb |
|---|---|
| Ett repo per kurs | En mapp per kund, projekt eller affär med avtal, underlag och mallar |
| Kursprojekt med repot som kunskap | Ett Claude-projekt per kund eller team med mappen som kunskap |
| Statusdokument per kurs | Ett statusdokument per kund: läget, nästa steg, öppna frågor |
| Att göra-listan | En gemensam lista över åtaganden |
| Kalender | Kalender, precis som förut |
| Morgon och eftermiddag | En sammanfattning inför dagens möten och en avstämning på eftermiddagen |

Stabilt och delat blir kundens underlag, era mallar och policyer. Föränderligt och privat blir status, anteckningar och bedömningar. Principen om en skrivare per dokument gäller oförändrad: den som äger kundrelationen skriver statusdokumentet, andra läser. Samma upplägg fungerar för en hobby med flera delprojekt, för ett föreningsuppdrag eller för ett litet företag.

Du behöver inte bygga allt på en gång. Börja med en mapp och ett projekt för det område där du tillbringar mest tid. Lägg till ett statusdokument när du märker att du förklarar läget för Claude om och om igen. Lägg till schemalagda uppgifter först när du har något som är värt att sammanfatta varje dag. Arkitekturen växer med behovet, och varje lager går att lägga till i efterhand utan att det som redan finns behöver göras om.

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/04-arkitekturen.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Fråga vilka områden jag har parallellt och var information hamnar fel eller blir inaktuell.
    Hjälp mig sedan att rita upp vilka lager jag behöver nu och vilket som är det första jag ska skapa.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 05: Individanpassad inlärning](05-individanpassad-inlarning.md)
