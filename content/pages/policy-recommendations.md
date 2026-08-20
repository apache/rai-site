Title: Policy Recommendations
license: https://www.apache.org/licenses/LICENSE-2.0

## DRAFT DOCUMENT

**This document is an UNOFFICIAL DRAFT and should not be considered official
policy.  Substantial changes may be made before being published as an official
policy.  Direct any questions to discuss@rai.apache.org.**

## Policy Recommendations for AI-Assisted Contributions

This page summarizes the Apache Software Foundation's guidance and key
recommendations for contributors who use AI tools when contributing code,
documentation, or other material to Apache projects.

## The Apache-ai Commit Tag

The **Apache-ai** tag is a voluntary disclosure mechanism. When added to a
commit, it signals that AI played a significant role in generating the
contribution.

### What It Is

- A tag in the commit message body, following the conventional `key: value`
  format used by Git trailer tags.
- A **disclosure**, not a warranty or a restriction. It tells downstream users
  the story without imposing additional legal obligations.
- Recognized by the ASF as a best practice for transparency, but it is not yet
  a mandatory requirement across all projects.

### When to Use It

| Situation | Recommendation |
|---|---|
| AI generated significant portions of code (core logic, large functions) | **Use the tag** — it is strongly recommended |
| AI helped generate documentation or prose | **Consider the tag** — use it if the AI substantially rewrote the text |
| AI assisted incidentally (suggested a single fix you heavily edited) | **Optional** — use it if you want to be thorough |
| You are unsure | **Use it** — it is a disclosure, not a liability |

### Example

```
Apache-ai: This contribution contains code significantly generated
by an AI tool. See AI tagging policy for details.
```

## Key Recommendations

1. **Be transparent about AI tooling used.** Name the tool in your commit
   message using the `Generated-by:` token (e.g., `Generated-by:
   Claude-3.5-Sonnet`). This helps future provenance-tracking tools.

2. **Verify tool terms are compatible with Apache License 2.0.** Check the
   terms of service for your AI tool. Some tools grant the provider broad
   rights over your input (your code) and output (the generated code). Make
   sure these terms do not conflict with contributing under the Apache License
   2.0.

3. **Understand that AI-generated-only content may not be copyrightable.**
   Under US law, only natural persons can be authors. Purely AI-generated
   material may not receive copyright protection. This does not prevent you
   from contributing it — but it is important for downstream users to know
   what is protected.

4. **Maintain human oversight and editorial control.** You are responsible
   for what you commit. Review AI-generated code, understand it, and be able
   to explain what it does. The `authored-by:` tag for the human who made
   the creative decisions is the standard and safe approach.

5. **Use attribution tags consistently.** Use `authored-by:` for the human
   author, `co-authored-by:` for other humans, and consider `ai-assisted-by:`
   for AI tools. Consistency helps the community understand how AI is being
   used.

6. **Document AI use in commit messages.** Use the `Generated-by:` token and
   describe what the AI produced and how you reviewed or edited it. This
   provides the provenance record that future tooling and reviewers need.

7. **Be aware of the EU AI Act.** If you or your project uses AI in ways
   that reach EU audiences (e.g., public-facing chatbots, AI-drafted
   public-interest content), review the transparency obligations under
   Article 50 of Regulation (EU) 2024/1689. See
   [EU AI Act and Copyright](eu-ai-act.html) for details.

## This Is Guidance, Not Binding Policy

The recommendations on this page are **guidance**, not binding policy.
Individual Apache projects remain self-governing under the Apache Way and may
adopt, adapt, or ignore these recommendations as they see fit. The initiative
offers these as shared good practices, and projects are encouraged to discuss
them on the [mailing list](get-involved.html).

## Cross-Reference: All Best Practices Pages

| Topic | Page |
|---|---|
| Guidelines for contributing AI-generated code | [AI-Generated Code in Apache Projects](ai-generated-code.html) |
| US copyright law and AI | [US Copyright Law and AI](us-copyright-law.html) |
| EU AI Act and copyright | [EU AI Act and Copyright](eu-ai-act.html) |
| Attribution tags | ["Authored by" and "Co-authored" Tags](authored-by-tags.html) |
| Commit message conventions | [Commit Messages for AI-Assisted Code](commit-messages.html) |

*Back to [Best Practices](best-practices.html).*
