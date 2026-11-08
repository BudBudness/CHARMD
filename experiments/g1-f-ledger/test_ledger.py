import unittest
from concurrent.futures import ThreadPoolExecutor
from ledger import Ledger, State, InsufficientCredits, IdempotencyConflict, InvalidTransition

class LedgerTests(unittest.TestCase):
    def test_reserve_settle_refund(self):
        x=Ledger(100); x.reserve("job1","k1",40); self.assertEqual(x.balance,60)
        x.settle("job1",25,"settle1"); self.assertEqual(x.balance,75)
        self.assertEqual(x.reservations["job1"].state,State.SETTLED)

    def test_duplicate_reserve_is_idempotent(self):
        x=Ledger(100); a=x.reserve("job1","k1",40); b=x.reserve("job1","k1",40)
        self.assertIs(a,b); self.assertEqual(x.balance,60); self.assertEqual(len(x.entries),2)

    def test_key_cannot_be_reused_for_other_operation(self):
        x=Ledger(100); x.reserve("job1","k1",10)
        with self.assertRaises(IdempotencyConflict): x.reserve("job2","k1",10)

    def test_concurrent_reservations_never_overdraw(self):
        x=Ledger(100)
        def attempt(i):
            try: x.reserve(f"job{i}",f"key{i}",30); return True
            except InsufficientCredits: return False
        with ThreadPoolExecutor(max_workers=12) as pool: results=list(pool.map(attempt,range(12)))
        self.assertEqual(sum(results),3); self.assertEqual(x.balance,10)

    def test_actual_over_reservation_requires_reconciliation(self):
        x=Ledger(100); x.reserve("job","k",20)
        r=x.settle("job",25,"settle"); self.assertEqual(r.state,State.RECONCILIATION_REQUIRED)
        x.reconcile("job",25,"reconcile"); self.assertEqual(x.balance,75)

    def test_failure_release_and_replay(self):
        x=Ledger(50); x.reserve("job","k",20); x.release("job","release")
        x.release("job","release"); self.assertEqual(x.balance,50)
        with self.assertRaises(InvalidTransition): x.settle("job",1,"s")

    def test_settlement_replay_must_match(self):
        x=Ledger(50); x.reserve("job","k",20); x.settle("job",12,"s")
        with self.assertRaises(IdempotencyConflict): x.settle("job",13,"s")

if __name__ == "__main__": unittest.main()
