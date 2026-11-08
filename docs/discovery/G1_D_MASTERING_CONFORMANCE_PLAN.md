# G1-D — Professional Mastering and DSP Conformance Plan

- Gate: G1 Discover
- Status: Test plan; no DSP implementation or conformance test run
- Date: 2026-11-08

## Required product capability

The standalone DAW scope includes a full professional mastering suite. This plan tests feasibility and measurable quality; it does not reduce the required scope.

## Processing and measurement inventory

- Parametric EQ, shelves and optional linear-phase EQ.
- Broadband compressor, limiter and multiband dynamics.
- Integrated and short-term loudness; true-peak.
- Spectrum, stereo balance, width and correlation.
- Saturation/harmonic processing, clipping detection/control.
- Oversampling and dither.
- Level-matched reference A/B.
- Non-destructive recallable chains and reproducible offline export.

## Reference standards

Use ITU-R BS.1770-5 as the loudness/true-peak measurement reference and relevant EBU documents for broadcast-specific profiles. Broadcast -23 LUFS is not a universal music-mastering target. Export targets must be explicit per profile.

References:
- https://www.itu.int/rec/R-REC-BS.1770/en
- https://tech.ebu.ch/publications/r128

## Golden signal suite

1. Digital silence and near-silence.
2. 1 kHz sine at calibrated levels.
3. Full-scale and inter-sample peak stress signals.
4. Log sweep and stepped-frequency multitone.
5. Impulse and step response.
6. Left-only, right-only, dual-mono and anti-phase stereo.
7. Known RMS/peak crest-factor signals.
8. Program-like test excerpts with independently computed reference loudness.
9. Dither/noise-floor test signals.

Every fixture must record sample rate, channel layout, sample format, exact generation method and SHA-256.

## Required assertions

- EQ magnitude response within documented tolerance; phase behavior recorded.
- Compressor/limiter gain reduction and attack/release response match test vectors.
- Loudness and true-peak readings compared against an independent reference implementation and tolerance documented per fixture.
- Stereo correlation and channel balance match known signals.
- Oversampling reduces aliasing under defined nonlinear test conditions.
- Dither statistical properties and output bit depth verified.
- Offline rendering is deterministic for identical project, plugin versions, seed and render settings.
- Reference A/B level matching prevents loudness bias.
- Export metadata, clipping report and profile target are reproducible.

## Performance matrix

Measure 44.1/48 kHz, mono/stereo, multiple buffer sizes, track counts and mastering-chain combinations on low/mid/high Android devices plus desktop. Record wall time, peak memory, thermal/power observations and output hash. Mobile playback feasibility and offline export feasibility are separate decisions.

## Licensing and implementation selection

For each candidate DSP library: record version, licence, patent/third-party notices, SIMD/WASM support, determinism, precision, test coverage, maintenance activity and mobile performance. No dependency is approved by this plan.

## Listening protocol

Use level-matched blind comparisons, randomized order and documented playback chain. Separate technical measurement from subjective preference. Preserve source and rendered files with hashes.

## Not yet proven

No mastering algorithm, meter, library, conformance tolerance, mobile performance or export determinism is validated.

## Exit decision

G1-D remains Partial until golden-signal fixtures, independent reference comparisons, reproducible renders, licensing review and performance results are attached.
