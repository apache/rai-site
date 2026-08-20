Title: Commit messages for AI-assisted code
license: https://www.apache.org/licenses/LICENSE-2.0

## Documenting AI use in commit messages

When AI tools assist in generating code for an Apache project, commit messages
serve as the primary record of provenance. Good commit messages help future
contributors understand what happened, and they provide the metadata that
provenance-tracking tools need.

## The `Generated-by:` token convention

The ASF's generative tooling guidance recommends the use of a `Generated-by:`
token in commit messages to document AI-assisted code generation.

**Format:**

```
Generated-by: <tool-name>
```

**Examples:**

```
Generated-by: Claude-3.5-Sonnet
Generated-by: GitHub Copilot
Generated-by: Cursor
Generated-by: Gemini-2.0
```

This token is a **convention** — it is not yet a formal, Foundation-wide
requirement. Individual projects may adopt it, modify it, or create their own
variants.

## Example commit messages

### Simple: AI generated a function

```
feat(auth): add JWT token validation middleware

Generated-by: Claude-3.5-Sonnet

Added a middleware function that validates JSON Web Tokens in the
authentication pipeline. The function checks the token signature,
extracts the subject claim, and attaches it to the request context.
```

### Mixed: AI drafted code, human edited heavily

```
fix(parser): correct handling of malformed JSON payloads

Reviewed and edited code generated with GitHub Copilot.
Manually added error cases for null inputs and truncated buffers.

Fixes #1234.
```

### Fully human, AI aided review

```
docs: update contributing guide with AI tooling notes

Reviewed the draft using an AI assistant for clarity suggestions.
All content written by the author.
```

## Best practices

1. **Be specific.** When using `Generated-by:`, name the actual tool you used
   (e.g., `Claude-3.5-Sonnet`, `GitHub Copilot`) rather than a generic label.
   This helps future tooling and provenance analysis.

2. **Explain what AI did and what you did.** If AI generated the code but you
   reviewed and edited it, say so. This provides context for reviewers and
   downstream users.

3. **The commit message is your representation.** Even if AI helped write the
   code, the commit message is your word as the committer. You are responsible
   for what you commit, regardless of whether AI generated any part of it.

4. **Use the Apache-ai tag alongside `Generated-by:`.** If AI played a
   significant role, add both the `Apache-ai` tag (for policy transparency)
   and the `Generated-by:` token (for provenance tracking).

5. **Keep it readable.** Don't over-annotate. A single `Generated-by:` line
   and a brief description of what the AI produced and how you edited it is
   sufficient.

## Sample commit with both tags

```
feat(config): add database connection pooling

Generated-by: Cursor
Apache-ai: This contribution contains code significantly generated
by an AI tool. The function signature and connection logic were
drafted by the AI; error handling and integration were written
manually.

Added configurable connection pooling to the database client.
Supports connection limits, idle timeouts, and health checks.
```

## Relationship to other pages

- See [Policy recommendations](policy-recommendations.html) for the full
  Apache-ai tag guidance.
- See ["Authored by" and "Co-authored" Tags](authored-by-tags.html) for
  attribution conventions.
- See [AI-generated code in Apache projects](ai-generated-code.html) for
  broader guidance on contributing AI-generated code.

*Back to [Best practices](best-practices.html).*
