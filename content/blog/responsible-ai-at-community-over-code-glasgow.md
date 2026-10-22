Title: Responsible AI at Community Over Code, Glasgow
Date: 2026-10-21
Byline: rai-bot
Topics: events, llmao, community
Summary: The Responsible AI initiative brought two sessions and a hackathon slot to Community Over Code in Glasgow. This included a working session on llm.apache.org and a roundtable on what AI is doing to open source maintainership.
license: https://www.apache.org/licenses/LICENSE-2.0

Community Over Code ran from 11 to 14 October at the Hilton Glasgow, and the Responsible AI
(RAI) Initiative was there with two sessions on the Monday and a slot in the hackathon room
alongside them. This is a short account of what we did, what we heard, and what happens next.

## The hackathon: getting people onto llm.apache.org

The RAI hackathon session was built around one practical goal: get committers signed in to
[llm.apache.org](https://llm.apache.org) and making their first model call before they left
the room.

LLMAO is the Foundation's LLM gateway. It exists because the alternative of every project
signing up for its own provider account and holding its own keys, scales badly and leaves the
Foundation with no way to see what is being spent, on whose behalf, or against which model.
The gateway gives the ASF a single sanctioned path to inference: you authenticate with your
Apache identity, you get a credential scoped to a project, and the usage is attributed to that
project and to you. Projects do not need their own vendor relationship to get useful work
done, and the Foundation can answer for the cost and the policy in one place.

For anyone who did not make it to Glasgow, the sign-up path is the same one we walked through
in the room, and the gateway is OpenAI-compatible. In most cases pointing an existing client
at a new base URL and key is the whole integration.

The hackathon ran Monday through Wednesday in the Wee Dram Room, with projects claiming
half-day slots across the three days. Responsible AI shared the schedule with ASF Tooling,
Apache Magpie, Apache Sourcelume, Apache Search and a long list of others. See the
[hackathon page](https://events.apache.org/events/2026/community-over-code/hackathon.html)
for how the time was carved up.

## The Roundtable: What AI is Doing to Maintainership

The Responsible AI Roundtable put six people on a panel — David Fisher, Holden Karau, Andrew
Musselman, Jarek Potiuk, Tim Storer, and Jeff Genender, VP RAI — and opened the floor.

The questions on the table were the uncomfortable ones rather than the promotional ones:

- How do you attract and keep committers when automated shortcuts are available for the work
  that used to be how people earned their way in?
- What does meritocracy mean under the Apache Way when a contribution's provenance is harder
  to read than it used to be?
- How do you re-engage maintainers staring down a large legacy refactor that a model could
  attempt but not be accountable for?
- What do projects do about the rising volume of automated vulnerability reports and
  low-quality submissions, which cost real maintainer attention whether or not they are valid?
- Underneath all of it: What is the risk to open source innovation if the answer to each of
  these is handled badly?

There was lively discussion, with perspectives covering the individual maintainer, project
committee manager, tooling and platform owners, and a welcome academic view. Thought-provoking
questions from the audience included how to include and mentor junior engineers in an
environment where everyone has a "head start" already with their tools, what the shape of
contributions will take in the future, how incentives will change over time, and what
motivates software engineers at their core.

## Where the platform actually is

The sessions were grounded in work that already exists rather than a roadmap, so it is worth
saying plainly what runs today and what does not.

**LLMAO** is the gateway described above: metered, attributed model access for Apache
projects, at [llm.apache.org](https://llm.apache.org).

**Gofannon** is an agent workbench for the Foundation, based on the project of the same name
that originated at the AI Alliance. It is where agents get built and run, so that a project
can get useful work done without standing up its own infrastructure.

**Memory** is the newest piece, and the least built. The problem it addresses is that agents
start every run empty: a scan run this month has no idea what last month's scan found or what
the project already fixed. Memory gives agents somewhere to write down what is worth keeping
and somewhere to read what an earlier run learned, with provenance attached so a human can see
where a claim came from. It is being built at pilot scope, on the services the platform
already runs.

Alongside the platform, Foundation-scale security scanning has continued. A recent pass
covered 230 repositories across 75 project management committees in three days. The results of
that work are what the memory pilot is being tested against first.

Two adjacent projects came up repeatedly in the hallway track as well:
[Apache Magpie](../projects.html), agent-assisted infrastructure for maintaining open source
repositories, and [Apache Sourcelume](../projects.html), instrumentation for tracking the
provenance of AI training data.

## Coming up: FeatherCast

We recorded with [FeatherCast](https://feathercast.apache.org/), the ASF's podcast, while we
were in Glasgow. The episode is not out yet; we will link it here and on
[What's New](../whats-new.html) when it lands.

## Getting involved

The initiative does its work in public and the easiest way in is to show up on the list.

- Mailing list: [general@rai.apache.org](https://lists.apache.org/list.html?general@rai.apache.org)
- ASF Slack: `#rai-discuss` (ASF Member-only)
- The gateway: [llm.apache.org](https://llm.apache.org)
- More ways in: [Get involved](../get-involved.html)
