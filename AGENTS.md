# CHARMD Agent Operating Contract

This file governs AI coding agents and automated contributors working in this repository.

## Product authority

- CHARMD is an independent, standalone AI-native DAW. It has no Pyong Recordz dependency or affiliation.
- Mobile-web first; responsive desktop is a design objective. Do not commit to native Android/iOS applications.
- AI generation includes vocals and instrumentals.
- The required advanced product scope includes a full professional mastering suite and a substantial plugin ecosystem.
- Preserve all exclusions and boundaries in `docs/PRODUCT_CONSTITUTION.md`. Do not add social networking, real-time multi-user collaboration, music marketplaces, unlimited generation, or unrelated integrations without an accepted product decision.
- Target platform direction is GitHub + Cloudflare + Termux. Do not introduce Vercel or Supabase as target dependencies.

## Engineering method

Use the project lifecycle:

`GOVERN → DISCOVER → SPECIFY → ARCHITECT → PLAN → BUILD → VERIFY → RELEASE → OPERATE → EVOLVE`

Use the execution workflow:

`SCOPE → INSPECT → EXECUTE → PRODUCE → VERIFY → DELIVER → REPORT`

Prefer folders and deterministic functions/workflows over agents. Use an agent only when flexible reasoning is materially necessary.

## Mandatory working rules

1. Read the relevant product constitution, requirements, architecture, release gates, roadmap, and decision register before changing product behavior or architecture.
2. Treat documents marked Proposed as hypotheses, not validated implementation constraints.
3. Do not claim a capability, test, benchmark, security property, gate, or deployment is complete without reproducible evidence.
4. Keep changes scoped to the assigned issue. Do not perform opportunistic refactors.
5. Work on a dedicated branch. Never commit directly to `main`.
6. Open a pull request with a concise summary, evidence, test results, risks, and rollback notes. Do not merge your own PR unless explicitly instructed.
7. Add or update tests with implementation changes. If a test cannot be run, state why and identify the required environment.
8. Do not commit secrets, tokens, credentials, private audio, user data, or generated copyrighted material.
9. Do not change repository permissions, secrets, environments, billing, Cloudflare resources, domains, production services, or external accounts.
10. Do not deploy, publish, spend money, provision paid resources, or trigger consequential external actions without explicit authorization.
11. Do not add a dependency, framework, AI provider, payment provider, plugin runtime, or cloud service as a committed decision without evidence and an approved decision record.
12. Do not execute third-party plugin code in a privileged context. Treat uploads and plugin packages as untrusted.
13. AI project operations must be typed, permission-checked, budget-checked, auditable, and reversible where practical.
14. Never expose provider keys or credentials to browser code, logs, plugins, or generated artifacts.

## G1 discovery mode

Until G1 evidence is reviewed and accepted, prioritize research, minimal isolated spikes, test harnesses, benchmark protocols, threat models, and decision records. Do not build the full DAW or make broad architectural commitments.

Every discovery result must include:
- Question and decision it informs.
- Method, environment, versions, and device/browser details.
- Reproducible steps or source references.
- Raw measurements or observable evidence.
- Limitations, uncertainties, and failure cases.
- Recommendation with alternatives and reversal conditions.
- Proposed ADR update; do not silently convert a proposal into an accepted decision.

## Required reporting format

At completion, report:
- Scope and issue.
- Files changed.
- Commands/tests run and exact outcomes.
- Evidence links/artifacts.
- Unverified items and blockers.
- Security, privacy, licensing, and cost implications.
- Gate impact: Passed / Partial / Blocked / Not assessed.

A documentation change is not proof of implementation. A passing unit test is not proof of mobile audio compatibility. Keep claims proportional to evidence.
