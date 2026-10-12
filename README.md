# Chargeback Evidence Assistant

A merchant-focused helper for organizing payment-dispute evidence, spotting missing items, and preparing a reviewable draft response.

## MVP goal

Start with user-provided sample case data and a deterministic evidence checklist. The app must never submit disputes, move money, or make a final decision automatically.

## Initial scope

- Load a simple JSON case format and example fixtures.
- Map a dispute reason to a checklist of relevant evidence.
- Mark evidence as present, missing, or needs human review.
- Produce an editable draft summary with source facts clearly separated from suggestions.
- Export a case packet for human review.

## Open-source foundation and attribution

Research/reference project: [opensyndicate/dispute-agent](https://github.com/opensyndicate/dispute-agent), which describes an MIT-licensed, read-only dispute triage library. This repository is a separate MVP scaffold and does **not** currently contain copied upstream source. Before importing any code, verify the current upstream `LICENSE`, preserve its copyright/license notices, and document modifications and dependency licenses.

## Status and safety

Early prototype scaffold; not legal, financial, or payment-network advice. All evidence and draft responses require human verification. Do not upload real customer payment data until privacy, security, and retention controls are implemented.

## Roadmap

1. Document a case JSON schema.
2. Build deterministic evidence-gap rules and tests.
3. Add a simple review screen and export.
4. Validate on synthetic cases before any gateway integration.

## License

Original code in this repository is licensed under the MIT License. Third-party components retain their own licenses and notices. See `LICENSE`.