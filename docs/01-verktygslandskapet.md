# Kapitel 01 — AI-verktygslandskapet

> *Du chattar redan med AI. Men visste du att det finns ett helt spektrum av verktyg, och att de flesta kunskapsarbetare bara använder det första steget?*

Det här kapitlet ger dig kartan. Vi går igenom de stora AI-verktygen, vad de gör, vad de är bra på, och hur de hänger ihop i en trappa från enkel chatt till autonoma agenter.

---

## De stora AI-verktygen — en snabb karta

Det finns idag flera kraftfulla AI-verktyg, och du använder förmodligen redan minst ett av dem:

| Verktyg | Styrka | Bra för |
|---------|--------|---------|
| **ChatGPT** (OpenAI) | Störst användarbas, Custom GPTs, bred pluginmiljö | Allround-chatt, anpassade GPT:er, bildgenerering |
| **Claude** (Anthropic) | Starkt på långa dokument, brett ekosystem (Chat → Code → Cowork) | Kunskapsarbete, analys, systembyggande |
| **Gemini** (Google) | Djup Google-integration, stark på sökning | Research, sammanfattning, arbete i Google Workspace |
| **Copilot** (Microsoft) | Inbyggd i Microsoft 365 | Excel, PowerPoint, Word, direkt i verktygen du redan använder |

**Varför Claude som huvudexempel?** Kort svar: det är verktyget jag själv lärt mig med, och Claude Projects GitHub-integration gör arbetsflödet smidigt. Längre förklaring finns på [startsidan](index.md). Principerna i guiden (persistent kontext, regler, återanvändbara arbetsflöden) gäller oavsett verktyg.

---

## Problemet du redan känner till

Du använder Claude eller ChatGPT dagligen. Du får bra svar. Men tre saker gnager:

**1. Du upprepar dig.** Varje gång du startar en ny session förklarar du samma sak: vem du är, hur du vill ha svaret, vilken kontext som gäller. Du har kanske till och med en prompt sparad någonstans som du klistrar in varje gång.

**2. Varje session börjar från noll.** Igår bad du Claude analysera ett kassaflöde och fick en utmärkt analys. Idag öppnar du en ny konversation, och Claude har ingen aning om vad ni pratade om.

**3. Du kopierar data fram och tillbaka.** Du öppnar en årsredovisning, kopierar relevanta siffror, klistrar in dem i chatten, får ett svar, kopierar svaret till ett dokument. För varje ny fråga börjar du om.

Det här är inte ett problem med dina prompts. Det är ett problem med *arbetsflödet*. Och det finns en lösning.

---

## Trappan: från engångsprompt till system

AI-verktygslandskapet är inte ett enda verktyg, det är ett spektrum. Varje steg ger dig mer kraft, mer automatisering och mindre upprepning.

```
  Engångsprompt                                          System
  (det du gör idag)                            (det du kan bygga)

  ├──────────┼──────────────┼──────────────┼──────────────┤
  AI-chatten    AI i           Claude Code    Claude Cowork
  (Claude/      Excel/PPT
   ChatGPT/
   Gemini)
```

Det här är guidens kärna: **trappan**. Varje steg löser begränsningarna i det föregående. Du behöver inte ta alla steg, men att förstå vilka som finns gör att du kan välja rätt verktyg för rätt uppgift.

---

## Steg 1: AI-chatten

### Grundupplevelsen

Du känner det redan. Du skriver en prompt, får ett svar. Snabbt och kraftfullt, men flyktigt.

Chatten ger dock mer kontext än många inser. När du chattar bygger du upp kontext på flera nivåer: hela konversationshistoriken, uppladdade filer och det samlade utbytet av frågor och svar. En lång konversation där du delar bakgrund, siffror och dokument kan ge imponerande resultat.

Men den kontexten är **flyktig**. Den försvinner när du stänger fliken eller startar en ny session. Den är bunden till en enda konversation. Och den är **manuell**: du bygger upp den från noll varje gång.

### Projekt och Custom GPTs — delad kontext i chatten

Det finns ett steg mellan ren chatt och Code-verktyg som många missar. Både Claude och ChatGPT erbjuder sätt att skapa **persistent kontext** direkt i chatten:

- **Claude Projects:** en delad arbetsyta där du laddar upp filer, skriver projektinstruktioner och startar flera konversationer som alla delar samma kontext.
- **ChatGPT Custom GPTs:** anpassade GPT:er med instruktioner, uppladdade filer och (valfritt) kopplingar till externa tjänster via Actions.

Koncepten mappar mot varandra:

| Koncept | Claude Projects | ChatGPT Custom GPTs |
|---------|----------------|-------------------|
| **Persistenta instruktioner** | Projektinstruktioner (fritext) | System-prompt i GPT-konfigurationen |
| **Uppladdade filer** | Ja, delas över konversationer | Ja, via Knowledge |
| **Flera konversationer** | Ja, inom projektet | Ja, varje GPT kan användas av flera |
| **Delning** | Inom team (Claude for Work) | Kan publiceras i GPT Store |

Precis som CLAUDE.md ger Claude Code regler och kontext, ger projektinstruktionerna (eller GPT-konfigurationen) AI:n en "grundförståelse" som gäller varje gång. **Skillnaden mot Claude Code** är att du fortfarande arbetar i webbläsaren, inte kan skapa egna kommandon (skills), och att AI:n inte kan skriva tillbaka till dina filer.

**Tumregel:** Projects/Custom GPTs är ett utmärkt mellansteg om du har ett avgränsat uppdrag med ett par filer och vill slippa upprepa instruktioner. Men för pågående arbete med många filer, automatisering och full kontroll är nästa steg i trappan.

**Vad du vinner:** Snabba svar, bollplank, sammanfattningar, och med Projects/Custom GPTs: delad kontext över flera konversationer.

**Vad du saknar:** Lokal filåtkomst, automatisering, skills, mappstruktur som kontext.

---

## Steg 2: AI i Office — Excel, PowerPoint och Word

AI som tillägg direkt i Office-programmen. Du markerar data i Excel och ställer en fråga. Du beskriver en presentation och AI:n skapar ett utkast i PowerPoint.

Här finns två huvudalternativ:

- **Claude-tillägget:** installeras som add-in i Excel/PowerPoint. Bra på analys och längre texter.
- **Microsoft Copilot:** inbyggt i Microsoft 365 (med Copilot-licens). Djupare integration med Office, kan skapa pivottabeller, diagram och hela presentationer direkt.

| | Claude-tillägg | Microsoft Copilot |
|--|---------------|-------------------|
| **Styrka** | Stark analys, bra på text och resonemang | Djup Office-integration, kan skapa diagram/pivottabeller |
| **Begränsning** | Kan inte modifiera kalkylbladet direkt | Ibland ytligare resonemang |

Båda är bra verktyg för snabba, avgränsade frågor när du redan arbetar i Office.

**Styrkan:** Du stannar i verktyget du redan arbetar i. Ingen kontextväxling. Perfekt för snabba frågor, formelhjälp och första utkast.

**Svagheten:** Varje fråga börjar fortfarande från noll. Det finns ingen CLAUDE.md, inga skills, inget minne. Du måste förklara kontexten varje gång.

**Tumregel:** Använd AI i Excel/PPT för snabba operativa frågor. Använd Claude Code för allt som gynnas av kontext, regler och struktur.

---

## Steg 3: Claude Code — ditt AI-system i terminalen

Här sker språnget. Claude Code är ett verktyg där Claude arbetar direkt med dina filer, följer dina regler och kan utföra återanvändbara arbetsflöden.

**Du behöver inte kunna programmera.** Du behöver inte kunna terminalen. Du behöver bara kunna beskriva vad du vill ha, och det kan du redan.

### Hur du börjar — från chatt till Code

Det naturliga sättet att börja med Claude Code är inte i terminalen, det är i chatten:

1. **Öppna en AI-chatt** (Claude Chat, ChatGPT, Gemini, spelar ingen roll)
2. **Beskriv vad du vill skapa:** ditt projekt, ditt arbete, dina behov
3. **Diskutera och iterera** tills du har en tydlig bild
4. **Be chatten ta fram en terminalredo prompt:** en komplett beskrivning du kan ge till Claude Code
5. **Klistra in prompten i Claude Code:** Claude bygger allt åt dig

Det enda manuella steget? Skapa en tom mapp och starta Claude Code. Resten (mappstruktur, CLAUDE.md, skills, README-filer) skapar Claude Code baserat på din beskrivning.

### Vad det innebär i praktiken

**Tänksätt:** Föreställ dig en extremt kompetent assistent som sitter bredvid dig vid datorn. Du pekar på en mapp med data och säger "analysera det här och skriv en sammanfattning." Assistenten läser filerna, gör beräkningarna, skriver rapporten och sparar den på rätt ställe.

Med Claude Code kan du:

- **Läsa filer** på din dator: PDF:er, Excel-exporter, textfiler, CSV
- **Skriva och redigera filer:** rapporter, analyser, sammanställningar
- **Köra kommandon:** organisera mappar, bearbeta data, automatisera uppgifter
- **Följa regler:** genom CLAUDE.md och skills som du definierar

### Varför det är ett språng jämfört med chatten

| Chatt | Claude Code |
|-------|-------------|
| Du kopierar in text manuellt | Claude läser dina filer direkt |
| Du får svar i chattfönster att kopiera | Claude skriver filer på din dator |
| Du förklarar regler varje session | CLAUDE.md gör att reglerna alltid gäller |
| Samma prompt varje gång | Skills automatiserar återanvändbara arbetsflöden |
| Kontextfönstret är allt som finns | Hela mappstrukturen är kontext |

Skillnaden är inte att Claude Code är "smartare", det är samma AI-modell. Skillnaden är att du ger den **bättre förutsättningar** att göra ett bra jobb.

### De två nyckelkoncepten

**CLAUDE.md** är en instruktionsfil i ditt projekt som Claude Code skapar baserat på din beskrivning. Claude läser den automatiskt varje session: dina regler, din kontext, din stil. Det är skillnaden mellan en assistent som börjar från noll varje dag och en som känner projektet.

**Skills** är återanvändbara arbetsflöden. Claude Code skapar dem baserat på dina behov. Du beskriver en uppgift du gör ofta, och Claude bygger en skill som utför alla stegen med ett enda kommando. Istället för att förklara hur en kassaflödesanalys ska göras varje gång, skriver du `/kassaflodesanalys` och Claude utför alla stegen.

> Hur du sätter upp CLAUDE.md och skills i praktiken täcks i [kapitel 03](03-mappstruktur-och-arbetssatt.md).

---

## Steg 4: Claude Cowork — autonom AI i molnet

Om Claude Code är en assistent vid ditt skrivbord, så är Cowork en junior analytiker du skickar iväg med ett uppdrag, och som kommer tillbaka med resultatet.

### Vad det är

Claude Cowork är en autonom AI-agent som körs i molnet. Du beskriver en uppgift, Cowork planerar sitt angreppssätt, arbetar igenom det steg för steg, och levererar ett färdigt resultat.

Det som skiljer det från Claude Code:

- **Körs i molnet:** du behöver inte ha datorn igång
- **Arbetar självständigt:** webbsökning, kodexekvering, dataanalys
- **Hanterar längre uppgifter:** saker som tar 15–60 minuter manuellt
- **Enklare gränssnitt:** ingen terminal krävs

### Vem passar det för?

Cowork är för dig som har uppgifter som är tidskrävande men väldefinierade. Research, sammanställningar, kartläggningar. Uppgifter där du vill ge ett uppdrag och få tillbaka ett resultat utan att övervaka varje steg.

### Konkreta exempel

- **Marknadskartläggning:** "Kartlägg den nordiska HR-tech-marknaden. Identifiera de 10 största spelarna med intäkter, tillväxt och ägarbild."
- **Dataanalys:** "Gå igenom bifogad årsredovisning. Extrahera nyckeltal för de senaste tre åren. Beräkna CAGR och marginaltrend."
- **Dokumentskapande:** "Skriv ett utkast till rapport baserat på bifogade data. Följ strukturen: sammanfattning, analys, slutsatser, rekommendation."

### Begränsningar

**Instruktionskvalitet är avgörande.** Vaga uppdrag ger vaga resultat. Var tydlig med: vad du vill ha, i vilket format, vad som är viktigt.

**Granska alltid resultatet.** Behandla Cowork-leveranser som ett första utkast från en junior medarbetare.

**Molnbaserat = datahantering.** Data skickas till Anthropics servrar. För känslig information, kontrollera med din organisation.

---

## Code vs Cowork — en jämförelse

| Aspekt | Claude Code | Claude Cowork |
|--------|------------|---------------|
| **Var körs det** | Din dator (terminalen) | Molnet |
| **Interaktion** | Iterativt, ni arbetar tillsammans | Ge uppdrag, få resultat |
| **Bäst för** | Arbete med lokala filer, finjustering, systembyggande | Längre research, autonoma uppgifter |
| **Kontroll** | Hög: du ser varje steg | Lägre: agenten arbetar självständigt |
| **CLAUDE.md och skills** | Ja, hela systemet | Nej, instruktionen är ditt uppdrag |

---

## Kombinera verktygen

Det mest kraftfulla arbetsflödet använder flera verktyg:

| Steg | Verktyg | Uppgift |
|------|---------|---------|
| 1 | **Cowork** | Researcha marknaden, samla data |
| 2 | **Code** | Bearbeta resultatet, skapa strukturerad analys |
| 3 | **Excel** | Bygg modell baserad på analysdata |
| 4 | **Code** | Generera rapport med kontext och regler |
| 5 | **PowerPoint** | Finjustera presentationen visuellt |
| 6 | **Chat** | Bollplank och snabba frågor |

Cowork gör det tunga lyftet. Code gör det precisa arbetet med kontext och regler. Excel och PowerPoint avslutar med operativa detaljer och visuell polish. Chat är alltid tillgängligt för snabba frågor.

---

## Nyckelinsikten

Skillnaden mellan Chat och Code är inte teknisk svårighet. Det är skillnaden mellan att skriva samma mejl från grunden varje gång och att ha en mall med förifyllda fält.

I chatten är din prompt allt. Varje gång du öppnar en ny konversation börjar du med tomt papper.

Med Claude Code bygger du ett **system**:

- **CLAUDE.md:** regler som alltid gäller
- **Skills:** återanvändbara arbetsflöden
- **Mappstruktur:** data, analys och output på rätt ställe
- **Mallar:** standardformat för rapporter och presentationer

Systemet gör att AI **blir smartare över tid** på just ditt jobb. Inte för att modellen förändras, utan för att den kontext och de regler du byggt upp gör varje session bättre än den föregående.

Du behöver inte göra allt på en gång. Men om du tar bort en sak från det här kapitlet, låt det vara detta:

**Sluta börja från noll. Börja bygga ett system.**

---

> *Föregående kapitel: [00 — Grundbegrepp](00-grundbegrepp.md)*
>
> *Nästa kapitel: [02 — Promptteknik och kontext](02-promptteknik-och-kontext.md)*
