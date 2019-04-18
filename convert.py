#!/usr/bin/env python3
# Unit conversion script
# internal unit is meters
import sys
import re

# TODO:
# - change output precision based on input precision
# - support 6'1" format

# The multiplier to turn meters into whatever
mults = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inches": 0.0254,
    "feet": 0.3048,
    "miles": 1609.344
    }

aliases = {
    '"': "inches",
    "'": "feet",
    }



def main():
    s1, _, s2 = " ".join(sys.argv[1:]).partition(" in ")

    reg = re.compile(r"^(\d+)\s*(\S+)$")
    m = reg.match(s1)
    if not m:
        print("couldn't match")
        sys.exit(2)
    inputvalue = float(m.group(1))
    inputunit = aliases.get(m.group(2), m.group(2))
    if inputunit not in mults or s2 not in mults:
        print("unsupported units")
        sys.exit(2)
    output = inputvalue * mults[inputunit] / mults[s2]
    print("{:,.2f}".format(output).rstrip('0').rstrip('.'))

if __name__ == '__main__':
    main()
