# AI-workflowguiden

*Samma AI-modeller finns tillgängliga för alla. Det som skiljer ett generiskt svar från ett användbart är vad modellen får att arbeta med, och med en vanlig prenumeration kan du bygga ett eget system som ger den rätt förutsättningar.*

## Börja här: låt din Claude läsa guiden

Du behöver inte läsa guiden från början till slut. Det snabbaste sättet att komma igång är att låta din egen Claude (eller ChatGPT) läsa den och hjälpa dig utifrån din situation. Klistra in det här i en ny konversation:

```text
Läs den här guiden om att bygga ett eget AI-arbetsflöde:
https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/llms-full.txt

Guiden beskriver en persons upplägg och är inget facit. Ta det som passar
mig och strunta i resten.

Intervjua mig först, en fråga i taget: vad jag använder AI till i dag,
vad som stör mig mest, om det gäller studier, jobb eller något annat,
och hur mycket jag vill bygga själv.

Föreslå sedan ett första konkret steg som jag kan göra i dag, och hänvisa
till det kapitel i guiden där jag kan läsa mer om jag vill.
```

Sedan kan du slå upp det du undrar över här på sajten.

## Hitta det du behöver

| Om du undrar | Läs |
|---|---|
| Varför börjar varje chatt från noll, och vad är steget efter chatten? | [01 Från chatt till system](01-fran-chatt-till-system.md) |
| Måste jag skriva långa prompter för att få bra svar? | [02 Kontext i stället för långa prompter](02-kontext.md) |
| Hur ordnar jag mina filer så att Claude hittar rätt? | [03 Struktur som kontext](03-struktur.md) |
| Hur hänger projekt, GitHub, Drive och schemalagda uppgifter ihop? | [04 Arkitekturen](04-arkitekturen.md) |
| Hur får jag ett upplägg som passar hur jag lär mig? | [05 Individanpassad inlärning](05-individanpassad-inlarning.md) |
| Kan Claude hålla koll på helheten och skicka en plan varje morgon? | [06 Hjärnan](06-hjarnan.md) |
| Vad kan jag bygga till när grunden fungerar? | [07 Att bygga vidare på](07-bygga-vidare.md) |
| Vilken modell ska jag använda, och spelar benchmarks någon roll? | [08 Modellerna](08-modellerna.md) |
| Varför känns det som att AI plötsligt kan så mycket mer? | [09 Tröskeln, inte förmågan](09-troskeln.md) |
| Varför slår jag i användningsgränsen hela tiden? | [10 Därför slår du i taket](10-anvandningsgransen.md) |
| Behöver jag betala för fler AI-tjänster? | [11 Vad en prenumeration räcker till](11-vad-en-prenumeration-racker-till.md) |
| Hur ser det här ut på ett jobb? | [Bilaga: Arbetslivet](bilaga-arbetsliv.md) |
| Vad betyder ett ord? | [Ordlista](ordlista.md) |

Varje kapitel börjar med en kort version på några rader och slutar med en prompt som låter dig göra kapitlets steg tillsammans med din Claude. Nya begrepp förklaras i hopfällda rutor som du fäller ut vid behov.

## Vem jag är

Jag heter Arvid och läser nationalekonomi vid Lunds universitet. Jag har byggt upp ett sätt att arbeta med Claude som gör att jag slipper börja om varje gång: en mapp per kurs, regler som Claude följer, projekt som känner till kursen och några schemalagda uppgifter som håller ordning på helheten.

Jag visar allt med mina egna kurser som exempel, framför allt flervariabelanalys. Plugget är exemplet, inte ämnet. Upplägget bygger på tre saker som finns överallt: material som är ordnat så att en AI kan navigera i det, regler som talar om hur du vill arbeta, och en rutin som håller läget uppdaterat. Det fungerar lika bra i ett jobb, en hobby eller i vardagen.

## Tesen: du betalar redan för det viktigaste

Alla som betalar för en prenumeration når i praktiken samma modeller. Ändå upplever folk helt olika nytta av dem, och förklaringen är vad modellen får att arbeta med. Det mesta av det kan du ordna själv: ett välordnat filsystem, några regelfiler, några skript och ett par schemalagda uppgifter räcker långt. Den som har Claude eller ChatGPT har sällan anledning att också betala för en rad separata AI-tjänster som var och en gör en liten del av samma sak.

Claude är huvudspåret eftersom det är det jag använder. ChatGPT och Codex tas upp där det finns en motsvarighet.

!!! info "Bra att veta"
    Verktygen och priserna ändras snabbt, så kontrollera aktuella uppgifter hos leverantören. I repots [`templates/`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates) finns färdiga mallar med regelfiler och skills för private equity, konsultarbete och marknadsföring.
