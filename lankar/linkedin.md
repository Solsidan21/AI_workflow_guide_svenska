# Spårade länkar till guiden

Filen ligger utanför docs/ och publiceras inte på sajten.

## LinkedIn-profilen

Kampanj: `linkedin_profil`. Källa/medium: `linkedin / profil`. Platsen i profilen syns i `utm_content`.

| Plats i profilen | Länk |
|---|---|
| Utvalt | https://solsidan21.github.io/AI_workflow_guide_svenska/?utm_source=linkedin&utm_medium=profil&utm_campaign=linkedin_profil&utm_content=utvalt |
| Kontaktinfo (webbplats) | https://solsidan21.github.io/AI_workflow_guide_svenska/?utm_source=linkedin&utm_medium=profil&utm_campaign=linkedin_profil&utm_content=kontaktinfo |

## Var trafiken syns i GA4

Rapporter > Förvärv > Trafikförvärv. Byt primär dimension till Sessionskälla/-medium eller Sessionskampanj och lägg till sekundär dimension Manuellt annonsinnehåll i sessionen (där hamnar `utm_content`).

Bara besökare som godkänner cookies räknas.

## Cookiefri räkning (Cloudflare Web Analytics)

Räknar alla besök, även från dem som avvisar cookies. Visar inte utm_content, så där syns LinkedIn som hänvisande webbplats (Referer: linkedin.com) men inte om klicket kom från Utvalt eller Kontaktinfo. Besök från LinkedIns mobilapp kan sakna hänvisning och hamnar då under direkta besök.

Token sätts i mkdocs.yml under extra.cloudflare_web_analytics_token.
