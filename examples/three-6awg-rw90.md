# Worked example 1 — three 6 AWG RW90 conductors

3 × 37.98 mm² = 113.94 mm² of conductor. Three conductors → 40% limit.

- EMT 21 mm: total internal area 330.08 mm² (132.03 at 40%) → fill 34.5% → **passes**;
  smallest verified EMT is **21 mm (3/4 in)**.
- Rigid PVC 21 mm: 122.79 mm² at 40% < 113.94? No — 113.94 ≤ 122.79, so PVC 21 mm
  also passes at 37.1% of its 306.98 mm² total.

Command: `python3 conduit_fill.py "6 AWG"=3`
