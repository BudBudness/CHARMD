# CHARMD Engineering Roadmap

- Status: Proposed sequencing; no implementation dates or delivery promises.
- Planning horizon: evidence-driven, not calendar-driven.

## Phase 0 — Establish the product baseline

**Objective:** Make the repository the authoritative source for product decisions and engineering evidence.

Deliverables:
- Product constitution.
- Requirements baseline.
- Proposed architecture and decision register.
- Release-gate model.
- Risk and discovery backlog.

Exit: owners accept the documentation baseline and open decisions are assigned.

## Phase 1 — Technical discovery and feasibility

**Priority: P0**

Workstreams:
1. **Mobile audio spike:** Web Audio/AudioWorklet playback, scheduling, multitrack graph, memory/CPU, interruptions, sample-rate behavior, and supported browser matrix.
2. **Project model spike:** versioned project schema, local persistence, autosave, crash recovery, and asset identity.
3. **Plugin spike:** manifest, typed parameters, WASM/AudioWorklet execution, isolation boundary, resource limits, and failure containment.
4. **Mastering spike:** representative EQ, dynamics, limiter, LUFS/true-peak measurement, spectrum, stereo analysis, offline rendering, and conformance tests.
5. **AI provider evaluation:** vocal/instrumental generation, licensing, output rights, quality, latency, API reliability, cost, and fallback options.
6. **Billing design:** subscription entitlements, credit reservation, settlement, idempotency, refunds, and unit economics.
7. **Security review:** threat model for user audio, generated assets, AI tools, plugin code, and account/project isolation.

Exit: P0 architecture decisions have evidence-backed records; critical feasibility risks are resolved or explicitly accepted.

## Phase 2 — Product and architecture specification

**Priority: P0**

Deliverables:
- Approved scope and acceptance criteria.
- Supported browser/device matrix.
- Canonical project and asset contracts.
- Audio engine and rendering design.
- Plugin format, SDK, runtime, catalog, and licensing model.
- Mastering processor and metering specifications.
- AI capability/provider contracts and autonomy policy.
- Billing/credit ledger and cost controls.
- Security, privacy, backup, and observability designs.
- Prioritized delivery backlog and test plan.

Exit: G2, G3, and G4 pass with traceable evidence.

## Phase 3 — Vertical-slice implementation

**Priority: after gates pass**

Build the smallest end-to-end path that proves project persistence, browser audio playback, a bounded AI generation job, reviewable project operations, and a valid export. Avoid broad feature work before this path is reliable.

Implementation order should follow measured dependencies, not assumed UI convenience.

## Phase 4 — Professional production capabilities

Build and validate:
- Multitrack editing and production workflows.
- Vocal and instrumental generation workflows.
- AI-directed arrangement and mixing operations.
- Professional mastering suite.
- First-party plugin set and plugin ecosystem foundation.
- Project portability, recovery, and export profiles.

Each capability ships only after its acceptance tests pass.

## Phase 5 — Controlled beta and release

- Invite a bounded cohort.
- Apply generation budgets and usage limits.
- Monitor audio stability, output quality, support load, abuse, and cost per successful task.
- Resolve critical defects and validate rollback.
- Publish supported devices, limitations, privacy and licensing terms.
- Pass G6 and G7 before general availability.

## Phase 6 — Operate and evolve

- Weekly engineering review.
- Reliability, quality, security, and unit-economics review.
- Provider and plugin ecosystem health.
- Cost and credit reconciliation.
- Evidence-based roadmap changes.

## Explicit non-goals for this baseline

Do not add native mobile apps, real-time collaboration, social features, a music marketplace, unlimited generation, or unrelated business integrations without a recorded product decision.
