Title: EU AI Act and copyright
license: https://www.apache.org/licenses/LICENSE-2.0

## The EU AI Act and its impact on Apache projects

The European Union's **Artificial Intelligence Act** (Regulation (EU) 2024/1689)
is the first comprehensive AI law in the world. It has phased into effect over
time, and as of August 2026, several key provisions are already in force.

This page summarizes the Act's relevance to the Apache Software Foundation and
to Apache contributors who use AI tools.

## The AI Act timeline

The Act entered into force on **1 August 2024**. Obligations apply in phases:

| Date | Provision | Status |
| --- | --- | --- |
| **February 2025** | Prohibited AI practices (Article 5) and AI literacy requirements (Article 4) | In force |
| **August 2025** | General-purpose AI (GPAI) model rules (Articles 51–56) | In force |
| **2 August 2026** | Transparency obligations (Article 50) | **In force** |
| **2 December 2027** | High-risk system rules (standalone Annex III systems), deferred by the Digital Omnibus Regulation | Deferred |
| **2 August 2028** | High-risk systems embedded in regulated products (Annex I), deferred | Deferred |

The Act also established enforcement powers for the AI Office as of 2 August
2026.

## Key transparency rules: Article 50

Article 50 is the most relevant provision for Apache contributors. It contains
transparency obligations for both **providers** (those who build and distribute
AI systems) and **deployers** (those who use AI systems).

### What providers must do

Providers of generative AI systems must ensure that their outputs (synthetic text,
images, audio, video) carry effective, **machine-readable marks** so they can be
detected as AI-generated. There is a transition period until 2 December 2026 for
systems that were already on the market before 2 August 2026.

### What deployers must do

Deployers (such as an organization that uses a third-party AI service) must:

- Clearly label **deepfakes** — AI-generated or manipulated images, audio, or
  video that resemble real persons, objects, or events and could appear authentic.
- Label **AI-generated or manipulated text** that is published to inform the
  public on matters of public interest (e.g., topics related to politics,
  democracy, public administration, public health), **but only if** the text has
  **not** undergone genuine human review or editorial control, and no natural or
  legal person assumes editorial responsibility for the publication.

### The human-review exception

This is an important exception: if the AI-generated text has gone through genuine
human review and someone takes editorial responsibility for it, the labeling duty
does not apply. This exception is central to the Act's design — it targets
unreviewed AI-generated content that could mislead the public, not every piece of
AI-assisted writing.

Artistic, creative, satirical, and fictional works also receive lighter or
different treatment.

## Article 50(4): the "public interest text" labeling duty

Article 50(4) is the specific paragraph that obligates deployers to label
AI-generated or manipulated text. The labeling duty applies when **all three**
of the following conditions are met:

1. **Published** — the text is made available to the public.
2. **To inform the public** — the purpose is to inform, not merely to share
   or entertain.
3. **On a matter of public interest** — this covers politics and democratic
   processes, public administration, justice, fundamental rights, public
   security and health, environment, consumer safety, and economic, financial,
   scientific, or cultural developments that are subjects of public debate.

These three conditions must **all** be satisfied for the duty to trigger.

**Exception:** The duty does **not** apply if the text has undergone genuine
human review or editorial control, and a natural or legal person has assumed
editorial responsibility for the publication.

### What this means for ASF projects

- **Code, commit messages, PR discussions, issue trackers, technical READMEs,
  API docs, and design docs** are not "informing the public on matters of
  public interest" — they are technical materials, not news-like content on
  politics, democracy, public administration, or similar topics.
- **Release notes** about a software release are also not "public interest
  text" in the sense targeted by the Act.
- **Blog posts or press releases** on technology policy topics could fall
  closer to the line — but the ASF's normal review process (PMC review,
  committer oversight) would normally satisfy the human-review exception.
- **Deepfakes** (AI-generated/manipulated images, audio, or video of real
  persons, objects, or events) require disclosure regardless of whether
  they relate to a public-interest topic.

## How this applies to the Apache Software Foundation

The AI Act has **extraterritorial reach** (Article 2): it applies to non-EU
providers and deployers if their AI output is used in the EU. Because the ASF is
a US-based nonprofit with European participants, websites, mailing lists, and
tools accessed from the EU, some provisions can apply.

However, for most ordinary ASF activities, the direct compliance burden under the
transparency provisions is expected to be **low to negligible** for several reasons:

- **Most ASF output is software and technical documentation**, not "text published
  to inform the public on matters of public interest" as defined by the Act.
- **Source code is explicitly carved out** from the labeling requirements. The
  Commission's guidance on Article 50(2) states that source code (and by extension
  typical code comments and docstrings) is a technical output, not human-facing
  content that risks misleading the public.
- **ASF processes involve human review and editorial control** — PMC review,
  committer oversight, and the contribution review process — which normally satisfy
  the human-review exception.
- **ASF is a deployer, not a provider** — when ASF or its contributors use
  third-party LLM APIs, the third-party company is the provider of the model.
  ASF is deploying those services, not selling them.

### Where the AI Act could matter for ASF

There are limited scenarios where the AI Act could create obligations:

1. **AI-assisted public-facing text** on topics of public interest (e.g.,
   an AI-drafted blog post about technology policy that is lightly or not
   reviewed) could trigger the labeling duty.

2. **Public-facing chatbots or interactive AI assistants** on ASF sites would
   need to disclose when users are interacting with an AI system.

3. **Releasing generative AI systems** (not just using one) — if a project
   releases a generative AI model or tool that is made available in the EU,
   provider-side rules could apply.

## The EU AI Act and copyright for contributors

For individual Apache contributors using AI tools, the most relevant provisions
are:

- **Article 4 (AI literacy):** Organizations deploying AI should ensure their
  staff understand how those systems work. This is a soft obligation — take
  reasonable measures so that people using AI tools understand their capabilities
  and limitations.

- **Article 5 (Prohibited practices):** Already in force. These include practices
  like manipulative or deceptive techniques, exploitative behavior toward
  vulnerable groups, and social scoring. These are unlikely to affect typical
  AI-assisted code contributions but are worth knowing.

- **Source code carve-out:** As noted above, source code is not subject to the
  AI Act's transparency labeling requirements. This means AI-generated code in
  an Apache project is not treated the same way as AI-generated blog posts or
  news articles.

## Bottom line

The EU AI Act has partially entered into force. The transparency rules that are
live (Article 50) have a broad scope but important exceptions — particularly the
human-review exception and the source-code carve-out — that shield most ordinary
Apache activities from direct compliance obligations.

If your project uses AI in a novel way (e.g., a public chatbot, a generative
AI tool, or AI-drafted public-interest content), those use cases should be
reviewed against the specific Article 50 criteria.

*Back to [Best practices](best-practices.html).*
