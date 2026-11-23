# Kapitel 02 — Kontext och prompter

*Skillnaden mellan ett okej svar och ett bra svar ligger sällan i hur du formulerar frågan. Den ligger i vad modellen har framför sig när den svarar.*

!!! abstract "Kort version"
    - Svarets kvalitet avgörs mest av vad modellen har framför sig, inte av hur frågan är formulerad.
    - Kontextfönstret är ett begränsat skrivbord, så det lönar sig att lägga dit rätt material och inte allt.
    - Sex tekniker gör störst skillnad: var specifik, berätta varför, be om stegen, iterera, säg vad du inte vill ha och visa ett exempel.
    - Filer och minne har fällor som går att undvika med några enkla vanor.

---

Du vet redan hur man skriver en prompt. Det här kapitlet handlar om det som omger den: vad kontext är, varför den avgör kvaliteten, vilka tekniker som gör störst skillnad och hur du undviker de vanligaste fällorna med filer och minne.

## Vad kontext är

När Claude svarar bygger svaret på all information som finns tillgänglig i det ögonblicket: din fråga, konversationen hittills, uppladdade filer, projektets instruktioner och kunskap, och i Claude Code även regelfilerna i mappen. Allt det tillsammans är kontexten.

??? begrepp "Begrepp: Kontext"
    --8<-- "kontext.md"

    [Se alla begrepp i ordlistan](ordlista.md#kontext)

Tänk dig att du ber en konsult analysera ett bolag. Säger du bara "analysera bolaget" får du ett generiskt svar. Ger du konsulten årsredovisningen, en branschrapport, en beskrivning av vad du letar efter och en mall för hur rapporten ska se ut, får du något helt annat. Konsulten blev inte plötsligt smartare. Förutsättningarna blev bättre. Samma sak gäller en AI.

Det gäller också i plugget. Frågar jag "förklara kritiska punkter" får jag en lärobokstext. Har jag ett projekt där kursboken finns som text, där reglerna säger att varje steg ska motiveras och där Claude vet att jag inte är nöjd förrän jag förstår varför, får jag en förklaring som passar mig.

## Kontextfönstret är ett skrivbord

Varje modell kan hålla en viss mängd information i huvudet åt gången. Den gränsen kallas kontextfönster.

??? begrepp "Begrepp: Kontextfönster"
    --8<-- "kontextfonster.md"

    [Se alla begrepp i ordlistan](ordlista.md#kontextfonster)

Tänk på det som ett skrivbord. Det rymmer en viss mängd papper. Du kan lägga dit din fråga, samtalet, filer och instruktioner. Lägger du dit en hel bokhylla blir skrivbordet fullt, och något hamnar på golvet. I ett långt samtal kan de tidigaste detaljerna bli mindre tydliga, vilket är en begränsning och inget fel.

Mängden mäts i tokens.

??? begrepp "Begrepp: Token"
    --8<-- "token.md"

    [Se alla begrepp i ordlistan](ordlista.md#token)

Praktiskt innebär det två saker. I ett långt samtal kan det löna sig att starta ett nytt, inom samma projekt, så att instruktionerna och filerna finns kvar men historiken börjar om. I Claude Code kan du köra `/compact` för att sammanfatta samtalet och frigöra plats. Och du bör tänka på vad som ligger på skrivbordet: en dokumentmängd du inte behöver gör att det du behöver får mindre plats.

## PDF-problemet

De flesta har sina viktigaste dokument som PDF: kursböcker, rapporter, årsredovisningar, avtal. AI-verktyg kan läsa dem, så vad är problemet? PDF är byggt för att människor ska läsa på en skärm. Det är inte byggt för att en AI ska arbeta med det, av tre skäl.

Modellen måste ta in hela dokumentet för att hitta det du frågar om. Den kan inte bläddra till rätt sida. En lång bok kostar därför många tokens varje gång den läses, även om du bara behöver tre rader. Och formateringen översätts ofta dåligt: tabeller hamnar i fel kolumner, formler förvanskas och sidbrytningar klipper mitt i meningar.

Samma innehåll som Markdown, ett enkelt textformat med rubriker, listor och tabeller, kostar en bråkdel och läses exakt som det står.

??? begrepp "Begrepp: Markdown"
    --8<-- "markdown.md"

    [Se alla begrepp i ordlistan](ordlista.md#markdown)

| Format | Kontextkostnad | Precision |
|---|---|---|
| Markdown | Låg | Hög, modellen läser exakt det som står |
| CSV | Låg | Hög, tydliga kolumner och rader |
| PDF | Hög | Varierande, tabeller och formler kan feltolkas |

Lösningen är inte att sluta använda PDF. Det är ofta det enda du får. Du bearbetar dem till Markdown en gång, arbetar mot den versionen och sparar originalet som källa. Hur det går till beskrivs i kapitel 03. I kursen jag visar i kapitel 05 ligger hela kursboken som Markdown, uppdelad per avsnitt, så att Claude kan gå direkt till rätt ställe.

## Sex tekniker som gör skillnad

Teknikerna fungerar i en vanlig chatt. De blir ännu viktigare när du beskriver ett helt system för Claude Code att bygga, eftersom det du kan beskriva tydligt är det du kan få byggt.

### 1. Var specifik

Vagt: "Förklara Taylorutveckling."

Specifikt: "Förklara Taylorutveckling av andra ordningen för en funktion av två variabler. Visa varje steg, definiera varje symbol du inför och avsluta med ett räknat exempel i punkten (0, 0)."

Ju mer du anger om innehåll, format och längd, desto mindre behöver modellen gissa.

### 2. Berätta varför och för vem

Berätta inte bara vad du vill ha utan också syftet och mottagaren.

Utan sammanhang: "Sammanfatta den här rapporten."

Med sammanhang: "Sammanfatta rapporten i fem punkter åt någon som ska besluta om en investering och bara har tio minuter. Lyft de största riskerna först."

Sammanhanget styr ton, detaljnivå och vinkel.

### 3. Be om stegen

För komplexa uppgifter hjälper det att dela upp arbetet:

1. Sammanfatta nyckeltalen per år.
2. Beräkna tillväxten över perioden.
3. Identifiera de tre tydligaste trenderna.
4. Ge en samlad bedömning.

Då minskar risken att modellen hoppar över ett moment eller blandar ihop resultat.

### 4. Iterera

Det bästa sättet att arbeta är i korta varv. Börja brett, titta på svaret, rikta om. Tre korta justeringar ger ofta ett bättre resultat än en lång, perfekt formulerad prompt.

```
Du: Sammanfatta kapitlet.
Claude: [sammanfattning]
Du: Bra, men fokusera på hur Hessianen hänger ihop med Taylor.
Claude: [ny version]
Du: Lägg till ett exempel med en funktion av två variabler.
Claude: [slutversion]
```

### 5. Säg vad du inte vill ha

En AI vill gärna hjälpa till, och ibland för mycket. Den lägger till egna antaganden, fyller luckor med gissningar eller skriver i en ton du inte bad om. Negativa instruktioner hjälper: "Gissa inte. Saknas underlag, säg det." "Inga säljfraser." "Använd bara det som står i de bifogade filerna." "Högst 300 ord."

### 6. Visa ett exempel

Vill du ha ett särskilt format, visa det:

```
Beskriv varje begrepp så här:

Begrepp: en mening om vad det är
Behövs för: vilket begrepp som bygger på det
Vanligt fel: ett typiskt misstag
```

Ett exempel förmedlar format snabbare än en lång beskrivning.

## Beskriv, så bygger Claude

Teknikerna ovan blir mest värda när du använder dem för att beskriva ett helt projekt. Börja i en vanlig chatt och förklara vad du vill skapa. Diskutera tills bilden är tydlig. Be sedan chatten sammanfatta allt som en beskrivning du ger till Claude Code, som bygger mappar, regelfiler och skript. Du beskriver, Claude bygger, och ju tydligare du beskriver desto bättre blir resultatet.

## Minne: vad Claude kommer ihåg mellan samtal

Instruktioner och filer i ett projekt är något du skriver och styr. Minnet är något Claude bygger upp själv av vad du berättar.

??? begrepp "Begrepp: Minne"
    --8<-- "minne.md"

    [Se alla begrepp i ordlistan](ordlista.md#minne)

Så här fungerar det i Claude. Minnet är påslaget som standard på Free, Pro och Max, och sparas som enskilda ämnen medan du chattar. Känsliga ämnen som hälsa, politik och religion sparas inte som standard, och uppgifter som id-nummer och kontonummer sparas aldrig. På betalplaner kan Claude dessutom söka i tidigare samtal. Chattar utanför projekt kan sökas överallt, medan projektchattar bara kan sökas inom sitt eget projekt.

Varje projekt har sitt eget minne som inte blandas med andra projekts. Vill du ha full isolering kan du stänga av kontominnet för projektet. Du kan också slå av minnet för ett enskilt samtal, och inkognitochattar sparas varken i historiken eller i minnet. Ta för vana att då och då titta på vad som sparats och rensa det som är fel eller inaktuellt. ChatGPT har också ett minne, med begränsat utrymme i gratisnivån och mer i de dyrare planerna.

Hur du ska tänka om det: minnet är ett komplement, aldrig grunden. Det är en sammanfattning som modellen själv väljer. Det som måste gälla varje gång, som hur du vill ha förklaringar eller vilka regler som styr en kurs, hör hemma i projektinstruktioner eller en regelfil, där du ser exakt vad som står.

## Artifacts: resultat som blir egna objekt

När Claude gör något som är fristående, som ett dokument, en tabell, ett litet program eller en interaktiv sida, kan det visas som en artifact i ett eget fönster bredvid samtalet.

??? begrepp "Begrepp: Artifact"
    --8<-- "artifact.md"

    [Se alla begrepp i ordlistan](ordlista.md#artifact)

Det gör resultatet lätt att kopiera, ladda ned och bygga vidare på: "lägg till en risksektion i dokumentet" i stället för att leta i ett långt samtal. Du kan styra genom att be om det uttryckligen, till exempel "skriv det som ett dokument" eller "gör en tabell".

## Sammanfattning

| Teknik | Effekt |
|---|---|
| Berätta varför och för vem | Modellen förstår uppgiften |
| Var specifik | Resultatet matchar det du förväntar dig |
| Be om stegen | Komplexa uppgifter delas upp rätt |
| Iterera | Du förfinar i stället för att jaga den perfekta prompten |
| Säg vad du inte vill ha | Mindre gissningar och brus |
| Visa ett exempel | Formatet blir rätt direkt |
| Projekt och regelfiler | Kontexten finns på plats, du slipper upprepa dig |
| Markdown i stället för PDF | Färre tokens och högre precision |

Det viktigaste att ta med sig är att kontext slår promptkvalitet. En medelmåttig prompt med rätt filer, tydliga regler och bra struktur ger nästan alltid bättre resultat än en perfekt prompt utan något av det. Det är också därför samma upplägg fungerar oavsett om du läser en kurs, förbereder ett möte eller sköter ett projekt.

---

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/02-kontext-och-prompter.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Fråga vilken uppgift jag brukar få tunna svar på och vilket material jag har till den.
    Hjälp mig sedan att skriva om en av mina egna prompter med teknikerna i kapitlet och förklara vad som blev bättre.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 03: Struktur som kontext](03-struktur.md)
