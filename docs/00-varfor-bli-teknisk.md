# Kapitel 00 — Varfor det lonar sig att bli lite teknisk

> *Du behover inte bli programmerare. Men dessa begrepp oppnar dorrar.*

Innan vi dyker in i Claudes varld ska vi ga igenom en handfull begrepp som dyker upp om och om igen. Tanken ar inte att du ska bli utvecklare — tanken ar att du ska kanna dig hemma nar dessa ord dyker upp i en konversation, en guide eller ett verktyg.

Varje begrepp forklaras med:
- **Vad det ar** — en enkel definition
- **En analogi** — kopplat till nagot du redan kanner
- **Varfor det spelar roll** — hur det hjalper dig i AI-arbete

---

## 1. Filer och mappar

**Vad det ar:** Datorns satt att organisera information. En fil ar ett enskilt dokument (en rapport, ett kalkylblad, en bild). En mapp samlar filer som hor ihop.

**Analogi:** Tank dig ett dokumentskap pa kontoret. Varje lada ar en mapp, och pappren inuti ar filer. Du kan ha en lada for "Kunder", en for "Internrapporter" och sa vidare. Pa datorn fungerar det likadant — fast ladorna kan ligga inuti varandra (undermappar).

**Varfor det spelar roll:** Nar du arbetar med AI-verktyg som Claude Code kommer du att hantera filer direkt — lasa dem, redigera dem, organisera dem. Att forsta strukturen ar som att kunna hitta i sitt eget arkiv.

---

## 2. Terminalen

**Vad det ar:** Ett textbaserat satt att ge instruktioner till din dator. Istallet for att klicka pa ikoner och menyer skriver du kommandon.

**Analogi:** Forestall dig skillnaden mellan att peka pa saker i en butik och att skriva en bestallningslista. Bada fungerar, men skriftliga instruktioner kan vara mycket mer exakta: "Hamta den tredje laden i den blaa hyllan, oppna filen som heter budget.xlsx och visa rad 14-28." Det ar vad terminalen lat dig gora.

**Varfor det spelar roll:** Claude Code lever i terminalen. Du behover inte kunna hundratals kommandon — Claude hjalper dig — men att forsta vad terminalen ar gor att det kanns mindre frammande. Tank pa det som att du far en erfaren assistent som sitter redo i terminalfonstret och vantar pa dina instruktioner.

---

## 3. Markdown

**Vad det ar:** Ett enkelt satt att formatera text med vanliga tecken. En rubrik skrivs med `#`, fetstil med `**dubbelstjarnor**`, och listor med bindestreck.

**Analogi:** Du kanner Word dar du klickar pa knappar for att gora text fet eller skapa rubriker. Markdown ar som att skriva formateringsinstruktioner rakt i texten. Det ar lattare an det later — du laser faktiskt Markdown just nu om du tittar pa den har filen pa GitHub.

**Varfor det spelar roll:** Nastan all dokumentation i AI-varlden ar skriven i Markdown. Nar du skriver instruktioner till Claude, eller lagger upp information pa GitHub, anvander du Markdown. Det tar fem minuter att lara sig grunderna och oppnar en hel varld av dokumentation.

### Snabbreferens

```
# Rubrik 1
## Rubrik 2
### Rubrik 3

**Fetstil**
*Kursivt*

- Punkt i lista
- Annan punkt

1. Numrerad lista
2. Andra punkten

[Lankttext](https://example.com)
```

---

## 4. Git och GitHub

**Vad det ar:** Git ar ett system for versionshantering — det haller reda pa varje andring du gor i dina filer. GitHub ar en webbplats dar du kan lagra och dela dina Git-projekt.

**Analogi:** Tank pa "Sparade versioner" i Word — den dar funktionen som later dig ga tillbaka till en tidigare version. Git ar som det systemet, men pa steroider. Det fungerar for alla filer i ett helt projekt, det later flera personer arbeta samtidigt, och du kan alltid atervanda till exakt hur allt sag ut vid en specifik tidpunkt.

**Varfor det spelar roll:** Nar du borjar anvanda Claude Code ar Git det som gor att du aldrig behover vara radd att nagot gar sonder. Varje andring loggas. Du kan experimentera fritt, och om nagot inte fungerar gar du bara tillbaka till en version som funkade. Det ar ditt sakerhetsnat.

---

## 5. Repository (repo)

**Vad det ar:** En projektmapp som overvakas av Git. Alla filer i mappen, plus hela andringshistoriken, bildar ett repository.

**Analogi:** Om Git ar systemet for att spara versioner sa ar ett repo den specifika arbetsytan — som en projektmapp pa kontoret, fast med inbyggd dagbok som skriver ner varje gang nagon andrar, laggar till eller tar bort nagot.

**Varfor det spelar roll:** Nar nagon sager "klona repot" menar de "ladda ner projektmappen med all dess historik till din dator." Guiden du laser just nu ligger i ett repo. Det ar sa vi delar och samarbetar kring dokument och kod i AI-varlden.

---

## 6. CLAUDE.md

**Vad det ar:** En speciell fil som du lagger i ditt projekt for att ge Claude instruktioner. Det ar som ett PM som Claude laser innan det borjar arbeta med dina filer.

**Analogi:** Tank dig att du far en ny konsult pa kontoret. Det forsta du gor ar att ge hen ett introduktionsdokument: "Sa har jobbar vi, det har ar vara konventioner, de har filerna ar viktiga, ratta aldrig klientens namn utan att fraga forst." CLAUDE.md ar exakt det dokumentet — fast for AI.

**Varfor det spelar roll:** Med en genomtankt CLAUDE.md behover du inte upprepa samma instruktioner varje gang. Claude kommer ihag projektets regler, stil och struktur. Det ar skillnaden mellan att jobba med nagon som kanner projektet och nagon som borjar fran noll varje gang.

---

## 7. API

**Vad det ar:** API star for Application Programming Interface. Det ar ett standardiserat satt for program att prata med varandra.

**Analogi:** Forestall dig en restaurang. Du (programmet) vill ha mat fran koket (en annan tjanst). Du pratar inte direkt med kocken — du ger din bestallning till kyparen (API:et), som formedlar den till koket och kommer tillbaka med ratt. API:et ar kyparen: det tar emot forfragan, vidarebefordrar den och levererar svaret.

**Varfor det spelar roll:** Nar du hor att nagon "kopplat Claude till sitt system via API:et" menar de att de byggt en bro sa att deras verktyg kan skicka fragor till Claude och fa svar automatiskt — utan att nagon sitter och skriver i chatten. Det ar sa avancerade arbetsfloden byggs.

---

## 8. Kontext (context)

**Vad det ar:** All den information som Claude har tillgang till nar det svarar pa din fraga — din prompt, tidigare meddelanden i konversationen, och eventuella dokument du bifogat.

**Analogi:** Tank dig att du briefar en ny konsult innan ett mote. Ju mer relevant bakgrund du ger — vilka som ar med, vad som diskuterats tidigare, vilka beslut som redan tagits — desto battre forberedd ar konsulten. Claudes kontext fungerar pa samma satt: ju mer relevant information du ger, desto battre svar far du.

**Varfor det spelar roll:** Manga som ar besvikna pa AI-svar har egentligen bara gett for lite kontext. Att forsta begreppet kontext ar nyckeln till att ga fran "AI ger generiska svar" till "AI ger exakt det jag behover." Hela kapitel 03 handlar om detta.

---

## 9. Prompt

**Vad det ar:** Din instruktion eller fraga till AI. Det kan vara allt fran "Sammanfatta den har rapporten" till en detaljerad instruktion pa tva sidor.

**Analogi:** Det ar som att ge en arbetsuppgift till en medarbetare. "Gor en presentation" ar en vag prompt. "Gor en 10-sidig presentation for styrelsen om Q3-resultaten, fokusera pa tillvaxt i Norden, anvand foretagnets PowerPoint-mall och inkludera tre rekommendationer" ar en utmarkt prompt. Samma person, helt olika resultat.

**Varfor det spelar roll:** Kvaliteten pa din prompt bestammer kvaliteten pa Claudes svar. Det ar ingen overkelse att saga att 80 % av vardet i att anvanda AI ligger i hur du formulerar dina prompts. Det ar darfor ett helt kapitel ar tillganat det amnet.

---

## 10. Token

**Vad det ar:** Den enhet som AI anvander for att mata textlangd. En token ar ungefar tre fjardedelar av ett ord pa engelska (pa svenska ar det aningen mindre, kanske tva tredjedelar av ett ord, eftersom svenska ord ofta ar langre).

**Analogi:** Tank pa det som ordraknarens lilla kusin. Precis som du kanner till teckenantal och ordantal i Word sa mater AI i tokens. Anledningen ar att AI inte laser ord som vi gor — den bryter ner text i mindre bitar (tokens) som den bearbetar en i taget.

**Varfor det spelar roll:** Varje AI-modell har en maximal kontextlangd matt i tokens. Claude kan hantera enorma texter (uppat 200 000 tokens — ungefar en hel roman), men det ar bra att forsta konceptet. Om nagon sager "det ryms inte i kontextfonstret" menar de att texten overskrider AI:s tokengraans. Du slipper raakna tokens i praktiken, men begreppet hjalper dig forsta hur AI tanker.

---

## Du ar redo

Det var allt. Tio begrepp. Du behover inte memorera dem — du kommer att stota pa dem naturligt nar du laser vidare, och varje gang kommer de att kanna sig lite mer bekanta.

Det viktiga ar inte att du kan alla definitioner utantill. Det viktiga ar att du inte kanns avskrackt nar du ser orden dyka upp. Du har nu en mental karta over landskapet, och det ar allt du behover for att ta nasta steg.

> *Nasta kapitel: [01 — Introduktion: Claudes AI-ekosystem](01-introduktion.md)*
