# CHARMD

**CHARMD** is an independent, AI-native digital audio workstation (DAW), designed mobile-web first.

Its purpose is to let creators direct and collaborate with an autonomous music-production system while retaining clear human control over creative decisions, project state, processing, and export.

## Product boundaries

- Standalone product. No dependency on or affiliation with Pyong Recordz.
- Mobile-web first; responsive desktop support is a design goal, not a separate native-app commitment.
- AI generation covers both vocals and instrumentals.
- Commercial model: subscription plus metered AI credits.
- Required advanced scope: a full professional mastering suite and a substantial plugin ecosystem.
- No real-time multi-user collaboration, social network, music marketplace, unlimited generation, or native mobile application is committed in this baseline.

## Current status

**Pre-implementation — governance, discovery, specification and architecture.**

This repository initially contains product and engineering documentation. No production implementation, provider integration, deployment, or validated audio engine is implied by these documents.

## Documentation

- [Product constitution](docs/PRODUCT_CONSTITUTION.md)
- [Product requirements](docs/PRODUCT_REQUIREMENTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Release gates](docs/RELEASE_GATES.md)
- [Roadmap](docs/ROADMAP.md)
- [Architecture decisions](docs/decisions/README.md)

## Engineering principles

1. Govern before building; document decisions and ownership.
2. Prefer deterministic functions and workflows over autonomous agents where they suffice.
3. AI operations must be typed, auditable, bounded, and reversible where practical.
4. Preserve non-destructive editing and explicit user control.
5. Validate browser audio performance on real target devices before committing to implementation details.
6. Measure generation quality and unit economics before scaling usage.
7. Never execute untrusted plugins in the privileged application context.
8. Do not claim a release gate has passed without reproducible evidence.

## Lifecycle

`GOVERN → DISCOVER → SPECIFY → ARCHITECT → PLAN → BUILD → VERIFY → RELEASE → OPERATE → EVOLVE`

Execution workflow: `SCOPE → INSPECT → EXECUTE → PRODUCE → VERIFY → DELIVER → REPORT`.

## Status vocabulary

- **Proposed** — a candidate direction, not approved as an implementation constraint.
- **Accepted** — a product or architecture decision adopted for this baseline.
- **Validated** — supported by reproducible test evidence.
- **Implemented** — present in the repository and verified to the stated level.
- **Released** — deployed and accepted against release criteria.

See the documentation for open decisions, acceptance criteria, risks, and gate requirements.
