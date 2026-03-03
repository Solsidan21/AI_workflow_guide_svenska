# AI-djupdykning — Från chatt till system

**En guide för dig som redan använder AI men vill förstå varför den ibland briljerar och ibland ger generiska svar, och vad du kan göra åt det.**

---

## Om den här guiden

Du använder sannolikt redan ChatGPT eller Claude dagligen — kanske laddar du upp filer, har skapat Custom GPTs, eller experimenterat med Projects. Du vet hur man skriver en bra prompt och du får bra svar.

Men du upprepar dig. Varje session börjar från noll. Du kopierar data fram och tillbaka. AI:n är inte problemet. Den är redan smart nog. Problemet är förutsättningarna du ger den. Den här guiden visar vad som händer när du ger AI struktur, regler och kontext istället för råa PDF:er och improviserade prompts.

**Guiden använder Claude som huvudexempel**, men principerna — persistent kontext, regler, mappstruktur, återanvändbara arbetsflöden — gäller oavsett vilket AI-verktyg du använder. Där det är relevant pekar vi ut hur koncept översätts mellan verktyg.

Guiden är skriven för **kunskapsarbetare** som använder AI dagligen men inte fått ut dess fulla potential. Du behöver inte kunna programmera. Du behöver inte ha öppnat en terminal förut. Men du är nyfiken på varför AI ibland levererar exakt det du behöver och ibland missar helt, och vad du kan göra annorlunda.

---

## Innehållsförteckning

### Del 1 — Förstå landskapet (koncept & tänkesätt)

| Nr | Kapitel | Beskrivning |
|----|---------|-------------|
| 01 | [AI-verktygslandskapet](docs/01-verktygslandskapet.md) | Trappan från chatt till system — Chat, Office, Code och Cowork |
| 02 | [Promptteknik och kontext](docs/02-promptteknik-och-kontext.md) | Varför kontext avgör allt — och teknikerna som gör skillnad |
| 03 | [Mappstruktur och arbetssätt](docs/03-mappstruktur-och-arbetssatt.md) | Det centrala arbetsflödet — CLAUDE.md, skills och PDF→Markdown→GitHub |
| 04 | [Strukturerad kontext](docs/04-strukturerad-kontext.md) | Varför navigerbar kontext + regler slår maxad kontext |

### Del 2 — Praktiska exempel

| Nr | Kapitel | Beskrivning |
|----|---------|-------------|
| 05 | [Exempel: Studier](docs/05-exempel-studier.md) | Hela kursen i fickan — AI-system för universitetsstudier |
| 06 | [Exempel: Private Equity](docs/06-exempel-private-equity.md) | Norvik Capital — hela firmans AI-system i praktiken |

### Referens

| | | |
|----|---------|-------------|
| — | [Ordlista](docs/ordlista.md) | Alla begrepp på ett ställe — din referens för tekniska termer |

### Mallar

I mappen [`templates/`](templates/) finns färdiga mallar och exempelfiler som du kan använda direkt:

- **Private Equity** — CLAUDE.md, skills för kassaflödesanalys, investment memo och due diligence
- **Konsulting** — CLAUDE.md, skills för marknadsanalys och strategisk rekommendation
- **Marknadsföring** — CLAUDE.md, skills för innehållsplanering och kampanjanalys

---

## Kom igång

Du kan läsa guiden från början till slut, eller hoppa direkt till det du behöver:

- **Vill förstå verktygen?** [Kapitel 01](docs/01-verktygslandskapet.md) ger dig hela kartan från chatt till autonoma agenter.
- **Vill förstå prompting och kontext?** [Kapitel 02](docs/02-promptteknik-och-kontext.md) visar teknikerna som gör störst skillnad.
- **Vill förstå hur struktur och kontext gör skillnad?** [Kapitel 03](docs/03-mappstruktur-och-arbetssatt.md) visar det i praktiken.
- **Vill se ett konkret exempel?** [Kapitel 06](docs/06-exempel-private-equity.md) visar hur en hel PE-firma sätter upp sitt AI-system.
- **Behöver du ett begrepp förklarat?** [Ordlistan](docs/ordlista.md) har alla tekniska termer samlade.

---

## Språk

Allt innehåll är på **svenska**. Tekniska termer förklaras första gången de dyker upp, och engelska facktermer används bara när det är branschstandard.

---

## Bidra och licens

Förslag, rättningar och tillägg är välkomna — öppna en issue eller skicka en pull request.

Innehållet är fritt att använda och dela vidare för icke-kommersiella ändamål.
