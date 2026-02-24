# Kapitel 01 — AI-verktygslandskapet

> *Du chattar med AI. Men visste du att du kan bygga ett system som gör AI 10x bättre på just ditt jobb?*

Det här är det viktigaste kapitlet i hela guiden. Inte för att det är det mest tekniska — utan för att det förklarar *varför* resten spelar roll — och var de olika AI-verktygen passar in.

---

## De stora AI-verktygen — en snabb karta

Innan vi dyker in: det finns idag flera kraftfulla AI-verktyg, och du använder förmodligen redan minst ett av dem. Här är en snabb översikt:

| Verktyg | Styrka | Bra för |
|---------|--------|---------|
| **ChatGPT** (OpenAI) | Störst användarbas, Custom GPTs, bred pluginmiljö | Allround-chatt, anpassade GPT:er, bildgenerering |
| **Claude** (Anthropic) | Starkt på långa dokument, brett ekosystem (Chat → Code → Cowork) | Kunskapsarbete, analys, systembyggande |
| **Gemini** (Google) | Djup Google-integration, stark på sökning | Research, sammanfattning, arbete i Google Workspace |
| **Copilot** (Microsoft) | Inbyggd i Microsoft 365 | Excel, PowerPoint, Word — direkt i verktygen du redan använder |

**Varför Claude som huvudexempel?** Claude erbjuder det bredaste spektrumet från enkel chatt till autonoma agenter (Cowork), med ett mellanlager (Claude Code) som ger kunskapsarbetare möjlighet att bygga persistenta system — regler, skills och mappstruktur. Det gör det till det mest illustrativa exemplet för den resa den här guiden beskriver. Men principerna — persistent kontext, regler, återanvändbara arbetsflöden — gäller oavsett verktyg.

> **Planerat:** Ett dedikerat jämförelsekapitel med djupare analys av vilket verktyg som passar bäst för vilken typ av arbete är på väg.

---

## Problemet du redan känner till

Du använder Claude eller ChatGPT dagligen. Du får bra svar. Men tre saker gnager:

**1. Du upprepar dig.** Varje gång du startar en ny session förklarar du samma sak: vem du är, hur du vill ha svaret, vilken kontext som gäller. Du har kanske till och med en prompt sparad någonstans som du klistrar in varje gång.

**2. Varje session börjar från noll.** Igår bad du Claude analysera ett kassaflöde och fick en utmärkt analys. Idag öppnar du en ny konversation — och Claude har ingen aning om vad ni pratade om.

**3. Du kopierar data fram och tillbaka.** Du öppnar en årsredovisning, kopierar relevanta siffror, klistrar in dem i chatten, får ett svar, kopierar svaret till ett dokument. För varje ny fråga börjar du om.

Det här är inte ett problem med dina prompts. Det är ett problem med *arbetsflödet*. Och det finns en lösning.

---

## Spektrumet: från engångsprompt till system

AI-verktygslandskapet är inte ett enda verktyg — det är ett spektrum. Varje steg ger dig mer kraft, mer automatisering och mindre upprepning.

```
  Engångsprompt                                          System
  (det du gör idag)                            (det du kan bygga)

  ├──────────┼──────────────┼──────────────┼──────────────┤
  AI-chatten    AI i           Claude Code    Claude Cowork
  (Claude/      Excel/PPT
   ChatGPT/
   Gemini)
```

### AI-chatten (Claude / ChatGPT / Gemini)

Du känner det redan. Du skriver en prompt, får ett svar. Snabbt och kraftfullt — men flyktigt.

Chatten ger dock mer kontext än många inser. När du chattar med AI:n bygger du upp kontext på flera nivåer: hela konversationshistoriken, uppladdade filer och det samlade utbytet av frågor och svar. En lång konversation där du delar bakgrund, siffror och dokument kan ge imponerande resultat — ibland förvånansvärt bra.

Men den kontexten är **flyktig**. Den försvinner när du stänger fliken eller startar en ny session. Den är bunden till en enda konversation. Och den är **manuell** — du bygger upp den från noll varje gång genom att kopiera in text, ladda upp filer och förklara vem du är och vad du behöver. Det är just den begränsningen som resten av spektrumet löser.

#### Projekt och Custom GPTs — delad kontext i chatten

Det finns ett steg mellan ren chatt och Code-verktyg som många missar. Både Claude och ChatGPT erbjuder sätt att skapa **persistent kontext** direkt i chatten:

- **Claude Projects** — en delad arbetsyta där du laddar upp filer, skriver projektinstruktioner och startar flera konversationer som alla delar samma kontext.
- **ChatGPT Custom GPTs** — anpassade GPT:er med instruktioner, uppladdade filer och (valfritt) kopplingar till externa tjänster via Actions.

Koncepten mappar mot varandra:

| Koncept | Claude Projects | ChatGPT Custom GPTs |
|---------|----------------|-------------------|
| **Persistenta instruktioner** | Projektinstruktioner (fritext) | System-prompt i GPT-konfigurationen |
| **Uppladdade filer** | Ja, delas över konversationer | Ja, via Knowledge |
| **Flera konversationer** | Ja, inom projektet | Ja, varje GPT kan användas av flera |
| **Delning** | Inom team (Claude for Work) | Kan publiceras i GPT Store |
| **Koppling till externa tjänster** | Nej (kräver Code/API) | Ja, via Actions |

Det liknar faktiskt Claude Code-konceptet mer än du tror. Precis som CLAUDE.md ger Claude regler och kontext, ger projektinstruktionerna (eller GPT-konfigurationen) AI:n en "grundförståelse" som gäller varje gång.

**Skillnaden mot Claude Code** är att du fortfarande arbetar i webbläsaren, inte kan skapa egna kommandon (skills), och att AI:n inte kan skriva tillbaka till dina filer. Projektet sparar kontext — men det bygger inte ett system.

**En viktig begränsning:** PDF-filer fungerar i projekt (och Custom GPTs), men de förbrukar mycket kontext (tokens) varje gång AI:n läser dem. En stor årsredovisning kan äta upp en betydande del av det tillgängliga kontextfönstret. Vi går in på djupet om PDF-problemet — och hur du löser det — i kapitel 04.

**Tumregel:** Projects/Custom GPTs är ett utmärkt mellansteg om du har ett avgränsat uppdrag med ett par filer och vill slippa upprepa instruktioner. Men för pågående arbete med många filer, automatisering och full kontroll är nästa steg i spektrumet.

**Vad du vinner:** Snabba svar, bollplank, sammanfattningar — och med Projects/Custom GPTs: delad kontext och instruktioner över flera konversationer.
**Vad du saknar:** Lokal filåtkomst, automatisering, skills, mappstruktur som kontext.

### AI i Excel och PowerPoint

AI som tillägg direkt i Office-programmen. Du markerar data i Excel och ställer en fråga. Du beskriver en presentation och AI:n skapar ett utkast i PowerPoint.

Här finns två huvudalternativ:

- **Claude-tillägget** — installeras som add-in i Excel/PowerPoint. Kräver Claude Pro. Bra på analys och längre texter.
- **Microsoft Copilot** — inbyggt i Microsoft 365 (kräver Copilot-licens). Djupare integration med Office — kan t.ex. skapa pivottabeller, diagram och hela presentationer direkt.

**Styrkan:** Du stannar i verktyget du redan arbetar i. Ingen kontextväxling. Perfekt för snabba frågor, formelhjälp och första utkast.

**Svagheten:** Varje fråga börjar fortfarande från noll. Det finns ingen CLAUDE.md, inga skills, inget minne. Du måste förklara kontexten varje gång.

### Claude Code

Här sker språnget. Claude Code är ett verktyg i terminalen där Claude arbetar direkt med dina filer, följer dina regler (CLAUDE.md) och kan utföra återanvändbara arbetsflöden (skills).

**Vad du vinner:** Persistent kontext, regler som alltid gäller, egna kommandon, mappstruktur som kontext. Du slutar upprepa dig.

### Claude Cowork

Claude som autonom agent i molnet. Du ger ett uppdrag, Claude arbetar självständigt och levererar ett färdigt resultat. Du behöver inte ha datorn igång.

**Vad du vinner:** Delegering av tidskrävande uppgifter. Research, sammanställningar och analyser som gör sig själva.

---

## Nyckelinsikten

Skillnaden mellan Chat och Code är inte teknisk svårighet. Det är skillnaden mellan att skriva samma mejl från grunden varje gång och att ha en mall med förifyllda fält.

I chatten är din prompt allt. Varje gång du öppnar en ny konversation börjar du med tomt papper.

Med Claude Code bygger du ett **system**:

- **CLAUDE.md** — regler som alltid gäller (språk, ton, format, branschkontext)
- **Skills** — återanvändbara arbetsflöden (kassaflödesanalys, investment memo, due diligence)
- **Mappstruktur** — data, analys och output på rätt ställe så Claude hittar det den behöver
- **Mallar** — standardformat för rapporter och presentationer

Systemet gör att AI **blir smartare över tid** på just ditt jobb. Inte för att modellen förändras, utan för att den kontext och de regler du byggt upp gör varje session bättre än den föregående.

---

## Konkret exempel: PE-arbete

För att göra skillnaden konkret, låt oss jämföra hur tre vanliga PE-uppgifter ser ut beroende på vilket verktyg du använder.

### Kassaflödesanalys

| | Chat | AI i Excel | Claude Code |
|--|------|---------------|-------------|
| **Du gör** | Kopierar siffror från årsredovisningen, klistrar in, skriver prompt med instruktioner för format och beräkning | Markerar celler i kalkylbladet, frågar AI:n i sidopanelen | Skriver: `/kassaflodesanalys` |
| **Claude gör** | Svarar med text och tabeller i chatten | Svarar med formler och sammanfattning i Excel | Läser filer i data/, beräknar FCF, skapar rapport, sparar på rätt ställe |
| **Resultat** | Text i chattfönster som du måste kopiera | Svar i Excel-panel | Färdig rapport som Markdown-fil i analys/kassaflode/ |
| **Nästa gång** | Börja om från början | Börja om från början | Kör samma skill — samma kvalitet, noll upprepning |

### Investment memo

| | Chat | AI i Excel | Claude Code |
|--|------|---------------|-------------|
| **Du gör** | Klistrar in bakgrund, siffror, målstruktur i en lång prompt | Ej lämpligt verktyg | Skriver: `/investment-memo` |
| **Claude gör** | Skriver ett memo baserat på det du gett | — | Läser all data i projektet, följer mallen i mallar/, fyller i alla sektioner |
| **Resultat** | Text att kopiera och formatera | — | Strukturerat memo sparat som fil, redo att redigera |

### Due diligence-checklista

| | Chat | AI i Excel | Claude Code |
|--|------|---------------|-------------|
| **Du gör** | Beskriver bolaget och ber om en checklista | Ej lämpligt verktyg | Skriver: `/due-diligence-checklista` |
| **Claude gör** | Genererar en generisk lista | — | Skapar checklista anpassad efter bolagets bransch, storlek och de data som redan finns i projektet |
| **Resultat** | Generisk lista | — | Skräddarsydd checklista som tar hänsyn till vad du redan har och vad som saknas |

Mönstret är tydligt: **ju längre åt höger i spektrumet, desto mindre upprepning och desto högre kvalitet.**

---

## AI i Excel och PowerPoint — kort översikt

Det finns idag två huvudvägar att använda AI direkt i Microsoft Office:

**Claude-tillägget** finns som add-in i Microsoft Excel och PowerPoint. Det kräver Microsoft 365 och minst Claude Pro. Du markerar celler och ställer frågor: "Sammanfatta trenderna i det här kassaflödet", "Skriv en formel som beräknar IRR", "Identifiera dubbletter i kolumn A." I PowerPoint kan du beskriva en presentation och få ett utkast, eller generera speaker notes.

**Microsoft Copilot** är inbyggt i Microsoft 365 (med Copilot-licens) och har djupare integration — det kan skapa pivottabeller, generera diagram, bygga hela presentationer från ett Word-dokument och koppla samman data mellan Office-appar.

| | Claude-tillägg | Microsoft Copilot |
|--|---------------|-------------------|
| **Styrka** | Stark analys, bra på text och resonemang | Djup Office-integration, kan skapa diagram/pivottabeller |
| **Begränsning** | Kan inte modifiera kalkylbladet direkt | Ibland ytligare resonemang |
| **Kräver** | Claude Pro + Microsoft 365 | Microsoft 365 Copilot-licens |

Båda är bra verktyg för snabba, avgränsade frågor när du redan arbetar i Office. Men ingen av dem har det som gör Claude Code kraftfullt: persistent kontext, regler och återanvändbara arbetsflöden. Varje fråga börjar från noll.

**Tumregel:** Använd AI i Excel/PPT för snabba operativa frågor. Använd Claude Code för allt som gynnas av kontext, regler och struktur.

---

## Vart vi är på väg

Resten av den här guiden fokuserar på Claude Code, Claude Cowork och mappstruktur — det är där det stora språnget sker.

- **Kapitel 02** tar dig genom Claude Code: installation, användning, CLAUDE.md och skills
- **Kapitel 03** visar hur Claude Cowork låt dig delegera större uppgifter
- **Kapitel 04** går på djupet med mappstruktur, CLAUDE.md-design och hur du bygger ett system som gör AI bättre över tid

Du behöver inte göra allt på en gång. Men om du tar bort en sak från det här kapitlet, låt det vara detta:

**Sluta börja från noll. Börja bygga ett system.**

> *Nästa kapitel: [02 — Claude Code](02-claude-code.md)*
