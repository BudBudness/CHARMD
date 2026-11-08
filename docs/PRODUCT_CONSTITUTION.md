# CHARMD Product Constitution

- Status: Accepted baseline; subject to explicit decision records for material changes.
- Version: 1.0
- Product stage: Pre-implementation
- Repository: `BudBudness/CHARMD`

## 1. Identity

CHARMD is an independent, autonomous AI-native digital audio workstation. It combines a browser-based music-production workspace with AI systems capable of generating and carrying out bounded production tasks.

The product is a DAW, not a chatbot wrapped around a music generator. The audio project, timeline, tracks, processing graph, automation, assets, and export pipeline are first-class product concepts.

## 2. Users

Primary users are independent music creators, vocalists, producers, songwriters, and technically capable audio practitioners who need a production environment accessible from mobile browsers.

Personas and priority segments require discovery and validation; this list is a starting hypothesis, not market research.

## 3. Problem

Music creation workflows are fragmented across generation services, editing tools, mixing/mastering tools, and asset-management systems. CHARMD aims to provide one coherent project environment where AI can perform useful production work while the creator remains able to inspect, direct, revise, and approve the result.

## 4. Core workflows

1. Create or open a project.
2. Describe a musical goal and provide optional lyrics, references, or source audio.
3. Generate vocals, instrumentals, or both.
4. Inspect generated assets and available stems/metadata.
5. Direct AI to perform bounded operations such as arranging, editing, sound selection, mixing, and effects configuration.
6. Review and revise the project in a multitrack editing environment.
7. Master through a professional processing and metering suite.
8. Export a reproducible final render and preserve project state.

The exact MVP workflow and feature ordering remain subject to discovery and product requirements approval.

## 5. Product boundaries

### Accepted

- Standalone product with independent identity and roadmap.
- Mobile-web first.
- Generation of vocals and instrumentals.
- Autonomous AI production with human oversight.
- Full professional mastering suite.
- Substantial plugin ecosystem.
- Hybrid subscription plus AI-credit business model.
- Responsive desktop experience as a design objective.

### Not committed in this baseline

- Native Android/iOS applications.
- Real-time multi-user collaboration.
- Social network, distribution marketplace, or creator marketplace.
- Unlimited AI generation.
- Full modular-synth development environment.
- Direct execution of native VST3 or Audio Unit binaries in the browser.
- Any dependency on Pyong Recordz or another label/business.

These boundaries may change only through an explicit product decision.

## 6. Business model

A hybrid model is accepted:

- Subscription provides defined workstation capabilities and a recurring included credit allowance.
- AI credits meter variable-cost operations such as generation and selected cloud processing.
- Additional credits may be purchased.
- Entitlements and credit balances are enforced server-side.

Pricing, tiers, included allowances, expiry/rollover, refunds, taxes, and payment provider remain open decisions. No pricing or margin claim is approved.

## 7. Human control and autonomy

AI is permitted to propose and execute typed project operations within user-authorized scope. The system must:

- Show the intended operation and affected project objects.
- Validate parameters and project state before execution.
- Maintain an operation history and provenance.
- Support undo/redo or compensating actions for supported operations.
- Preserve source assets and non-destructive processing where practical.
- Require confirmation for destructive, irreversible, externally consequential, or unusually costly operations.
- Enforce user-defined budgets and job limits.
- Require explicit consent and rights checks for voice cloning or identity imitation.

Autonomy does not mean unrestricted access to user assets, accounts, funds, or external services.

## 8. Architecture principles

- Browser-native audio execution where technically viable.
- Separate audio engine, project model, UI, AI orchestration, provider adapters, and platform services.
- Provider-independent interfaces for AI capabilities.
- Deterministic operations before agentic orchestration.
- Explicit contracts, versioned schemas, observability, and reproducible rendering.
- Least privilege, tenant isolation, secure asset handling, and auditable billing.
- Validate mobile-browser constraints before committing to high-cost architecture.

A proposed architecture is documented separately and is not evidence of implementation.

## 9. Security and trust

Security requirements include authentication, project-level authorization, server-side secret storage, validated uploads, abuse controls, plugin isolation, licensing controls, auditable AI operations, privacy controls, and recoverable project storage.

Voice and likeness generation must have consent, provenance, and abuse-prevention safeguards. Applicable legal and regulatory obligations require jurisdiction-specific review.

## 10. Success metrics

Metrics must be defined and baselined before public release. Candidate measures:

- Project creation-to-first-playable-result time.
- Generation completion and failure rates.
- User acceptance and revision rates for AI operations.
- Export success and render reproducibility.
- Audio-engine stability and interaction latency on supported devices.
- Plugin crash/isolation failure rates.
- Mastering measurement accuracy and output conformance.
- Credit cost per successful generation and gross contribution margin.
- Retention, conversion, and paid-user value.

Do not optimize vanity usage while generation quality, safety, and unit economics remain unproven.

## 11. Governance

Material changes to product identity, platform commitment, monetization, data handling, AI autonomy, plugin trust model, or external integrations require a recorded decision.

Release gates are evidence-based. No gate is passed by intention or documentation alone.

## 12. Initial decisions

- D-001: CHARMD is standalone and independent.
- D-002: Mobile-web is the initial platform.
- D-003: AI generation includes vocals and instrumentals.
- D-004: Monetization is subscription plus AI credits.
- D-005: Professional mastering suite is required scope.
- D-006: A substantial plugin ecosystem is required scope.
- D-007: Human control, bounded autonomy, and auditable project operations are core principles.

See [architecture decisions](decisions/README.md) for decision status and future records.
