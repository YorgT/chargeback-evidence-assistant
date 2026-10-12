import unittest
from evidence_assistant import triage

class TriageTests(unittest.TestCase):
    def test_missing_evidence_is_flagged(self):
        r = triage({"case_id":"x", "reason":"product_not_received", "evidence_present":["order_confirmation"]})
        self.assertEqual(r['status'], 'evidence_gaps_found')
        self.assertIn('delivery_tracking_or_access_log', r['missing'])
    def test_unknown_reason_gets_generic_checklist(self):
        r = triage({"reason":"unknown", "evidence_present":[]})
        self.assertIn('transaction_record', r['required_evidence'])

if __name__ == '__main__': unittest.main()
