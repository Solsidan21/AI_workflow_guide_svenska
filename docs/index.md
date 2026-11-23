# AI Workflow Guide: Från chatt till system

*Samma AI-modeller finns tillgängliga för alla. Det som skiljer ett generiskt svar från ett användbart är skalet runt modellen, och med en vanlig prenumeration kan du bygga ett eget.*

---

## Vem jag är

Jag heter Arvid och läser nationalekonomi vid Lunds universitet. Jag har byggt upp ett sätt att arbeta med Claude som gör att jag slipper börja om varje gång: en mapp per kurs, regler som Claude följer, projekt som känner till kursen och några schemalagda uppgifter som håller ordning på helheten.

Det här är guiden jag önskar att jag hade haft när jag började. Den är skriven för dig som inte är tekniker.

## Tesen: modellen är densamma, skalet är det som skiljer

Modellerna kommer från ett fåtal stora labb, och alla som betalar för en prenumeration når i praktiken samma modeller. Ändå upplever folk helt olika nytta av dem. Förklaringen är det som byggs runt modellen: vilka verktyg den får, vilka källor den läser, vilka instruktioner den följer och vilka arbetsflöden den ingår i. Det kallas ett skal, på engelska *harness*.

Bolag gör just det här som affär. Juristplattformen [Legora](https://legora.com/wip-legal-benchmark-2) beskriver modellen som resonemangsmotorn och bygger verktyg, skills, juridiska källor och arbetsflöden runt den. Appbyggaren [Lovable](https://claude.com/customers/lovable) låter en huvudagent dela ut deluppgifter till subagenter och matchar varje uppgift mot den modell som passar bäst. Båda lever på modeller de inte själva har tränat.

Poängen med guiden är att en privatperson kan bygga sitt eget skal för eget bruk. Det blir mindre och enklare än ett bolags, men det är ditt, och det är anpassat efter hur just du arbetar. Kapitel 08 går igenom vad som går att bygga själv och vad som inte går att kopiera.

## Plugget är exemplet, inte ämnet

Jag visar allt med mina egna kurser som konkret fall, framför allt flervariabelanalys. Det är ett bra exempel eftersom en kurs har tydliga mål, mycket material och ett slutdatum. Men upplägget bygger på tre saker som finns överallt: material som är ordnat så att en AI kan navigera i det, regler som talar om hur du vill arbeta, och en rutin som håller status uppdaterad. Det fungerar lika bra i ett jobb, i en hobby eller i vardagen. Jag påpekar det genom hela guiden, och bilagan visar hur samma tänk ser ut i arbetslivet.

## Vem guiden är för

Du använder förmodligen redan Claude eller ChatGPT. Du får bra svar ibland, men du förklarar samma sak om och om igen, kopierar text fram och tillbaka och börjar varje samtal från noll. Du behöver inte kunna programmera eller ha öppnat en terminal. Du behöver vara beredd att tänka på AI som något du ger förutsättningar, inte bara ställer frågor till.

Claude är huvudspåret i guiden, eftersom det är det jag själv använder. ChatGPT och Codex tas upp där det finns en motsvarighet, så att du kan följa med även om du föredrar OpenAI. Principerna gäller oavsett verktyg.

## Så läser du guiden

Kapitlen bygger på varandra, men du kan hoppa om du vet vad du söker. Varje kapitel börjar med en kort ingress. När ett nytt begrepp dyker upp finns en hopfälld ruta som förklarar det kort. Du fäller ut den om du behöver, och hittar alla begrepp samlade i [ordlistan](ordlista.md).

## Kapitelöversikt

**[Kapitel 01: Från chatt till system](01-fran-chatt-till-system.md)**
Trappan från vanlig chatt via projekt och Claude-appen på datorn till Claude Code, med planer och priser.

**[Kapitel 02: Kontext och prompter](02-kontext-och-prompter.md)**
Varför kontext avgör svarets kvalitet, sex tekniker som gör skillnad, PDF-problemet och hur minnet fungerar.

**[Kapitel 03: Struktur som kontext](03-struktur.md)**
Mappar, Markdown, regelfiler och skills. Varför navigerbar kontext med tydliga regler slår en maxad kontext.

**[Kapitel 04: Arkitekturen](04-arkitekturen.md)**
Hur delarna hänger ihop: lokala repon, GitHub, projekt, Drive, kalender och schemalagda uppgifter.

**[Kapitel 05: Individanpassad inlärning](05-individanpassad-inlarning.md)**
Huvudkapitlet. Hur upplägget formas efter hur du lär dig, med flervariabelanalys som fall.

**[Kapitel 06: Hjärnan](06-hjarnan.md)**
Ett centralt projekt som håller koll på helheten och skickar en plan varje morgon.

**[Kapitel 07: Att bygga vidare på](07-bygga-vidare.md)**
Sätt att utveckla systemet vidare, och idéer utanför plugget.

**[Kapitel 08: Modellen och skalet](08-modellen-och-skalet.md)**
Tesen i detalj, nyanserna, och vad en vanlig prenumeration räcker till.

**[Bilaga: Samma upplägg i arbetslivet](bilaga-arbetsliv.md)**
En kort version av hur upplägget ser ut i ett investeringsbolag, med pekare till färdiga mallar.

**[Ordlista](ordlista.md)**
Alla begrepp samlade.

---

??? tip "Färdigbyggda mallar"
    I repots [`templates/`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates)-mapp finns startpunkter med regelfiler, skills och projektstrukturer för private equity, konsultarbete och marknadsföring.

!!! info "Bra att veta"
    Guiden är på svenska. Engelska facktermer används när de är branschstandard och förklaras första gången de dyker upp. Verktygen och priserna ändras snabbt, så kontrollera alltid aktuella uppgifter hos leverantören innan du bestämmer dig.
