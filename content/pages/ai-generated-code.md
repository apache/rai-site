Title: AI-generated code in Apache projects
license: https://www.apache.org/licenses/LICENSE-2.0

## DRAFT DOCUMENT

**This document is an UNOFFICIAL DRAFT and should not be considered official policy. Substantial changes may be made before being published as an official policy. Direct any questions to discuss@rai.apache.org.**

## Contributing AI-generated code to Apache projects

Apache contributors increasingly use AI tools (such as GitHub Copilot, Claude, Cursor, and other large language model assistants) to help generate code, fix bugs, write documentation, and review pull requests. When the code you contribute to an Apache project has been significantly generated or modified by an AI tool, there are practical and legal considerations to keep in mind.

## Your obligations as a contributor

Under the Apache Individual Contributor License Agreement (ICLA) and the Apache License 2.0, every contribution carries two core expectations: you are legally entitled to grant the license (ICLA Section 4), and the contribution is your original creation (ICLA Section 5) with any third-party copyrighted material disclosed and compatible with the [ASF 3rd Party Licensing Policy](https://www.apache.org/legal/resolved.html).

Note that while ICLA Section 7 allows submitting third-party work separately with full details of its source and license, those details are generally not knowable for generative AI output. As noted in the [ASF Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html), Section 7 is therefore not a practical route for contributing AI-generated material; contributors instead need to meet the tool-terms and third-party material conditions below.

If you later learn that an AI-assisted contribution reproduced code under an incompatible license, notify the Foundation (ICLA Section 8).

## How the US Copyright Office views AI-generated material

The US Copyright Office's guidance on AI-generated works distinguishes between three scenarios:

### Scenario 1: purely AI-generated

If a work is generated entirely by an AI without any human creative input, it receives **no copyright protection**. The US Court of Appeals held in *Thaler v. Perlmutter*, No. 23-5233, 2025 WL 839178 (D.C. Cir. Mar. 18, 2025) that only natural persons can be authors under the Copyright Act.

**What this means for you:** You can contribute AI-generated code as long as it follows the [ASF Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html). In practice, the main things to check are the tool's terms and whether any third-party code was copied, since copyright status alone does not settle whether a contribution is safe to include.

### Scenario 2: human-authored work with embedded AI material

If you wrote a substantial amount of code and the AI contributed some portions (e.g., you used it to generate a function but then edited, reorganized, and integrated it into a larger module), the **human-authored portions** are copyrightable, while the AI-generated portions are not.

**What this means for you:** If you curate, edit, or substantially modify AI-generated code, the human contribution is protectable. Document what you did to make it your own creation.

### Scenario 3: AI-assisted (human uses AI as a tool)

If you use AI as an assistive tool (much like using a compiler, a linter, or an IDE autocomplete) and you exercise creative control over the result, the work as a whole is copyrightable, and **you** are the author.

**What this means for you:** This is the most common scenario for Apache contributors. Using AI to suggest code, identify bugs, or generate a draft that you then review and integrate is generally safe.

## Conditions for contributing AI-generated code

Before contributing code that was significantly generated or modified by an AI tool, consider the following:

1. **Check the tool's terms of service.** Confirm that the tool's terms place no restrictions on the output inconsistent with the Open Source Definition and grant you sufficient rights to contribute the output under the Apache License 2.0.

2. **Check for third-party material.** AI models can reproduce snippets from copyrighted training data. Ensure the output either includes no third-party material, uses any included third-party material under an Apache-2.0-compatible license with proper attribution, or is not copyrightable subject matter (note that meeting the first two conditions is the sounder route, since copyrightability of AI output remains unsettled across jurisdictions). Using tools with similarity checks or code scanning helps gain reasonable certainty here.

3. **Review and understand the output.** You are responsible for what you commit. Read the AI-generated code, verify it is correct, and be able to explain what it does.

4. **Follow project disclosure practices.** Check whether the project you are contributing to asks for AI disclosure (for example, in the pull request description or via an optional commit trailer). See [Policy recommendations](policy-recommendations.html) for details.

## Further reading

* See the [ASF Generative Tooling Guidance](https://www.apache.org/legal/generative-tooling.html) for the official ASF legal policy.
* See [US copyright law and AI](us-copyright-law.html) for the full legal context.
* See [Policy recommendations](policy-recommendations.html) for a summary of key recommendations.

*Back to [Best practices](best-practices.html).*
