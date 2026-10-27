Title: Tool-use risk for AI assistants
license: https://www.apache.org/licenses/LICENSE-2.0

## DRAFT DOCUMENT

**This document is an UNOFFICIAL DRAFT and should not be considered official
policy.  Substantial changes may be made before being published as an official
policy.  Direct any questions to discuss@rai.apache.org.**

## Official legal policies live at Legal Affairs

The normative documents on legal risk for the Foundation and its PMCs are
published by Legal Affairs at [apache.org/legal](https://www.apache.org/legal/),
not on this site. For generative AI tooling, and for what may go into a
release, the relevant documents are:

* [Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html)
* [ASF 3rd Party License Policy](https://www.apache.org/legal/resolved.html)
* [ASF Release Policy](https://www.apache.org/legal/release-policy.html)
* [Generative AI tool terms: review results (draft)](https://www.apache.org/legal/generative-tooling-terms-reviewed.html)
* [Generative AI tool terms: what to look for (draft)](https://www.apache.org/legal/generative-tooling-terms-categories.html)

The best practices on this page are not legal policy. Verify them against the
Legal Affairs documents before acting on them, rather than following them as
written. The two can be at odds, and where they are, the Legal Affairs
documents apply. This site is maintained under commit-then-review, so anyone
with commit access can change this page at any time; do not treat its
current wording as a stable reference. Questions about legal risk belong on
`legal-discuss@apache.org`.

## What this page is (and is not)

This page is about **tool-use risk**: conditions a vendor places on the
*person using the tool* (the account holder). Those conditions can include
acceptable-use rules, compete clauses, rate limits, account termination, and
indemnity in the vendor's terms.

This page is **not** about whether generated output can be contributed under
the Apache License 2.0, and it is not a row in the Legal Affairs
[generative-tooling terms review](https://www.apache.org/legal/generative-tooling-terms-reviewed.html).
Those pages ask whether a restriction **travels with the output** into a
release. Tool-use risk does not travel with the output. A breach, if any, sits
with the contributor's vendor account.

Keep the two questions separate:

| Question | Who it binds | Where it lives |
| --- | --- | --- |
| Can this output be contributed and released under ALv2? | The contribution / the release | Legal guidance and the terms-review A/B/X rows |
| Can *I* use this vendor while working on *this* project without picking a fight with my vendor account? | The account holder | This page (RAI best practices) |

A vendor shutting off someone's login does not change the license of
`httpd`, Spark, or any other Apache tree. Downstream users of an ALv2
release do not inherit the contributor's vendor AUP.

## Why this is a RAI topic

Vendor catalogs move. Acceptable-use policies change without a license change
on any Apache artifact. RAI can keep a short, living note of "this tool is a
poor fit for that kind of work" without turning every vendor mood swing into a
Foundation-wide license reclassification.

Individual projects remain self-governing. Nothing here vetoes a commit or
replaces PMC review.

## Three kinds of work

When you pick an assistant, look at what you are building, not only at the
tool's marketing page.

### 1. Ordinary Apache software

Most ASF work is libraries, servers, formats, data systems, build tools, and
the like. Using an AI coding assistant on that work is ordinary tool use,
same family as an IDE or a compiler. A vendor "don't compete with us" clause
does not turn that output into a restricted artifact, and it does not reach
through ALv2 to later users of the release.

Examples: Spark, HTTP Server, Kafka, Flink (the engine, not an
agent-product overlay), Tomcat, Maven.

### 2. Work in a vendor's product lane

Some vendors forbid using their *service or outputs* to develop (or help
anyone develop) machine-learning models or products that compete with them,
directly or indirectly. That rule binds the account holder.

If the Apache project you are touching is itself a general assistant, a
coding-agent workspace, a hosted chatbot, or another product that a
reasonable reader would put in that vendor's current catalog, **do not use
that vendor as the assistant for that work.** Use a different model or write
the change by hand.

This is a "pick another tool" problem, not a "this file cannot enter the
tree" problem. The project can still take the patch. The contributor should
not generate it with the vendor they would be competing with.

Examples that *may* sit in this bucket, depending on the vendor's current
catalog: incubating agent workspaces, general-purpose coding agents, hosted
ASF-operated assistants. A harness that *calls* many vendors, including the
one in question, is usually the opposite of competing with that vendor.

### 3. Training, distillation, and synthetic corpora

Using a vendor's outputs as training data, preference data, or distillation
targets for another model is the clause almost every frontier vendor already
writes down. Do not do that with vendor outputs unless that vendor's terms
clearly allow it. This is independent of cases 1 and 2.

## What a compete-style AUP does *not* do

* It does not place a field-of-use on software that later ships under ALv2.
* It does not mean "someone could use this Apache release to compete,
  therefore the original assistant use was a breach." Third parties have
  always been free to take Apache software and compete with anyone. That is
  the license.
* It does not oblige downstream recipients to hold an account with the
  vendor, accept the vendor's terms, or refrain from competing.
* It does not change because the vendor later acquires an unrelated company
  or launches an unrelated product. If the *project you are editing today*
  is not in their lane today, case 1 still applies. RAI can update this
  page if a named project clearly moves into case 2.

"Indirectly" and "assist anyone" in vendor AUPs are read here as the act of
using *that service* to help build a competing product. Publishing ordinary
ALv2 software is not that act.

## Practical advice for contributors

1. **Read the terms that govern your own login** (consumer vs API vs
   enterprise often differ). The public row on the Legal review page is a
   snapshot; your click-through may be newer.
2. **Match the tool to the work.** Case 1: use whatever assistant you
   already trust and can review. Case 2: switch vendors or do not use an
   assistant. Case 3: do not use vendor outputs as training data.
3. **You still own the commit.** Review the output. Do not commit what you
   cannot explain. Follow the project's usual review rules.
4. **Disclose as the project asks.** See
   [Commit messages for AI-assisted code](commit-messages.html) and
   [Policy recommendations](policy-recommendations.html). Attribution
   (Generated-by / Co-authored-by) is documentation of how the patch was
   made. It is not an admission that the vendor's AUP rides with the file.
5. **Secrets and private lists stay out of prompts.** Tool-use risk includes
   sending project-private or embargoed material to a vendor. That is
   operational, not a license category.
6. **Account loss is personal.** Termination or indemnity in a vendor ToS is
   a risk to the person who clicked "agree." It is not a defect in the
   Apache release. If that risk is unacceptable to you, use another tool.

## Practical advice for PMCs

* Do not treat a contributor's vendor AUP as a third-party license on the
  tree.
* If the project is in case 2 for a named vendor, say so in the project's
  contributor docs ("don't use vendor X to generate patches for this
  repo; use Y or write it"). That is enough.
* Vendor neutrality for *runtime* support (calling many models) is separate
  from which model a committer used to write a patch.
* Point people at this page rather than opening a Legal category fight over
  an account-holder rule.

## How this relates to Legal's A/B/X rows

The draft
[What to Look For](https://www.apache.org/legal/generative-tooling-terms-categories.html)
page is about terms that restrict **output** or impose duties on
**recipients of the code**. Its own text draws the line this page relies on:

> Rules about your use of the service are not the issue; rules that travel
> with the output are.

A compete-style acceptable-use rule is a rule about use of the service. If
Legal records a handling note on a review row ("account holders should not
use this vendor to build products in the vendor's lane"), that note can
point here. It should not, by itself, move an ordinary coding assistant to
Category X for the whole Foundation.

Updates to this page belong on `discuss@rai.apache.org` (and
`general@rai.apache.org` where the RAI team uses that list). Questions
about whether a given output is contributable under ALv2 belong on
`legal-discuss@apache.org`.

## Further reading

* [AI-generated code in Apache projects](ai-generated-code.html)
* [Commit messages for AI-assisted code](commit-messages.html)
* [Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html)
* [Generative AI tool terms: review results (draft)](https://www.apache.org/legal/generative-tooling-terms-reviewed.html)
* [Generative AI tool terms: what to look for (draft)](https://www.apache.org/legal/generative-tooling-terms-categories.html)

*Back to [Best practices](best-practices.html).*
