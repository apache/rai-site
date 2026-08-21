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
- Changes go through a pull request (fork, branch, PR) - for small fixes, GitHub's
  pencil icon on a file is a quick way to start one straight from the file view.
- **Note** when making any substantive changes run `make check` before committing. This will surface any potential CI/CD failures in your PR.

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
