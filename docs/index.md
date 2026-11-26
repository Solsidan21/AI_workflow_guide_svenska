# AI-workflowguide på svenska

*Samma AI-modeller finns tillgängliga för alla. Det som skiljer ett generiskt svar från ett användbart är vad modellen får att arbeta med, och med en vanlig prenumeration kan du bygga ett eget system som ger den rätt förutsättningar.*

## Från chatt till system

De flesta använder AI som en chatt: du frågar, får ett svar och börjar om från noll nästa gång. Ett system är när Claude redan vet vem du är, vad du arbetar med, var ditt material ligger och hur du vill ha hjälp, innan du har skrivit något. Det byggs av några enkla delar: ett projekt per område med egna instruktioner, ett centralt projekt som håller koll på helheten och material som ligger där Claude hittar det. Inget av det kräver att du kan programmera.

## Känner du igen dig?

- **Du skriver långa prompter** och förklarar vem du är och vad som gäller, varje gång.
- **Det tar tid att komma igång i en ny chatt**, så du stannar i samma chatt i veckor eller månader. Men Claude har inte koll på allt i en så lång chatt. Det äldre komprimeras, detaljer faller bort och svaren blir sämre, samtidigt som varje nytt meddelande drar mer av din användning.
- **Du laddar upp samma filer om och om igen**, gärna stora PDF:er som gör svaren sämre.
- **Du slår i användningsgränsen**, fast du bara pluggar eller jobbar.
- **Det du ska göra finns i huvudet** eller på lösa lappar, och ingen håller koll på helheten.

Det är just de problemen upplägget i guiden löser. [Kapitel 02](02-kontext.md) förklarar varför kontext slår långa prompter, och [kapitel 10](10-anvandningsgransen.md#varfor-langa-chattar-blir-dyra) varför en lång chatt blir både sämre och dyrare än flera korta.

**Har du redan ett genomtänkt upplägg?** Kanske har du flera projekt, mappar på datorn och till och med ett projekt som håller koll på helheten. Då kan setup-sessionen ändå vara värd att testa. Jag kan inte lova några stora förändringar. Se den snarare som en utvärdering av det du redan har, på samma sätt som jag själv hela tiden prövar och förbättrar mitt eget upplägg. Claude utgår från dina projekt och letar efter det som går att göra bättre.

## Börja här: en setup-session med din egen Claude

Du behöver inte läsa guiden för att komma igång. Öppna en helt ny chatt i Claude (eller ChatGPT), utanför alla projekt, och klistra in det här:

```text
Det här är en setup-session. Läs och följ instruktionerna här:
https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/setup/setup-session.md

Använd den här chatten bara till att sätta upp mitt arbetssätt, inte till att jobba med mina uppgifter.
```

Claude frågar hur du arbetar i dag och vad du använder den till, och anpassar sig efter det.

Det du gör i sessionen är att lägga grunden, inte att bygga ett stort system på en gång. Efter ungefär en halvtimme har du två projekt: Hjärnan, som håller koll på helheten och där setup-chatten bor kvar, och ett projekt för det du främst vill få gjort, till exempel ett examensarbete. Sedan är du igång med ditt arbete. Grunden gör att du senare kan bygga vidare utan att börja om: fler projekt, ett morgonbrev som sammanfattar dagen eller ett upplägg anpassat efter hur du lär dig bäst. Har du redan projekt utgår Claude från dem. Då kan det ta lite längre tid, men det ger också mer. [Kom igång](kom-igang.md) beskriver vad som händer steg för steg.

## När du vill bygga vidare

När grunden fungerar och du vill ta nästa steg, till exempel ett nytt projekt, ett morgonbrev eller en bättre ordning på dina filer: öppna en ny chatt i ditt Hjärnan-projekt och klistra in det här. Claude läser hela guiden och utgår från hur du arbetar i dag.

```text
Jag vill bygga vidare på mitt upplägg. Läs AI-workflowguide på svenska:
https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/llms-full.txt
Guiden beskriver en persons upplägg och är inget facit.
Utgå från hur jag arbetar i dag, fråga var det skaver och föreslå ett nästa steg.
Ställ en fråga i taget.

Det här vill jag göra:
```

Skriv det du vill göra på sista raden, eller lämna den tom om du vill att Claude ska föreslå något. Guiden här på sajten är till för när du vill förstå varför, och både setup-sessionen och Claude länkar hit när det passar.

## Hitta det du behöver

| Om du undrar | Läs |
|---|---|
| Vad händer i setup-sessionen, och varför en egen chatt för den? | [Kom igång](kom-igang.md) |
| Varför börjar varje chatt från noll, och vad är steget efter chatten? | [01 Från chatt till system](01-fran-chatt-till-system.md) |
| Måste jag skriva långa prompter för att få bra svar? | [02 Kontext i stället för långa prompter](02-kontext.md) |
| Hur ordnar jag mina filer så att Claude hittar rätt? | [03 Struktur som kontext](03-struktur.md) |
| Hur hänger projekt, GitHub, Drive och schemalagda uppgifter ihop? | [04 Arkitekturen](04-arkitekturen.md) |
| Hur hänger projekten ihop med varandra, och vad har det med Claude Code att göra? | [04 Arkitekturen](04-arkitekturen.md#hur-projekten-hanger-ihop) |
| Hur får jag ett upplägg som passar hur jag lär mig? | [05 Individanpassad inlärning](05-individanpassad-inlarning.md) |
| Var ska saker ligga: på datorn, i Drive eller i Claude? | [04 Arkitekturen](04-arkitekturen.md#tumregeln-vem-laser) |
| Kan Claude hålla koll på helheten och skicka en plan varje morgon? | [06 Hjärnan](06-hjarnan.md) |
| Vad kan jag bygga till när grunden fungerar? | [07 Att bygga vidare på](07-bygga-vidare.md) |
| Vilken modell ska jag använda, och spelar benchmarks någon roll? | [08 Modellerna](08-modellerna.md) |
| Varför känns det som att AI plötsligt kan så mycket mer? | [09 Tröskeln, inte förmågan](09-troskeln.md) |
| Varför slår jag i användningsgränsen hela tiden? | [10 Därför slår du i taket](10-anvandningsgransen.md) |
| Behöver jag betala för fler AI-tjänster? | [11 Vad en prenumeration räcker till](11-vad-en-prenumeration-racker-till.md) |
| Hur ser det här ut på ett jobb? | [Bilaga: Arbetslivet](bilaga-arbetsliv.md) |
| Hur kopplar man ihop flera personers upplägg, och var passar Notion och Claude Team in? | [Bilaga: Arbetslivet](bilaga-arbetsliv.md#nar-hjarnorna-ska-prata-med-varandra) |
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
