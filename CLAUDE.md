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
- Setup-sessionen sätter bara upp läsarens upplägg och arbetar aldrig med läsarens egna uppgifter. Den slutar alltid med exakt två projekt: Hjärnan, där setupen fortsätter i en ny chatt som blir kvar som Setup-chatt, och ett fokusprojekt för det läsaren främst vill få gjort. Befintliga projekt får bli de två, och har läsaren redan motsvarande blir sessionen en utvärdering. Den ska inte försöka ge läsaren ett lika utbyggt upplägg som guiden beskriver, men ska säga vad läsaren lägger grunden till.
- Setup-filerna värderar aldrig läsarens nivå. De anpassar sig efter vad läsaren använder och hur.
- Vid beslut som formar upplägget föreslår setup-sessionen ett avsnitt i guiden att läsa innan läsaren svarar.
- Prompten "När du vill bygga vidare" finns på startsidan, i Kom igång och i setup-session.md (avsnittet "Prompten från startsidan" och prompterna i steg 4, 6 och 7). Ändras den, ändra på alla ställena.
- Varje prompt som setup-sessionen ger för en ny chatt börjar ordagrant med den prompten och fortsätter efter "Det här vill jag göra:" med länken till rätt setupfil och vad som är bestämt. Lita aldrig på att en chatt går att flytta mellan projekt.
- Appen ser olika ut i webbläsaren, i appen för datorn och mellan versioner (klassisk och ny projektvy). Setup-sessionen tar därför först reda på app, versionsnummer och vy, och har instruktioner för båda vyerna.
- Fokusprojektet sätts upp i en egen kort chatt som startas med en prompt från Hjärnan och följer `setup/fokusprojekt.md`. Prompten innehåller länken till llms-full.txt och säger att projektet inte är Hjärnan. Chatten slutar med en prompt för den första arbetschatten.
- Båda filerna innehåller en karta med länkar till kapitel och avsnitt på sajten. När en rubrik i docs/ byts eller ett kapitel flyttas: uppdatera kartan och kontrollera att ankarlänkarna fortfarande fungerar.
- Prompterna i rutorna "Gör det med din Claude" klistras in i läsarens projekt, inte i en lös chatt.
- Startprompten ska förbli kort. Förbättringar görs i `setup/setup-session.md`, så att samma prompt fortsätter att fungera.
