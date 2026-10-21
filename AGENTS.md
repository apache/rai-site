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
for how that mechanism works). The build runs on **ASF BuildBot**
([ci2.apache.org](https://ci2.apache.org)) — commits on `asf-site` are labelled
"Automatic Site Publish by Buildbot". There is **no GitHub Actions build**: the only
workflow in this repo is `pre-commit.yml`, so the Actions tab will never show a site
build, and build results arrive by email instead (`notifications.jobs` in `.asf.yaml`,
plus the pushing committer's `@apache.org` address).

> **`pelicanconf.py` is not what the build reads.** `buildsite.py` in
> [`apache/infrastructure-pelican`](https://github.com/apache/infrastructure-pelican)
> checks for `pelicanconf.yaml` first, and when it exists — it does here — it
> *generates* `pelican.auto.py` from that YAML via `bin/pelican.auto.ezt` and passes
> that to Pelican. `pelicanconf.py` is only a fallback for repositories with no YAML,
> and the copy in this repository is a stale snapshot of the generated file, kept for
> local builds. **Editing `pelicanconf.py` has no effect on the published site**, and
> the YAML schema is fixed: it accepts the keys in
> [`pelicanconf.md`](https://github.com/apache/infrastructure-pelican/blob/master/pelicanconf.md)
> and offers no way to set arbitrary Pelican settings. Anything the generated settings
> don't give you has to be solved in the theme or in content metadata.

The ASF plugins the config requires (`asfgenid`, `asfrun`, plus `toc`, `spu`, `gfm`) come
from `infrastructure-pelican`, not `pyproject.toml`, which lists only `pelican` + helpers.
So `pelican` alone will **not** reproduce the real build.

`pagefind.sh` (`postrun` in `pelicanconf.yaml`, `ASF_POSTRUN` in the generated settings)
downloads the `pagefind` binary at build time and generates the search index into
`_pagefind/`.

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
  `Byline:`, `Topics:`, `Summary:`). They publish to `/blog/<slug>.html`. See README.md
  for the front matter.
- **Never use `Author:`, `Tags:` or `Category:` in front matter.** The ASF build reads
  Markdown through the `gfm` plugin, whose reader builds its own metadata dict and
  **never calls Pelican's metadata processors**. Pelican expects those three fields to be
  `Author`/`Tag`/`Category` objects; from `gfm` they arrive as plain strings, and the
  build dies in `Content.url_format`, which does `self.author.slug`. The failure is
  `CRITICAL: 'str' object has no attribute 'slug'`, it names no file, and it happens for
  any post carrying either field — verified by bisecting the front matter. Use the custom
  `Byline:` and `Topics:` fields instead; they are plain strings and the theme renders
  them (`postlist.html`, `generic.html`). This also means per-tag and per-author pages
  can never be generated here.
- **The blog index is a page, not a direct template.** `content/pages/blog.md` carries
  `Template: blog`, `Save_as: blog/index.html` and `URL: blog/`, and holds no content of
  its own. It is done this way because `DIRECT_TEMPLATES` can only be set in Pelican
  settings, and the generated settings aren't ours to change (see above).
- **`category.html` must exist** (with `tag.html` and `author.html` kept beside it). The
  generated settings set only the plural switches (`TAGS_SAVE_AS` and friends) and leave
  the singular ones at their defaults, so Pelican writes a page per category for every
  post whether we want one or not — every post gets a category even with no `Category:`
  line, because `USE_FOLDER_AS_CATEGORY` derives it from `content/blog/`. With no
  template of our own, Pelican falls back to its built-in simple theme, which extends
  `index.html`, which expects a `page`, and the build dies with `'page' is undefined`.
  The thin templates and the shared `taxonomy.html` exist to catch that; they are marked
  `noindex`. `tag.html` and `author.html` are unreachable today (see the metadata rule
  above) and are kept so that a future fix upstream doesn't reintroduce the crash.
- Adding a page does **not** add it to the navigation. Update the nav by hand in
  `content/theme/templates/menu.html`.
- **Links are deliberately relative** (`about.html`, `css/…`, not `/about.html`,
  `/css/…`). Pages are all at the root; blog posts are the one exception and live one
  level down, under `/blog/`. Templates handle that with a `root` variable: `article.html`
  and `blog.html` set `{% set root = '../' %}`, every other template defaults it to `''`,
  and the shared includes (`menu.html`, `footer.html`, `styles.html`, `post.html`,
  `generic.html`, `blogindex.html`, `postlist.html`) prefix internal links with
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
