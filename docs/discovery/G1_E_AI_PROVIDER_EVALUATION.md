# G1-E — AI Generation Provider Evaluation Protocol

- Gate: G1 Discover
- Status: Evaluation protocol; no provider selected and no API calls made
- Date: 2026-11-08

## Product requirements

Evaluate providers for both generated vocals and instrumentals. The product remains provider-agnostic; consumer subscription terms must not be assumed to grant API embedding, resale or competing-product rights.

## Provider scorecard

Score each provider independently for:
1. Vocal generation quality, intelligibility, phrasing, musicality and controllability.
2. Instrumental generation quality, arrangement, structure and genre coverage.
3. Stem separation/export, duration, format, sample rate and channel support.
4. Prompt adherence, editability, regeneration and consistency.
5. API access, commercial embedding/resale rights and output rights.
6. Input/output retention, training use, deletion and data residency.
7. Voice identity, consent, impersonation restrictions and provenance.
8. Latency, rate limits, cancellation, retries, idempotency and uptime.
9. Price per request and cost per usable output, including failed generations.
10. Contract stability, support, regional availability and fallback options.

## Reproducible quality protocol

- Create a fixed prompt set for vocals and instrumentals, covering diverse genres and production requirements.
- Use identical prompt intent, duration and output settings across providers where possible.
- Record model/version, API date, request parameters, latency, errors, output metadata and full cost.
- Have reviewers score anonymized outputs using a predeclared rubric.
- Separate objective checks (format, duration, clipping, silence, sample rate, channel count) from subjective listening scores.
- Repeat prompts to estimate output variance and failure rate.
- Do not upload private or third-party audio without explicit authorization and documented rights.

## Legal and commercial review checklist

Obtain the exact API contract and written clarification on:
- Commercial use and embedding inside a paid DAW.
- Resale/sublicensing and whether users may commercially exploit outputs.
- Whether the provider restricts competing products or model training.
- Ownership/licensing of prompts, uploaded audio, generated outputs and stems.
- Training use, retention, deletion and subprocessors.
- Voice cloning/identity consent, prohibited use and takedown handling.
- Attribution, indemnity, warranty, liability and termination effects.
- Geographic availability and applicable law.

Consumer plan terms are not substitutes for API terms. Public marketing claims are not legal conclusions.

## Cost model

For each workflow calculate:
- Cost per attempt.
- Success probability.
- Usable-output probability.
- Expected retries.
- Cost per accepted output.
- Queue/storage/transcoding overhead.
- Credit reserve and refund exposure.
- Gross margin under proposed subscription and credit pricing.

Do not offer unlimited generation until cost distribution and abuse exposure are measured.

## Candidate set

Initial research may include Stability AI, ElevenLabs and other providers with documented music/vocal APIs. Suno's public terms contain restrictions that may be incompatible with integrating its service into a competing standalone music-generation product; treat as a legal blocker pending written clarification, not as an approved provider.

Reference starting points (recheck current versions before evaluation):
- https://platform.stability.ai/
- https://elevenlabs.io/music-terms
- https://suno.com/terms

## Authorization boundary

No provider accounts, paid plans, API keys, API calls, generations, private-audio uploads or acceptance of terms are authorized by this protocol. Proceed to a measured evaluation only after the provider, budget and data handling are approved.

## Exit decision

G1-E remains Partial until dated API-specific terms, rights review, quality results, latency/cost measurements and a documented provider decision are available.
