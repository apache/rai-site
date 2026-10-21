# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project overview

This is the source for the [Apache Responsible AI](https://rai.apache.org/) initiative
website. It is a static [Pelican](https://getpelican.com/) site, with its structure
adapted from [`apache/tooling-docs`](https://github.com/apache/tooling-docs).

## How the site is built

There is **no simple local build**. The authoritative build runs on **ASF
infrastructure**, driven by `.asf.yaml`: the `pelican`/`publish` configuration builds
the `main` branch and publishes the generated HTML to the `asf-site` branch, which is
served at `rai.apache.org` (see [`apache/infrastructure-asfyaml`](https://github.com/apache/infrastructure-asfyaml#deploy)
for how that mechanism works). In CI this is mirrored by
`apache/infrastructure-actions/pelican` (`.github/workflows/build-pelican.yml`).

That action — not `pyproject.toml` — supplies the ASF Pelican plugins the config
requires (`asfgenid`, `asfrun`, plus `toc`, `spu`, `gfm`). `pyproject.toml` lists only
`pelican` + helpers, so `pelican` alone will **not** reproduce the real build. To build
outside the ASF action you need the plugins from
[`apache/infrastructure-pelican`](https://github.com/apache/infrastructure-pelican).

`pagefind.sh` (referenced as `ASF_POSTRUN` in `pelicanconf.py`) downloads the `pagefind`
binary at build time and generates the search index into `_pagefind/`.

## Build and test commands

Dependency and check tooling is driven by `uv` and `pre-commit` via the `Makefile`:

- `make sync` — install non-dev dependencies (`uv sync --no-dev`)
- `make sync-all` — install all dependency groups
- `make check` — run all pre-commit checks (`ruff`, `pyright`, etc.) over all files
- `make check-light` — run the lighter pre-commit set (`.pre-commit-light.yaml`)
- `make update-deps` — refresh pre-commit hooks and `uv` locks

There is no automated content/behavior test suite; `make check` is the gate to run
before opening or updating a PR.

## Editing content

- Pages live in `content/pages/*.md`, one Markdown file per page. Each starts with a
  Pelican metadata block — at least `Title:` and `license:`; the home page also sets
  `Template: index`. Mermaid code blocks render as diagrams.
- Blog posts live in `content/blog/*.md` and need `Date:` as well (plus optional
  `Author:`, `Tags:`, `Summary:`). They publish to `/blog/<slug>.html` with an index at
  `/blog/index.html`, rendered by `blog.html` as a Pelican `DIRECT_TEMPLATES` entry. Tag,
  category and author pages are deliberately not generated (`TAG_SAVE_AS` and friends are
  `""`); tags are labels only. See README.md for the post front matter.
- Adding a page does **not** add it to the navigation. Update the nav by hand in
  `content/theme/templates/menu.html`.
- **Links are deliberately relative** (`about.html`, `css/…`, not `/about.html`,
  `/css/…`). Pages are all at the root; blog posts are the one exception and live one
  level down, under `/blog/`. Templates handle that with a `root` variable: `article.html`
  and `blog.html` set `{% set root = '../' %}`, every other template defaults it to `''`,
  and the shared includes (`menu.html`, `footer.html`, `styles.html`, `post.html`,
  `breadcrumbs.html`, `generic.html`, `blogindex.html`) prefix internal links with
  `{{ root }}`. **Any new internal link in a shared template needs that prefix**, or it
  breaks on post pages. In post *Markdown*, link to pages with `../` (`../faq.html`).
- **The navigation bar is full.** `--rai-nav-h` (62px) sets the body's top padding, so if
  a nav item wraps onto a second line the bar grows taller than that and page content
  slides underneath it. Adding another nav item means re-checking the bar's height from
  992px up, not just eyeballing it on a wide screen.
- Branding lives in `pelicanconf.py` / `pelicanconf.yaml` (site name, domain, URL,
  repository) and `content/theme/templates/menu.html` + `styles.html`.
- `generic.html` (used by most pages) already renders an `<h1>` from the page's
  `Title:` metadata — don't repeat that title as the page's own top-level Markdown
  heading, or it shows up twice. Start pages at `##`/H2 for the first section.
  `index.md` (`Template: index`, rendered via `frontpage.html`) is the exception: that
  template doesn't auto-render a title, so its own top-level heading is the page's only
  one.

## Content constraints (current editorial conventions)

- Write **neutral, public, factual** copy. **Do not** include ASF-internal governance
  debate (PMC vs committee vs advisors, board-resolution wording, rosters, votes).
- **Do not** mention the initiative's funding, sponsorship, or donations (the April 2026
  announcement, the $10M goal, Anthropic / Alpha-Omega), unless a maintainer decides
  otherwise.
- English (`en_US`) is the published language. Non-English drafts, if any, are for
  review only and belong outside this repository.
- Some facts here evolve on-list (`discuss@rai.apache.org`) faster than they're
  reflected on the site — e.g. mailing list visibility/access has been under active
  discussion. When in doubt, check recent list traffic before stating something as
  settled fact.

## PR guidelines

- This repository is [dual-hosted](https://infra.apache.org/github.html): the
  authoritative history is on `gitbox.apache.org`, mirrored to/from GitHub. Contribute
  via a GitHub pull request against `main` (fork this repo, branch, PR) — that's the
  established, working path here.
- `main` and `asf-site` are protected branches (see `.asf.yaml`). Don't touch
  `.asf.yaml` build/publish/notifications config without checking with the people
  already maintaining it — several fields (e.g. mailing list addresses) depend on
  ASF infra state that isn't visible from the repo alone.
