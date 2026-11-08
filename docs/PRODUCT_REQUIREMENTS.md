# CHARMD Product Requirements

- Status: Baseline requirements for discovery and validation.
- Normative terms: **MUST**, **SHOULD**, and **MAY** indicate requirement strength.
- A requirement is not implemented merely because it appears here.

## 1. Product experience

### Project and session model

- PRJ-001: The system MUST represent a project as a persistent, versioned collection of tracks, clips, source assets, processing, automation, markers, and metadata.
- PRJ-002: Users MUST be able to create, open, rename, duplicate, and recover projects.
- PRJ-003: Autosave and recovery behavior MUST be defined and tested before release.
- PRJ-004: Project changes MUST be auditable; supported operations SHOULD provide undo/redo.
- PRJ-005: Missing, incompatible, or unavailable plugins MUST not silently corrupt project state.

### Audio workspace

- AUD-001: The product MUST provide a multitrack timeline model.
- AUD-002: Users MUST be able to inspect and control track/clip gain, mute, solo, pan, routing, and supported automation.
- AUD-003: Playback and editing MUST remain usable on explicitly supported mobile browser/device combinations.
- AUD-004: Recording, monitoring, latency compensation, sample-rate handling, and background suspension behavior require device validation before being promised.
- AUD-005: Audio rendering MUST define sample format, sample rate, channel layout, headroom, and deterministic processing expectations.

## 2. AI generation and production

- AI-001: The system MUST support generation workflows for both vocals and instrumentals.
- AI-002: A generation request MUST expose relevant inputs, constraints, estimated credit cost, and expected outputs before submission.
- AI-003: Jobs MUST have explicit states, progress, cancellation semantics, retries, and failure reasons.
- AI-004: Generated assets MUST retain provider/model, request, timestamp, license/provenance, and relevant generation metadata where available.
- AI-005: The system MUST abstract providers behind versioned capability interfaces.
- AI-006: The AI production layer MUST express edits as typed operations against a project model rather than arbitrary database or filesystem access.
- AI-007: Operations MUST validate permissions, parameters, budget, and project version before applying.
- AI-008: Users MUST be able to inspect and approve material changes; destructive or externally consequential actions require confirmation.
- AI-009: Quality evaluation MUST distinguish automated estimates from human approval.
- AI-010: Voice cloning or identity imitation MUST require explicit consent and appropriate provenance/safety controls.

### AI capability discovery

Open validation areas include prompt-to-music, lyrics-to-vocal, vocal/instrumental separation or stem delivery, continuation, variation, arrangement, editing, mix assistance, and automated quality evaluation. No specific capability is considered available until a provider and its licensing, latency, reliability, and cost have been validated.

## 3. Professional mastering suite

The mastering suite is required product scope, not a future optional add-on.

- MST-001: Parametric EQ with frequency, gain, and Q controls.
- MST-002: Shelving filters and a validated linear-phase EQ option.
- MST-003: Broadband compression and limiting.
- MST-004: Multiband dynamics processing.
- MST-005: Integrated and short-term LUFS metering and true-peak measurement.
- MST-006: Spectrum analysis.
- MST-007: Stereo width, balance, and correlation analysis.
- MST-008: Saturation/harmonic processing.
- MST-009: Clipping detection and controlled clipping management.
- MST-010: Oversampling controls where supported by the processor.
- MST-011: Dither options appropriate to output bit depth.
- MST-012: Reference-track A/B comparison with level-matching support.
- MST-013: Export profiles for defined WAV and MP3 targets.
- MST-014: Non-destructive processing chains, recallable settings, and reproducible renders.
- MST-015: Mastering meters and export reports MUST identify measurement method, target, and relevant tolerances.

Acceptance requires DSP correctness, metering conformance, artifact testing, listening evaluation, and reproducible offline render tests. Loudness targets must be user-selectable; the product must not imply one universal target for every distribution context.

## 4. Plugin ecosystem

A substantial plugin ecosystem is required product scope.

- PLG-001: CHARMD MUST define a versioned plugin manifest and compatibility contract.
- PLG-002: Plugin parameters MUST use typed, versioned schemas with defaults, ranges, units, and automation behavior.
- PLG-003: Plugin processing MUST have a documented audio input/output contract, including channel layout, sample rate, block size, and latency reporting.
- PLG-004: Plugin execution MUST be isolated from privileged application and account capabilities.
- PLG-005: Plugins MUST receive only explicitly granted capabilities; network, file, and project access MUST be permission-controlled.
- PLG-006: The platform MUST validate plugin packages, signatures/provenance where available, compatibility, and resource limits.
- PLG-007: Users MUST be able to discover, inspect, install, disable, update, and remove plugins.
- PLG-008: Projects MUST preserve plugin identity and parameter state; unavailable plugins MUST fail safely.
- PLG-009: Licensing, entitlement, attribution, and update policy MUST be represented.
- PLG-010: First-party and approved third-party plugins SHOULD be supported through the same published contract.
- PLG-011: Plugin failures MUST be contained and observable without taking down the project or exposing unrelated data.

Initial categories to support across the ecosystem: EQ, dynamics, reverb/delay, distortion/saturation, modulation, synthesizers, samplers, vocal processing, spatial processing, and mastering. This is a category target, not a commitment that every category ships in the first release.

Browser-native Web Audio, AudioWorklet, and WebAssembly are candidate execution technologies. Native VST3/AU binaries are not assumed to run in mobile browsers.

## 5. Export and project portability

- EXP-001: Export MUST report format, sample rate, bit depth where applicable, channel count, duration, and processing chain.
- EXP-002: Failed exports MUST be recoverable and must not silently consume credits for a completed render that was not delivered.
- EXP-003: Project backup/export format and asset portability MUST be specified before production launch.
- EXP-004: Render output MUST be checked for clipping, truncation, silence, and other defined integrity failures.

## 6. Billing and credits

- BILL-001: Subscription entitlements and credit balances MUST be enforced server-side.
- BILL-002: A variable-cost job MUST reserve an estimated credit amount before execution.
- BILL-003: Final usage MUST be reconciled idempotently after job completion.
- BILL-004: Failed or cancelled jobs MUST follow a documented refund/reconciliation policy.
- BILL-005: The ledger MUST be append-only or otherwise auditable, transactionally consistent, and protected from replay/double-spend.
- BILL-006: Users MUST see estimated cost before expensive generation.
- BILL-007: Pricing, tax, payment provider, and jurisdictional compliance require separate approval.

## 7. Security, privacy, and operations

- SEC-001: Every project and asset request MUST be authorized against the authenticated user and tenant.
- SEC-002: Provider credentials and signing secrets MUST remain server-side.
- SEC-003: Uploads MUST be size/type validated and processed in a constrained environment.
- SEC-004: Plugin code MUST be treated as untrusted unless explicitly verified and still sandboxed.
- SEC-005: User audio and prompts MUST have documented retention, deletion, and provider-sharing policies.
- SEC-006: AI actions, billing events, plugin lifecycle events, and security-relevant changes MUST be auditable.
- SEC-007: Backups and restore procedures MUST be tested.
- SEC-008: Rate limits, abuse controls, quotas, and cost ceilings MUST exist before public generation access.

## 8. Mobile-web compatibility

- MOB-001: The team MUST publish an explicit supported browser/device matrix.
- MOB-002: AudioWorklet availability, memory, CPU, latency, microphone permissions, sample-rate conversion, and background behavior MUST be benchmarked.
- MOB-003: Unsupported features MUST degrade explicitly rather than silently.
- MOB-004: Touch-first controls MUST remain accessible and usable at common mobile viewport sizes.
- MOB-005: Desktop browser support MUST be validated separately.

## 9. Non-functional acceptance

Before public release, define measurable thresholds for:
- Playback stability, audio underruns, UI responsiveness, and project-size limits.
- Generation latency, success rate, cancellation, and provider fallback behavior.
- Mastering meter accuracy and render integrity.
- Plugin isolation, CPU/memory budgets, crash containment, and compatibility.
- Recovery-point and recovery-time objectives.
- Availability, observability, and support response.
- Credit ledger correctness and cost ceilings.

No numeric threshold is silently assumed in this baseline; thresholds must be selected from benchmarks and documented in test plans.
