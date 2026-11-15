#!/usr/bin/env python3
"""Conduit fill — CEC Rule 12-910 / Tables 8, 6A, 9.
Usage: python3 conduit_fill.py "SIZE"=COUNT ["SIZE"=COUNT ...]
Example: python3 conduit_fill.py "6 AWG"=3 "12 AWG"=1
Conductor areas: RW90 XLPE 600 V. Fill limits: 1 conductor 53%, 2 -> 31%,
3 or more -> 40% of the conduit internal area.
"""
import json, os, sys

DATA = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "conduit-fill-data.json")))

def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    total_area, count = 0.0, 0
    for arg in sys.argv[1:]:
        size, _, n = arg.partition("=")
        a = DATA["conductor_areas_mm2_rw90"][size]
        total_area += a * int(n); count += int(n)
        print(f"  {n} x {size}: {a} mm2 each = {a * int(n):.2f} mm2")
    limit = 53 if count == 1 else 31 if count == 2 else 40
    print(f"Total conductor area {total_area:.2f} mm2; {count} conductors -> fill limit {limit}%")
    totals = DATA["conduit_total_internal_area_mm2_derived"]
    for ctype, sizes in totals.items():
        for sname, tot in sizes.items():
            fill = 100.0 * total_area / tot
            if fill <= limit:
                print(f"RESULT {ctype}: smallest verified size {sname} — fill {fill:.1f}% (limit {limit}%)")
                break
        else:
            print(f"RESULT {ctype}: no verified size in this tool is large enough")

if __name__ == "__main__":
    main()
