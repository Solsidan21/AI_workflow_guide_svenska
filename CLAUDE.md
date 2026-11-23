# CLAUDE.md — Projektstilregler

## Skrivregler

### Tankstreck (em dash)
- Tankstreck (—) ska INTE användas mitt i meningar i löpande text. Skriv om till punkt, komma, kolon eller omformulering istället.
- Undantag: kapitelrubriker och titlar där det är vedertaget format (t.ex. `# Kapitel 01 — Titel`).

## Två läsare

- Sajten (docs/ byggd med MkDocs) är för människor. Den ska gå att slå upp i, inte läsas från pärm till pärm: kort version överst i varje kapitel, en fråga per avsnitt, begrepp i hopfällbara rutor.
- Repot är för läsarens egen AI. Prompterna i rutorna "Gör det med din Claude" pekar därför på råfilerna på raw.githubusercontent.com, inte på sajten.
- Efter varje ändring i docs/ eller begrepp/: kör `python3 scripts/build_llms.py` och commita llms.txt och llms-full.txt.
