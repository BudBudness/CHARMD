# G1 Technical Discovery Execution Batch

- Status: Planned execution baseline
- Gate: G1 — Discover
- Repository: `BudBudness/CHARMD`
- Execution mode: evidence-first; no production implementation or provisioning

## Objective

Resolve or sharply bound the P0 feasibility risks before broad DAW implementation. This plan defines work packages and acceptance evidence; it does not claim that experiments have already run.

## Work packages

### G1-A — Mobile browser audio feasibility (P0)

Investigate representative Android mobile browsers and desktop browsers.

Required experiments:
- AudioContext creation/resume/suspend and lifecycle recovery.
- AudioWorklet availability, startup, messaging, and scheduling stability.
- Multi-track playback graph with representative track counts and processing.
- CPU, memory, underruns, UI responsiveness, and thermal/power behavior.
- Sample-rate mismatch and resampling behavior.
- Bluetooth output latency and route changes.
- Tab backgrounding, screen lock, interruption, and recovery.
- Microphone permissions and recording feasibility, separately from playback.

Evidence:
- Device/browser/OS matrix with exact versions.
- Minimal reproducible test harness and instructions.
- Measurements, failure logs, limitations, and repeatability.
- Explicit supported/unsupported candidate matrix.

Do not promise professional low-latency recording or monitoring based on desktop-only results.

### G1-B — Project model and local persistence (P0)

Evaluate a versioned project schema and browser persistence strategy.

Required experiments:
- Project/track/clip/bus/asset/processor/automation representation.
- IndexedDB and OPFS availability, quotas, and behavior.
- Autosave strategy and transactional boundaries.
- Crash/reload recovery and interrupted writes.
- Asset identity, checksums, deduplication, and derived assets.
- Schema migration and forward/backward compatibility.
- Project portability and export/import.

Evidence:
- Candidate schema and example project fixture.
- Persistence prototype or isolated test harness.
- Recovery/migration test results.
- Quota and browser support findings.

### G1-C — Plugin format and isolation (P0)

Evaluate a browser-native plugin contract. Treat plugin code as untrusted.

Required experiments:
- Versioned manifest and typed parameter schema.
- Audio I/O contract: channels, sample rate, block size, latency.
- AudioWorklet/WASM execution feasibility.
- Worker/origin/CSP boundaries and actual capability isolation.
- CPU, memory, execution-time, and message-size budgets.
- Crash containment and project-state preservation.
- Plugin versioning, package integrity, and missing-plugin behavior.

Evidence:
- Threat model and trust-boundary diagram.
- Minimal benign plugin prototype, not arbitrary third-party execution.
- Attack-surface analysis and tested isolation claims.
- Compatibility and resource-budget proposal.

An AudioWorklet alone must not be described as a complete security sandbox. Native VST3/AU execution is not a mobile-browser assumption.

### G1-D — Professional mastering and DSP feasibility (P0)

Evaluate DSP approaches and measurement conformance for the required mastering suite.

Required experiments:
- Parametric/shelving EQ and linear-phase EQ feasibility.
- Broadband compression, limiting, multiband dynamics.
- Integrated/short-term LUFS and true-peak meter algorithms.
- Spectrum, stereo width, balance, and correlation analysis.
- Saturation, clipping control, oversampling, and dither.
- Offline render determinism, artifact detection, and performance.
- CPU/memory impact on target mobile devices.

Evidence:
- DSP candidate comparison and licensing review.
- Reference test signals and expected outputs.
- Metering algorithm definitions and conformance tolerances.
- Render comparisons, performance results, and listening-test protocol.

### G1-E — AI provider capability and rights evaluation (P0)

Evaluate providers for vocal and instrumental generation and adjacent workflows only where relevant.

Compare:
- Capability coverage and output quality.
- Commercial-use rights, training/data terms, attribution, and restrictions.
- Voice identity/consent controls.
- API stability, latency, rate limits, cancellation, and retries.
- Output formats, stems, metadata, and provenance.
- Cost per successful usable output and fallback options.
- Data retention, privacy, and regional constraints.

Evidence:
- Dated provider comparison with source links.
- Terms/licensing review notes; flag questions requiring legal review.
- Reproducible evaluation prompts and scoring rubric.
- Cost model with assumptions and uncertainty.

Do not create provider accounts, incur charges, upload private audio, or accept terms on the user's behalf.

### G1-F — Billing and credit ledger design (P0)

Design the subscription/credit model without selecting a payment processor.

Required analysis:
- Entitlement model and authoritative balance.
- Append-only or auditable ledger.
- Reservation, settlement, cancellation, expiry, and refund state machine.
- Idempotency and replay/double-spend prevention.
- Concurrency and reconciliation.
- Cost estimation and user-visible preflight.
- Abuse controls and unit economics.

Evidence:
- State diagram and invariants.
- Example ledger schema and transaction boundaries.
- Failure/concurrency test cases.
- Unit economics model with assumptions.

No live payments, billing configuration, or real credit charging.

### G1-G — Security, privacy, and threat model (P0)

Model threats across browser audio, uploaded media, generated assets, AI operations, plugins, project isolation, and billing.

Required analysis:
- Authentication and authorization boundaries.
- Tenant/project/asset isolation.
- Untrusted media and parser risks.
- Plugin sandbox escape and resource exhaustion.
- Prompt injection and AI tool misuse.
- Provider data sharing, retention, and deletion.
- Secrets and supply-chain controls.
- Abuse, quotas, cost exhaustion, audit and incident response.

Evidence:
- Threat model with assets, actors, trust boundaries, threats, mitigations.
- Security test plan and prioritized findings.
- Explicit residual risks and owner decisions.

## Cross-workstream rules

- Keep experiments isolated from production services and real user data.
- Do not provision Cloudflare resources or deploy.
- Do not add Vercel or Supabase.
- Do not add paid dependencies or incur provider costs.
- Record source URLs and access dates for external research.
- Separate measured facts, vendor claims, assumptions, and recommendations.
- Every proposed decision must list alternatives and what evidence would reverse it.

## Exit criteria

G1 is ready for review only when:
1. All seven work packages have evidence or explicitly documented blockers.
2. P0 risks are resolved or accepted with owners and mitigation.
3. Browser/device support candidates are evidence-backed.
4. Audio, project, plugin, mastering, AI, billing, and security decisions have draft ADRs.
5. A reproducible test plan exists for each implementation-critical claim.
6. The decision register and roadmap reflect findings.

G1 does not automatically pass G2, G3, or G4. Gate status changes require review of evidence.

## Execution report template

For each work package, record:
- Question and decision.
- Method and exact environment.
- Steps and versions.
- Results and artifacts.
- Limitations and confidence.
- Risks and cost/licensing implications.
- Recommendation and alternatives.
- Draft ADR and follow-up issue.
- Gate impact: Passed / Partial / Blocked / Not assessed.
