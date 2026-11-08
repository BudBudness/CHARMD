# CHARMD Architecture

- Status: Proposed architecture baseline; critical decisions remain open.
- This document describes a target design, not deployed infrastructure.

## 1. System context

CHARMD is a mobile-web-first DAW. The browser hosts the interactive workspace and, where supported, the real-time audio engine. Cloud services provide identity/session APIs, project metadata, asset storage, AI job orchestration, provider integration, billing/entitlements, plugin catalog metadata, and operational telemetry.

## 2. Proposed technology direction

| Concern | Candidate direction | Status |
|---|---|---|
| Web application | TypeScript, React, Next.js | Proposed |
| UI styling | Tailwind CSS or equivalent | Proposed |
| Audio runtime | Web Audio API + AudioWorklet | Proposed |
| DSP extensions | WebAssembly where justified | Proposed |
| Local persistence | IndexedDB; OPFS where supported | Proposed |
| API/edge | Cloudflare Workers | Proposed |
| Relational metadata | Cloudflare D1 | Proposed |
| Audio/assets | Cloudflare R2 | Proposed |
| Async jobs | Cloudflare Queues and durable job records | Proposed |
| Source control | GitHub | Accepted |
| CI | GitHub Actions | Proposed |
| AI providers | Provider adapters behind internal contracts | Accepted principle; providers undecided |

Cloudflare is the preferred platform direction, subject to feature, region, storage, egress, media-processing, and cost validation. Do not introduce Vercel or Supabase as target dependencies. No infrastructure has been provisioned by this architecture document.

## 3. Logical components

1. **Studio UI** — project browser, timeline, mixer, mastering, plugin manager, AI command surface.
2. **Project domain** — canonical project schema, tracks, clips, routing, automation, assets, versions, operation history.
3. **Audio engine** — transport, scheduling, graph construction, playback, supported recording/monitoring, offline render.
4. **DSP and plugin host** — built-in processors, plugin manifests, sandbox/runtime boundary, parameter automation.
5. **AI orchestration** — request planning, typed operation generation, policy checks, approval, execution, audit.
6. **Generation adapters** — provider-specific generation, transformation, stem, and analysis capabilities.
7. **Quality evaluation** — technical validation and optional model-assisted evaluation with confidence/provenance.
8. **Platform API** — identity, authorization, projects, jobs, assets, plugin catalog, entitlements.
9. **Billing ledger** — subscription entitlements, credit reservation, settlement, refunds, audit.
10. **Operations** — logs, metrics, traces, cost accounting, abuse detection, backup/restore.

## 4. Audio engine design

The real-time path should remain local to the browser wherever feasible:

- UI thread handles interaction and state projection.
- AudioWorklet handles time-sensitive processing.
- Web Audio nodes provide supported native graph primitives.
- WASM is considered for DSP where browser APIs are insufficient and performance is measured.
- Offline rendering is separated from interactive playback where possible.
- The project model is not coupled to a specific provider or plugin implementation.

The architecture must explicitly account for browser/device variability, audio context suspension, mobile power management, Bluetooth latency, sample-rate mismatch, memory pressure, and interruption recovery.

Do not claim professional low-latency recording or monitoring on all mobile browsers before testing actual devices.

## 5. Project and asset model

The canonical project model should be versioned and independent of UI component state. It should represent:

- Project metadata and schema version.
- Tracks, buses, clips, regions, markers, and routing.
- Source assets and derived assets with content identity.
- Processor/plugin instances and typed parameter state.
- Automation and timeline events.
- AI operation history and provenance.
- Render/export profiles and render metadata.

Large audio files should not be embedded in relational project records. Use object storage for durable assets and local browser storage for cache/offline work. Define resumable uploads, checksums, asset lifecycle, retention, and deletion.

## 6. AI execution architecture

The AI orchestrator should use a constrained pipeline:

1. Parse user intent into a structured task.
2. Resolve project context and permitted capabilities.
3. Produce a typed operation plan.
4. Estimate resource and credit cost.
5. Validate policy, schema, project version, and user authorization.
6. Request approval when required.
7. Execute deterministic operations or dispatch a bounded generation job.
8. Validate outputs and record provenance.
9. Reconcile credit usage and update project state.
10. Present a reviewable result with undo/compensation where supported.

Agents are not the default execution substrate. Use deterministic functions and workflows first; use an agent only where flexible planning materially improves the task.

Provider adapters must expose capability, model/version, licensing, input/output limits, latency, cost estimate, cancellation, retryability, and failure semantics.

## 7. Plugin runtime and trust boundary

Treat all third-party plugin code as untrusted. A candidate browser-native model is a constrained AudioWorklet/WASM runtime with:

- Signed or integrity-checked package metadata where feasible.
- Strict manifest and parameter schema validation.
- Explicit capability permissions.
- No ambient access to credentials, arbitrary project files, or privileged APIs.
- CPU, memory, execution-time, and message-size budgets.
- Version compatibility and safe failure behavior.
- Crash containment and project-state preservation.

The final sandbox mechanism is a P0 architecture decision. An AudioWorklet alone is not a complete security sandbox. Evaluate origin isolation, worker boundaries, WASM constraints, message protocols, CSP, and browser-specific security guarantees. Native VST3/AU hosting is out of scope for the mobile-browser baseline.

## 8. Mastering and render architecture

Separate the mastering signal chain from UI controls. Processors must have versioned parameter schemas and stable serialization. Metering must define algorithms and measurement windows. Offline render should be reproducible within documented tolerances and should report clipping, loudness, true peak, sample rate, bit depth, and dither configuration.

Linear-phase processing, oversampling, multiband dynamics, and high-quality limiting require performance and artifact tests on target devices. A cloud render fallback may be evaluated, but must not be assumed without cost, privacy, and latency analysis.

## 9. Platform data and job architecture

Candidate Cloudflare service mapping:

- Workers: authenticated API and control-plane endpoints.
- D1: users, projects, metadata, job state, plugin catalog, entitlements, and ledger records where transactional semantics suffice.
- R2: source audio, generated audio, stems, exports, and plugin packages.
- Queues: asynchronous generation and processing jobs.
- Durable Objects: only where coordination or strongly ordered per-entity state is demonstrated to be necessary.

Avoid using a queue as the source of truth. Persist job state and idempotency keys. Define retry limits, dead-letter handling, cancellation, timeouts, and reconciliation.

Validate D1 transaction/concurrency behavior and Cloudflare platform limits against the intended workload before committing to schema or throughput assumptions.

## 10. Security and privacy

- Authentication and authorization must be explicit at every API boundary.
- Use least-privilege service bindings and scoped credentials.
- Keep AI provider keys and signing keys server-side.
- Enforce tenant/project ownership for every asset and operation.
- Validate media inputs and process untrusted files in constrained environments.
- Keep plugin runtime isolated from privileged application capabilities.
- Maintain audit trails for AI actions, billing, plugin lifecycle, and admin actions.
- Define retention, deletion, backup, restore, and provider data-use policies.
- Use rate limits, quotas, cost ceilings, and abuse detection.

## 11. Reliability and observability

Instrument audio engine health separately from cloud API health. Track job lifecycle, provider outcomes, render validation, plugin faults, credit ledger reconciliation, storage operations, and cost per successful task. Do not collect audio content or sensitive prompts in logs by default.

Define service-level objectives only after baseline measurement. Recovery and backup procedures must be exercised, not merely documented.

## 12. Critical architecture decisions

P0 before implementation commitments:
- Supported mobile browsers and device baseline.
- Audio engine runtime and local/cloud render split.
- Plugin sandbox and package execution contract.
- Mastering DSP implementation strategy and measurement conformance.
- AI provider selection and fallback strategy.
- Canonical project schema and asset lifecycle.
- Credit ledger and idempotent job model.

See [decision register](decisions/README.md). Proposed technology choices may change after evidence-based spikes.
