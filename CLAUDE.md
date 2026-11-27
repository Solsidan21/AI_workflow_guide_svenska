# CLAUDE.md — Projektstilregler

## Skrivregler

### Tankstreck (em dash)
- Tankstreck (—) ska INTE användas mitt i meningar i löpande text. Skriv om till punkt, komma, kolon eller omformulering istället.
- Undantag: kapitelrubriker och titlar där det är vedertaget format (t.ex. `# Kapitel 01 — Titel`).

## Två läsare

- Sajten (docs/ byggd med MkDocs) är för människor. Den ska gå att slå upp i, inte läsas från pärm till pärm: kort version överst i varje kapitel, en fråga per avsnitt, begrepp i hopfällbara rutor.
- Repot är för läsarens egen AI. Prompterna i rutorna "Gör det med din Claude" pekar därför på råfilerna på raw.githubusercontent.com, inte på sajten.
- Efter varje ändring i docs/ eller begrepp/: kör `python3 scripts/build_llms.py` och commita llms.txt och llms-full.txt.

## Setup-sessionen

- Läsarens första steg är prompten på startsidan och sidan Kom igång. Den pekar på `setup/setup-session.md`, som är instruktionen läsarens AI följer. Filerna i `setup/` är skrivna till AI:n, inte till läsaren.
- Setup-sessionen sätter bara upp läsarens upplägg och arbetar aldrig med läsarens egna uppgifter. Grunden är projekt, inte Hjärnan. Sessionen frågar tidigt vilka projekt läsaren har. Har läsaren inga skapas ett projekt för det hen främst vill göra. Har läsaren projekt väljs det viktigaste, och sessionen ger snabbt en prompt dit så att utvärderingen görs inne i projektet. Guiden och min setup är en mall, inget facit, och sessionen ska inte försöka ge läsaren ett lika utbyggt upplägg som guiden beskriver.
- Hjärnan, listor och morgonbrev skapas inte av setup-sessionen om inte läsaren själv vill. Vill hen det tar sessionen först reda på vad hen vill åstadkomma, vad det ska innehålla och vad som behövs, och föreslår det minsta som löser problemet.
- Setup-sessionen förklarar vad läsaren lägger grunden till när den vet hur läsaren arbetar, med längd och djup efter det, och utgår från att läsaren inte har läst något annat. Grundprincipen ska alltid fram: strukturerat material är ingenting utan tydliga regler, och reglerna blir bra först när de justeras med användning.
- Setup-filerna värderar aldrig läsarens nivå. De anpassar sig efter vad läsaren använder och hur.
- Vid beslut som formar upplägget föreslår setup-sessionen ett avsnitt i guiden att läsa innan läsaren svarar.
- Prompten "När du vill bygga vidare" finns på startsidan, i Kom igång och i setup-session.md (avsnittet "Prompten från startsidan" och prompterna i steg 3a, 3b och 4). Ändras den, ändra på alla ställena.
- Varje prompt som setup-sessionen ger för en ny chatt börjar ordagrant med den prompten och fortsätter efter "Det här vill jag göra:" med länken till rätt setupfil och vad som är bestämt. Lita aldrig på att en chatt går att flytta mellan projekt.
- När setup-sessionen låter läsaren skapa ett nytt projekt ger den bara två saker: hur projektet skapas och döps, och startprompten. Inga projektinstruktioner, filer eller mappar i samma veva. De tas inne i projektet, eftersom instruktioner som skrivs innan materialet är strukturerat blir inaktuella direkt.
- Projektets setup (`setup/fokusprojekt.md`) har två lägen: nytt projekt och projekt som redan används. Ett projekt som används analyseras först (instruktioner, material, minne, chattar), läsaren intervjuas om det som skaver och sessionen frågar innan den ändrar något.
- Sedan materialet: analysera, strukturera och skriv om till Markdown i en egen mapp innan instruktionerna skrivs och innan något arbete görs, gärna med subagenter. Originalfilerna ändras aldrig. Filer som är uppladdade i projektets kontext tas via en kopplad mapp på datorn. Markdown-filerna ligger lokalt, med en kopia i molnet om läsaren vill nå dem från mobilen.
- Projektinstruktionerna som setupen skriver har med hur Claude hanterar det den producerar (vem läser, behövs ett dokument alls, var ska det ligga) och att instruktionerna är levande.
- Appen ser olika ut i webbläsaren, i appen för datorn och mellan versioner (klassisk och ny projektvy). Setup-sessionen tar därför först reda på app, versionsnummer och vy, och har instruktioner för båda vyerna.
- Projektet sätts upp i en egen chatt som startas med en prompt från setup-sessionen och följer `setup/fokusprojekt.md`. Prompten innehåller länken till llms-full.txt, säger om projektet är nytt eller redan används och har en bakgrund från setup-sessionen. Chatten slutar med en prompt för nästa arbetschatt.
- Båda filerna innehåller en karta med länkar till kapitel och avsnitt på sajten. När en rubrik i docs/ byts eller ett kapitel flyttas: uppdatera kartan och kontrollera att ankarlänkarna fortfarande fungerar.
- Prompterna i rutorna "Gör det med din Claude" klistras in i det projekt kapitlet gäller, inte i en lös chatt.
- Startprompten ska förbli kort. Förbättringar görs i `setup/setup-session.md`, så att samma prompt fortsätter att fungera.
