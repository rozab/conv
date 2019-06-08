#!/usr/bin/env python3
# Unit conversion script
import re
from cmd import Cmd

# Base units are metres, square metres, seconds, celsius, etc. 
# mults dicts have multipliers for converting these base units to others

# multiplier to turn metres into whatever
length_mults = {
    "millimetres": 0.001,
    "centimetres": 0.01,
    "metres": 1,
    "kilometres": 1000,
    "inches": 0.0254,
    "feet": 0.3048,
    "yards": 0.9144,
    "miles": 1609.344
}

# multiplier to turn seconds into whatever
time_mults = {
    "milliseconds": 0.001,
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,
    "days": 86400,
    "weeks": 604800,
    "months": 2592000,
    "years": 31536000
}


unit_types = {
    "length": length_mults,
    "time": time_mults
}

aliases = {
    # length metric
    "mm": "millimetres",
    "millimeters": "millimetres",
    "cm": "centimetres",
    "centimeters": "centimetres",
    "m": "metres",
    "meters": "metres",
    "km": "kilometres",
    "kilometers": "kilometres",
    # length imperial
    '"': "inches",
    "inch": "inches",
    "in": "inches",
    "'": "feet",
    "foot": "feet",
    "ft": "feet",
    "yds": "yards",
    "mile": "miles",

    #time
    "ms": "milliseconds",
    "s": "seconds",
    "mins": "minutes",
    "h": "hours",
    "hrs": "hours",
    "d": "days",
    "w": "weeks",
    "y": "years",
    "yrs": "years"
}

# turn easy plurals into singular and add alias
# it adds some junk values like 'inche' but whatever
unitlist = list(aliases.keys())
for t in unit_types.values():
    for u in t.keys():
        unitlist.append(u)
for u in unitlist:
    if u[-1] == "s" and u[:-1] not in aliases:
        aliases[u[:-1]] = u

def convert(inp):
    s1, _, s2 = inp.partition(" in ")

    reg = re.compile(r"^(\d+)\s*(\S+)$")
    m = reg.match(s1)
    if not m:
        return "bad input format"
    inputvalue = float(m.group(1))
    inputunit = aliases.get(m.group(2), m.group(2))
    outputunit = aliases.get(s2, s2)

    type = "none"
    for t, mults in unit_types.items():
        if inputunit in mults.keys():
            if outputunit not in mults:
                return "units mismatch"
            type = t
            output = inputvalue * mults[inputunit] / mults[outputunit]

    if type == "none":
        return "unsupported units"
    else:
        return "{:,.2f}".format(output).rstrip('0').rstrip('.')

class Prompt(Cmd):
    prompt = "(conv) "

    def do_exit(self, inp):
        print()
        return True

    def do_help(self, inp):
        print("To convert from inches to cm:\n")
        print("    (conv) 12 inches in cm\n")
        print("or\n")
        print('    (conv) 12" in centimeters\n')
        print("or whatever you like really.\n")
        print("Available unit types:")
        print(", ".join(list(unit_types.keys())))
        print()

    def default(self, inp):
        print(convert(inp))

    do_q = do_exit
    do_EOF = do_exit

if __name__ == "__main__":
    p = Prompt()
    try:
        p.cmdloop()
    except KeyboardInterrupt:
        print("\n")
        exit()
