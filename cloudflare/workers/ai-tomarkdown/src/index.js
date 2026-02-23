/**
 * Cloudflare Worker — LLM-friendly Markdown + Content-Signal policy
 *
 * Goal:
 * - If the client requests Markdown (Accept: text/markdown) and the response is Markdown,
 *   force a canonical Content-Signal policy:
 *     ai-train=no, search=yes, ai-input=yes
 *
 * - Avoid converting or touching “technical” endpoints (wp-json, assets, .well-known, etc.).
 *
 * Notes:
 * - This Worker assumes “Markdown for Agents” is enabled at the zone level.
 *   Cloudflare will serve text/markdown when the request negotiates it.
 * - We intentionally only mutate headers when the *response* is text/markdown.
 */

const POLICY_MARKDOWN = "ai-train=no, search=yes, ai-input=yes";
const POLICY_TAG = "worker-ai-tomarkdown";

// Path prefixes to exclude from Markdown conversion.
const BYPASS_PREFIXES = [
  "/wp-json",
  "/wp-admin",
  "/wp-login",
  "/xmlrpc.php",
  "/.well-known/",
  "/cdn-cgi/",
];

// File extensions that should never be converted to Markdown.
// (If they return HTML in edge cases, we still bypass conversion.)
const BYPASS_EXTENSIONS = [
  ".json",
  ".jsonld",
  ".yaml",
  ".yml",
  ".txt",
  ".md",
  ".xml",
  ".rss",
  ".atom",
  ".webmanifest",
  ".svg",
  ".png",
  ".jpg",
  ".jpeg",
  ".webp",
  ".gif",
  ".ico",
  ".css",
  ".js",
  ".map",
  ".woff",
  ".woff2",
  ".ttf",
  ".otf",
  ".eot",
  ".pdf",
  ".zip",
];

function wantsMarkdown(request) {
  const accept = request.headers.get("Accept") || "";
  return accept.toLowerCase().includes("text/markdown");
}

function shouldBypass(pathname) {
  const p = pathname || "/";
  const lower = p.toLowerCase();

  for (const prefix of BYPASS_PREFIXES) {
    if (lower.startsWith(prefix)) return true;
  }

  for (const ext of BYPASS_EXTENSIONS) {
    if (lower.endsWith(ext)) return true;
  }

  return false;
}

function setVary(headers, token) {
  const existing = headers.get("Vary");
  if (!existing) {
    headers.set("Vary", token);
    return;
  }
  const parts = existing
    .split(",")
    .map((s) => s.trim().toLowerCase())
    .filter(Boolean);
  if (!parts.includes(token.toLowerCase())) {
    headers.set("Vary", existing + ", " + token);
  }
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Only act when the client explicitly negotiates Markdown.
    if (!wantsMarkdown(request)) {
      return fetch(request);
    }

    // Safety: do not convert “technical” endpoints.
    // We strip the markdown accept header for upstream fetch to avoid conversion.
    if (shouldBypass(url.pathname)) {
      const h = new Headers(request.headers);
      // Force HTML negotiation upstream.
      h.set("Accept", "text/html,*/*;q=0.8");
      const upstreamReq = new Request(request, { headers: h });
      return fetch(upstreamReq);
    }

    // Default behavior: let Cloudflare produce Markdown (Markdown for Agents).
    const resp = await fetch(request);

    const ct = (resp.headers.get("Content-Type") || "").toLowerCase();
    if (!ct.startsWith("text/markdown")) {
      // Not a Markdown response — do not touch.
      return resp;
    }

    // Mutate headers (stream body through).
    const headers = new Headers(resp.headers);
    headers.set("Content-Signal", POLICY_MARKDOWN);
    headers.set("X-Markdown-Policy", POLICY_TAG);
    // Make sure caches and clients vary on Accept.
    setVary(headers, "accept");

    return new Response(resp.body, {
      status: resp.status,
      statusText: resp.statusText,
      headers,
    });
  },
};
