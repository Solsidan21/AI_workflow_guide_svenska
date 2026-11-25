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

- Läsarens första steg är prompten på startsidan och sidan Kom igång. Den pekar på `setup/setup-session.md`, som är instruktionen läsarens AI följer. Filen är skriven till AI:n, inte till läsaren.
- Setup-sessionen sätter bara upp läsarens upplägg (Hjärnan, eventuella områdesprojekt, var saker ska ligga) och avslutas med att chatten flyttas in i projektet och ett nästa steg. Den arbetar aldrig med läsarens egna uppgifter.
- Filen innehåller en karta med länkar till kapitel och avsnitt på sajten. När en rubrik i docs/ byts eller ett kapitel flyttas: uppdatera kartan och kontrollera att ankarlänkarna fortfarande fungerar.
- Prompterna i rutorna "Gör det med din Claude" klistras in i läsarens projekt, inte i en lös chatt.
- Startprompten ska förbli kort. Förbättringar görs i `setup/setup-session.md`, så att samma prompt fortsätter att fungera.
