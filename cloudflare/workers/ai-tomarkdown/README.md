# Worker Cloudflare : Markdown + Content-Signal (LLM-first)

Ce Worker est une **référence d’implémentation** pour les sites WordPress placés derrière Cloudflare.

Objectif :

- Activer un rendu **Markdown** (via « Markdown for Agents » de Cloudflare)
- Forcer une politique canonique sur les réponses Markdown :
  - `Content-Signal: ai-train=no, search=yes, ai-input=yes`
- Éviter la conversion Markdown sur des endpoints « techniques » :
  - `/.well-known/`, `/wp-json/`, `/wp-admin/`, assets (css/js/images), etc.

## Pré-requis

1) **Cloudflare : Markdown for Agents activé** sur le domaine.

2) Le Worker est attaché au domaine via un **route pattern**.

## Déploiement (2 options)

### Option A : Dashboard Cloudflare (simple)

1) Workers & Pages → Workers → Create Worker
2) Copie le contenu de `src/index.js`
3) Déploie
4) Ajoute une route, ex. :
   - `gautierdorval.com/*`

### Option B : Wrangler (CLI)

Dans PowerShell :

```powershell
cd cloudflare/workers/ai-tomarkdown
wrangler deploy
```

Ajoute ensuite la route via le Dashboard (ou via Wrangler, selon ton setup).

## Tests (PowerShell)

### 1) Page HTML → Markdown

```powershell
$url = "https://gautierdorval.com/definitions/"
curl.exe -s -o NUL -D - -H "Accept: text/markdown" $url |
  Select-String -Pattern "content-type|vary|x-markdown-tokens|x-markdown-policy|content-signal" -CaseSensitive:$false
```

Résultat attendu (exemple) :

- `Content-Type: text/markdown; charset=utf-8`
- `Content-Signal: ai-train=no, search=yes, ai-input=yes`
- `X-Markdown-Policy: worker-ai-tomarkdown`

### 2) Endpoint technique (JSON/YAML) → passthrough

```powershell
$url = "https://gautierdorval.com/.well-known/ai-governance.json"
curl.exe -s -o NUL -D - -H "Accept: text/markdown" $url |
  Select-String -Pattern "content-type|vary|x-markdown-policy|content-signal" -CaseSensitive:$false
```

Résultat attendu :

- `Content-Type: application/json` (ou `application/ld+json`, `text/yaml`, etc.)
- Pas de `X-Markdown-Policy`
- `Vary: Accept-Encoding` (ou similaire), **sans** `accept`

## Personnalisation

Les listes `BYPASS_PREFIXES` et `BYPASS_EXTENSIONS` dans `src/index.js` sont faites pour être adaptées.

## Garantie de design

Ce Worker est volontairement minimal :

- Il n’essaie pas de transformer du HTML en Markdown lui-même.
- Il s’appuie sur Cloudflare (Markdown for Agents) et **ne fait que gouverner** la sortie.
