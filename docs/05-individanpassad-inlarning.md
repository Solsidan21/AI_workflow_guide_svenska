# Kapitel 05 — Individanpassad inlärning

*En kurs är byggd för 500 studenter, eller 30. Med AI kan upplägget formas efter hur just du lär dig, och kursens ramar och mål ligger kvar. Kapitlet visar hur jag gjort det i Flervariabelanalys, och hur du gör ditt eget.*

!!! abstract "Kort version"
    - Kurser är byggda för en genomsnittlig student, och med AI kan upplägget formas efter hur just du lär dig.
    - Det börjar med en kartläggning av kursen och hur kapitlen hänger ihop, innan några uppgifter.
    - Ordningen följer begreppens beroenden, och konkreta bilder gör att abstrakta begrepp fastnar.
    - Regler i projektet tvingar fram förståelse i stället för memorering, och gamla tentor används som test.
    - Du formar ditt eget upplägg genom att beskriva hur du lär dig och vilka regler Claude ska följa.

---

## Problemet med den genomsnittliga studenten

En kurs har en bok, en föreläsningsserie och en ordning som passar ungefär alla. Det är rimligt. Ingen lärare kan bygga trettio olika kurser, och ännu mindre femhundra. Resultatet är ändå att ordningen, tempot och förklaringarna är valda för en student som inte finns.

Jag är en sådan student som inte passar ordningen. Jag lär mig nerifrån och upp. Jag har svårt att acceptera en regel innan jag förstår varför den gäller, och när en bit saknas faller jag tillbaka på att memorera procedurer. Det tar mig igenom en tenta men det känns inte som förståelse, och det håller inte till nästa kurs. Det som får något att klicka är en helhetsbild och en konkret bild, till exempel att uppskatta var en bil befinner sig när man vet hur fort den kör. Och jag lär mig mer av det som intresserar mig än av det som är svårt.

Med en vanlig prenumeration på Claude går det att bygga ett upplägg runt det. Det handlar inte om att kringgå kursen. Tentan, målen och kursboken är desamma. Det som ändras är vägen dit: vilken ordning jag läser i, hur saker förklaras, vad jag övar på och vad som följs upp.

Allt det här ryms i den prenumeration jag redan har. Det krävs ingen särskild studieapp, bara att modellen får rätt material och rätt regler.

Plugget är exemplet i det här kapitlet, inte ämnet. Allt som beskrivs nedan fungerar likadant när du ska lära dig ett nytt jobb, en bransch eller en hobby. Jag återkommer till det i slutet.

---

## Mitt fall: Flervariabelanalys

Kursen är MATB21 Flervariabelanalys på Lunds universitet, hösten 2026. Boken är Adams och Essex *Calculus*. Hela upplägget ligger öppet på GitHub, så du kan titta på de riktiga filerna: [Flervariabelanalys_ht26](https://github.com/Solsidan21/Flervariabelanalys_ht26). Jag hänvisar dit genom hela kapitlet.

Innan jag går in på mekanismerna vill jag visa var det började.

### Screenshot-cirkusen

På vårterminen läste jag Algebra och vektorgeometri. Jag satt med en uppgift, tog en screenshot och skickade den till Claude. Claude löste den snabbt och korrekt, men med Gauss-eliminering. Min kurs hade inte kommit dit. Vi använde ekvivalenta ekvationer och substitution.

Jag tog en ny screenshot, den här gången på facit, och skrev: "Lös som de gör här istället." Claude anpassade sig halvvägs men blandade fortfarande in notation som inte hörde till kursen. Tredje försöket var att tvinga Claude att läsa en hel föreläsnings-PDF på fyrtio sidor. Det funkade till slut, men det tog femton minuter. Nästa dag, ny uppgift, och Claude hade glömt allt.

Felet låg inte i modellen. Den fick kursens material i fel format, utan regler och utan minne mellan samtalen. Det här kapitlet handlar om vad som hände när jag i stället byggde ett system där kursens egen text och mina egna regler alltid finns med. De tekniska delarna, alltså mappar, Markdown och CLAUDE.md, förklaras i [kapitel 03](03-struktur.md). Här visar jag vad de används till för att lära sig.

---

## Steg 1: kartläggning före uppgifter

De flesta pluggplaner börjar med uppgifterna. Räkna 13.1 uppgift 5, 7, 14, sedan 13.2. Det är rimligt om man redan har en bild av området. Jag har ingen sådan bild på förhand, och uppgifter utan bild blir mekanik.

Därför börjar mitt upplägg med en kartläggning av kursen. Innan jag räknar något går Claude och jag igenom hur kapitlen hänger ihop och vad kursen i stort handlar om. I kursrepot finns det på två ställen. Det ena är [kapitelguiden](https://github.com/Solsidan21/Flervariabelanalys_ht26/blob/main/01_kursmaterial/kapitelguide.md), som för varje sektion anger ämnet, rekommenderade uppgifter och vad som är en "typisk lösning", alltså vilken sorts tänkande uppgifterna kräver. Det andra är en sammanfattning per kapitel i [`06_bokinnehall/`](https://github.com/Solsidan21/Flervariabelanalys_ht26/blob/main/06_bokinnehall/kap_13_partiella_derivator.md). Sammanfattningen av kapitel 13 börjar så här:

```text
Kapitlet bygger upp begreppen i en tydlig kedja: funktioner av flera
variabler och deras grafer/nivåkurvor (13.1) -> gränsvärden och
kontinuitet (13.2) -> partiella derivator, en variabel i taget (13.3)
-> ... -> gradienten och riktningsderivator (13.7) -> implicita
funktioner (13.8) -> Taylors formel för flera variabler (13.9).
```

Det är en kedja jag kan hålla i huvudet. Och längre ned i samma fil står varför kapitlet spelar roll: det är förutsättningen för kapitel 14 om extremvärden, och Jacobideterminanten från 13.8 återkommer i variabelbytena i kapitel 15. När jag sedan sitter med en uppgift vet jag var i kedjan jag befinner mig.

Planen i mitt kursdokument är med flit omvänd mot en vanlig uppgiftsplan. Först kartläggning och förståelse, sedan en genomgång per avsnitt, och först därefter en uppgift per avsnitt som test. Uppgiften visar om jag förstått. Den är inte själva inlärningen.

??? begrepp "Begrepp: Markdown"
    --8<-- "markdown.md"

    [Se alla begrepp i ordlistan](ordlista.md#markdown)

---

## Steg 2: ordning efter begreppens beroenden

Boken har en ordning, och den är inte alltid min. När jag byggde om planen flyttade jag Taylors formel före kritiska punkter. Skälet är beroendet: andraderivatatestet för extremvärden använder Hessianen, och Hessianen bygger på Taylorutvecklingen till andra ordningen. Läser man kritiska punkter först får man en regel för hur man klassificerar dem utan att veta varför regeln ser ut som den gör. Det är precis den sortens regel jag har svårt att acceptera.

Det syns i kursens egen text också. I sammanfattningen av kapitel 14 står att andraderivatatestet bygger på definitheten hos Hessianmatrisen, och att beviset går via Taylors formel. Beroendet finns alltså redan i materialet. Det som saknades var att planen följde det.

Veckoplanen i [`04_studieplan/veckoplan.md`](https://github.com/Solsidan21/Flervariabelanalys_ht26/blob/main/04_studieplan/veckoplan.md) är byggd så. Taylors formel (13.9) ligger vecka 4 och extremvärden (14.1 och 14.2) vecka 5. En sak till är värd att nämna om den filen: varje vecka har ett fält "Mål" som är skrivet som en förmåga och inte som ett kapitelnummer. Veckan med Taylor har målet att kunna ställa upp Taylorpolynom av andra ordningen för funktioner av flera variabler. Veckan efter har målet att kunna klassificera kritiska punkter med Hessianen. Den som läser planen ser direkt vad som ska sitta, och vad som i så fall bygger på vad.

Så här kan du få fram ordningen i din egen kurs. Be Claude läsa kursplanen och kapitelrubrikerna och göra en lista över vilka begrepp som förutsätter vilka. Titta sedan på var boken eller föreläsningarna går emot den ordningen. Du behöver inte ändra på något, men du vet var du kommer att behöva gå tillbaka.

---

## Steg 3: konkreta bilder

När ett begrepp inte klickar ber jag om en bild. Mitt tydligaste exempel är gradienten. Den är en regel, men den ser olika ut beroende på vad man tillämpar den på. Bilden som fungerade för mig var ett berg. Tänk dig en graf z = h(x, y) som ett landskap och nivåkurvorna som höjdkurvorna på en vandringskarta. Gradienten av h pekar uppför, åt det håll där berget stiger brantast, och den är vinkelrät mot höjdkurvan. Kursboken säger samma sak som en sats:

```text
THEOREM 6: If f(x, y) is differentiable at the point (a, b) and
grad f(a, b) is not 0, then grad f(a, b) is a normal vector to the
level curve of f that passes through (a, b).
```

Satsen har jag läst många gånger. Berget är det som gjorde att jag trodde på den. Och bilden bär längre än till den ena satsen: tät gruppering av nivåkurvor betyder brant terräng, vilket kapitel 13 också påpekar med en hänvisning till topografiska kartor.

Bilder kommer med en risk. En liknelse som är nästan rätt kan ge ett fel som sitter kvar. Därför har jag en fråga som jag ställer själv, och det är den som ligger kvar under rubriken "Osäkert" i mitt kursdokument. Om grafen är z = h(x, y), pekar gradienten av h uppför i kartan, medan gradienten av F(x, y, z) = z minus h(x, y) är normal till tangentplanet i rummet. Två gradienter, två olika objekt, samma regel. Jag lät den stå som osäker tills jag testat den på en riktig tentauppgift. En bild är en genväg till förståelse, och förståelsen prövas mot uppgifter.

---

## Steg 4: regler som tvingar fram förståelse

Det som flyttar upplägget från att vara en idé till att fungera varje dag är reglerna i [`CLAUDE.md`](https://github.com/Solsidan21/Flervariabelanalys_ht26/blob/main/CLAUDE.md). Där står sådant som annars hade stått i en prompt jag skrev om varje dag.

??? begrepp "Begrepp: CLAUDE.md"
    --8<-- "claude-md.md"

    [Se alla begrepp i ordlistan](ordlista.md#claude-md)

Tre regler gör mest för förståelsen. Den första är att visa hela lösningen och inte bara svaret. Så här står det i filen, i min förkortning:

```text
Visa fullständiga steg, inte bara svar. Kursen examinerar matematisk
kommunikation lika mycket som rätt svar: motivera varje steg, definiera
symboler du inför, och ange vilken sats eller metod som används.
```

Den andra är att varje ny symbol definieras och varje sats får sitt namn och sin sektion. Då slipper jag stå med ett h eller ett theta som dykt upp utan förklaring. Den tredje är att teorin läses först. Innan Claude löser en uppgift ska den läsa hela sektionens text, inklusive definitioner, satser och lösta exempel, och lösningen ska utgå från kursens egen text. Det löser en stor del av screenshot-problemet: Claude gissar inte längre vilken metod kursen använder, den slår upp den.

Kursen följer dessutom 10:e upplagan medan min fulltext kommer ur den 9:e. Det finns en regel för det också: nämn alltid båda numren. Det är en liten sak, men den visar vad en regelfil är bra till. Allt som annars hade blivit en förvirring om och om igen skrivs ned en gång.

Ett tips om regler: skriv dem när något går fel. Varje gång Claude gör något som irriterar mig, till exempel hoppar över ett steg, byter notation eller lånar en metod från en annan kurs, frågar jag mig om det ska bli en rad i CLAUDE.md. Efter några veckor har filen blivit en beskrivning av hur jag vill ha det.

??? begrepp "Begrepp: Projekt"
    --8<-- "projekt.md"

    [Se alla begrepp i ordlistan](ordlista.md#projekt)

Kursen har sitt eget projekt i Claude, med repot som kunskap. Projektinstruktionerna är en kortare version av CLAUDE.md, så att de viktigaste reglerna alltid finns med. Det är samma upplägg som i kapitel 04, men tillämpat på en enda kurs.

---

## Steg 5: teorin precis där den behövs

Regeln om att läsa teorin först fungerar bara om Claude hittar rätt text snabbt. Femton minuter med en PDF på fyrtio sidor är precis det jag ville bort från. Så fulltexten är byggd för att gå att slå upp i.

Varje sektion i boken ligger som en egen fil, [`07_fulltext/kap_13/13.7.md`](https://github.com/Solsidan21/Flervariabelanalys_ht26/blob/main/07_fulltext/kap_13/13.7.md) för sektion 13.7 om gradienter. I filen har varje definition, sats och exempel en egen rubrik:

```text
## DEFINITION 6
## EXAMPLE 1
## THEOREM 6
### PROOF
...
## Exercises 13.7
### Uppgift 1
### Uppgift 2
```

Varje övning har alltså en egen rubrik, och en rubrik är ett ankare man kan länka till. När jag skriver "uppgift 11 i 13.5" går Claude direkt till `07_fulltext/kap_13/13.5.md#uppgift-11`, läser teorin som står ovanför och löser uppgiften med den. Boksidorna finns kvar som markörer i texten, så jag kan alltid gå till boken om jag vill se figuren.

Ovanpå det ligger [`00_index/uppgiftsindex.md`](https://github.com/Solsidan21/Flervariabelanalys_ht26/blob/main/00_index/uppgiftsindex.md), en tabell över sektion, uppgiftsspann och filväg. Den är inte skriven för hand. Ett skript, [`scripts/build_uppgiftsindex.py`](https://github.com/Solsidan21/Flervariabelanalys_ht26/blob/main/scripts/build_uppgiftsindex.py), genererar den ur de faktiska rubrikerna, så att indexet inte kan komma ur synk med texterna. Det är ett litet exempel på något jag har lärt mig av det här: allt som kan genereras bör genereras. Då behöver jag aldrig fråga mig om indexet stämmer.

Skripten ersätter inte tänkandet, men de tar bort en sorts fel. Jag har också ett skript som kontrollerar att ingen sats eller definition försvunnit när jag extraherade boken ur PDF, för där hade jag tappat innehåll vid sidgränser. Det kan du läsa mer om i [kapitel 03](03-struktur.md).

---

## Steg 6: veckoplan med mål som förmågor

Veckoplanen nämnde jag redan i samband med ordningen. Det finns en poäng till med den. En kursplan säger vilka kapitel som hör till vilken vecka. Den säger inte vad jag ska kunna efteråt.

Jag skriver varje veckas mål som en förmåga som går att pröva: "avgöra om ett gränsvärde existerar genom att jämföra olika vägar", "tillämpa kedjeregeln med variabelträd i flera led", "verifiera villkoren i implicita funktionssatsen". Ett kapitelnummer kan jag läsa utan att ha förstått något. En förmåga kan jag inte intyga utan att visa den. När veckan är slut är frågan om jag kan göra det, och inte om jag har läst klart.

Tidsstyrningen sköts av kursdokumentet i mitt projekt, som har samma sektioner för varje kurs: Nästa examination, Läget, Kvar (med timmar per avsnitt), Nästa pass, Osäkert och Logg. Jag skriver inte mycket i det själv. Kursprojektet uppdaterar det när jag har pluggat klart, och en schemalagd uppgift läser det varje morgon och föreslår hur mycket plugg dagen kräver. Ju närmare tentan, desto tydligare förslag. Hur det hänger ihop beskrivs i [kapitel 04](04-arkitekturen.md) och [kapitel 06](06-hjarnan.md).

??? begrepp "Begrepp: Schemalagd uppgift"
    --8<-- "schemalagd-uppgift.md"

    [Se alla begrepp i ordlistan](ordlista.md#schemalagd-uppgift)



---

## Steg 7: gamla tentor som test, misstag på felnivå

Gamla tentor är den bästa testen jag har. I repot ligger de som [skarpa tentor](https://github.com/Solsidan21/Flervariabelanalys_ht26/tree/main/05_tentor/skarpa_tentor) med [lösningsförslag](https://github.com/Solsidan21/Flervariabelanalys_ht26/tree/main/05_tentor/losningsforslag) i samma format, `### Uppgift N` och `### Lösning N`. Eftersom formatet är detsamma kan Claude plocka ut en uppgift, låta mig försöka och sedan jämföra med lösningsförslaget.

Jag använder dem på tre sätt. De visar vilken sorts uppgifter som brukar komma, så att jag vet vilka förmågor veckomålen egentligen ska leda till. De avgör om en bild håller: den osäkra frågan om de två gradienterna prövas mot en tentauppgift och inte mot min känsla. Och de är sista kontrollen före en tenta, där jag räknar en hel tenta på tid och ser vilka sektioner som inte sitter.

Det som gör att det bygger på sig själv är loggen. Den är skriven på felnivå. En rad säger inte "repetera kedjeregeln", den säger vad som gick fel: "räknade e upphöjt till 1 som 1", eller "teckenfel när ekvationerna adderades, fångat vid kontroll". Nästa pass bygger på det som faktiskt gick fel och inte på ett allmänt behov av repetition. Det är skillnaden mellan att plugga mer och att plugga rätt sak.

Loggen är också där jag ser mönster. Skriver jag tre gånger att jag tappar ett minustecken i samma typ av uppgift är det inte ett slumpfel. Då är det en vana, och den kan jag arbeta med.

---

## Vad Claude gör, och vad jag gör

Jag vill vara tydlig med en sak, eftersom det är lätt att få fel intryck. Systemet gör inte jobbet åt mig. Reglerna är byggda för att göra det motsatta: Claude ska visa stegen, motivera dem och utgå från kursens text, så att jag kan följa med och göra om det själv. Skulle jag använda upplägget för att få färdiga lösningar att skriva av skulle det fungera sämre än att inte ha något system alls, eftersom jag då skulle sakna det som tentan prövar.

Arbetsfördelningen ser ut så här. Claude Code och jag bygger repot: extraherar boken, skriver skripten, justerar reglerna. Det är jobb som görs ibland. Claude i kursprojektet läser repot och är min studiekamrat i det dagliga: förklarar, ger bilder, rättar mina lösningar, föreslår nästa pass. Jag gör själva räknandet och själva tänkandet. Claude-appen på datorn kan arbeta i mina lokala mappar, och det betyder att jag kan lägga till nytt material i en mapp och att det finns med nästa gång jag frågar.

Det är också en gräns. Repot är offentligt, så det innehåller bara kursmaterial och arbetssätt. Det som är personligt, som hur det går för mig och vad som är på gång, ligger i privata dokument. Mer om den gränsen finns i kapitel 04.

---

## Så formar du ditt eget upplägg

Du behöver inte kopiera mitt. Det är viktigare att du hittar ditt eget, och det första steget är att ta reda på hur du lär dig. Det kan du göra tillsammans med Claude. Börja en ny konversation och be den intervjua dig. Du kan klistra in något i stil med det här:

```text
Jag ska läsa [kurs] och vill att du hjälper mig bygga ett upplägg som
passar hur jag lär mig. Intervjua mig först, en fråga i taget. Fråga
bland annat:
1. Behöver jag förstå varför en regel gäller innan jag kan använda den,
   eller räcker det att jag ser ett exempel?
2. Lär jag mig bäst uppifrån (helheten först) eller nerifrån
   (detaljerna först)?
3. Vilken sorts förklaring har fungerat bäst för mig tidigare? Be mig
   ge ett exempel.
4. Vad är det som får mig att tappa intresset?
5. Vad brukar gå fel när jag räknar: slarvfel, saknad förståelse, tid?
6. Hur ska jag veta att jag har förstått något?
Sammanfatta svaren i ett utkast till regler som jag kan lägga i en
CLAUDE.md för kursen.
```

När du har svaren går du igenom mekanismerna ovan och väljer ut dem som passar:

| Om du känner igen dig i det här | Prova det här |
|---|---|
| Du kastas runt av ordningen i boken | Be om en kartläggning av kursen först och en ordning efter begreppens beroenden |
| Du accepterar inte en regel utan skäl | Lägg in "motivera varje steg" och "definiera varje symbol" i CLAUDE.md |
| Du lär dig av bilder | Skriv ned de bilder som fungerat, och be om en bild när ett begrepp inte klickar |
| Du tappar tid på att leta | Dela upp boken i en fil per avsnitt med ankare per uppgift |
| Du repeterar fel saker | Logga misstag på felnivå och låt nästa pass bygga på dem |
| Du vet inte om du har förstått | Skriv veckomål som förmågor och testa mot gamla tentor |

Börja med en kurs och med det som stör dig mest. En enda regel i CLAUDE.md som löser ett återkommande irritationsmoment är en bra början, och det är bättre än att bygga hela systemet på en gång.

Mallen för CLAUDE.md kan se ut så här i sin enklaste form:

```text
## Om mig
Jag lär mig nerifrån och upp. Jag behöver förstå varför innan jag
accepterar en regel.

## Regler
- Visa hela lösningen med motivering av varje steg.
- Definiera varje symbol första gången den används.
- Läs kursens egen text först och använd bara kursens metoder.
- Börja alltid nytt avsnitt med hur det hänger ihop med det förra.
- När jag ber om en förklaring: ge en konkret bild först.

## Efter varje pass
- Föreslå en loggrad som beskriver vad som gick fel, inte bara vad
  jag ska repetera.
```

---

## Samma tänk när du lär dig ett jobb

Allt det här gäller lika mycket utanför universitetet. Den som börjar ett nytt jobb står inför samma problem som en student: ett område man inte har en bild av, en ordning som någon annan har valt, begrepp som bygger på varandra och en omgivning som antar att man redan kan en massa.

Det finns en direkt översättning. Kartläggningen blir en genomgång av företaget, branschen eller rollen innan du börjar på de första uppgifterna. Beroendena blir frågan om vilka begrepp i jobbet som bygger på vilka. Fulltexten blir de interna dokumenten, uppdelade så att du hittar rätt avsnitt. Veckoplanens mål som förmågor blir "vad ska jag kunna efter min första månad". Gamla tentor blir tidigare projekt, avslutade affärer eller genomförda leveranser. Och loggen på felnivå blir en lista över vad som gick fel och varför, så att samma sak inte händer två gånger.

Det finns ett exempel på hur en sådan översättning kan se ut i [bilagan om arbetslivet](bilaga-arbetsliv.md). Det är också ett bra ställe att börja om du inte studerar just nu.

Det som bär hela vägen är en enkel tanke. Modellen är densamma för dig som för alla andra. Det som skiljer är vad du ger den att arbeta med och vilka regler du sätter. Det går att göra på en eftermiddag, med den prenumeration du redan har, och det blir bättre för varje vecka.

---

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny chatt i ditt Hjärnan-projekt, eller i det projekt som kapitlet gäller. Har du inget projekt än, börja med [setup-sessionen](kom-igang.md).

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/05-individanpassad-inlarning.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Utgå från det du redan vet om mig i det här projektet och fråga bara om det som saknas.
    Fråga hur jag lär mig bäst, vad jag har svårt för och vilken kurs eller vilket ämne jag vill börja med.
    Hjälp mig sedan att skriva ett första utkast till en personlig beskrivning och några regler för mitt eget upplägg.
    Ställ en fråga i taget innan du föreslår något.
    ```

*Nästa: [Kapitel 06: Hjärnan](06-hjarnan.md)*
