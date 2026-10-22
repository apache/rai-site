# Apache Responsible AI — website (`rai-site`)

Source for the [Apache Responsible AI](https://rai.apache.org/) initiative website.

The site is a static [Pelican](https://getpelican.com/) site, built by the ASF
infrastructure from this repository via `.asf.yaml` (the `pelican:` block builds
`main` and publishes the generated HTML to the `asf-site` branch, which is served at
`rai.apache.org`). Content is written in **Markdown** with **Mermaid** diagram support.

## Layout

```
content/
  pages/        Markdown pages (one file per page)
  blog/         Markdown blog posts (one file per post, published under /blog/)
  theme/        Pelican theme (templates)
  css/ js/ fonts/ highlight/ images/   static assets
pelicanconf.yaml  Pelican configuration — the one the ASF build reads
pelicanconf.py    Stale copy of the generated settings, for local builds only
.asf.yaml       ASF infrastructure configuration (build + notifications)
pyproject.toml  Python dependencies (managed with uv)
```

## Editing content

- Pages live in `content/pages/*.md`. Each page starts with a short metadata block
  (`Title:` and `license:`); the home page also sets `Template: index`.
- New pages appear automatically; add them to the navigation in
  `content/theme/templates/menu.html`.
- Changes go through a pull request (fork, branch, PR) - for small fixes, GitHub's
  pencil icon on a file is a quick way to start one straight from the file view.
- **Note** when making any substantive changes run `make check` before committing. This will surface any potential CI/CD failures in your PR.

## Writing a blog post

Posts live in `content/blog/*.md` and are published at `/blog/<slug>.html`, with an index
at [`/blog/`](https://rai.apache.org/blog/). The filename becomes the slug.

```
Title: Responsible AI at Community Over Code, Glasgow
Date: 2026-10-21
Byline: Andrew Musselman
Topics: events, llmao, community
Summary: One or two sentences, shown on the blog index.
license: https://www.apache.org/licenses/LICENSE-2.0
```

`Title`, `Date` and `license` are required; `Byline`, `Topics` and `Summary` are
optional.

> **Use `Byline` and `Topics`, never `Author`, `Tags` or `Category`.** The ASF build
> reads Markdown through a plugin that hands those three to Pelican as plain strings
> where it expects objects, and the build fails with
> `CRITICAL: 'str' object has no attribute 'slug'` — which names no file and is horrible
> to track down. `Byline` and `Topics` are plain strings the theme renders itself.

Three things to watch:

- **Don't repeat the title as an H1** — the template renders it from `Title:`. Start the
  body at `##`, as pages do.
- **Links to pages need `../`** — a post lives one directory down, so link to
  `../get-involved.html`, not `get-involved.html`. Links between posts are plain
  (`other-post.html`), and so are external links.

The index at `/blog/` is `content/pages/blog.md`, which only tells Pelican where to put
the page; the heading and the post list come from the theme. Posts also generate
`/tag/*.html`, `/category/*.html` and `/author/*.html` listings — those are a requirement
of the ASF build rather than a feature, and they're marked `noindex`. See AGENTS.md
before touching any of it.

## Local build (optional)

The authoritative build runs on ASF infrastructure. To preview locally you need the ASF
Pelican plugins (`asfgenid`, `asfrun`, `gfm`, …) provided by
[`apache/infrastructure-pelican`](https://github.com/apache/infrastructure-pelican); see
that project for setup.

## Previewing proposed changes

Any branch in this repository that is named `preview/*` will auto-build and stage to `rai-*.staged.apache.org`.

If you need to test your changes, create a branch such as `preview/<your-asf-id>`.

Commits to it will be staged at `rai-<your-asf-id>.staged.apache.org`.

> [!NOTE]
>
> The branch name must not include any "." characters, or browsers will refuse to display the site due to an invalid SSL certificate. The underscore character ("_") should not be used either, as it is disallowed in host names.

## Get involved

- Mailing list: discuss@rai.apache.org ([archives](https://lists.apache.org/list.html?discuss@rai.apache.org))
- ASF Slack: #rai-discuss (Ask to be invited)

## License

This project is licensed under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
