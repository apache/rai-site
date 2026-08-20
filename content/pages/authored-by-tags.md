Title: "Authored by" and "Co-authored" Tags
license: https://www.apache.org/licenses/LICENSE-2.0

## Attribution Tags When AI Assists in Creating Content

Git commit messages support trailer tags that record who contributed to a piece of
code. The two most common are:

- **`Author:`** — the person who created the work
- **`Co-authored-by:`** — another person who contributed meaningfully to the work

When AI tools have assisted in creating or modifying code, contributors have
asked: *How should I record that?*

This page provides practical guidance for Apache contributors.

## Understanding the Tags

### `authored-by: Person Name`

Use this when **the human made the substantive creative choices** for the
contribution. Even if AI helped generate parts of the code (e.g., a function was
drafted by an AI tool but the human selected, edited, reviewed, and integrated
it), the human is the author.

This is the standard and safe approach. It is consistent with US copyright law
(_Thaler v. Perlmutter_, 49 F.4th 611 (D.C. Cir. 2023)), which holds that only
natural persons can be authors.

**Example:**

```
authored-by: Jane Doe <jane@example.com>
```

### `co-authored-by: Person Name`

Use this when **another person** contributed meaningfully to the work — for
example, they reviewed, provided the design, or wrote a section of code that you
integrated. The `co-authored-by` trailer is a convention originated by GitHub and
is widely supported by project management tools.

What about using `co-authored-by` for the AI tool itself? This is a developing
area. Legally, AI cannot be an author under US law. But conventionally, some
projects use this tag as a **provenance record** rather than a legal assertion.

**Examples:**

```
# As a provenance record (not a legal assertion):
co-authored-by: Claude <noreply@anthropic.com>

# When another person also contributed:
co-authored-by: Jane Doe <jane@example.com>
co-authored-by: Claude <noreply@anthropic.com>
```

Both are acceptable conventions — choose what your project prefers.

### A Proposed Convention: `ai-assisted-by`

Some contributors have suggested a new trailer tag specifically for AI tools:

```
ai-assisted-by: Claude-3.5-Sonnet
```

This tag is not yet a standard, but it has the advantage of being unambiguous:
it clearly indicates that an AI tool assisted in creating the work, without
implying that the AI is a legal author or a human co-author.

## Best Practices

1. **Be transparent.** If AI assisted in creating a contribution, document it.
   This helps downstream users understand the provenance of the code.

2. **Use `authored-by` for the human.** The human who exercised creative control
   over the contribution is the author, regardless of whether AI helped generate
   parts of the code.

3. **Use `co-authored-by` for people.** If another person contributed, use the
   standard `co-authored-by` trailer.

4. **Consider `ai-assisted-by` for AI tools.** If your project adopts this
   convention, it provides clear, unambiguous attribution for AI assistance.

5. **Use the `Apache-ai` commit tag** if AI played a significant role. See
   [Policy Recommendations](policy-recommendations.html) for details on the
   Apache-ai tag.

6. **These are conventions, not legal requirements.** Individual projects may
   adopt whatever attribution practices they find useful. The ASF does not
   mandate a specific convention.

## Relationship to Other Pages

- See [Commit Messages for AI-Assisted Code](commit-messages.html) for conventions
  on documenting AI use in commit messages.
- See [AI-Generated Code in Apache Projects](ai-generated-code.html) for broader
  guidance on contributing AI-generated code.

*Back to [Best Practices](best-practices.html).*
