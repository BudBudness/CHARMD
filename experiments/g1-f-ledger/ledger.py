"""Deterministic, in-memory model of a server-authoritative AI credit ledger.

This is a discovery simulator, not production billing code. It intentionally
uses a single-process lock to model atomic transactions; a real backend must
prove equivalent database transaction/uniqueness guarantees.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from threading import RLock

class State(str, Enum):
    RESERVED = "reserved"
    SETTLED = "settled"
    RELEASED = "released"
    RECONCILIATION_REQUIRED = "reconciliation_required"

@dataclass(frozen=True)
class Entry:
    entry_id: str
    operation_id: str
    kind: str
    amount: int
    idempotency_key: str

@dataclass
class Reservation:
    operation_id: str
    idempotency_key: str
    reserved: int
    state: State = State.RESERVED
    settled: int | None = None

class InsufficientCredits(Exception): pass
class IdempotencyConflict(Exception): pass
class InvalidTransition(Exception): pass

class Ledger:
    def __init__(self, opening_balance: int):
        if opening_balance < 0: raise ValueError("opening balance cannot be negative")
        self._lock = RLock()
        self.entries = [Entry("opening", "opening", "opening", opening_balance, "opening")]
        self.reservations: dict[str, Reservation] = {}
        self.keys: dict[str, str] = {}
        self._sequence = 0

    @property
    def balance(self) -> int:
        return sum(e.amount for e in self.entries)

    def _append(self, operation_id: str, kind: str, amount: int, key: str) -> None:
        self._sequence += 1
        self.entries.append(Entry(f"entry-{self._sequence}", operation_id, kind, amount, key))

    def reserve(self, operation_id: str, key: str, amount: int) -> Reservation:
        if not operation_id or not key or amount <= 0: raise ValueError("operation, key and positive amount required")
        with self._lock:
            prior = self.keys.get(key)
            if prior:
                if prior != operation_id: raise IdempotencyConflict(key)
                existing = self.reservations[prior]
                if existing.reserved != amount: raise IdempotencyConflict("amount differs on replay")
                return existing
            if amount > self.balance: raise InsufficientCredits()
            r = Reservation(operation_id, key, amount)
            self.reservations[operation_id] = r
            self.keys[key] = operation_id
            self._append(operation_id, "reserve", -amount, key)
            return r

    def settle(self, operation_id: str, actual: int, key: str) -> Reservation:
        if actual < 0: raise ValueError("actual usage cannot be negative")
        with self._lock:
            r = self.reservations[operation_id]
            if r.state == State.SETTLED:
                if r.settled != actual: raise IdempotencyConflict("settlement differs on replay")
                return r
            if r.state != State.RESERVED: raise InvalidTransition(r.state)
            # A larger actual charge cannot silently overdraw the account.
            if actual > r.reserved: 
                r.state = State.RECONCILIATION_REQUIRED
                return r
            refund = r.reserved - actual
            if refund: self._append(operation_id, "settlement_refund", refund, key)
            r.settled, r.state = actual, State.SETTLED
            return r

    def release(self, operation_id: str, key: str) -> Reservation:
        with self._lock:
            r = self.reservations[operation_id]
            if r.state == State.RELEASED: return r
            if r.state != State.RESERVED: raise InvalidTransition(r.state)
            self._append(operation_id, "release", r.reserved, key)
            r.state = State.RELEASED
            return r

    def reconcile(self, operation_id: str, actual: int, key: str) -> Reservation:
        if actual < 0: raise ValueError("actual usage cannot be negative")
        with self._lock:
            r = self.reservations[operation_id]
            if r.state != State.RECONCILIATION_REQUIRED: raise InvalidTransition(r.state)
            # Explicitly debit any overage only if available credits cover it.
            extra = actual - r.reserved
            if extra > self.balance: raise InsufficientCredits("overage needs manual resolution")
            if extra > 0: self._append(operation_id, "reconciled_overage", -extra, key)
            elif extra < 0: self._append(operation_id, "reconciliation_refund", -extra, key)
            r.settled, r.state = actual, State.SETTLED
            return r

    def audit(self) -> list[dict]:
        return [e.__dict__.copy() for e in self.entries]
