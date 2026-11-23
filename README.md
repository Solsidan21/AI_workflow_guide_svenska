# AI-workflowguiden: från chatt till eget system

**Läs guiden på [solsidan21.github.io/AI_workflow_guide_svenska](https://solsidan21.github.io/AI_workflow_guide_svenska/).**

Samma AI-modeller finns tillgängliga för alla. Det som avgör nyttan är vad modellen får att arbeta med: källor, regler, verktyg och rutiner. Den här guiden visar hur du bygger ett eget system för det med en vanlig prenumeration, i stället för att betala för en rad separata AI-tjänster. Claude är huvudspåret, och ChatGPT och Codex tas upp där det finns motsvarigheter.

Jag använder mina egna universitetskurser som konkret exempel, framför allt Flervariabelanalys ([kursrepot finns här](https://github.com/Solsidan21/Flervariabelanalys_ht26)). Plugget är exemplet, inte ämnet. Samma upplägg fungerar i ett jobb, en hobby eller i vardagen.

## Innehåll

**Del 1: Grunden**

1. [Från chatt till system](docs/01-fran-chatt-till-system.md): verktygen i dag, från chatt till Claude Code
2. [Kontext i stället för långa prompter](docs/02-kontext.md): därför räcker en kort fråga
3. [Struktur som kontext](docs/03-struktur.md): mappar, Markdown, CLAUDE.md och skills

**Del 2: Mitt system**

4. [Arkitekturen](docs/04-arkitekturen.md): repon, projekt, Drive och schemalagda uppgifter
5. [Individanpassad inlärning](docs/05-individanpassad-inlarning.md): en kurs formad efter hur jag lär mig
6. [Hjärnan](docs/06-hjarnan.md): ett centralt projekt som håller koll på helheten
7. [Att bygga vidare på](docs/07-bygga-vidare.md): sätt att utveckla systemet

**Del 3: Helheten**

8. [Modellerna](docs/08-modellerna.md): Haiku, Sonnet, Opus och Fable, benchmarks och produkt mot modell
9. [Tröskeln, inte förmågan](docs/09-troskeln.md): varför det mesta har gått att göra länge och vad som faktiskt har ändrats
10. [Därför slår du i taket](docs/10-anvandningsgransen.md): användningsgränsen och hur du får mer för mindre
11. [Vad en prenumeration räcker till](docs/11-vad-en-prenumeration-racker-till.md): vad du redan betalar för och när en färdig tjänst är värd pengarna
- [Bilaga: Samma upplägg i arbetslivet](docs/bilaga-arbetsliv.md)
- [Ordlista](docs/ordlista.md)

## Mallar

I [`templates/`](templates/) finns färdiga mallar med CLAUDE.md och skills för private equity, konsultarbete och marknadsföring.

## Teknik

Sajten byggs med MkDocs Material och publiceras automatiskt när main uppdateras. Begreppsförklaringarna skrivs en gång i `begrepp/` och visas både som hopfällbara rutor i kapitlen och i ordlistan.
