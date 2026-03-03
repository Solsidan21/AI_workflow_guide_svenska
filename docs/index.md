# AI Workflow Guide — Från chatt till system

> *Jag heter Arvid, läser ekonomi och matematik på Lunds Universitet och har egentligen ingen teknisk bakgrund. Under några intensiva veckor dök jag djupt ner i hur AI-verktyg faktiskt fungerar — bortom chatten. Det här är vad jag önskar att någon hade förklarat för mig innan jag började.*

---

Du använder sannolikt redan ChatGPT eller Claude dagligen. Du vet hur man skriver en bra prompt och du får bra svar.

Men du gör samma sak om och om igen. Varje session börjar från noll. Du kopierar data fram och tillbaka. Du förklarar samma kontext för tionde gången.

**Den här guiden handlar om en insikt: AI:n du redan använder är tillräckligt smart för att göra mycket mer än du tror.** Inte genom bättre promptar, utan genom att ge den bättre förutsättningar: struktur, regler och kontext.

Du behöver inte kunna programmera. Du behöver inte ha öppnat en terminal förut. Men du är redo att förstå varför AI ibland ger fantastiska svar och ibland generiska, och vad du kan göra åt det.

---

## Vad blir möjligt?

När du går från chatt till system öppnas helt nya sätt att arbeta med AI:

- **Studier:** Synca hela din kurs — kursplan, föreläsningsanteckningar, övningar — till ett AI-projekt och få en studieassistent som kan kursen utantill
- **Private Equity:** Peka AI mot en datamapp, säg "screening-memo på det här bolaget" och få ett komplett utkast i ditt format på sekunder
- **Marknadsföring:** Bygg ett arbetsflöde som genererar kanalanpassat innehåll med rätt varumärkeston, utan att du förklarar brand guidelines varje gång
- **Konsulting:** Definiera firmans metodik en gång och låt varje analys följa den automatiskt

Det kräver inte att du lär dig ett specifikt verktyg eller arbetsflöde. Verktygen förändras ständigt. Men principerna bakom dem, att ge AI rätt kontext i rätt format, håller oavsett. Den här guiden finns för att ge dig den förståelsen.

??? note "Vem har skrivit det här?"
    Jag heter Arvid, läser ekonomi och matematik på Lunds Universitet och har egentligen ingen teknisk bakgrund. Det är enormt mycket snack om AI just nu, så jag tänkte: om det verkligen stämmer borde jag kunna bygga den app jag gått och tänkt på länge.

    Jag startade. Och fick börja om. Tre gånger på tre veckor, för att jag inte förstod hur man faktiskt bygger ett system, inte bara chattar med AI. Parallellt upptäckte jag vad verktygen kunde göra i arbetslivet: jag satte upp en agent åt min mamma som automatiserade uppgifter som normalt tog timmar.

    När jag sedan försökte förklara allt jag lärt mig för familj och vänner utan teknisk bakgrund insåg jag hur svårt det var. Det här är resultatet: guiden jag önskar att jag hade haft innan jag dök in i det här enorma området.

!!! info "En insikt som förändrade mitt arbetsflöde"
    Det enklaste sättet att göra AI bättre är inte att skriva bättre promptar. Det är att sluta mata den med råa PDF:er. PDF:er kostar mångfalt mer kontext, tabeller feltolkas, och AI:n kan inte navigera till rätt sida. Kapitel 02 och 03 visar hur du löser det.

---

## Kapitelöversikt

=== "Del 1 — Förstå landskapet"

    **[01 — AI-verktygslandskapet](01-verktygslandskapet.md)**
    Trappan från chatt till system: Chat, Office, Code och Cowork

    **[02 — Promptteknik och kontext](02-promptteknik-och-kontext.md)**
    Varför kontext avgör allt, och teknikerna som gör skillnad

    **[03 — Mappstruktur och arbetssätt](03-mappstruktur-och-arbetssatt.md)**
    Det centrala arbetsflödet: CLAUDE.md, skills och PDF→Markdown→GitHub

    **[04 — Strukturerad kontext](04-strukturerad-kontext.md)**
    Varför navigerbar kontext + regler slår maxad kontext

=== "Del 2 — Praktiska exempel"

    **[05 — Exempel: Studier](05-exempel-studier.md)**
    Hela kursen i fickan: AI-system för universitetsstudier

    **[06 — Exempel: Private Equity](06-exempel-private-equity.md)**
    Norvik Capital: hela firmans AI-system i praktiken

=== "Referens"

    **[Ordlista](ordlista.md)**
    Alla begrepp på ett ställe. Kom tillbaka hit när du stöter på ett ord du inte känner igen.

---

!!! tip "Varför Claude som huvudexempel?"
    Jag började faktiskt med OpenAI:s Codex via ChatGPT Pro, testade sedan Claude Code, och använder Cursor för apputveckling. Jag kan inte säga vilken AI som är "bäst". Landskapet förändras varje vecka och det finns starka alternativ från OpenAI, Google, Meta och DeepSeek.

    Anledningen till att Claude är huvudexemplet i den här guiden är konkret: **Claude Projects har en inbyggd GitHub-integration.** Jag syncar mitt repo till ett projekt, och Claude ser alla ändringar automatiskt, utan att jag behöver ladda ner och ladda upp filer varje gång jag pushar. Det sparar enormt med tid och gör arbetsflödet smidigt.

    Det är den enda anledningen jag med säkerhet kan peka på. Principerna i guiden (regler, struktur, persistent kontext) fungerar oavsett verktyg.

---

??? tip "Färdigbyggda mallar"
    I repots [`templates/`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates)-mapp finns färdiga startpunkter: CLAUDE.md-exempel, skills och projektstrukturer för Private Equity, marknadsföring och konsulting.

---

!!! info ""
    Allt innehåll på svenska. Tekniska termer förklaras första gången de dyker upp. Engelska facktermer används bara när det är branschstandard.
