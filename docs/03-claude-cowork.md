# Kapitel 03 — Claude Cowork

> *Om Claude Code är en assistent vid ditt skrivbord, så är Cowork en junior analytiker du skickar iväg med ett uppdrag — och som kommer tillbaka med resultatet.*

!!! note "Det här kapitlet är Claude-specifikt"
    Claude Cowork är Anthropics lösning för autonoma AI-agenter. Liknande koncept finns hos andra leverantörer — t.ex. ChatGPT:s **Operator** och Googles **Gemini agents** — men ekosystemen skiljer sig åt. Principen att delegera väldefinierade uppgifter till en autonom AI gäller oavsett verktyg.

---

## Vad är det?

Claude Cowork är en autonom AI-agent som körs i molnet. Du beskriver en uppgift, Cowork planerar sitt angreppssätt, arbetar igenom det steg för steg, och levererar ett färdigt resultat.

Det som skiljer det från Claude Code:

- **Körs i molnet** — du behöver inte ha datorn igång
- **Arbetar självständigt** — webbsökning, kodexekvering, dataanalys
- **Hanterar längre uppgifter** — saker som tar 15-60 minuter manuellt
- **Enklare gränsnitt** — ingen terminal krävs

---

## Vem passar det för?

Cowork är för dig som:

- Har uppgifter som är tidskrävande men väldefinierade
- Vill delegera utan att övervaka varje steg
- Föredrar att ge ett uppdrag och få tillbaka ett resultat
- Inte vill öppna en terminal men vill ha mer kraft än chatten

---

## Konkreta exempel

**Research och sammanställning:**
> "Kartlägg den nordiska HR-tech-marknaden. Identifiera de 10 största spelarna med intäkter, tillväxt, ägarbild och antal anställda. Presentera i tabell med kort marknadssammanfattning."

**Dataanalys:**
> "Gå igenom bifogad årsredovisning. Extrahera nyckeltal för de senaste tre åren: revenue, EBITDA, nettoskuld. Beräkna CAGR och EBITDA-marginaltrend. Spara som tabell."

**Transaktionsresearch:**
> "Sammanställ de 5 senaste förvärvstransaktionerna i nordisk HR-tech. Inkludera köpare, säljare, transaktionsvärdering och EV/Revenue-multipel."

**Dokumentskapande:**
> "Skriv ett utkast till investment memo baserat på bifogade data. Följ strukturen: executive summary, bolaget i korthet, investeringsrationale, risker, förenklad värdering."

---

## Claude Code vs Claude Cowork

| Aspekt | Claude Code | Claude Cowork |
|--------|------------|---------------|
| **Var körs det** | Din dator (terminalen) | Molnet |
| **Interaktion** | Iterativt — ni arbetar tillsammans | Ge uppdrag, få resultat |
| **Bäst för** | Arbete med lokala filer, finjustering, systembyggande | Längre research, autonoma uppgifter |
| **Teknisk nivå** | Medel — terminal | Lägre — enklare gränsnitt |
| **Kontroll** | Hög — du ser varje steg | Lägre — agenten arbetar självständigt |
| **CLAUDE.md och skills** | Ja — hela systemet | Nej — instruktionen är ditt uppdrag |
| **Sessionslängd** | Minuter till en timme | Kan köra i timmar |

---

## Begränsningar

**Instruktionskvalitet är avgörande.** Vaga uppdrag ger vaga resultat. Var tydlig med: vad du vill ha, i vilket format, vad som är viktigt, vad som inte behöver vara med.

**Bäst för väldefinierade uppgifter.** Cowork presterar bäst när det finns ett tydligt mål, avgränsad omfattning och specificerat format.

**Granska alltid resultatet.** Behandla Cowork-leveranser som ett första utkast från en junior medarbetare. Kontrollera fakta, verifiera siffror, justera formuleringar.

**Molnbaserat = datahantering.** Data skickas till Anthropics servrar. För känslig information — kontrollera med din organisation.

---

## Kombinera Code och Cowork

Det mest kraftfulla arbetsflödet använder båda:

1. **Cowork researchar** — "Sammanställ data om 20 SaaS-bolag i Norden"
2. **Code bearbetar** — "Läs Cowork-rapporten och skapa en jämförelsetabell sorterad efter tillväxt"
3. **Code finjusterar** — "Formatera enligt vår mall i mallar/investment-memo-mall.md"

Cowork gör det tunga lyftet. Code gör det precisa arbetet med dina lokala filer, regler och mallar.

---

## Tips för att komma igång

1. **Börja med avgränsade uppgifter.** "Sammanfatta den här rapporten i 10 punkter" är bättre som första uppdrag än "Gör en fullständig marknadsanalys."

2. **Var explicit med format.** Ange struktur, längd, språk och vad som ska inkluderas.

3. **Bygg ett bibliotek av uppdrags-mallar.** När du hittar formuleringar som ger bra resultat, spara dem och återanvänd.

---

> *Föregående kapitel: [02 — Claude Code](02-claude-code.md)*
>
> *Nästa kapitel: [04 — Mappstruktur och kontext](04-mappstruktur-och-kontext.md)*
