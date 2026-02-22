# WordPress implementation notes (gautierdorval.com)

This is a practical guide to deploy the LLM-first JSON-LD profile on WordPress while keeping optional SEO schema.

## Recommended approach (content negotiation)

Use **Accept-based negotiation**:

- Default (`text/html`): keep your existing SEO schema (if you want).
- Markdown (`Accept: text/markdown`): suppress heavy SEO JSON-LD, emit **one compact LLM-first JSON-LD graph**.

This keeps the Markdown rendition light and reduces token overhead.

Cloudflare already surfaces `Vary: accept` when Markdown is enabled, which is the correct HTTP signal for negotiation.

## Minimal plugin/snippet

Create a small MU-plugin, or use a code snippet plugin, and add:

- a function to detect Markdown requests,
- optional filters to suppress SEO JSON-LD output when Markdown is requested,
- an early `wp_head` output for your compact JSON-LD graph.

### Detect Markdown requests

```php
function gd_is_markdown_request(): bool {
  if (!isset($_SERVER['HTTP_ACCEPT'])) return false;
  return (stripos($_SERVER['HTTP_ACCEPT'], 'text/markdown') !== false);
}
```

### Suppress Yoast JSON-LD when Markdown is requested (optional)

```php
add_filter('wpseo_json_ld_output', function($data) {
  if (function_exists('gd_is_markdown_request') && gd_is_markdown_request()) {
    return [];
  }
  return $data;
}, 100);
```

### Suppress Rank Math JSON-LD when Markdown is requested (optional)

```php
add_filter('rank_math/json_ld', function($data) {
  if (function_exists('gd_is_markdown_request') && gd_is_markdown_request()) {
    return [];
  }
  return $data;
}, 100);
```

### Emit a compact JSON-LD graph (Markdown only)

```php
add_action('wp_head', function() {
  if (!function_exists('gd_is_markdown_request') || !gd_is_markdown_request()) return;

  $url   = get_permalink();
  $title = wp_strip_all_tags(get_the_title());
  $desc  = wp_strip_all_tags(get_the_excerpt());
  if (!$desc) $desc = $title;

  $graph = [
    '@context' => 'https://schema.org',
    '@graph' => [
      [
        '@type' => 'WebSite',
        '@id'   => 'https://gautierdorval.com/#website',
        'url'   => 'https://gautierdorval.com/',
        'name'  => 'gautierdorval.com',
        'inLanguage' => 'fr-CA',
        'publisher'  => ['@id' => 'https://gautierdorval.com/entite/#person']
      ],
      [
        '@type' => 'Person',
        '@id'   => 'https://gautierdorval.com/entite/#person',
        'name'  => 'Gautier Dorval',
        'url'   => 'https://gautierdorval.com/entite/'
      ],
      [
        '@type' => 'WebPage',
        '@id'   => $url . '#webpage',
        'url'   => $url,
        'name'  => $title,
        'headline' => $title,
        'description' => $desc,
        'inLanguage' => 'fr-CA',
        'isPartOf' => ['@id' => 'https://gautierdorval.com/#website'],
        'author' => ['@id' => 'https://gautierdorval.com/entite/#person'],
        'publisher' => ['@id' => 'https://gautierdorval.com/entite/#person'],
      ]
    ]
  ];

  echo '<script type="application/ld+json">' . wp_json_encode($graph, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES) . '</script>';
}, 1);
```

## Optional: auto-derive `mentions` from internal links

To keep schema minimal and avoid manual curation, you can derive `mentions` by extracting internal links to canonical term pages (for example `/definitions/.../`).

- Parse `the_content()` HTML,
- Collect matching URLs,
- Convert them to `DefinedTerm` ids by appending `#definedterm`,
- Deduplicate and cap to 10.

This approach turns **explicit linking** into a canonical interpretive signal.

## Verification (PowerShell)

```powershell
$url = "https://gautierdorval.com/definitions/"
curl.exe -s -o NUL -D - -H "Accept: text/markdown" $url |
  Select-String -Pattern "content-type|vary|x-markdown-tokens|content-signal" -CaseSensitive:$false
```

Then fetch the body and confirm you see only the compact JSON-LD block.

