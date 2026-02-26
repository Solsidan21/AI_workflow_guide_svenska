# AI-djupdykning — Från chatt till system

> *Jag heter Arvid, läser ekonomi och har ingen teknisk bakgrund. Under några intensiva veckor dök jag djupt ner i hur AI-verktyg faktiskt fungerar — bortom chatten. Det här är vad jag önskar att någon hade förklarat för mig innan jag började.*

---

## Varför den här guiden finns

I början av 2025 hörde jag alla prata om AI — att man måste lära sig koda, att jobb kommer försvinna, att allt förändras. Så jag tänkte: om AI verkligen är så kraftfullt borde jag kunna bygga den app jag gått och tänkt på länge.

Jag startade. Och fick börja om. Tre gånger på tre veckor — för att jag inte förstod hur man faktiskt bygger ett system, inte bara chattar med AI. Parallellt upptäckte jag vad verktygen kunde göra i arbetslivet: jag satte upp en agent åt min mamma som automatiserade uppgifter som normalt tog timmar.

När jag sedan försökte förklara allt jag lärt mig för familj och vänner utan teknisk bakgrund insåg jag hur svårt det var. Det här är resultatet — guiden jag önskar att jag hade haft innan jag dök in i det här enorma området.

Den är skriven för dig som redan använder AI dagligen men vill förstå hur du bygger system som gör AI 10x bättre på just ditt jobb. Inte genom bättre promptar — utan genom struktur, regler och minne.

Du behöver inte kunna programmera. Jag kan inte det heller. Men du är redo att ta ett steg utanför chatten.

---

!!! tip "Varför Claude som huvudexempel?"
    Jag började faktiskt med OpenAI:s Codex via ChatGPT Pro, testade sedan Claude Code, och använder Cursor för apputveckling. Jag kan inte säga vilken AI som är "bäst" — landskapet förändras varje vecka och det finns starka alternativ från OpenAI, Google, Meta och DeepSeek.

    Anledningen till att Claude är huvudexemplet i den här guiden är konkret: **Claude Projects har en inbyggd GitHub-integration.** Jag syncar mitt repo till ett projekt, och Claude ser alla ändringar automatiskt — utan att jag behöver ladda ner och ladda upp filer varje gång jag pushar. Det sparar enormt med tid och gör arbetsflödet smidigt.

    Det är den enda anledningen jag med säkerhet kan peka på. Principerna i guiden — regler, struktur, persistent kontext — fungerar oavsett verktyg.

---

## Känner du igen dig?

- Du har en Custom GPT eller ett Claude-projekt som ger bra svar — men ibland helt ignorerar sina instruktioner, och du vet inte varför
- Du laddar upp filer varje gång, men AI:n verkar glömma hälften ändå
- Du kopierar samma kontext mellan sessioner och undrar om det finns ett bättre sätt
- Du vill att AI:n ska följa *din* metod, inte sin egen — men vet inte hur du styr den

Om något av det stämmer in är du på rätt ställe. Den här guiden visar vad som händer när du ger AI regler, struktur och minne.

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
