# Bilaga — Samma upplägg i arbetslivet

*Guidens exempel är en kurs, men upplägget är inte bundet till plugg. Här visas det i en fiktiv investeringsfirma, och sedan pekar jag på färdiga mallar för tre branscher.*

!!! abstract "Kort version"
    - Samma upplägg som i kapitlen går att flytta från en kurs till ett jobb.
    - Exemplet är en påhittad investeringsfirma, och strukturen kan anpassas till andra branscher.
    - Mappar speglar verksamheten, regelfiler finns på tre nivåer och skills tar hand om det som återkommer.
    - Det stabila delas i teamet, medan det personliga hålls privat.
    - Färdiga mallar finns i repot och är utgångspunkter, inte facit.

Allt i guiden går att flytta från en kurs till ett jobb. Mapparna, regelfilerna, skillsen och delningen mellan det stabila och det föränderliga ser likadana ut. Det som byts ut är innehållet. Som exempel använder jag Norvik Capital, en påhittad private equity-firma med sex anställda. Firman finns inte på riktigt, men strukturen är byggd för att vara realistisk och går att anpassa.

## Norvik Capital i korthet

Norvik är en nordisk investerare i mellansegmentet, grundad 2018, med en fond och fyra portföljbolag inom SaaS, industri, bemanning och medtech. Teamet är litet och varje person bär flera roller, vilket är just den miljö där en gemensam struktur gör störst nytta.

## Mappstrukturen speglar verksamheten

Firmans mappar följer hur arbetet är organiserat, med tre nivåer som ändras i olika takt.

```
firma-exempel/
├── CLAUDE.md          regler som gäller överallt
├── firma/             compliance, kapitalanskaffning, investerarkontakt, team
├── fonder/fond-I/     fondvillkor, rapportering, prestanda
├── portfoljbolag/     en mapp per bolag, med eget CLAUDE.md
├── pipeline/          screening, pågående due diligence, avslutade
└── gemensamt/         mallar, skills, ramverk, lärdomar, branschdata
```

Firmanivån ändras sällan, fondnivån kvartalsvis och bolagsnivån löpande. Uppdelningen gör att Claude får rätt kontext utan brus. När någon arbetar i ett bolags mapp behöver Claude kunna allt om bolagets nyckeltal men ingenting om fondens investerarvillkor. Mappen `gemensamt/` är firmans bibliotek, byggt efter principen en källa, många användare. Det är samma tanke som att kursmaterialet i mina repon är stabilt och delat.

## Regelfiler i tre nivåer

??? begrepp "Begrepp: CLAUDE.md"
    --8<-- "claude-md.md"

    [Se alla begrepp i ordlistan](ordlista.md#claude-md)

Hos Norvik finns regelfiler på tre nivåer, och Claude läser de som ligger närmast där arbetet sker.

1. **Firmanivå.** Roll, språk, valuta och datumformat, och en analysstandard: börja med en sammanfattning på högst fem punkter, avsluta med handlingsbara rekommendationer, ta med scenarier vid värdering.
2. **Fond eller pipeline.** Fondens villkor och rapporteringsregler, eller screeningkriterierna för nya affärer med hårda krav på storlek, geografi och lönsamhet.
3. **Bolag.** Bolagets egna definitioner och nyckeltal. Ett SaaS-bolag och en industrikoncern behöver olika mått, och definitionerna måste vara exakta, till exempel vad som får räknas in i återkommande intäkter.

Det motsvarar hierarkin i en kursmapp, där en regelfil på kursnivå kompletteras av regler för ett visst avsnitt.

## Skills för det som återkommer

??? begrepp "Begrepp: Skill"
    --8<-- "skill.md"

    [Se alla begrepp i ordlistan](ordlista.md#skill)

Uppgifter som upprepas blir skills: ett screeningmemo, en kvartalsrapport till styrelsen, en rapport till fondens investerare, en genomgång av ett förvärv. Varje skill beskriver stegen, formatet och vad som ska kontrolleras. På så sätt får en nyanställd samma utgångspunkt som den som varit med i åratal, och resultatet blir jämnare.

## Vem delar vad

Norvik skiljer på tre lager.

| Lager | Innehåll | Var det bor |
|---|---|---|
| Gemensam infrastruktur | Mappstruktur, regelfiler, skills, mallar | Ett delat repo |
| Gemensam kunskap | Årsredovisningar, rapporter, styrelsematerial | Delade projekt i Claude |
| Individuellt arbete | Utkast, hypoteser, anteckningar | Privata konversationer |

??? begrepp "Begrepp: Git"
    --8<-- "git.md"

    [Se alla begrepp i ordlistan](ordlista.md#git)

Repot innehåller sådant som alla behöver och som inte är konfidentiellt. Känsligt material, som avtal och finansiella data om enskilda bolag, hör hemma i projekt med begränsad åtkomst och aldrig i repot. Det är samma gräns som jag drar mellan mina offentliga kursrepon och mina privata dokument, fast med högre insatser.

Verktygen skiftar efter roll. Analytikern arbetar mest i Claude Code och bygger skills. Chefer och partners arbetar i projekt i chatten, ofta från telefonen. Alla drar nytta av samma underliggande struktur.

## Lärdomar som samlas

Norvik bygger ett minne utanför modellen. Efter en slutförd uppgift frågar Claude sig vad som lärdes om data, struktur, format och arbetsgång, och skriver en kort lärdom i en gemensam fil. Varje lärdom har en status: ny, granskad, inarbetad eller arkiverad. Först när en människa har granskat den förs den in i en regelfil eller en skill.

Granskningen är ingen formalitet. En felaktig lärdom som inarbetas upprepas av Claude vid varje uppgift, och för många inarbetade lärdomar gör regelfilerna långa och trögläsliga. Poängen är densamma som i kapitel 07: det som ska bli bestående ska passera en människa.

## Mallarna i repot

Det finns färdiga filer att utgå från i mappen [`templates/`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates/). Ge dem till Claude Code, beskriv vad du vill ändra, och låt Claude bygga resten.

- **Private equity:** den kompletta firman Norvik, med mappar, regelfiler och exempel i [`firma-exempel`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates/private-equity/firma-exempel/), samt en regelfil och tre skills i [`private-equity`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates/private-equity/): due diligence, investeringsmemo och kassaflödesanalys.
- **Konsult:** en regelfil och två skills i [`consulting`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates/consulting/), för marknadsanalys och strategisk rekommendation.
- **Marknadsföring:** en regelfil och två skills i [`marketing`](https://github.com/Solsidan21/AI_workflow_guide_svenska/tree/main/templates/marketing/), för innehållsplanering och kampanjanalys.

Mallarna är utgångspunkter, inte färdiga sanningar. Byt ut siffrorna, ersätt de påhittade bolagen med dina egna uppgifter och ta bort det som inte passar. Ett bra första steg är att be Claude intervjua dig om hur din arbetsvecka ser ut och sedan föreslå vilken struktur som passar.

Om du är på väg in i ett nytt jobb går samma tänk att använda för att lära sig det. Bygg en begreppsmapp för branschens ord, en regelfil som beskriver hur din chef vill ha saker levererade, och en enkel logg över vad som gick fel. Det är kapitel 05 och 07 i ett annat sammanhang.

!!! tip "Gör det med din Claude"
    Klistra in det här i en ny konversation i Claude eller ChatGPT:

    ```text
    Läs det här kapitlet ur en guide om AI-arbetsflöden: https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/docs/bilaga-arbetsliv.md
    Guiden beskriver en persons upplägg och är inget facit. Ta det som passar mig.
    Fråga vad jag jobbar med, hur min arbetsvecka ser ut och vilka uppgifter som återkommer.
    Hjälp mig sedan att föreslå en mappstruktur och en första regelfil för mitt jobb.
    Ställ en fråga i taget innan du föreslår något.
    ```
