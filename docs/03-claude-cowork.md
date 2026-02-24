# Kapitel 03 — Claude Cowork

> *Om Claude Code ar en assistent vid ditt skrivbord, sa ar Cowork en junior analytiker du skickar ivag med ett uppdrag — och som kommer tillbaka med resultatet.*

---

## Vad ar det?

Claude Cowork ar en autonom AI-agent som kors i molnet. Du beskriver en uppgift, Cowork planerar sitt angreppssatt, arbetar igenom det steg for steg, och levererar ett fardigt resultat.

Det som skipper det fran Claude Code:

- **Kors i molnet** — du behover inte ha datorn igong
- **Arbetar sjalvstandigt** — webbsokning, kodexekvering, dataanalys
- **Hanterar langre uppgifter** — saker som tar 15-60 minuter manuellt
- **Enklare gransnitt** — ingen terminal kravs

---

## Vem passar det for?

Cowork ar for dig som:

- Har uppgifter som ar tidskravande men valsdefinierade
- Vill delegera utan att overvaka varje steg
- Foredrar att ge ett uppdrag och fa tillbaka ett resultat
- Inte vill oppna en terminal men vill ha mer kraft an chatten

---

## Konkreta exempel

**Research och sammanstallning:**
> "Kartlagg den nordiska HR-tech-marknaden. Identifiera de 10 storsta spelarna med intakter, tillvaxt, agarbild och antal anstallda. Presentera i tabell med kort marknadssammanfattning."

**Dataanalys:**
> "Ga igenom bifogad arsredovisning. Extrahera nyckeltal for de senaste tre aren: revenue, EBITDA, nettoskuld. Berakna CAGR och EBITDA-marginaltrend. Spara som tabell."

**Transaktionsresearch:**
> "Sammanstall de 5 senaste forvarvstransaktionerna i nordisk HR-tech. Inkludera kopare, saljare, transaktionsvardering och EV/Revenue-multipel."

**Dokumentskapande:**
> "Skriv ett utkast till investment memo baserat pa bifogade data. Folj strukturen: executive summary, bolaget i korthet, investeringsrationale, risker, forenklad vardering."

---

## Claude Code vs Claude Cowork

| Aspekt | Claude Code | Claude Cowork |
|--------|------------|---------------|
| **Var kors det** | Din dator (terminalen) | Molnet |
| **Interaktion** | Iterativt — ni arbetar tillsammans | Ge uppdrag, fa resultat |
| **Bast for** | Arbete med lokala filer, finjustering, systembyggande | Langre research, autonoma uppgifter |
| **Teknisk niva** | Medel — terminal | Lagre — enklare gransnitt |
| **Kontroll** | Hog — du ser varje steg | Lagre — agenten arbetar sjalvstandigt |
| **CLAUDE.md och skills** | Ja — hela systemet | Nej — instruktionen ar ditt uppdrag |
| **Sessionslangd** | Minuter till en timme | Kan kora i timmar |

---

## Begransningar

**Instruktionskvalitet ar avgorande.** Vaga uppdrag ger vaga resultat. Var tydlig med: vad du vill ha, i vilket format, vad som ar viktigt, vad som inte behover vara med.

**Bast for valsdefinierade uppgifter.** Cowork presterar bast nar det finns ett tydligt mal, avgransad omfattning och specificerat format.

**Granska alltid resultatet.** Behandla Cowork-leveranser som ett forsta utkast fran en junior medarbetare. Kontrollera fakta, verifiera siffror, justera formuleringar.

**Molnbaserat = datahantering.** Data skickas till Anthropics servrar. For kanslig information — kontrollera med din organisation.

---

## Kombinera Code och Cowork

Det mest kraftfulla arbetsflödet anvander bada:

1. **Cowork researchar** — "Sammanstall data om 20 SaaS-bolag i Norden"
2. **Code bearbetar** — "Las Cowork-rapporten och skapa en jamforelsetabell sorterad efter tillvaxt"
3. **Code finjusterar** — "Formatera enligt var mall i mallar/investment-memo-mall.md"

Cowork gor det tunga lyftet. Code gor det precisa arbetet med dina lokala filer, regler och mallar.

---

## Tips for att komma igang

1. **Borja med avgransade uppgifter.** "Sammanfatta den har rapporten i 10 punkter" ar battre som forsta uppdrag an "Gor en fullstandig marknadsanalys."

2. **Var explicit med format.** Ange struktur, langd, sprak och vad som ska inkluderas.

3. **Bygg ett bibliotek av uppdrags-mallar.** Nar du hittar formuleringar som ger bra resultat, spara dem och ateranvand.

---

> *Foregaende kapitel: [02 — Claude Code](02-claude-code.md)*
>
> *Nasta kapitel: [04 — Mappstruktur och kontext](04-mappstruktur-och-kontext.md)*
