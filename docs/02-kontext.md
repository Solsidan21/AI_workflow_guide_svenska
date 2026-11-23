# Kapitel 02 — Kontext i stället för långa prompter

*Det känns uråldrigt att prata om hur man skriver en bra prompt. Poängen med ett upplägg är att du kan vara kort och vag, eftersom allt Claude behöver veta redan finns på plats.*

!!! abstract "Kort version"
    - Svarets kvalitet avgörs mest av vad modellen har framför sig, inte av hur lång eller välformulerad frågan är.
    - Med instruktioner, kunskap och regler i ett projekt räcker en kort fråga som "uppgift 11 i 13.5".
    - Kontextfönstret är ett begränsat skrivbord, så det lönar sig att lägga dit rätt material och inte allt.
    - När jag korrigerar Claude ändras svaret direkt, och återkommande korrigeringar kan bli en regel i projektet.
    - Filer och minne har fällor som går att undvika med några enkla vanor.

---

Det här kapitlet handlar om vad kontext är, varför den väger tyngre än prompten, hur en kort fråga kan ge rätt svar och hur systemet lär sig av det jag rättar. Där finns också de vanligaste fällorna med filer och minne.

## Vad kontext är

När Claude svarar bygger svaret på all information som finns tillgänglig i det ögonblicket: min fråga, konversationen hittills, uppladdade filer, projektets instruktioner och kunskap, och i Claude Code även regelfilerna i mappen. Allt det tillsammans är kontexten.

??? begrepp "Begrepp: Kontext"
    --8<-- "kontext.md"

    [Se alla begrepp i ordlistan](ordlista.md#kontext)

Tänk dig en konsult som ska analysera ett bolag. Får konsulten bara orden "analysera bolaget" blir svaret generiskt. Får konsulten årsredovisningen, en branschrapport, en beskrivning av vad jag letar efter och en mall för rapporten, blir resultatet ett helt annat. Konsulten blev inte smartare. Förutsättningarna blev bättre. Samma sak gäller en AI.

## Kontextfönstret är ett skrivbord

Varje modell kan hålla en viss mängd information i huvudet åt gången. Den gränsen kallas kontextfönster.

??? begrepp "Begrepp: Kontextfönster"
    --8<-- "kontextfonster.md"

    [Se alla begrepp i ordlistan](ordlista.md#kontextfonster)

Tänk på det som ett skrivbord. Det rymmer en viss mängd papper. Lägger jag dit en hel bokhylla blir det fullt, och något hamnar på golvet. I ett långt samtal kan de tidigaste detaljerna bli mindre tydliga, vilket är en begränsning och inget fel. Mängden mäts i tokens.

??? begrepp "Begrepp: Token"
    --8<-- "token.md"

    [Se alla begrepp i ordlistan](ordlista.md#token)

Praktiskt betyder det att jag startar ett nytt samtal inom samma projekt när ett blir långt, så att instruktionerna och filerna finns kvar men historiken börjar om. I Claude Code kan jag köra `/compact` för att sammanfatta samtalet och frigöra plats. Och jag lägger bara på skrivbordet det jag behöver.

## PDF-problemet

De flesta har sina viktigaste dokument som PDF, till exempel kursböcker, rapporter och avtal. Formatet är byggt för att människor ska läsa på en skärm, inte för att en AI ska arbeta med det. Modellen måste ta in hela dokumentet för att hitta tre rader, så en lång bok kostar många tokens varje gång. Tabeller och formler översätts dessutom ofta dåligt.

Samma innehåll som Markdown, ett enkelt textformat med rubriker, listor och tabeller, kostar en bråkdel och läses exakt som det står.

??? begrepp "Begrepp: Markdown"
    --8<-- "markdown.md"

    [Se alla begrepp i ordlistan](ordlista.md#markdown)

Lösningen är inte att sluta använda PDF. Jag bearbetar dem till Markdown en gång, arbetar mot den versionen och sparar originalet som källa. Hur det går till beskrivs i kapitel 03, och vad det betyder för kostnaden finns i kapitel 10.

## Kort fråga, rätt svar

Så här såg det ut när jag arbetade i en vanlig chatt. Varje gång jag ville ha hjälp med en uppgift skrev jag ungefär så här:

```text
Jag läser flervariabelanalys på Lunds universitet, kursen MATB21. Jag är
ekonomistudent och har läst envariabelanalys, så förklara på den nivån.
Använd samma notation som kursboken, till exempel ∇f för gradienten.
Visa varje steg och motivera varför du gör det. Svara på svenska, avsluta
med en kort kontroll av resultatet. Uppgiften är uppgift 11 i avsnitt 13.5.
```

Det är fem rader som jag skrev om och om igen, och glömde jag en av dem fick jag ett svar som inte passade. Med ett projekt som är uppsatt skriver jag i stället:

```text
uppgift 11 i 13.5
```

eller:

```text
förklara gradienten igen
```

Det räcker, eftersom projektets instruktioner redan säger vilken kurs det är, vilken nivå jag ligger på, vilken notation som gäller och att varje steg ska motiveras. Kunskapsfilerna innehåller kursboken, så Claude vet vad uppgift 11 i 13.5 är utan att jag klistrar in den. Uppsättningen av ett sådant projekt visar jag i kapitel 05.

Det här är hela poängen med upplägget. Jag lägger arbetet en gång, i instruktioner, filer och regler, och sedan kostar varje fråga nästan ingenting att ställa.

## Systemet lär sig av dina korrigeringar

Ingen instruktion blir komplett på första försöket. Då gör jag det enklaste möjliga: jag säger det.

- "Kortare."
- "Visa alla steg."
- "Använd kursens notation."

Claude ändrar svaret direkt. Gäller korrigeringen bara just den här uppgiften är det slut där. Verkar den gälla framöver kan minnet spara den som en preferens, så att nästa samtal börjar på rätt sätt.

Det finns ett steg till. En rad i projektinstruktionerna kan be Claude själv påpeka när en korrigering borde bli en permanent regel. Jag har lagt in något i den här stilen:

```text
När jag korrigerar hur du svarar och det verkar gälla framöver: föreslå en
formulering jag kan lägga in i projektinstruktionerna.
```

Kommer jag med samma korrigering för tredje gången svarar Claude med ett förslag på en rad att lägga in. Jag bestämmer själv om den läggs in. Claude ändrar aldrig mina instruktioner på egen hand, och det är en fördel: instruktionerna är den del av systemet där jag ser exakt vad som gäller. Över tid blir de kortare frågorna möjliga just för att korrigeringarna samlas där.

## När en längre instruktion ändå är rätt

Ibland skriver jag fortfarande en lång text. Skillnaden är att den då inte är en engångsprompt. Jag skriver långt när jag formulerar en regel som ska ligga kvar, till exempel hur förklaringar ska byggas upp eller vad Claude aldrig ska gissa. En sådan text lönar sig eftersom den används varje gång.

Claude skriver dessutom ofta bättre prompter till sig själv än jag gör. Behöver en uppgift en detaljerad instruktion kan jag därför be Claude formulera den. Hur det går till beskrivs i kapitel 10.

## Minne: vad Claude kommer ihåg mellan samtal

Instruktioner och filer i ett projekt är något jag skriver och styr. Minnet är något Claude bygger upp själv av det jag berättar.

??? begrepp "Begrepp: Minne"
    --8<-- "minne.md"

    [Se alla begrepp i ordlistan](ordlista.md#minne)

Så här fungerar det i Claude. Minnet är påslaget som standard på Free, Pro och Max, och sparas som enskilda ämnen medan du chattar. Känsliga ämnen som hälsa, politik och religion sparas inte som standard, och uppgifter som id-nummer och kontonummer sparas aldrig. På betalplaner kan Claude dessutom söka i tidigare samtal. Chattar utanför projekt kan sökas överallt, medan projektchattar bara kan sökas inom sitt eget projekt.

Varje projekt har sitt eget minne som inte blandas med andra projekts. Vill du ha full isolering kan du stänga av kontominnet för projektet. Du kan också slå av minnet för ett enskilt samtal, och inkognitochattar sparas varken i historiken eller i minnet. Ta för vana att då och då titta på vad som sparats och rensa det som är fel eller inaktuellt. ChatGPT har också ett minne, med begränsat utrymme i gratisnivån och mer i de dyrare planerna.

Minnet är ett komplement, aldrig grunden. Det är en sammanfattning som modellen själv väljer. Det som måste gälla varje gång hör hemma i projektinstruktioner eller en regelfil, där jag ser exakt vad som står.

## Artifacts

När Claude gör något fristående, som ett dokument, en tabell eller en liten sida, kan det visas som en artifact i ett eget fönster bredvid samtalet. Då kan jag be om ändringar i just det objektet i stället för att leta i ett långt samtal.

## Sammanfattning

Det viktigaste att ta med sig är att kontext slår promptkvalitet. En kort fråga med rätt filer, tydliga regler och bra struktur ger nästan alltid bättre resultat än en perfekt prompt utan något av det.

---

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/02-kontext.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Fråga vad jag upprepar i mina prompter i dag, till exempel kurs, nivå, ton eller format.
    Hjälp mig sedan att flytta det till projektinstruktioner, så att mina frågor kan bli kortare.
    Ställ en fråga i taget innan du föreslår något.
    ```

Nästa: [Kapitel 03: Struktur som kontext](03-struktur.md)
