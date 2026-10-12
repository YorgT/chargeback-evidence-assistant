#!/usr/bin/env python3
"""Read-only dispute evidence checklist prototype; no payment API calls."""
import argparse, json
from pathlib import Path

CHECKLISTS = {
    "product_not_received": ["order_confirmation", "delivery_tracking_or_access_log", "customer_communications", "refund_or_cancellation_history"],
    "duplicate": ["original_transaction_record", "both_transaction_records", "refund_or_void_record_if_any"],
    "subscription_cancelled": ["subscription_terms_at_signup", "cancellation_timestamp", "billing_history", "customer_communications"],
    "credit_not_processed": ["refund_policy", "refund_initiation_record", "customer_communications", "transaction_record"],
}

def triage(case):
    reason = str(case.get("reason", "unknown")).strip().lower()
    present = set(case.get("evidence_present", []))
    required = CHECKLISTS.get(reason, ["transaction_record", "customer_communications", "relevant_policy", "delivery_or_service_proof"])
    missing = [item for item in required if item not in present]
    return {"case_id": case.get("case_id", "unspecified"), "reason": reason, "required_evidence": required, "present": [x for x in required if x in present], "missing": missing, "status": "ready_for_human_review" if not missing else "evidence_gaps_found", "notice": "Checklist assistance only. Verify facts and applicable payment-provider rules; this tool does not decide or submit a dispute."}

def main():
    p = argparse.ArgumentParser(description="Create a dispute evidence checklist from JSON")
    p.add_argument("case_json", help="JSON file containing reason and evidence_present")
    p.add_argument("--out", help="Optional output JSON file")
    a = p.parse_args()
    result = triage(json.loads(Path(a.case_json).read_text(encoding="utf-8")))
    output = json.dumps(result, indent=2)
    if a.out: Path(a.out).write_text(output + "\n", encoding="utf-8")
    print(output)

if __name__ == "__main__": main()
