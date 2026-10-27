Title: Tiny model, full provenance — where Apache Sourcelume is, and where it is heading
Date: 2026-10-27
Byline: Achim Nierbeck and Jamie Goodyear
Topics: sourcelume, provenance, projects
Summary: Apache Sourcelume now records provenance for models as well as datasets, and a sample project trains a tiny model that writes its own training provenance record as part of the run.
license: https://www.apache.org/licenses/LICENSE-2.0

Ask anyone who ships a language model a simple question: which data was this trained on, and what license comes with it? The honest answer today is a shrug with a bibliography. Training corpora are assembled from dozens or hundreds of sources, licensing information is missing, wrong, or unverifiable — a 2024 audit found license-omission rates above 70% across popular dataset-hosting sites — and what a producer does publish is usually a claim you have to take on faith: a paragraph in a paper, a model card, a PDF. Nothing you can check.

## What Sourcelume is

That is the gap [Apache Sourcelume](https://sourcelume.apache.org/) is built for. It is not a certification authority and it does not decide whether anyone's licensing claims are true. It is plumbing: a versioned, JSON-LD metadata specification for dataset origin, custody chain, and licensing; a reference registry built on Apache Atlas that stores and serves those records through plain REST APIs; and tooling that turns "documenting your data" from a favor into a build step. The point is narrower and more radical than a licensing database: when a claim is published as a record, in a shared shape, at a stable identifier, then others can finally check it — resolve it, compare it, count it — instead of trusting it.

## Datasets, and then models

The dataset side of this is already real. The spec's `ProvenanceRecord` has been exercised against a public example we could find: the [DFM Mímir training corpus](https://huggingface.co/danish-foundation-models/DFM-Mimir). We verified dataset by dataset, straight from the report's own tables. But records about datasets were only ever half of the question.

On the model side, the situation is inverted: model producers know exactly what they trained on, but there has been no neutral place to say it. When a downstream consumer recently asked whether they could fetch structured provenance for a model — machine-readable, not prose — the piece that would answer them did not exist. The mental model that emerged in the discussion was an SBOM for models: software bills of materials let a shipped artifact declare its ingredients; a model should be able to do the same for its training data, with the producer attesting to the list. So Sourcelume grew a second record type: the `TrainingProvenanceRecord`. A model producer publishes it; it references dataset records by their canonical identifiers, with token counts and shares; it can say `disclosure: complete`, `partial`, or honestly `undisclosed`, because an honest "we don't disclose" is also information worth publishing.

## A record you can watch being born

Which brings us to the demo, because a record type is only as real as a record you can watch being born. The [`apache/sourcelume-sample`](https://github.com/apache/sourcelume-sample) repository trains a character-level language model of 71,891 parameters, on a corpus every reader knows is public domain: *Alice's Adventures in Wonderland*, Project Gutenberg ebook #11, 1865. Then, in the same run, the trainer writes the model's provenance record: a `TrainingProvenanceRecord` pointing at the dataset record by its canonical IRI, with the *actual* numbers from the run — tokens, share, loss, timestamp.

This is where the sober result lands. Not a claim restated in a PDF paper — the run's own tokens, shares, and loss now sit in Sourcelume, written by the trainer that produced them. And as the sample shows, the whole thing drops straight into existing build tooling. Nothing is reconstructed by hand after the fact: the record is written where the data is already being used, in the same pipeline that trains the model.

Our sample code lives at [github.com/apache/sourcelume-sample](https://github.com/apache/sourcelume-sample) for those who would like to dive in.

## What it does not do yet

As it stands today, Sourcelume can show the data that was deposited in it. What it does not do yet — and where community discussion still needs to happen — is verify that any of it is true. Today, Sourcelume's job is exactly this: information can be filed and fetched back by machines. Our community is working towards its initial release goals, with attestation features becoming our next target.

## Getting involved

Sourcelume is an open project, and there is room to help shape what comes next. Whether you're interested in provenance metadata, dataset licensing, model training, API design, or responsible AI more broadly, we welcome people who want to help build and test the specification, contribute to the reference implementation, improve the examples and documentation, or participate in discussions about how provenance claims should be represented and eventually verified.

If this work interests you, join the Apache Sourcelume community. Explore the code and examples, try the sample training pipeline, share your feedback, or get involved in the discussions around the project's next milestones. The goal is not just to make provenance machine-readable, but to build an open, community-driven infrastructure that makes it easier to understand where datasets and models come from — and what we can actually verify about them.

Apache Sourcelume is an ASF Top-level Project. For more information, visit [sourcelume.apache.org](https://sourcelume.apache.org/).

---

*Achim Nierbeck is an ASF Member and a member of the Apache Karaf and Apache Sourcelume PMCs. Jamie Goodyear is an ASF Member and Vice President, Apache Sourcelume.*
