Title: Strategy
license: https://www.apache.org/licenses/LICENSE-2.0

Apache projects are adopting AI the way everyone else is: quickly, and one account at a time. A
committer signs up with a provider, pays out of pocket or through an employer, and wires the
result into a project workflow. That works for one project. At the scale of hundreds of projects
it leaves the Foundation with no view of what is being spent, no shared catalog of what is
approved, and no way to extend a donated pool of tokens across communities fairly.

The Responsible AI initiative is building a Foundation-managed alternative. Committers remain
free to use whatever tools they like; this is the path the ASF runs and can account for.

<div class="rai-cards">

<div class="rai-card">

## Free to projects

A project draws on a budget the Foundation allocates, rather than a personal account or an
employer's.

</div>

<div class="rai-card">

## Governed by default

Every call is matched to a committer, metered, and charged to their project.

</div>

<div class="rai-card">

## Private where it matters

Sensitive work runs on models the Foundation hosts itself, so the content never leaves ASF
infrastructure.

</div>

</div>

<a id="how-it-fits-together"></a>

## How the pieces fit together

The work divides into four layers. A project asks for work; agents do it; shared services run
those agents and govern every model call; models answer.

<svg viewBox="0 0 720 178" width="100%" role="img" aria-label="Four layers: workloads, agents, services, models" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;margin:1.5rem 0">
  <defs>
    <marker id="s-ar" viewBox="0 0 8 8" refX="6.5" refY="4" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0 1 L6.5 4 L0 7 z" fill="#9aa3ac"/></marker>
  </defs>
  <g>
    <g font-size="7.6" fill="#6a737d" letter-spacing="1.4">
      <text x="0" y="14">WORKLOADS</text><text x="0" y="60">AGENTS</text>
      <text x="0" y="106">SERVICES</text><text x="0" y="166">MODELS</text>
    </g>
    <rect x="82" y="0" width="638" height="25" rx="5" fill="#fdf2f4" stroke="#e8c3c9"/>
    <text x="401" y="16.5" font-size="9.2" fill="#8c0a22" font-weight="600" text-anchor="middle">define · schedule · report runs</text>
    <path d="M401 25 L401 42" stroke="#9aa3ac" stroke-width="1.2" marker-end="url(#s-ar)"/>
    <rect x="82" y="44" width="152" height="27" rx="5" fill="#fdf6ec" stroke="#edc98f"/>
    <rect x="244" y="44" width="152" height="27" rx="5" fill="#fdf6ec" stroke="#edc98f"/>
    <rect x="406" y="44" width="152" height="27" rx="5" fill="#fdf6ec" stroke="#edc98f"/>
    <rect x="568" y="44" width="152" height="27" rx="5" fill="#f7f8fa" stroke="#d7dbe1" stroke-dasharray="3 2"/>
    <g font-size="8.6" fill="#96590a" font-weight="600" text-anchor="middle">
      <text x="158" y="61.5">security scans</text><text x="320" y="61.5">issue triage</text><text x="482" y="61.5">CI/CD review</text>
    </g>
    <text x="644" y="61.5" font-size="8.6" fill="#5a6472" font-weight="600" text-anchor="middle">what projects build</text>
    <path d="M401 71 L401 88" stroke="#9aa3ac" stroke-width="1.2" marker-end="url(#s-ar)"/>
    <rect x="82" y="90" width="638" height="46" rx="5" fill="#f7f8fa" stroke="#d7dbe1"/>
    <rect x="94" y="99" width="148" height="29" rx="4" fill="#fff" stroke="#bfc6d0"/>
    <text x="168" y="111" font-size="8.8" fill="#15181d" font-weight="700" text-anchor="middle">agent workbench</text>
    <text x="168" y="121.5" font-size="7" fill="#5a6472" text-anchor="middle">build and run agents</text>
    <rect x="252" y="99" width="148" height="29" rx="4" fill="#fff" stroke="#bfc6d0"/>
    <text x="326" y="111" font-size="8.8" fill="#15181d" font-weight="700" text-anchor="middle">MCP federation</text>
    <text x="326" y="121.5" font-size="7" fill="#5a6472" text-anchor="middle">governed tool access</text>
    <rect x="410" y="99" width="148" height="29" rx="4" fill="#fdf2f4" stroke="#b21326" stroke-width="1.4"/>
    <text x="484" y="111" font-size="8.8" fill="#8c0a22" font-weight="700" text-anchor="middle">llm.apache.org</text>
    <text x="484" y="121.5" font-size="7" fill="#8c0a22" text-anchor="middle">metered model access</text>
    <rect x="568" y="99" width="140" height="29" rx="4" fill="#fff" stroke="#bfc6d0"/>
    <text x="638" y="111" font-size="8.8" fill="#15181d" font-weight="700" text-anchor="middle">advisor</text>
    <text x="638" y="121.5" font-size="7" fill="#5a6472" text-anchor="middle">cost · quality · policy</text>
    <path d="M484 136 L484 150" stroke="#9aa3ac" stroke-width="1.2" marker-end="url(#s-ar)"/>
    <rect x="82" y="152" width="638" height="25" rx="5" fill="#f7f8fa" stroke="#e6e8ec"/>
    <g font-size="8.6" fill="#3d4652" font-weight="600" text-anchor="middle">
      <text x="188" y="168.5">first-party providers</text><text x="401" y="168.5">hosted under ASF terms</text><text x="614" y="168.5">ASF-hosted models</text>
    </g>
    <line x1="295" y1="156" x2="295" y2="173" stroke="#e6e8ec"/><line x1="507" y1="156" x2="507" y2="173" stroke="#e6e8ec"/>
  </g>
</svg>

**Workloads** is what a project asks for: which job to run, on what schedule, reported where.
**Agents** are the implementations that do the work, and the layer where projects contribute their
own. **Services** are the shared infrastructure the Foundation builds and operates. **Models** are
the classes of model available behind the gateway.

The dividing line matters. Projects contribute at the agents layer; the Foundation is responsible
for keeping the services underneath them running.

## One governed path to models

`llm.apache.org` is the address AI calls go to. It matches the caller to an Apache committer and
their project, then picks a model that fits the job, metering the call against that project's
budget. Some of those models run on the Foundation's own hardware, so sensitive material need
never leave ASF infrastructure.

<svg viewBox="0 0 720 152" width="100%" role="img" aria-label="Projects call llm.apache.org, which routes to available model classes" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;margin:1.5rem 0">
  <defs>
    <marker id="s-in" viewBox="0 0 8 8" refX="6.5" refY="4" markerWidth="6.5" markerHeight="6.5" orient="auto">
      <path d="M0 1 L6.5 4 L0 7 z" fill="#b21326"/></marker>
    <marker id="s-out" viewBox="0 0 8 8" refX="6.5" refY="4" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0 1 L6.5 4 L0 7 z" fill="#9aa3ac"/></marker>
  </defs>
  <g>
    <text x="0" y="10" font-size="7.6" fill="#6a737d" letter-spacing="1.4">PROJECTS</text>
    <rect x="0" y="21" width="134" height="26" rx="4" fill="#f7f8fa" stroke="#d7dbe1"/>
    <text x="67" y="37.5" font-size="8.6" fill="#3d4652" font-weight="600" text-anchor="middle">CI pipelines</text>
    <rect x="0" y="54" width="134" height="26" rx="4" fill="#f7f8fa" stroke="#d7dbe1"/>
    <text x="67" y="70.5" font-size="8.6" fill="#3d4652" font-weight="600" text-anchor="middle">committer tools</text>
    <rect x="0" y="87" width="134" height="26" rx="4" fill="#f7f8fa" stroke="#d7dbe1"/>
    <text x="67" y="103.5" font-size="8.6" fill="#3d4652" font-weight="600" text-anchor="middle">agents</text>
    <rect x="0" y="120" width="134" height="26" rx="4" fill="#f7f8fa" stroke="#d7dbe1"/>
    <text x="67" y="136.5" font-size="8.6" fill="#3d4652" font-weight="600" text-anchor="middle">committees</text>
    <g stroke="#b21326" stroke-width="1.3" fill="none" marker-end="url(#s-in)">
      <path d="M134 33 C170 33 176 64 208 70"/><path d="M134 66 C172 66 176 72 208 74"/>
      <path d="M134 99 C172 99 176 84 208 78"/><path d="M134 132 C170 132 176 90 208 82"/>
    </g>
    <text x="170" y="21" font-size="7.2" fill="#b21326" font-weight="600" text-anchor="middle">one address</text>
    <rect x="210" y="24" width="180" height="106" rx="7" fill="#fdf2f4" stroke="#b21326" stroke-width="1.6"/>
    <text x="300" y="43" font-size="10.5" fill="#8c0a22" font-weight="700" text-anchor="middle">llm.apache.org</text>
    <line x1="226" y1="51" x2="374" y2="51" stroke="#e8c3c9"/>
    <g font-size="8.4" fill="#6a0d28" text-anchor="middle">
      <text x="300" y="66">Apache identity</text><text x="300" y="82">per-project budget</text>
      <text x="300" y="98">metered &amp; attributed</text><text x="300" y="114">routed to best fit</text>
    </g>
    <g stroke="#9aa3ac" stroke-width="1.3" fill="none" marker-end="url(#s-out)">
      <path d="M390 52 C428 52 434 36 472 34"/><path d="M390 77 C428 77 434 77 472 77"/>
      <path d="M390 102 C428 102 434 118 472 120"/>
    </g>
    <text x="474" y="10" font-size="7.6" fill="#6a737d" letter-spacing="1.4">MODELS</text>
    <rect x="474" y="22" width="246" height="26" rx="4" fill="#f7f8fa" stroke="#d7dbe1"/>
    <text x="486" y="38.5" font-size="8.8" fill="#15181d" font-weight="600">first-party providers</text>
    <text x="708" y="38.5" font-size="7.4" fill="#5a6472" text-anchor="end">best capability</text>
    <rect x="474" y="65" width="246" height="26" rx="4" fill="#f7f8fa" stroke="#d7dbe1"/>
    <text x="486" y="81.5" font-size="8.8" fill="#15181d" font-weight="600">hosted under ASF terms</text>
    <text x="708" y="81.5" font-size="7.4" fill="#5a6472" text-anchor="end">safer terms</text>
    <rect x="474" y="108" width="246" height="26" rx="4" fill="#fdf6ec" stroke="#edc98f"/>
    <text x="486" y="124.5" font-size="8.8" fill="#96590a" font-weight="700">ASF-hosted models</text>
    <text x="708" y="124.5" font-size="7.4" fill="#96590a" text-anchor="end">private · low cost</text>
  </g>
</svg>

Tokens reach that pool from several directions: providers donate them, the Foundation procures
capacity, and we run open-weight models on our own rented hardware. A project asks for what it
needs; the Foundation decides where it comes from.

## Where this is going

The initiative is early, and this page describes direction rather than finished work.

| | |
| --- | --- |
| **Running now** | Automated security scanning across Apache projects, with findings delivered to maintainers through the Foundation's standard disclosure process |
| **In development** | The model gateway at `llm.apache.org`, and the agent workbench the scanning pipelines already run on |
| **In design** | Tool federation, and the advisor layer that tracks cost, quality, and routing policy |
| **Ahead** | Self-serve access for any project that wants it, and open-weight models the Foundation controls |

Each piece is being built in the open. As they land, this page will say so.

## Take part

The initiative works in public on the [discussion list](get-involved.html), and welcomes
participation from any Apache committer — on the technical work, on policy, or on the questions
projects are facing right now.

- [Get involved](get-involved.html) — the mailing list and how to join in
- [What we do](what-we-do.html) — the initiative's wider activities
- [Best practices](best-practices.html) — guidance for projects using AI today

*This page describes work in progress and will be updated as the work develops.*
