# Kapitel 01 — Från chatt till system

> *Du chattar med AI. Men visste du att du kan bygga ett system som gör AI 10x bättre på just ditt jobb?*

Det här är det viktigaste kapitlet i hela guiden. Inte för att det är det mest tekniska — utan för att det förklarar *varför* resten spelar roll.

---

## Problemet du redan känner till

Du använder Claude eller ChatGPT dagligen. Du får bra svar. Men tre saker gnager:

**1. Du upprepar dig.** Varje gång du startar en ny session förklarar du samma sak: vem du är, hur du vill ha svaret, vilken kontext som gäller. Du har kanske till och med en prompt sparad någonstans som du klistrar in varje gång.

**2. Varje session börjar från noll.** Igår bad du Claude analysera ett kassaflöde och fick en utmärkt analys. Idag öppnar du en ny konversation — och Claude har ingen aning om vad ni pratade om.

**3. Du kopierar data fram och tillbaka.** Du öppnar en årsredovisning, kopierar relevanta siffror, klistrar in dem i chatten, får ett svar, kopierar svaret till ett dokument. För varje ny fråga börjar du om.

Det här är inte ett problem med dina prompts. Det är ett problem med *arbetsflödet*. Och det finns en lösning.

---

## Spektrumet: från engångsprompt till system

Claudes ekosystem är inte ett verktyg — det är ett spektrum. Varje steg ger dig mer kraft, mer automatisering och mindre upprepning.

```
  Engångsprompt                                          System
  (det du gör idag)                            (det du kan bygga)

  ├──────────┼──────────────┼──────────────┼──────────────┤
  Chat       Claude i       Claude Code    Claude Cowork
             Excel/PPT
```

### Claude Chat

Du känner det redan. Du skriver en prompt, får ett svar. Snabbt och kraftfullt — men flyktigt. Varje session är en enstaka interaktion.

**Vad du vinner:** Snabba svar, bollplank, sammanfattningar.
**Vad du saknar:** Persistens, regler, automatisering.

### Claude i Excel och PowerPoint

Claude som tillägg direkt i Office-programmen. Du markerar data i Excel och ställer en fråga. Du beskriver en presentation och Claude skapar ett utkast i PowerPoint.

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

| | Chat | Claude i Excel | Claude Code |
|--|------|---------------|-------------|
| **Du gör** | Kopierar siffror från årsredovisningen, klistrar in, skriver prompt med instruktioner för format och beräkning | Markerar celler i kalkylbladet, frågar Claude i sidopanelen | Skriver: `/kassaflodesanalys` |
| **Claude gör** | Svarar med text och tabeller i chatten | Svarar med formler och sammanfattning i Excel | Läser filer i data/, beräknar FCF, skapar rapport, sparar på rätt ställe |
| **Resultat** | Text i chattfönster som du måste kopiera | Svar i Excel-panel | Färdig rapport som Markdown-fil i analys/kassaflode/ |
| **Nästa gång** | Börja om från början | Börja om från början | Kör samma skill — samma kvalitet, noll upprepning |

### Investment memo

| | Chat | Claude i Excel | Claude Code |
|--|------|---------------|-------------|
| **Du gör** | Klistrar in bakgrund, siffror, målstruktur i en lång prompt | Ej lämpligt verktyg | Skriver: `/investment-memo` |
| **Claude gör** | Skriver ett memo baserat på det du gett | — | Läser all data i projektet, följer mallen i mallar/, fyller i alla sektioner |
| **Resultat** | Text att kopiera och formatera | — | Strukturerat memo sparat som fil, redo att redigera |

### Due diligence-checklista

| | Chat | Claude i Excel | Claude Code |
|--|------|---------------|-------------|
| **Du gör** | Beskriver bolaget och ber om en checklista | Ej lämpligt verktyg | Skriver: `/due-diligence-checklista` |
| **Claude gör** | Genererar en generisk lista | — | Skapar checklista anpassad efter bolagets bransch, storlek och de data som redan finns i projektet |
| **Resultat** | Generisk lista | — | Skräddarsydd checklista som tar hänsyn till vad du redan har och vad som saknas |

Mönstret är tydligt: **ju längre åt höger i spektrumet, desto mindre upprepning och desto högre kvalitet.**

---

## Claude i Excel och PowerPoint — kort översikt

Claude finns som tillägg (add-in) direkt i Microsoft Excel och PowerPoint. Det kräver Microsoft 365 och minst Claude Pro (20 USD/månad).

**I Excel** markerar du celler och ställer frågor: "Sammanfatta trenderna i det här kassaflödet", "Skriv en formel som beräknar IRR", "Identifiera dubbletter i kolumn A." Svaren kommer direkt i programmet — snabbt och utan kontextväxling.

**I PowerPoint** kan du beskriva en presentation och få ett utkast med slides, be Claude förkorta text på en slide, eller generera speaker notes.

Det är ett bra verktyg för snabba, avgränsade frågor när du redan arbetar i Office. Men det saknar det som gör Claude Code kraftfullt: persistent kontext, regler och återanvändbara arbetsflöden. Varje fråga börjar från noll.

**Tumregel:** Använd Excel/PPT-tillägget för snabba operativa frågor. Använd Claude Code för allt som gynnas av kontext, regler och struktur.

---

## Vart vi är på väg

Resten av den här guiden fokuserar på Claude Code, Claude Cowork och mappstruktur — det är där det stora språnget sker.

- **Kapitel 02** tar dig genom Claude Code: installation, användning, CLAUDE.md och skills
- **Kapitel 03** visar hur Claude Cowork låt dig delegera större uppgifter
- **Kapitel 04** går på djupet med mappstruktur, CLAUDE.md-design och hur du bygger ett system som gör AI bättre över tid

Du behöver inte göra allt på en gång. Men om du tar bort en sak från det här kapitlet, låt det vara detta:

**Sluta börja från noll. Börja bygga ett system.**

> *Nästa kapitel: [02 — Claude Code](02-claude-code.md)*
