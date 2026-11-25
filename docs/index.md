# AI-workflowguiden

*Samma AI-modeller finns tillgängliga för alla. Det som skiljer ett generiskt svar från ett användbart är vad modellen får att arbeta med, och med en vanlig prenumeration kan du bygga ett eget system som ger den rätt förutsättningar.*

## Börja här: en setup-session med din egen Claude

Du behöver inte läsa guiden för att komma igång. Öppna en helt ny chatt i Claude (eller ChatGPT), utanför alla projekt, och klistra in det här:

```text
Det här är en setup-session. Läs och följ instruktionerna här:
https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/setup/setup-session.md

Använd den här chatten bara till att sätta upp mitt arbetssätt, inte till att jobba med mina uppgifter.
```

Claude frågar hur du arbetar i dag, föreslår ett upplägg som passar dig och guidar dig genom att skapa ett projekt som blir din "hjärna". Sedan flyttar du in chatten dit och fortsätter därifrån. [Kom igång](kom-igang.md) beskriver vad som händer steg för steg.

Guiden här på sajten är till för när du vill förstå varför. Setup-sessionen länkar hit när det passar.

## Hitta det du behöver

| Om du undrar | Läs |
|---|---|
| Vad händer i setup-sessionen, och varför en egen chatt för den? | [Kom igång](kom-igang.md) |
| Varför börjar varje chatt från noll, och vad är steget efter chatten? | [01 Från chatt till system](01-fran-chatt-till-system.md) |
| Måste jag skriva långa prompter för att få bra svar? | [02 Kontext i stället för långa prompter](02-kontext.md) |
| Hur ordnar jag mina filer så att Claude hittar rätt? | [03 Struktur som kontext](03-struktur.md) |
| Hur hänger projekt, GitHub, Drive och schemalagda uppgifter ihop? | [04 Arkitekturen](04-arkitekturen.md) |
| Hur får jag ett upplägg som passar hur jag lär mig? | [05 Individanpassad inlärning](05-individanpassad-inlarning.md) |
| Vad ska ligga på datorn, i Drive och i Claude? | [04 Arkitekturen](04-arkitekturen.md#lokalt-i-drive-eller-i-claudes-moln) |
| Kan Claude hålla koll på helheten och skicka en plan varje morgon? | [06 Hjärnan](06-hjarnan.md) |
| Vad kan jag bygga till när grunden fungerar? | [07 Att bygga vidare på](07-bygga-vidare.md) |
| Vilken modell ska jag använda, och spelar benchmarks någon roll? | [08 Modellerna](08-modellerna.md) |
| Varför känns det som att AI plötsligt kan så mycket mer? | [09 Tröskeln, inte förmågan](09-troskeln.md) |
| Varför slår jag i användningsgränsen hela tiden? | [10 Därför slår du i taket](10-anvandningsgransen.md) |
| Behöver jag betala för fler AI-tjänster? | [11 Vad en prenumeration räcker till](11-vad-en-prenumeration-racker-till.md) |
| Hur ser det här ut på ett jobb? | [Bilaga: Arbetslivet](bilaga-arbetsliv.md) |
| Vad betyder ett ord? | [Ordlista](ordlista.md) |

Varje kapitel börjar med en kort version på några rader och slutar med en prompt som du klistrar in i en ny chatt i ett av dina projekt, så att du gör kapitlets steg tillsammans med din Claude. Nya begrepp förklaras i hopfällda rutor som du fäller ut vid behov.

## Vem jag är

Jag heter Arvid och läser nationalekonomi vid Lunds universitet. Jag har byggt upp ett sätt att arbeta med Claude som gör att jag slipper börja om varje gång: en mapp per kurs, regler som Claude följer, projekt som känner till kursen och några schemalagda uppgifter som håller ordning på helheten.

Jag visar allt med mina egna kurser som exempel, framför allt flervariabelanalys. Plugget är exemplet, inte ämnet. Upplägget bygger på tre saker som finns överallt: material som är ordnat så att en AI kan navigera i det, regler som talar om hur du vill arbeta, och en rutin som håller läget uppdaterat. Det fungerar lika bra i ett jobb, en hobby eller i vardagen.

## Tesen: du betalar redan för det viktigaste

Alla som betalar för en prenumeration når i praktiken samma modeller. Ändå upplever folk helt olika nytta av dem, och förklaringen är vad modellen får att arbeta med. Det mesta av det kan du ordna själv: ett välordnat filsystem, några regelfiler, några skript och ett par schemalagda uppgifter räcker långt. Den som har Claude eller ChatGPT har sällan anledning att också betala för en rad separata AI-tjänster som var och en gör en liten del av samma sak.

Claude är huvudspåret eftersom det är det jag använder. ChatGPT och Codex tas upp där det finns en motsvarighet.

!!! info "Bra att veta"
    Verktygen och priserna ändras snabbt, så kontrollera aktuella uppgifter hos leverantören. I repots [`templates/`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates) finns färdiga mallar med regelfiler och skills för private equity, konsultarbete och marknadsföring.
