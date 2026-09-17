# Geoff Olegario — portfolio

Single-page portfolio. Case studies can be read from three points of view —
designer, PM, or engineer — through one "Read as" switch in the header.

## Files

- `index.html` — the whole site. CSS in the `<style>` block at the top, content
  and behavior in the `<script>` at the bottom.
- `fonts/` — Maragsâ v0.2 (display), in woff2 with woff fallbacks.
- `build-artifact.py` — builds a single self-contained file with the fonts
  embedded, for sharing a preview.

## Editing content

Case studies live in the `CASES` array near the bottom of `index.html`. Each one
has `meta`, `overview`, `problem`, `perspectives` (design / product / eng), and
`results`. A results figure set to `"TK"` renders as a to-come placeholder.

Set `SHOW_DRAFT_NOTE = false` once the copy is final.

## Type

- Maragsâ — hero, work index, project titles, footer.
- DM Sans 500 — case study headings and labels (Google Fonts).
- DM Mono Light — body copy (Google Fonts).

## Local preview

Open `index.html` directly, or run `python3 -m http.server 8000` and visit
<http://localhost:8000>.
