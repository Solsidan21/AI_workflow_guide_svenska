# AI-workflowguiden: ditt eget skal runt modellen

**Läs guiden på [solsidan21.github.io/AI_workflow_guide_svenska](https://solsidan21.github.io/AI_workflow_guide_svenska/).**

Samma AI-modeller finns tillgängliga för alla. Bolag som Legora och Lovable bygger sina produkter som ett skal runt modeller från de stora labben: verktyg, källor, instruktioner och arbetsflöden. Den här guiden visar hur du bygger ditt eget skal för eget bruk med en vanlig prenumeration. Claude är huvudspåret, och ChatGPT och Codex tas upp där det finns motsvarigheter.

Jag använder mina egna universitetskurser som konkret exempel, framför allt Flervariabelanalys ([kursrepot finns här](https://github.com/Solsidan21/Flervariabelanalys_ht26)). Plugget är exemplet, inte ämnet. Samma upplägg fungerar i ett jobb, en hobby eller i vardagen.

## Innehåll

**Del 1: Grunden**

1. [Från chatt till system](docs/01-fran-chatt-till-system.md): verktygen i dag, från chatt till Claude Code
2. [Kontext och prompter](docs/02-kontext-och-prompter.md): varför kontext avgör kvaliteten
3. [Struktur som kontext](docs/03-struktur.md): mappar, Markdown, CLAUDE.md och skills

**Del 2: Mitt system**

4. [Arkitekturen](docs/04-arkitekturen.md): repon, projekt, Drive och schemalagda uppgifter
5. [Individanpassad inlärning](docs/05-individanpassad-inlarning.md): en kurs formad efter hur jag lär mig
6. [Hjärnan](docs/06-hjarnan.md): ett centralt projekt som håller koll på helheten
7. [Att bygga vidare på](docs/07-bygga-vidare.md): sätt att utveckla systemet

**Del 3: Modellen och skalet**

8. [Modellen och skalet](docs/08-modellen-och-skalet.md): vad bolagen bygger, och vad du kan bygga själv
- [Bilaga: Samma upplägg i arbetslivet](docs/bilaga-arbetsliv.md)
- [Ordlista](docs/ordlista.md)

## Mallar

I [`templates/`](templates/) finns färdiga mallar med CLAUDE.md och skills för private equity, konsultarbete och marknadsföring.

## Teknik

Sajten byggs med MkDocs Material och publiceras automatiskt när main uppdateras. Begreppsförklaringarna skrivs en gång i `begrepp/` och visas både som hopfällbara rutor i kapitlen och i ordlistan.
