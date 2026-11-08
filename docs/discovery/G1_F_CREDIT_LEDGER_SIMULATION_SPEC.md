# G1-F — Subscription and AI Credit Ledger Simulation Specification

- Gate: G1 Discover
- Status: Deterministic simulation specification; no live billing or provider integration
- Date: 2026-11-08

## Objective

Test whether a server-authoritative subscription and usage-credit model can prevent double spending, duplicate charging and ambiguous refunds under retries and concurrent jobs.

## Core records

- Account: stable account identifier and status.
- Entitlement: plan, effective interval, limits and source.
- LedgerEntry: immutable ID, account, operation, signed amount, currency/unit, timestamp, idempotency key and reference.
- Reservation: operation ID, estimated amount, reserved amount, state and expiry.
- Job: stable job ID, provider request ID, status and result reference.
- Reconciliation: expected vs actual provider usage and discrepancy status.

The balance is derived from ledger entries; browser state is never authoritative.

## State machine

```text
CREATED -> RESERVED -> RUNNING -> SETTLED
                    -> FAILED -> REFUNDED
                    -> CANCELLED -> RELEASED/REFUNDED
                    -> UNKNOWN -> RECONCILIATION_REQUIRED
```

A timeout after provider success is UNKNOWN, not automatically FAILED. Reconciliation must query/resolve the provider outcome before releasing or charging again.

## Invariants

1. One idempotency key maps to one logical operation and one reservation.
2. Concurrent reservations cannot make available balance negative.
3. Every reserve has exactly one terminal settlement/release/refund outcome.
4. Ledger entries are append-only; corrections use compensating entries.
5. Duplicate queue deliveries do not duplicate provider work or ledger mutations.
6. A retry reuses the same logical operation identity.
7. Credits are charged against defined billable units and displayed estimate.
8. Partial success, cancellation and provider failure have explicit refund semantics.
9. Reconciliation discrepancies remain visible and auditable.
10. No client-provided balance or job status is trusted.

## Deterministic test scenarios

- Two concurrent reservations compete for insufficient balance.
- Same request submitted repeatedly with same idempotency key.
- Same request submitted with different keys.
- Duplicate and out-of-order queue deliveries.
- Worker crashes before provider call, after provider call, before settlement.
- Provider timeout with eventual success.
- Partial output and partial provider billing.
- User cancellation during queued/running phases.
- Refund replay and settlement replay.
- Expired reservation with delayed provider completion.
- Subscription entitlement changes while job is running.
- Reconciliation detects provider cost above estimate.

For every case assert final balance, ledger sequence, reservation state, provider-call count and audit trail.

## Simulation outputs

Generate deterministic scenario report and machine-readable event log. Include seeded concurrency schedule so failures reproduce exactly.

## Cloudflare implementation implications (not selected)

If Cloudflare D1 is selected later, enforce balance checks and ledger writes transactionally. Queue delivery is at-least-once; use stable job IDs and idempotent consumers. These are design constraints, not proof that a future implementation is correct.

## Not yet proven

No simulator, schema, concurrency test, unit economics model, pricing, payment processor or live billing has been implemented or selected.

## Exit decision

G1-F remains Partial until the simulator passes all scenarios and estimated AI costs are reconciled against representative approved provider usage.
