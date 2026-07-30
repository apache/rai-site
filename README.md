# Apache Responsible AI — website (`rai-site`)

Source for the [Apache Responsible AI](https://rai.apache.org/) initiative website.

The site is a static [Pelican](https://getpelican.com/) site, built by the ASF
infrastructure from this repository via `.asf.yaml` (the `pelican:` block builds
`main` and publishes the generated HTML to the `asf-site` branch, which is served at
`rai.apache.org`). Content is written in **Markdown** with **Mermaid** diagram support.

The structure is adapted from [`apache/tooling-docs`](https://github.com/apache/tooling-docs).

## Layout

```
content/
  pages/        Markdown pages (one file per page)
  theme/        Pelican theme (templates)
  css/ js/ fonts/ highlight/ images/   static assets
pelicanconf.py  Pelican configuration (Python)
pelicanconf.yaml
.asf.yaml       ASF infrastructure configuration (build + notifications)
pyproject.toml  Python dependencies (managed with uv)
```

## Editing content

- Pages live in `content/pages/*.md`. Each page starts with a short metadata block
  (`Title:` and `license:`); the home page also sets `Template: index`.
- New pages appear automatically; add them to the navigation in
  `content/theme/templates/menu.html`.
- Small fixes can be made with the GitHub pencil icon; larger changes via a pull request.

## Local build (optional)

The authoritative build runs on ASF infrastructure. To preview locally you need the ASF
Pelican plugins (`asfgenid`, `asfrun`, `gfm`, …) provided by
[`apache/infrastructure-pelican`](https://github.com/apache/infrastructure-pelican); see
that project for setup.

## Get involved

- Mailing list: **discuss@rai.apache.org** —
  [archives](https://lists.apache.org/list.html?discuss@rai.apache.org)
- ASF Slack: **#ai-discuss** (ask to be invited)

## License

Apache License 2.0. See [`LICENSE`](LICENSE).
