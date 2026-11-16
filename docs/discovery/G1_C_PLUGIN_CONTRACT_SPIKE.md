# G1-C — Browser Plugin Contract and Isolation Spike

- Gate: G1 Discover
- Status: Contract proposal; no plugin code executed
- Date: 2026-11-08

## Objective

Specify the smallest safe browser-native plugin boundary to test. This is not approval to execute arbitrary third-party plugins or a commitment to a final runtime.

## Candidate package manifest

```json
{
  "manifestVersion": 1,
  "pluginId": "com.example.gain",
  "version": "1.0.0",
  "name": "Gain",
  "kind": "audio-effect",
  "entry": "plugin.wasm",
  "audio": {
    "inputs": 2,
    "outputs": 2,
    "supportedSampleRates": [44100, 48000],
    "maximumBlockFrames": 2048,
    "reportedLatencyFrames": 0
  },
  "parameters": [{
    "id": "gain",
    "type": "float",
    "default": 1,
    "min": 0,
    "max": 2,
    "unit": "linear",
    "automatable": true
  }],
  "stateVersion": 1,
  "capabilities": []
}
```

The schema is illustrative and requires validation before adoption. Reject unknown required capabilities and malformed or out-of-range parameter values.

## Proposed processing contract

- Fixed, explicit audio channel layout and sample-rate negotiation.
- Bounded block size and bounded input/output memory.
- No network, filesystem, credential, DOM, project database or arbitrary host access from DSP code.
- Host passes audio buffers and typed parameter snapshots through a narrow ABI.
- Plugin cannot choose arbitrary memory addresses outside its linear memory.
- Parameter automation is timestamped and deterministic at block boundaries.
- State serialization is versioned, bounded and validated by the host.
- Invalid output, trap, timeout or budget violation results in bypass/silence policy defined by host; project state remains intact.

## Trust boundaries

1. Package intake: untrusted archive/manifest; validate size, paths, hashes and schema.
2. Plugin UI: separate origin/context from privileged application state.
3. DSP runtime: WASM module with no ambient imports; explicit host ABI only.
4. Audio scheduler: enforce bounded work; never allow plugin work to block UI.
5. State persistence: host validates and stores bounded serialized state.
6. Updates: version pinning, integrity verification, compatibility and rollback.

AudioWorklet is an execution context, not a complete security sandbox. WASM safety depends on imports and host capabilities. Browser resource limits and hard real-time guarantees are not assumed.

## Benign prototype test matrix

- Identity/gain DSP correctness against known vectors.
- Manifest missing fields, unknown versions, invalid ranges and duplicate IDs.
- Oversized module, state blob, parameter payload and message.
- NaN/Infinity output, malformed buffer lengths and channel mismatch.
- Infinite loop / excessive instruction budget and memory growth.
- Traps and invalid state restoration.
- Unsupported sample rate/block size.
- Plugin version unavailable on project load.
- Attempted network, DOM, filesystem and host API access must fail by construction.

## Required evidence

Record exact browser/OS, module hash, runtime, sample rate, block size, execution time distribution, memory ceiling, failure mode and recovery. Include adversarial test outcomes; a passing benign DSP test is not evidence of isolation.

## Alternatives

- First-party fixed DSP nodes only: smallest attack surface, least ecosystem flexibility.
- WASM with narrow host ABI: broadest plausible portable ecosystem, but requires rigorous capability and resource controls.
- JavaScript plugin modules: simpler authoring, weaker isolation and more difficult resource containment.

## Reversal conditions

If mobile browser resource control or crash containment cannot be demonstrated, restrict launch to first-party DSP nodes and defer third-party executable plugins while preserving the plugin ecosystem as a product requirement.

## Exit decision

G1-C remains Partial. No claim of secure plugin sandbox or third-party plugin compatibility is made.
