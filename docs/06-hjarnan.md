# Kapitel 06 — Hjärnan

> *Ett centralt projekt som håller koll på helheten, så att jag slipper hålla allt i huvudet. Det här kapitlet visar hur det är uppbyggt och vilka regler som gör att jag kan lita på det.*

!!! abstract "Kort version"
    - Hjärnan är ett centralt projekt som överblickar helheten i vardagen, så att du slipper hålla allt i huvudet.
    - Kärnan är en lista med fasta rubriker och en tydlig prioriteringsordning.
    - Dokument från andra projekt läses men ändras aldrig härifrån.
    - Ett morgonbrev och en eftermiddagskoll gör att viktiga saker kommer till dig.
    - Regeln att aldrig hitta på gör att du kan lita på det som står i brevet.

I kapitel 04 beskrev jag arkitekturen med ett projekt per område. Det ger ren kontext, men det lämnar en fråga öppen: vem ser helheten? Ett kursprojekt vet hur det går i sin kurs, men inte vad som är viktigast just nu när flera saker pockar på uppmärksamhet samtidigt.

Det är den uppgiften jag har gett åt ett eget projekt som jag kallar Hjärnan. Namnet är en halv skämtsamhet, men beskrivningen stämmer: det är ett ställe som minns och överblickar, så att jag inte behöver göra det.

Mitt exempel är hur en student kan organisera sin vardag. Samma konstruktion passar för ett jobb med många parallella spår, för ett företag eller för vilken period som helst där flera saker konkurrerar om tid.

## Vad projektet är

Hjärnan är ett vanligt Claude-projekt. Det som gör det till något särskilt är instruktionerna och vilka källor det får läsa.

??? begrepp "Begrepp: Projekt"
    --8<-- "projekt.md"

    [Se alla begrepp i ordlistan](ordlista.md#projekt)

Instruktionerna gör tre saker. De anger en prioritetsordning mellan livsområdena. De talar om var saker finns. Och de beskriver vad Claude ska göra när jag nämner något jag behöver eller vill göra. Jag skriver inget hårt schema, för ett schema som inte överlever första veckan är värre än inget. I stället finns en ordning att luta sig mot när något måste väljas bort: tentor och administration kring studierna först, därefter vardagssysslor, jobb och till sist sådant som är roligt.

## Listan med rubriker

Hjärnans kärna är ett enda dokument med en lista. Den har en rubrik per livsområde, och en sista rubrik för det som är klart. Jag har valt rubriker som motsvarar de områden jag faktiskt delar upp mitt liv i, och du väljer dina egna. Antalet spelar mindre roll än att varje sak har ett självklart hem.

Reglerna för hur listan används är korta och ger mig mycket:

1. När jag nämner något jag vill göra läser Claude först listan.
2. Finns det redan där, utgår Claude från att jag vill ha hjälp med det nu och sätter igång.
3. Finns det inte, läggs det in under rätt rubrik med dagens datum, utan att Claude frågar. Därefter frågar Claude kort om vi ska göra det nu eller senare.
4. Om det blir senare och saken har en fast tid hamnar den i kalendern. Annars får den en påminnelse med ett datum, som fångas upp av nästa morgonbrev.
5. När något är klart flyttas det till den sista rubriken, med datum.

Det viktiga är punkt 3. Att behöva avgöra var en sak ska stå, och sedan formulera den, är exakt det som gör att man skjuter upp att skriva ned den. Om Claude gör det direkt kostar det mig ingenting att fånga en tanke. Jag vill inte heller behöva förklara mer än nödvändigt, så Claude väljer rubrik själv och skriver kort. Listan har en rad överst som visar när den senast uppdaterades, så att jag och de schemalagda uppgifterna kan se hur färsk den är.

## Kursdokument som läses men aldrig ändras

Förutom listan läser Hjärnan ett statusdokument per kurs. De skrivs av kursprojekten, som kapitel 04 beskrev. Här gäller ägarregeln utan undantag: Hjärnan läser dem och ändrar aldrig i dem.

Det kan kännas krångligt att inte låta det centrala projektet rätta ett uppenbart fel. Men det är precis regeln som gör att systemet håller. Om Hjärnan skrev i kursdokumenten skulle kursprojekten och Hjärnan kunna ha olika bilder av samma kurs, och då vet jag inte längre vilken jag ska tro. När Hjärnan ser något som inte stämmer säger den det till mig, och jag tar det med kursprojektet.

Läsningen ger ändå mycket. Hjärnan vet hur nära nästa examination är, hur många timmar som är kvar och vad jag själv har markerat som osäkert. Det räcker för att föreslå vad som är rimligt att göra en viss dag, utan att jag behöver sammanfatta något.

## Morgonbrev och eftermiddagskoll

De två schemalagda uppgifterna som läser listan och kursdokumenten är det som gör att Hjärnan märks i vardagen. Jag behöver inte öppna något, utan informationen kommer till mig.

??? begrepp "Begrepp: Schemalagd uppgift"
    --8<-- "schemalagd-uppgift.md"

    [Se alla begrepp i ordlistan](ordlista.md#schemalagd-uppgift)

Morgonbrevet kommer tidigt varje dag. Det läser listan, statusdokumenten och kalendern och skriver en sammanfattning av dagen. Ju närmare en examination, desto tydligare blir förslagen om hur mycket plugg dagen kräver. Brevet kan också hämta en nyhet eller en idé utifrån mina intressen, men bara som krydda.

Eftermiddagskollen är kortare. Den tittar på vad som har flyttats till den färdiga rubriken under dagen, på loggraderna i kursdokumenten och på resten av kvällens kalender, och skickar ett kort, uppmuntrande meddelande. Poängen är att det ska märkas när något har gått bra, och att jag ska få en lugn bild av hur resten av dagen ser ut.

Ingen av dem ändrar något i källorna. De läser och skriver ett meddelande, och det är allt. En uppgift som körs utan att jag ser den ska ha så litet utrymme att göra fel som möjligt.

## Brevet som en text, inte en lista

Morgonbrevet är skrivet som ett brev. Det beror på något jag lärde mig tidigt: en punktlista med dagens uppgifter känns som en order, och jag börjar undvika den. Ett brev i löpande text, där förslagen formuleras som "du skulle kunna", känns som hjälp.

Några av de val jag gjort i utformningen:

- Nyheter och idéer sprids ut mellan de delar som handlar om arbete, så att brevet inte blir en lång arbetslista med en bilaga.
- Förslag är förslag. Brevet talar om vad som vore klokt, men bestämmer ingenting.
- Brevet håller en vänlig men saklig ton. Det ska inte peppa, och det ska inte skuldbelägga om något blivit liggande.

??? begrepp "Begrepp: Prompt"
    --8<-- "prompt.md"

    [Se alla begrepp i ordlistan](ordlista.md#prompt)

Brevet slutar alltid med en färdig prompt i ett kodblock. Den innehåller det första jag skulle vilja be Hjärnan om den dagen, till exempel att gå igenom en viss sak eller sätta igång med dagens viktigaste pass. Jag kopierar den, klistrar in den i Hjärnan och är igång på några sekunder. Det tar bort det besvärligaste ögonblicket i en arbetsdag, nämligen att sitta framför en tom ruta och inte veta var man ska börja.

## Regeln "hitta aldrig på"

Alla mina schemalagda uppgifter har en gemensam regel i sina instruktioner: hitta aldrig på. Något får bara påstås om det syns i källorna. Om en uppgift inte finns i listan nämns den inte som klar. Om ett statusdokument inte uppdaterats skriver brevet att det inte uppdaterats, och gissar inte vad som kan ha hänt.

Regeln kan verka självklar, men den är nödvändig av en särskild anledning. När en uppgift körs utan att jag tittar på kan jag inte fånga ett påhitt i stunden. Och ett morgonbrev som ibland ljuger om läget är värre än inget brev, eftersom jag då måste kontrollera allt som står i det. Förtroendet för hela systemet hänger på att texten går att lita på utan kontroll.

I praktiken innebär regeln att varje påstående i ett brev ska kunna kopplas till en rad i en källa. Saknas underlag skriver uppgiften det rakt ut, och föreslår hellre att jag kollar än att den fyller i luckan.

## Så bygger du din egen

Du behöver inte kopiera mitt upplägg. Det här är en ordning som fungerar för att komma igång.

1. Skapa ett projekt och en lista med rubriker för de områden du faktiskt har. Börja med tre eller fyra.
2. Skriv projektinstruktioner med en prioritetsordning, var saker finns och de fem reglerna för hur listan används.
3. Låt det gå en vecka med bara listan. Justera rubrikerna efter vad som känns fel.
4. Lägg till ett statusdokument för det område som tar mest tid, med en tydlig regel om vem som skriver.
5. Lägg till ett morgonbrev när du har något att sammanfatta. Börja enkelt, med en uppgift som bara läser, och ge den regeln om att aldrig hitta på från första dagen.

Det går att göra i vilken ordning du vill, och det går att stanna efter första steget. Redan ett projekt med en lista och några tydliga regler ersätter mycket av det som annars bor i huvudet eller på lösa lappar.

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/06-hjarnan.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Fråga vilka områden som konkurrerar om min tid och vad jag oftast glömmer eller tappar bort.
    Hjälp mig sedan att skapa en första lista med rubriker och några regler för hur den ska skötas.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 07: Att bygga vidare på](07-bygga-vidare.md)
