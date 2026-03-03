# Kapitel 04 — Strukturerad kontext

> *Du har gett AI hela kursboken, alla rapporter och ett halvår av mejl. Varför ger den fortfarande generiska svar?*

---

Du gör redan mer än de flesta. Du har laddat upp filer i ett Claude-projekt eller ChatGPT, skrivit projektinstruktioner, kanske till och med organiserat materialet i mappar. Och det fungerar, hyfsat. Du får svar som är bättre än utan kontext.

Men det är just det som är fällan. Det *känns* som att du redan gör rätt. Så varför ta ytterligare ett steg?

---

## Fällan: mer information = bättre svar?

De flesta som börjar använda AI på allvar gör ungefär samma sak: laddar upp filer, skriver korta instruktioner, och lägger till mer material i tron att kvantitet ger kvalitet.

Det stämmer till en punkt. Men sedan planar det ut, eller blir sämre. Och det beror på en enkel sak:

**AI:n är redan smart nog att förstå ditt material. Den vet bara inte var den ska titta.**

Tänk dig en extremt kompetent konsult som du ger en pappershög med 200 osorterade sidor och säger: "Analysera det här. Du har fem minuter." Konsulten är fortfarande kompetent. Men hälften av tiden går åt att sortera istället för att tänka.

Det är exakt vad som händer när du ger AI ostrukturerad kontext. Problemet förvärras av att PDF:er (det vanligaste formatet) dessutom kostar mångfalt mer tokens och ofta feltolkas, som beskrevs i [kapitel 02](02-promptteknik-och-kontext.md) och [kapitel 03](03-mappstruktur-och-arbetssatt.md).

---

## Nyckelinsikten

**Navigerbar kontext + regler > maxad kontext.**

Tänk dig två studenter som pluggar inför tenta. Den ena har en hög med alla utskrivna föreläsningar och hela kursboken på skrivbordet. Den andra har en välorganiserad pärm med flikar: föreläsning per föreläsning, kapitelsammanfattningar, och en innehållsförteckning.

Båda har samma information. Men den andra hittar svaret på tio sekunder.

Det är exakt vad strukturerad kontext handlar om: att ta samma kunskap och göra den navigerbar. Tydliga rubriker, logiska filnamn, regler som säger "för den typen av fråga, titta här." Du gör inte AI:n smartare. Du låter den använda sin kapacitet.

---

## Skillnaden i praktiken

Tänk dig att du frågar: *"Hur har CloudFlows marginal utvecklats de senaste tre åren?"*

**Med ostrukturerad kontext:** AI:n processar hela årsredovisningen (50 sidor, tusentals tokens), försöker hitta rätt tabell, kanske tolkar den fel, och ger ett svar blandat med irrelevant information.

**Med strukturerad kontext:** AI:n ser `portfoljbolag/cloudflow-ab/bolagsdata/nyckeltal.md`, läser en fil med exakt rätt data (några hundra tokens), och svarar med precision. Reglerna har redan sagt att siffror ska vara i MSEK med en decimal.

Samma fråga. Samma underliggande information. Samma AI-modell. Men helt olika kvalitet på svaret.

Det handlar inte om att använda ett specifikt verktyg eller följa ett specifikt arbetsflöde. Det handlar om principen: **ge AI rätt information i rätt format, med regler som hjälper den fokusera.** Hur du implementerar det beror på dina verktyg och ditt arbete. Principen håller oavsett.

---

## Koppling framåt

Du har nu bilden av *varför* strukturerad kontext gör skillnad. Del 2 visar hur det ser ut i praktiken: för [studier](05-exempel-studier.md) och för [Private Equity](06-exempel-private-equity.md). Men principen är densamma oavsett bransch eller roll.

---

> *Föregående kapitel: [03 — Mappstruktur och arbetssätt](03-mappstruktur-och-arbetssatt.md)*
>
> *Nästa kapitel: [05 — Exempel: Studier](05-exempel-studier.md)*
