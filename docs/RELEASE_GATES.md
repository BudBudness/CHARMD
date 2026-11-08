# CHARMD Release Gates

The project lifecycle is governed by evidence. A gate is not passed because work is planned, a document exists, or a feature appears in a demo.

## Gate model

| Gate | Stage | Exit evidence | Current status |
|---|---|---|---|
| G0 | Govern | Product identity, boundaries, decision authority, safety and approval policy | Passed for initial baseline |
| G1 | Discover | Validated users/problems/workflows, browser/device research, provider and market evidence | In progress |
| G2 | Specify | Approved requirements, acceptance criteria, non-functional thresholds, scope | Partial |
| G3 | Architect | Validated architecture decisions, threat model, data/audio/plugin contracts | Partial |
| G4 | Plan | Prioritized backlog, dependencies, estimates, test strategy, cost model | Not started |
| G5 | Build | Reviewed implementation, reproducible builds, documented feature evidence | Not started |
| G6 | Verify | Automated and manual tests, audio/device matrix, security, performance, recovery, billing and plugin evidence | Not ready |
| G7 | Release | Release approval, rollback, operational readiness, legal/licensing checks, support and monitoring | Not ready |
| G8 | Operate | SLO reporting, incident response, backups, cost and abuse controls | Not reached |
| G9 | Evolve | Measured feedback, roadmap decisions, controlled migrations and deprecations | Not reached |

## G0 — Govern

Initial pass conditions:
- Standalone product identity confirmed.
- Mobile-web-first platform direction recorded.
- Vocal and instrumental generation included.
- Subscription plus AI credits model recorded.
- Full professional mastering suite and substantial plugin ecosystem required.
- Human control and bounded AI autonomy established.
- No unapproved external dependencies or consequential actions.

Reopen G0 when product identity, scope, data governance, or decision authority materially changes.

## G1 — Discover

Required evidence:
- Target user interviews or equivalent primary research.
- Core workflow and competitor/workflow analysis.
- Supported device/browser candidates and constraints.
- Audio engine feasibility on representative Android and desktop devices.
- AI generation provider capability, licensing, latency, reliability, and price comparison.
- Plugin ecosystem user needs and developer feasibility.
- Mastering workflow and output-standard research.

## G2 — Specify

Required evidence:
- Prioritized product requirements and explicit exclusions.
- Testable acceptance criteria for each committed capability.
- Project schema and portability requirements.
- AI autonomy and approval matrix.
- Mastering measurement, DSP, and export acceptance criteria.
- Plugin manifest, SDK, security, compatibility, and licensing requirements.
- Billing/credit state machine and failure/refund policy.
- Non-functional thresholds selected from benchmarks.

## G3 — Architect

Required evidence:
- Approved context/container/component diagrams.
- Audio runtime and render strategy validated by spikes.
- Plugin threat model and isolation proof of concept.
- AI provider adapter and job contract.
- Canonical project and asset model.
- Transactional credit ledger design and idempotency strategy.
- Data protection, backup, restore, observability, and cost model.

## G4 — Plan

Required evidence:
- Dependency-aware backlog with owners and acceptance criteria.
- Delivery increments and rollback boundaries.
- CI and test strategy.
- Device lab/test matrix.
- Provider and infrastructure cost estimates.
- Risk register with mitigations and decision deadlines.

## G5 — Build

Required evidence:
- Changes reviewed and tested.
- No secrets committed.
- Versioned schemas and migrations.
- Audio and plugin runtime instrumentation.
- AI operation audit and budget enforcement.
- Documentation updated with implementation evidence.

## G6 — Verify

Required evidence:
- Browser/device playback and editing stability.
- Recording/monitoring claims tested where supported.
- Render integrity and mastering meter conformance.
- Plugin isolation, compatibility, resource limits, and crash containment.
- AI output quality, licensing, cancellation, retries, and provider fallback.
- Credit ledger concurrency, duplicate submission, refund, and reconciliation tests.
- Security, privacy, restore, load, and failure-injection tests.

## G7 — Release

Required evidence:
- Product, security, legal/licensing, and operational sign-off.
- Explicit supported-device matrix and known limitations.
- Tested backup and rollback plan.
- Monitoring, alerting, support, and incident runbooks.
- Cost ceilings and abuse controls enabled.
- No unresolved critical/high-severity release blockers.

## Change control

A gate may be reopened when new evidence invalidates a prior assumption. Record the evidence, impact, owner, and re-entry criteria. Never bypass a gate silently.
