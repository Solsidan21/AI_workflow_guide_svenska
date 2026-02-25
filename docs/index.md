# Sluta hoppas att AI:n förstår

> **Du har redan bra promptar och smarta uppsättningar. Den här guiden visar hur du går från "det funkar oftast" till "den gör exakt vad jag vill, varje gång."**

---

Du har Custom GPTs med instruktioner.
Du har Projects med filer.
Resultatet är bra — ibland.

Men du kan inte riktigt förklara varför det funkar när det funkar.
Och du vet inte vad som gick fel när det inte gör det.

**Den här guiden visar hur du bygger AI-system du faktiskt kan styra —
med regler, struktur och minne som inte försvinner.**

Guiden använder **Claude som huvudexempel**, men principerna gäller oavsett AI-verktyg.

---

!!! tip "Du behöver inte programmera"
    Jag som skrivit guiden — Arvid — läser ekonomie kandidatprogrammet och är inte programmerare. Allt du ser här har jag byggt utan att kunna koda. Du behöver inte ha öppnat en terminal förut, men du behöver vara redo att ta ett steg utanför chatten.

---

## Känner du igen dig?

- Du har en Custom GPT som ger bra svar — men ibland helt ignorerar sina instruktioner, och du vet inte varför
- Du laddar upp filer i ett Project varje gång, men Claude verkar glömma hälften ändå
- Du kopierar samma kontext mellan sessioner och undrar om det finns ett bättre sätt
- Du vill att AI:n ska följa *kursens* metod, inte sin egen — men vet inte hur du tvingar den

Om något av det stämmer in är du på rätt ställe.

---

## Kapitelöversikt

=== "Del 1 — Förstå landskapet"

    **[00 — Grundbegrepp](00-grundbegrepp.md)**
    De ~10 begrepp som öppnar dörren till nästa nivå

    **[01 — AI-verktygslandskapet](01-verktygslandskapet.md)**
    Trappan från chatt till system — Chat, Office, Code och Cowork

    **[02 — Promptteknik och kontext](02-promptteknik-och-kontext.md)**
    Varför kontext avgör allt — och teknikerna som gör skillnad

    **[03 — Mappstruktur och arbetssätt](03-mappstruktur-och-arbetssatt.md)**
    Det centrala arbetsflödet — CLAUDE.md, skills och PDF→Markdown→GitHub

    **[04 — Strukturerad kontext](04-strukturerad-kontext.md)**
    Varför navigerbar kontext + regler slår maxad kontext

=== "Del 2 — Praktiska exempel"

    **[05 — Exempel: Studier](05-exempel-studier.md)**
    Hela kursen i fickan — AI-system för universitetsstudier

    **[06 — Exempel: Private Equity](06-exempel-private-equity.md)**
    Norvik Capital — hela firmans AI-system i praktiken

    **[07 — Exempel: Marknadsförare](07-exempel-marknadsforing.md)**
    AI i det dagliga arbetet *(kommer snart)*

    **[08 — Exempel: Konsult](08-exempel-konsult.md)**
    Från analys till leverans *(kommer snart)*

---

??? tip "Färdigbyggda mallar"
    I repots [`templates/`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates)-mapp finns färdiga startpunkter — CLAUDE.md-exempel, skills och projektstrukturer för Private Equity, marknadsföring och konsulting.

---

!!! info ""
    Allt innehåll på svenska. Tekniska termer förklaras första gången de dyker upp. Engelska facktermer används bara när det är branschstandard.
