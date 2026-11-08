# Architecture Decision Register

This register tracks material product and engineering decisions. Detailed records use the format `ADR-NNNN-short-title.md`.

## Accepted decisions

| ID | Decision | Status | Notes |
|---|---|---|---|
| D-001 | CHARMD is an independent standalone product | Accepted | No Pyong Recordz dependency |
| D-002 | Mobile-web is the initial platform | Accepted | Native mobile apps are not committed |
| D-003 | AI generation includes vocals and instrumentals | Accepted | Provider capabilities remain to be validated |
| D-004 | Commercial model is subscription plus AI credits | Accepted | Pricing and payment provider remain open |
| D-005 | Full professional mastering suite is required scope | Accepted | DSP implementation and acceptance thresholds remain open |
| D-006 | A substantial plugin ecosystem is required scope | Accepted | Format, sandbox, SDK and licensing remain open |
| D-007 | AI autonomy is bounded, auditable, and human-governed | Accepted | Typed project operations and approval boundaries required |

## Open P0 decisions

| ID | Decision required | Why it blocks |
|---|---|---|
| O-001 | Supported mobile browser/device baseline | Determines audio engine and product claims |
| O-002 | Audio runtime and local/cloud render split | Determines performance and architecture |
| O-003 | Plugin execution format and security isolation | Required before plugin SDK or third-party code |
| O-004 | Mastering DSP strategy and measurement conformance | Required for professional-quality claims |
| O-005 | AI providers and fallback policy | Determines generation capabilities, licensing, cost and reliability |
| O-006 | Canonical project schema and asset lifecycle | Required for persistence, editing, recovery and portability |
| O-007 | Credit ledger and job idempotency model | Required before charging for variable-cost work |

## Open P1 decisions

- Plugin marketplace/catalog ownership, submission review, and revenue/licensing model.
- Subscription tiers, included credits, rollover/expiry, top-ups, and refund rules.
- Export profile defaults and distribution-specific mastering presets.
- Cloud region strategy, retention policy, and backup objectives.
- Product analytics and privacy-preserving telemetry.

## Decision record template

For each material decision, document:
- Status and date.
- Context and constraints.
- Decision and alternatives considered.
- Evidence and validation method.
- Security, privacy, cost, and operational consequences.
- Reversal conditions and follow-up actions.

Do not mark a proposal accepted without recording the decision authority and supporting evidence.
