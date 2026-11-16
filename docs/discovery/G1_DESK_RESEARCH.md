# G1 Desk-Research Evidence — Initial Pass

- Date: 2026-11-08
- Gate: G1 — Discover
- Status: Partial; desk research only
- Branch: chore/github-agent-bootstrap
- Scope: Public technical documentation and published terms. No device tests, paid API calls, private-audio uploads, provider account creation, or infrastructure provisioning were performed.

## Executive result

Desk research confirms that the proposed browser-native direction is technically plausible, but does not validate production-grade mobile DAW performance. The highest-risk unknowns remain empirical: sustained multitrack audio on target Android devices, interruption/recovery, browser storage survival under pressure, real plugin isolation, mastering conformance/performance, and AI generation quality/cost/rights under the exact commercial/API contract.

**No P0 architecture decision is promoted to Validated by this report.** Broad implementation remains blocked pending the experiments listed below.

## G1-A — Mobile browser audio

### Evidence
- MDN classifies AudioWorklet as widely available since April 2021, available only in secure contexts, and executing custom processing on a separate Web Audio thread: https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet
- Web Audio contexts may begin suspended when created outside a user gesture; explicit resume handling is required: https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices
- AudioContext exposes running, suspended, closed and interrupted states; interruption is a platform event outside application control: https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/state
- The Web Audio specification defines OfflineAudioContext and rendering behavior, but specification support is not a performance benchmark: https://www.w3.org/TR/webaudio/

### Finding / recommendation
Keep the browser audio engine as a candidate, not a validated commitment. Require user-gesture startup, explicit state/recovery handling, clock-based scheduling, underrun instrumentation and graceful interruption recovery. Separate playback, recording and low-latency monitoring acceptance criteria.

### Not measured
No Android handset/browser matrix, multitrack stress test, CPU/memory/thermal test, Bluetooth latency test, background/screen-lock test, microphone test or long-session soak was run.

### Required next experiment
Build a minimal isolated harness with configurable track count, buffer/block sizes, effects and test signals. Record browser/OS/device/build, sample rate, callback timing, underruns, CPU, memory, temperature/power proxies, output route, interruptions and recovery. Repeat on representative low/mid/high Android devices and desktop browsers.

## G1-B — Project model and local persistence

### Evidence
- IndexedDB and OPFS are available browser storage mechanisms; browser quotas and eviction policies vary by browser and device: https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria
- Browser storage is best-effort by default. navigator.storage.persist() may request persistent storage, but browser approval behavior differs. Quota estimates are approximate; writes can fail with QuotaExceededError.

### Finding / recommendation
Use a versioned logical project schema independent of the storage backend. Treat IndexedDB as the transactional metadata/index candidate and evaluate OPFS for large binary audio assets; do not assume either is permanent. Implement explicit storage health, quota preflight, recoverable writes, checksums, export/backup and user-visible recovery status.

### Not measured
No schema fixture, quota measurement, crash injection, migration test, storage eviction test or import/export round trip was run.

### Required next experiment
Prototype project/track/clip/bus/asset/processor/automation records; atomically persist project revisions and asset manifests; inject reloads and interrupted writes; test migration, checksum validation, export/import and quota exhaustion.

## G1-C — Plugin format and isolation

### Evidence
- WebAssembly is designed to execute modules in a sandbox separated from the host runtime, with access mediated by embedding APIs: https://webassembly.org/docs/security/
- AudioWorklet provides a separate audio-processing execution context/thread, not a complete application security boundary: https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet

### Finding / recommendation
Evaluate a versioned, typed plugin contract with WASM DSP and a narrowly defined host capability API. Keep plugin package loading, UI, DSP execution and project persistence as separate trust boundaries. Enforce resource budgets, timeouts, bounded messages, integrity checks, crash containment and missing-plugin fallback. Do not describe AudioWorklet alone as a sandbox or assume native VST3/AU execution in mobile browsers.

### Not measured
No plugin prototype, adversarial test, CSP/origin isolation test, memory/CPU budget enforcement or crash-containment test was run.

### Required next experiment
Implement only a benign test plugin in an isolated harness. Test denied capabilities, malformed manifests, oversized messages, CPU exhaustion, invalid output, crashes, version mismatch and project recovery. Document what the platform cannot safely enforce.

## G1-D — Professional mastering and DSP

### Evidence
- ITU-R BS.1770-5 (November 2023) is the current in-force recommendation for programme loudness and true-peak measurement: https://www.itu.int/rec/R-REC-BS.1770/en
- EBU R 128 version 5.0 (November 2023) recommends -23 LUFS programme loudness for broadcast workflows and uses Loudness Range and Maximum True Peak descriptors: https://tech.ebu.ch/publications/r128

### Finding / recommendation
Base loudness/true-peak measurement conformance on the current ITU algorithm and relevant EBU technical documents. Treat EBU's -23 LUFS as a broadcast recommendation, not a universal music-mastering or streaming target. Product export profiles must make target loudness and true-peak ceilings explicit per destination/use case. The required mastering scope remains EQ (including linear-phase option), dynamics, limiter, multiband, saturation, oversampling, dither, stereo/spectrum analysis, reference A/B and deterministic offline rendering.

### Not measured
No DSP library/licence comparison, reference-signal suite, meter conformance, null/AB test, offline render determinism or mobile CPU benchmark was run.

### Required next experiment
Create golden reference signals and independently verified expected values. Compare candidate implementations for frequency response, phase, gain reduction, true-peak, loudness, dither and render determinism. Profile representative mobile devices and desktop export.

## G1-E — AI generation provider and rights

### Public-source observations
- Suno's current terms distinguish paid-tier commercial-use rights from free-tier non-commercial use; the terms also contain restrictions relevant to using its service/output to create a competing music-generation product. This is a material legal/commercial concern for a standalone DAW and requires counsel/provider clarification before any integration: https://suno.com/terms
- Stability AI's Stable Audio platform states that API-generated audio is commercially usable under its terms and advertises music, effects, ambience and loops. This is a vendor statement, not a legal review or quality benchmark: https://platform.stability.ai/
- ElevenLabs publishes plan-specific Music terms, including differences in API access, streaming distribution, download limits and permitted media use: https://elevenlabs.io/music-terms

### Finding / recommendation
Do not select a provider from marketing pages. Evaluate API-specific contracts separately from consumer subscriptions. Require written confirmation of application embedding/resale rights, commercial output rights, training/data handling, user input ownership, output provenance, voice consent, retention/deletion, regional availability, rate limits, cancellation, retries and support. Measure cost per usable output, not cost per request. Maintain provider adapters and a fallback strategy.

### Not measured
No provider account, API call, generation, quality blind test, latency test or legal review was performed. Public terms can change and may not cover negotiated API contracts.

### Required next experiment
Prepare a dated shortlist and common prompt/scorecard for vocals and instrumentals. Obtain current API terms and pricing, then conduct a small approved evaluation only after spend and data-use authorization.

## G1-F — Billing and credit ledger

### Evidence
- Cloudflare D1 batch() executes prepared statements sequentially as a transaction; a failing statement aborts/rolls back the batch: https://developers.cloudflare.com/d1/worker-api/d1-database/
- Cloudflare Queues provides at-least-once delivery by default; duplicate delivery is possible, so consumers must use stable IDs/idempotency keys: https://developers.cloudflare.com/queues/reference/delivery-guarantees/
- Cloudflare documents queue retry and dead-letter behavior; repeated failures may be discarded unless a DLQ is configured: https://developers.cloudflare.com/queues/configuration/batching-retries/

### Finding / recommendation
A future credit ledger must be authoritative server-side and auditable. Model reserve → execute → settle/refund with unique operation IDs, idempotency keys, transactional balance checks, append-only ledger entries, explicit expiry/cancellation/refund semantics and reconciliation. Queue consumers must assume duplicate and out-of-order delivery. Do not assume exactly-once execution or charge users based only on browser state.

### Not measured
No schema, transaction race test, replay/double-spend test, failure injection, cost model or billing integration was implemented.

### Required next experiment
Write a state machine and invariants, then test concurrent reservations, duplicate messages, worker retries, timeout after provider success, cancellation, partial output, refund and reconciliation using a local deterministic simulator. No live payments.

## G1-G — Security and privacy

### Evidence
- OWASP recommends layered file-upload defenses: allowlists, content validation (not trusting Content-Type), size limits, generated filenames, authorization, isolated storage and scanning/sandboxing where appropriate: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
- OWASP prompt-injection guidance states that input screening is not a security boundary and recommends enforcing tool permissions and action-specific approval outside the model: https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
- WebAssembly isolation depends on the embedding API and granted host capabilities: https://webassembly.org/docs/security/

### Finding / recommendation
Threat-model media parsers, project/tenant isolation, plugin packages, AI-generated operation plans, provider data flows, credentials, credit abuse and deletion/retention. Treat every model output, uploaded file, plugin and provider response as untrusted. Enforce authorization, cost budgets and action permissions in deterministic application code, not prompts. Keep provider secrets server-side.

### Not measured
No threat-model workshop, code review, penetration test, parser fuzzing, tenant-isolation test or privacy/legal review was run.

### Required next experiment
Create a data-flow/trust-boundary diagram, abuse cases and prioritized security test plan. Test tenant/asset access control, malicious media, plugin isolation, prompt-injection-to-tool boundaries, cost exhaustion, auditability and deletion.

## Cross-workstream architecture implications (provisional)

1. Browser-local audio processing is plausible, but sustained mobile performance and lifecycle resilience are unproven.
2. Audio assets require explicit quota, backup, export and recovery design; browser storage cannot be treated as the sole durable copy.
3. A plugin ecosystem requires a formal trust boundary and capability model; WASM is a useful primitive, not a complete product security solution.
4. Mastering measurements need reference conformance tests before product claims.
5. Provider licensing is a product architecture constraint, not a late procurement detail.
6. Asynchronous generation must be idempotent across queue redelivery and provider retries.
7. Workers should coordinate/control generation jobs, not perform long-running DSP rendering in request handlers without a separate feasibility test.

## G1 status after this pass

| Work package | Status | Reason |
|---|---|---|
| G1-A Mobile audio | Partial | Standards/docs reviewed; target-device measurements missing |
| G1-B Persistence | Partial | Storage behavior documented; schema/recovery prototype missing |
| G1-C Plugins | Partial | WASM/AudioWorklet boundaries reviewed; isolation prototype missing |
| G1-D Mastering | Partial | Standards identified; DSP conformance/performance missing |
| G1-E AI providers | Partial | Public terms reviewed; API contract, quality, latency and cost tests missing |
| G1-F Credits | Partial | Queue/transaction semantics reviewed; ledger and concurrency tests missing |
| G1-G Security | Partial | Initial control themes identified; formal threat model and tests missing |

## Sources and access date

All linked public sources were accessed on 2026-11-08. Vendor statements and public terms are not legal advice and must be rechecked before provider selection or commercial launch.
