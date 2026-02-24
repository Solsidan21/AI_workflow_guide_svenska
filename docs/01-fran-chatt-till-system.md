# Kapitel 01 — Fran chatt till system

> *Du chattar med AI. Men visste du att du kan bygga ett system som gor AI 10x battre pa just ditt jobb?*

Det har ar det viktigaste kapitlet i hela guiden. Inte for att det ar det mest tekniska — utan for att det forklarar *varfor* resten spelar roll.

---

## Problemet du redan kanner till

Du anvander Claude eller ChatGPT dagligen. Du far bra svar. Men tre saker gnager:

**1. Du upprepar dig.** Varje gang du startar en ny session forklarar du samma sak: vem du ar, hur du vill ha svaret, vilken kontext som galler. Du har kanske till och med en prompt sparad nagonstans som du klistrar in varje gang.

**2. Varje session borjar fran noll.** Igaar bad du Claude analysera ett kassaflode och fick en utmarkt analys. Idag oppnar du en ny konversation — och Claude har ingen aning om vad ni pratade om.

**3. Du kopierar data fram och tillbaka.** Du oppnar en arsredovisning, kopierar relevanta siffror, klistrar in dem i chatten, far ett svar, kopierar svaret till ett dokument. For varje ny fraga borjar du om.

Det har ar inte ett problem med dina prompts. Det ar ett problem med *arbetsflödet*. Och det finns en losning.

---

## Spektrumet: fran engangsprompt till system

Claudes ekosystem ar inte ett verktyg — det ar ett spektrum. Varje steg ger dig mer kraft, mer automatisering och mindre upprepning.

```
  Engangsprompt                                          System
  (det du gor idag)                            (det du kan bygga)

  ├──────────┼──────────────┼──────────────┼──────────────┤
  Chat       Claude i       Claude Code    Claude Cowork
             Excel/PPT
```

### Claude Chat

Du kanner det redan. Du skriver en prompt, far ett svar. Snabbt och kraftfullt — men flyktigt. Varje session ar en enstaka interaktion.

**Vad du vinner:** Snabba svar, bollplank, sammanfattningar.
**Vad du saknar:** Persistens, regler, automatisering.

### Claude i Excel och PowerPoint

Claude som tillagg direkt i Office-programmen. Du markerar data i Excel och staller en fraga. Du beskriver en presentation och Claude skapar ett utkast i PowerPoint.

**Styrkan:** Du stannar i verktyget du redan arbetar i. Ingen kontextvaxling. Perfekt for snabba fragor, formelhjalp och forsta utkast.

**Svagheten:** Varje fraga borjar fortfarande fran noll. Det finns ingen CLAUDE.md, inga skills, inget minne. Du maste forklara kontexten varje gang.

### Claude Code

Har sker sproanget. Claude Code ar ett verktyg i terminalen dar Claude arbetar direkt med dina filer, foljer dina regler (CLAUDE.md) och kan utfora ateranvandbara arbetsfloden (skills).

**Vad du vinner:** Persistent kontext, regler som alltid galler, egna kommandon, mappstruktur som kontext. Du slutar upprepa dig.

### Claude Cowork

Claude som autonom agent i molnet. Du ger ett uppdrag, Claude arbetar sjalvstandigt och levererar ett fardigt resultat. Du behover inte ha datorn igong.

**Vad du vinner:** Delegering av tidskravande uppgifter. Research, sammanstallningar och analyser som gor sig sjalva.

---

## Nyckelinsikten

Skillnaden mellan Chat och Code ar inte teknisk svarighet. Det ar skillnaden mellan att skriva samma mejl fran grunden varje gang och att ha en mall med forifyllda falt.

I chatten ar din prompt allt. Varje gang du oppnar en ny konversation borjar du med tomt papper.

Med Claude Code bygger du ett **system**:

- **CLAUDE.md** — regler som alltid galler (sprak, ton, format, branschkontext)
- **Skills** — ateranvandbara arbetsfloden (kassaflodesanalys, investment memo, due diligence)
- **Mappstruktur** — data, analys och output pa ratt stalle sa Claude hittar det den behover
- **Mallar** — standardformat for rapporter och presentationer

Systemet gor att AI **blir smartare over tid** pa just ditt jobb. Inte for att modellen forandras, utan for att den kontext och de regler du byggt upp gor varje session battre an den foregaende.

---

## Konkret exempel: PE-arbete

For att gora skillnaden konkret, lat oss jamfora hur tre vanliga PE-uppgifter ser ut beroende pa vilket verktyg du anvander.

### Kassaflodesanalys

| | Chat | Claude i Excel | Claude Code |
|--|------|---------------|-------------|
| **Du gor** | Kopierar siffror fran arsredovisningen, klistrar in, skriver prompt med instruktioner for format och berakning | Markerar celler i kalkylbladet, fragar Claude i sidopanelen | Skriver: `/kassaflodesanalys` |
| **Claude gor** | Svarar med text och tabeller i chatten | Svarar med formler och sammanfattning i Excel | Laser filer i data/, beraknar FCF, skapar rapport, sparar pa ratt stalle |
| **Resultat** | Text i chattfonster som du maste kopiera | Svar i Excel-panel | Fardig rapport som Markdown-fil i analys/kassaflode/ |
| **Nasta gang** | Borja om fran borjan | Borja om fran borjan | Kor samma skill — samma kvalitet, noll upprepning |

### Investment memo

| | Chat | Claude i Excel | Claude Code |
|--|------|---------------|-------------|
| **Du gor** | Klistrar in bakgrund, siffror, malstruktur i en lang prompt | Ej lampligt verktyg | Skriver: `/investment-memo` |
| **Claude gor** | Skriver ett memo baserat pa det du gett | — | Laser all data i projektet, foljer mallen i mallar/, fyller i alla sektioner |
| **Resultat** | Text att kopiera och formatera | — | Strukturerat memo sparat som fil, redo att redigera |

### Due diligence-checklista

| | Chat | Claude i Excel | Claude Code |
|--|------|---------------|-------------|
| **Du gor** | Beskriver bolaget och ber om en checklista | Ej lampligt verktyg | Skriver: `/due-diligence-checklista` |
| **Claude gor** | Genererar en generisk lista | — | Skapar checklista anpassad efter bolagets bransch, storlek och de data som redan finns i projektet |
| **Resultat** | Generisk lista | — | Skraddarsydd checklista som tar hansyn till vad du redan har och vad som saknas |

Monstret ar tydligt: **ju langre at hoger i spektrumet, desto mindre upprepning och desto hogre kvalitet.**

---

## Claude i Excel och PowerPoint — kort oversikt

Claude finns som tillagg (add-in) direkt i Microsoft Excel och PowerPoint. Det kraver Microsoft 365 och minst Claude Pro (20 USD/manad).

**I Excel** markerar du celler och staller fragor: "Sammanfatta trenderna i det har kassaflodet", "Skriv en formel som beraknar IRR", "Identifiera dubbletter i kolumn A." Svaren kommer direkt i programmet — snabbt och utan kontextvaxling.

**I PowerPoint** kan du beskriva en presentation och fa ett utkast med slides, be Claude forkorta text pa en slide, eller generera speaker notes.

Det ar ett bra verktyg for snabba, avgransade fragor nar du redan arbetar i Office. Men det saknar det som gor Claude Code kraftfullt: persistent kontext, regler och ateranvandbara arbetsfloden. Varje fraga borjar fran noll.

**Tumregel:** Anvand Excel/PPT-tillagget for snabba operativa fragor. Anvand Claude Code for allt som gynnas av kontext, regler och struktur.

---

## Vart vi ar pa vag

Resten av den har guiden fokuserar pa Claude Code, Claude Cowork och mappstruktur — det ar dar det stora sproanget sker.

- **Kapitel 02** tar dig genom Claude Code: installation, anvandning, CLAUDE.md och skills
- **Kapitel 03** visar hur Claude Cowork lat dig delegera storre uppgifter
- **Kapitel 04** gar pa djupet med mappstruktur, CLAUDE.md-design och hur du bygger ett system som gor AI battre over tid

Du behover inte gora allt pa en gang. Men om du tar bort en sak fran det har kapitlet, lat det vara detta:

**Sluta borja fran noll. Borja bygga ett system.**

> *Nasta kapitel: [02 — Claude Code](02-claude-code.md)*
