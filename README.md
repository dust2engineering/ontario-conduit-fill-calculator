# Ontario Conduit Fill Calculator (CEC Rule 12-910)

Checks conduit fill for RW90 conductors under the Canadian Electrical Code: totals conductor cross-sectional areas (Table 6A), applies the Table 8 fill limits for the conductor count, and returns the smallest conduit from the CEC Table 9-series areas for EMT, rigid PVC and ENT.

**Live web tool:** https://dust2engineering.github.io/ontario-conduit-fill-calculator/web/

## How it works

- Enter conductor sizes and counts; fill limit is 53% for 1 conductor, 31% for 2, 40% for 3 or more (Table 8, not lead-sheathed).
- Conduit usable areas are published at the 40% level; total internal areas used for the 1- and 2-conductor limits are derived from them (published value / 0.40) and labelled as derived in the data file.
- Scope: EMT limited to publicly verifiable sizes (21, 27, 41, 63 mm); PVC full range; ENT partial. Other insulation types have different conductor areas.

## Data in this repository

- `conduit-fill-data.json` — RW90 areas for 17 sizes, Table 8 limits, Table 9-series conduit areas and derived totals, from published CEC reproductions cross-checked 2026-11-15.
- `conduit_fill.py` — command-line checker using the same JSON.

## Command line

```bash
python3 conduit_fill.py "6 AWG"=3
```

## Worked examples

- [three-6awg-rw90.md](examples/three-6awg-rw90.md)
- [three-250kcmil-feeders.md](examples/three-250kcmil-feeders.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Electrical. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
