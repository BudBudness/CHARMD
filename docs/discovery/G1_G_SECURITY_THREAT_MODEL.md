# G1-G — CHARMD Security and Privacy Threat Model

- Gate: G1 Discover
- Status: Initial qualitative model; no security testing performed
- Date: 2026-11-08

## Scope and assumptions

Standalone mobile-web AI-native DAW. Users create projects, upload/import audio, generate vocals and instrumentals through provider adapters, use first-party and potentially third-party plugins, and purchase subscription/AI credits. All uploaded media, plugin packages, model outputs and provider responses are untrusted.

## Assets

- User identity, sessions and authorization state.
- Project metadata, arrangement, automation and plugin state.
- Original audio, generated audio, stems and exports.
- Voice identity/consent records and provenance.
- Provider credentials and integration configuration.
- Subscription entitlements, credit balance and immutable ledger.
- Plugin packages, manifests and signatures/hashes.
- Audit events, deletion requests and retention metadata.

## Actors and trust boundaries

- Anonymous visitor vs authenticated user.
- User vs another tenant/project.
- Browser UI vs server API.
- Browser audio runtime vs plugin package.
- Application backend vs AI provider.
- Queue producer vs at-least-once consumer.
- Uploaded file parser vs application process.
- Build pipeline/dependency source vs released artifacts.
- Support/operator access vs user content.

## Threat register

| ID | Threat | Impact | Primary controls |
|---|---|---|---|
| T01 | Cross-tenant project/asset IDOR | Private media disclosure or modification | Server-side ownership checks on every object operation; negative authorization tests |
| T02 | Malicious media/parser exploit | Code execution, crash or resource exhaustion | Type sniffing, size/duration limits, isolated parsing/transcoding, patched parsers |
| T03 | Plugin capability abuse | Data theft, network exfiltration, audio thread denial | Narrow host ABI, no ambient authority, resource budgets, integrity checks, kill/bypass |
| T04 | Prompt injection via project/audio metadata | Unauthorized actions or data leakage | Treat model output as untrusted; deterministic tool allowlists and server authorization |
| T05 | Provider credential exposure | Account compromise and financial loss | Server-side secrets, scoped credentials, rotation, no secrets in browser/logs |
| T06 | Credit double spend/replay | Financial loss and user disputes | Transactional reservations, idempotency, append-only ledger, reconciliation |
| T07 | Queue duplicate/out-of-order work | Duplicate generation or charge | Stable operation IDs, idempotent handlers, explicit state machine |
| T08 | Cost exhaustion/abuse | Provider bill spike and service degradation | Preflight estimates, quotas, rate limits, concurrency limits, anomaly alerts |
| T09 | Voice impersonation without consent | Identity harm and legal exposure | Explicit consent, provenance, restrictions and reporting/escalation path |
| T10 | Supply-chain compromise | Malicious app/plugin/dependency release | Lockfiles, provenance, review, pinned versions, build isolation and artifact verification |
| T11 | Incomplete deletion/retention | Persistent sensitive media after user request | Data inventory, lifecycle policy, provider deletion workflow and verifiable status |
| T12 | Session theft/CSRF | Account and project compromise | Secure cookies, CSRF defenses, session rotation, origin checks, MFA policy review |
| T13 | Export/import archive traversal | Arbitrary file overwrite or disclosure | Safe path handling, archive limits, generated storage keys, validation |
| T14 | Audit log tampering or leakage | Loss of accountability or sensitive data exposure | Append-only server events, restricted access, data minimization and retention controls |

## Mandatory security invariants

- Every server-side project/asset operation is authorized against the authenticated tenant.
- No provider key or privileged secret reaches browser code or plugin code.
- AI-generated action plans cannot grant themselves permissions.
- Credits are charged only through server-authoritative idempotent state transitions.
- Plugin and media processing are resource bounded and fail closed.
- Voice generation/identity features require explicit, auditable consent.
- Deletion requests cover primary storage, derived assets, backups and provider-held data according to a disclosed retention policy.
- Logs avoid raw audio, secrets, access tokens and unnecessary personal content.

## Prioritized verification plan

P0: cross-tenant IDOR tests; session/CSRF review; upload/parser limits; provider-secret scan; credit replay/concurrency; plugin capability tests; cost-exhaustion controls.

P1: dependency and build provenance; archive traversal; deletion propagation; audit access controls; queue retry/reconciliation; voice-consent abuse cases.

P2: incident exercises, privacy UX review, accessibility and abuse-report workflow.

Each test must include setup, attacker capability, expected denial/containment, observed result and artifact.

## Residual risks / open decisions

- Browser plugin hard real-time and resource isolation guarantees are limited.
- Provider retention and deletion behavior depends on exact API contracts.
- Voice identity risk depends on product capability and jurisdiction.
- Browser storage eviction and local device compromise remain outside full server control.
- Legal/privacy obligations require jurisdiction-specific review before launch.

## Exit decision

G1-G remains Partial. This is an initial threat model, not a security audit, penetration test or certification.
