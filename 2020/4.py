# submit=True
from aocd import data
import sys
import u

valid = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


def parse(txt):
    passport = {}
    for field in " ".join(txt.split("\n")).split(" "):
        k, v = field.split(":")
        passport[k] = v

    if not all(k in valid for k in passport.keys()):
        return None

    for k in valid:
        if k not in passport and k != "cid":
            return None

    return passport


def is_valid(passport):
    if passport is None:
        return False
    return all(
        [
            passport["byr"].isdigit() and 1920 <= int(passport["byr"]) <= 2002,
            passport["iyr"].isdigit() and 2010 <= int(passport["iyr"]) <= 2020,
            passport["eyr"].isdigit() and 2020 <= int(passport["eyr"]) <= 2030,
            passport["hgt"][:-2].isdigit()
            and passport["hgt"][-2:] in ("cm", "in")
            and (150 if passport["hgt"][-2:] == "cm" else 59)
            <= int(passport["hgt"][:-2])
            <= (193 if passport["hgt"][-2:] == "cm" else 76),
            passport["hcl"][0] == "#"
            and all(c in "0123456789abcdef" for c in passport["hcl"][1:])
            and len(passport["hcl"]) == 7,
            passport["ecl"] in "amb blu brn gry grn hzl oth".split(" "),
            passport["pid"].isdigit() and len(passport["pid"]) == 9,
        ]
    )


def a():
    s = 0
    for txt in data.split("\n\n"):
        passport = parse(txt)
        if passport:
            s += 1
    return s


def b():
    s = 0
    for txt in data.split("\n\n"):
        passport = parse(txt)
        if is_valid(passport):
            s += 1
    return s


u.main(a, b, submit=globals().get("submit", False))
