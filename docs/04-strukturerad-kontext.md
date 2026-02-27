# Kapitel 04 — Strukturerad kontext

> *Du har gett AI hela kursboken, alla rapporter och ett halvår av mejl. Varför ger den fortfarande generiska svar?*

---

Du gör redan mer än de flesta. Du har laddat upp filer i ett Claude-projekt eller ChatGPT, skrivit projektinstruktioner, kanske till och med organiserat materialet i mappar. Och det fungerar, hyfsat. Du får svar som är bättre än utan kontext.

Men det är just det som är fällan. Det *känns* som att du redan gör rätt. Så varför ta ytterligare ett steg?

Det här kapitlet förklarar varför, och vad det steget innebär.

---

## Det vanliga beteendet

De flesta som börjar använda AI på allvar gör ungefär samma sak:

1. **Laddar upp PDF:er** i ett Claude-projekt eller ChatGPT
2. **Skriver korta projektinstruktioner:** "du är min assistent för kvartalsrapportering"
3. **Lägger till mer material** i tron att mer information = bättre svar
4. **Får hyfsat bra svar,** och stannar där

Det är en rimlig strategi. Mer kontext *borde* ge bättre svar. Och det gör det, till en punkt. Men sedan planar det ut, eller blir sämre. Och det beror på två problem som hänger ihop.

---

## Två problem som förstärker varandra

### Problem 1 — PDF-formatet

PDF:er är gjorda för människor att läsa på skärm eller skriva ut. De är **inte gjorda för AI att navigera.**

- **Token-kostnad.** En PDF förbrukar mångfalt fler tokens än samma information i Markdown. Varje gång AI:n läser din 50-sidiga årsredovisning äter den tusentals tokens, även om du bara behöver tre rader.
- **Opålitlig extraktion.** Tabeller, formler och layout bryts ofta vid tolkning. Siffror hamnar fel. Kolumner blandas ihop.
- **Ingen navigering.** AI:n kan inte "bläddra" till rätt sida. Den processar allt, från framsida till appendix, varje gång.

Du har redan läst om detta i [kapitel 02](02-promptteknik-och-kontext.md) och [kapitel 03](03-mappstruktur-och-arbetssatt.md). Poängen här är inte att upprepa det, utan att koppla det till det andra problemet.

### Problem 2 — Ostrukturerad kontext

Mer information är inte automatiskt bättre. Det är den vanligaste missuppfattningen.

AI:n med 200 sidor ostrukturerad text i kontexten är som en student med hela bokhyllan uppslagen på skrivbordet. Allt är synligt, men inget sticker ut. Utan tydlig struktur vet AI:n inte vilken del av materialet som är relevant för just din fråga.

Dessutom har kontextfönstret en gräns. Fyller du det med obearbetad text tränger du ut utrymmet för själva resonerandet. Det är som att ge konsulten en hög med papper och sedan säga "du har fem minuter". Hälften av tiden går åt att sortera istället för att tänka.

### Hur problemen förstärker varandra

PDF:er tar upp mycket plats *och* saknar struktur. Du fyller kontexten med material som är svårt att navigera, och lämnar mindre plats för AI:n att faktiskt arbeta med din fråga. Resultatet: generiska svar som inte utnyttjar materialet du faktiskt gett den.

---

## Nyckelinsikten

**Navigerbar kontext + regler > maxad kontext.**

Tänk dig två studenter som pluggar inför tenta. Den ena har en hög med alla utskrivna föreläsningar och hela kursboken på skrivbordet. Den andra har en välorganiserad pärm med flikar: föreläsning per föreläsning, kapitelsammanfattningar, och en innehållsförteckning.

Båda har samma information. Men den andra hittar svaret på tio sekunder.

Det du bygger med Markdown + mappstruktur + CLAUDE.md är **pärmen med flikar**. Du tar exakt samma kunskap och gör den navigerbar, med tydliga rubriker, logiska filnamn och regler som säger "för den typen av fråga, titta här."

Det här gäller oavsett vad du gör. Student, konsult, PE-analytiker, marknadsförare. Principen är densamma: **ge AI rätt information i rätt format, med regler som hjälper den fokusera.**

---

## Vad "strukturerad kontext" betyder i praktiken

Det handlar om fyra delar som samverkar:

### 1. Markdown istället för PDF

Markdown är ren text med struktur: rubriker, listor, tabeller. Det är lättnavigerat, token-effektivt och tolkas korrekt varje gång. En PDF som kostar tusentals tokens kostar några hundra som Markdown.

Du behöver inte skriva Markdown manuellt. Du ber Claude extrahera det viktiga från PDF:en en gång, och sedan arbetar du mot Markdown-versionen. Originalet behåller du som källa.

### 2. Mappstruktur som organiserar

Filnamn och mappar **är** instruktioner. När Claude ser `data/finansiellt/arsredovisning-2024/nyckeltal.md` vet den exakt vad filen innehåller, utan att du förklarat det. Jämför med `dokument/fil3.pdf`. Då vet Claude ingenting.

Det här är inte arkivering för arkiveringens skull. Det är kontext som AI:n använder varje gång den letar efter information. (Mer om detta i [kapitel 03](03-mappstruktur-och-arbetssatt.md).)

### 3. CLAUDE.md som styr fokus

Utan regler vet AI:n inte vad som är relevant. CLAUDE.md säger: "det här är projektet, det här är tonen, och för den typen av fråga, titta i den mappen." Det är skillnaden mellan en assistent som börjar från noll och en som känner projektet.

### 4. Skills som definierar arbetsflöden

En skill är en återanvändbar instruktion: "när du gör en kvartalsrapport, gå igenom de här stegen, i den här ordningen, med det här formatet." Istället för att förklara processen varje gång aktiverar du den med ett kommando.

### Skillnaden i praktiken

Tänk dig att du frågar: *"Hur har CloudFlows marginal utvecklats de senaste tre åren?"*

**Med dumpade PDF:er:** AI:n processar hela årsredovisningen (50 sidor, tusentals tokens), försöker hitta rätt tabell, kanske tolkar den fel, och ger ett svar baserat på allt den hittade, blandat med irrelevant information.

**Med strukturerat repo:** AI:n ser `portfoljbolag/cloudflow-ab/bolagsdata/nyckeltal.md`, läser en fil med exakt rätt data (några hundra tokens), och svarar med precision. CLAUDE.md har redan sagt att siffror ska vara i MSEK med en decimal.

Samma fråga. Samma underliggande information. Men helt olika kvalitet på svaret, och helt olika kostnad i tokens och tid.

---

## Koppling framåt

Du har nu bilden av *varför* strukturerad kontext gör skillnad. Del 2 visar hur det ser ut i praktiken: för [studier](05-exempel-studier.md), för [Private Equity](06-exempel-private-equity.md), för [marknadsföring](07-exempel-marknadsforing.md). Men principen är densamma: ge AI rätt information i rätt format med regler som hjälper den fokusera.

---

> *Föregående kapitel: [03 — Mappstruktur och arbetssätt](03-mappstruktur-och-arbetssatt.md)*
>
> *Nästa kapitel: [05 — Exempel: Studier](05-exempel-studier.md)*
