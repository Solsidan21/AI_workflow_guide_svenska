# Kapitel 00 — Grundbegrepp

> *Du är redan bra på AI. Här är de tio begreppen som tar dig till en helt annan nivå.*

Du vet hur man skriver en bra prompt. Du får bra svar från Claude eller ChatGPT. Men varje gång du startar en ny session börjar du från noll — samma kontext, samma instruktioner, samma format.

Det beror inte på att du gör något fel. Det beror på att du saknar ett ordförråd — en handfull tekniska begrepp som öppnar dörren till verktyg där AI faktiskt kan minnas, följa regler och arbeta med dina filer.

Det här är de tio begreppen. Inget av dem är svårare än att lära sig ett nytt Excel-kortkommando. Men tillsammans förändrar de hur du arbetar med AI.

---

## 1. Filer och mappar

**Vad det är:** Datorns sätt att organisera information. En fil är ett enskilt dokument. En mapp samlar filer som hör ihop.

**Analogi:** Tänk dig ett dokumentskåp på kontoret. Varje låda är en mapp, och pappren inuti är filer. Lådorna kan ligga inuti varandra (undermappar).

**Varför det spelar roll:** I nästa steg av AI-arbete pekar du AI mot mappar med data istället för att klistra in text i en chatt. Dina filnamn och mappnamn blir instruktioner i sig själva — `data/finansiellt/arsredovisning-2024.pdf` talar om för AI exakt vad filen innehåller utan att du behöver förklara det.

---

## 2. Terminalen

**Vad det är:** Ett textbaserat sätt att ge instruktioner till din dator. Istället för att klicka på ikoner skriver du kommandon.

**Analogi:** Skillnaden mellan att peka på saker i en butik och att skriva en beställningslista. Båda fungerar, men skriftliga instruktioner kan vara mycket mer exakta: "Öppna mappen mitt-projekt, läs alla PDF:er i data/ och skriv en sammanfattning."

**Varför det spelar roll:** Claude Code lever i terminalen. Du behöver inte lära dig kommandon — Claude hjälper dig. Men att veta att terminalen finns, och att den inte är farlig, är steget som skiljer dig från "chattanvändare" till "AI-systembyggare".

---

## 3. Markdown

**Vad det är:** Ett enkelt sätt att formatera text med vanliga tecken. En rubrik skrivs med `#`, fetstil med `**dubbelstjärnor**`, listor med bindestreck.

**Analogi:** I Word klickar du på knappar för att formatera. I Markdown skriver du formateringen rakt i texten. Det är lättare än det låter — du läser faktiskt Markdown just nu om du tittar på den här filen.

**Varför det spelar roll:** CLAUDE.md, skills, och nästan all AI-dokumentation skrivs i Markdown. Det tar fem minuter att lära sig grunderna, och det är nyckeln till att skriva regler och instruktioner som AI följer automatiskt.

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
```

---

## 4. Git

**Vad det är:** Ett system för versionshantering — det håller reda på varje ändring du gör i dina filer.

**Analogi:** Tänk på "Spara version" i Word, men på steroider. Git fungerar för alla filer i ett helt projekt, låter flera personer arbeta samtidigt, och du kan alltid återvända till exakt hur allt såg ut vid en specifik tidpunkt.

**Varför det spelar roll:** När du arbetar med Claude Code är Git ditt säkerhetsnät. Varje ändring loggas. Du kan experimentera fritt — om något inte fungerar går du bara tillbaka. Det gör att du aldrig behöver vara rädd att AI förstört något.

---

## 5. Repository (repo)

**Vad det är:** En projektmapp som övervakas av Git. Alla filer plus hela ändringshistoriken bildar ett repository.

**Analogi:** Om Git är versionshanteringssystemet så är ett repo den specifika arbetsytan — som en projektmapp med inbyggd dagbok som skriver ner varje ändring.

**Varför det spelar roll:** När någon säger "klona repot" menar de "ladda ner projektmappen." Det repo du läser just nu är ett bra exempel. Det är så man delar och samarbetar kring dokument och struktur i AI-världen.

---

## 6. CLAUDE.md

**Vad det är:** En speciell fil i ditt projekt som ger Claude instruktioner. Claude Code skapar den åt dig baserat på din beskrivning — du berättar vad projektet handlar om, och CLAUDE.md genereras automatiskt. Sedan läser Claude den varje gång den börjar arbeta.

**Analogi:** Tänk dig att du får en ny konsult på kontoret. Första dagen finns det redan ett introduktionsdokument klart: "Så här jobbar vi, det här är våra konventioner, de här filerna är viktiga." CLAUDE.md är exakt det dokumentet — fast för AI.

**Varför det spelar roll:** Det här är den enskilt viktigaste grejen i hela den här guiden. Med en CLAUDE.md behöver du aldrig upprepa samma instruktioner. Claude följer dina regler, din stil och din struktur — automatiskt, varje gång. Det är skillnaden mellan att chatta med AI och att ha ett system.

---

## 7. API

**Vad det är:** API står för Application Programming Interface. Det är ett standardiserat sätt för program att prata med varandra.

**Analogi:** Tänk på en restaurang. Du (programmet) vill ha mat från köket (en annan tjänst). Du pratar inte direkt med kocken — du ger din beställning till kyparen (API:et), som vidarebefordrar den och kommer tillbaka med rätt.

**Varför det spelar roll:** När någon säger "kopplat AI:n till sitt system via API:et" menar de att deras verktyg kan skicka frågor till en AI-modell och få svar automatiskt — utan att någon sitter i chatten. Alla stora AI-leverantörer (OpenAI, Anthropic, Google) erbjuder API:er. Du behöver inte bygga något med API:er själv, men att förstå begreppet gör att du kan ha en informerad diskussion med tekniska kollegor.

---

## 8. Kontext (context)

**Vad det är:** All information som Claude har tillgång till när den svarar — din prompt, tidigare meddelanden, bifogade dokument och eventuella instruktionsfiler.

**Analogi:** Ju mer relevant bakgrund du ger en konsult innan ett möte, desto bättre förberedd är konsulten. Claudes kontext fungerar likadant.

**Varför det spelar roll:** Du förstår redan att bra prompts ger bra svar. Men nästa steg är att förstå att kontext är mer än bara din prompt. Med CLAUDE.md, mappstruktur och skills bygger du ett **permanent kontextlager** som alltid finns där — istället för att skriva om det varje gång.

---

## 9. Prompt

**Vad det är:** Din instruktion till AI. Du vet redan vad det är — du skriver dem varje dag.

**Varför det spelar roll här:** I chatten är prompten allt du har. I Claude Code är prompten bara en del av bilden. Resten är CLAUDE.md (regler), skills (återanvändbara arbetsflöden), och mappstruktur (kontext). Det är därför denna guide fokuserar på systemet runt prompten — inte på prompten i sig.

---

## 10. Token

**Vad det är:** Den enhet som AI använder för att mäta textlängd. En token är ungefär tre fjärdedelar av ett ord på engelska (lite mindre på svenska).

**Analogi:** Ordräknaren i Word, fast för AI. Claude bryter ner text i tokens och bearbetar dem en i taget. Varje modell har en maximal kontextlängd mätt i tokens.

**Varför det spelar roll:** Om någon säger "det ryms inte i kontextfönstret" menar de att texten överskrider AI:ns tokengräns. Du slipper räkna tokens i praktiken, men det förklarar varför du ibland behöver sammanfatta för att frigöra plats. Filformat spelar också roll — en obearbetad PDF förbrukar många fler tokens än samma information i Markdown (mer om det i [kapitel 02](02-promptteknik-och-kontext.md)).

---

## Du är redo

Tio begrepp. Inget av dem är raketvetenskap. Men tillsammans ger de dig ett språk för att ta dig bortom chatten.

Det viktiga är inte att du memorerar definitionerna. Det viktiga är att du inte känns avskräckt när du ser orden dyka upp. Du har nu kartan — resten av guiden visar vägen.

---

> *Nästa kapitel: [01 — AI-verktygslandskapet](01-verktygslandskapet.md)*
