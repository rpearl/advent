from aocd import data, submit
import sys

print(len(data.split("\n")))


def nosubmit(answer, **kwargs):
    print(answer)


if len(sys.argv) < 2 or sys.argv[1] != "y":
    submit = nosubmit

# valid = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
#
# def parse(txt):
#    passport = {}
#    for field in " ".join(txt.split("\n")).split(" "):
#        k,v = field.split(':')
#        passport[k] = v
#
#    if not all(k in valid for k in passport.keys()):
#        return None
#
#    for k in valid:
#        if k not in passport and k != "cid":
#            return None
#
#    return passport
#
#
# def is_valid(passport):
#    if passport is None:
#        return False
#    return all(
#        [
#            passport["byr"].isdigit() and 1920 <= int(passport["byr"]) <= 2002,
#            passport["iyr"].isdigit() and 2010 <= int(passport["iyr"]) <= 2020,
#            passport["eyr"].isdigit() and 2020 <= int(passport["eyr"]) <= 2030,
#            passport["hgt"][:-2].isdigit()
#            and passport["hgt"][-2:] in ("cm", "in")
#            and (150 if passport["hgt"][-2:] == "cm" else 59)
#            <= int(passport["hgt"][:-2])
#            <= (193 if passport["hgt"][-2:] == "cm" else 76),
#            passport["hcl"][0] == "#"
#            and all(c in "0123456789abcdef" for c in passport["hcl"][1:])
#            and len(passport["hcl"]) == 7,
#            passport["ecl"] in "amb blu brn gry grn hzl oth".split(" "),
#            passport["pid"].isdigit() and len(passport["pid"]) == 9,
#        ]
#    )

# data = "FBFBBFFRLR\nBFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL"

tbl = str.maketrans("FBLR", "0101")

sids = [int(sid.translate(tbl), 2) for sid in data.split("\n")]


def a():
    return max(sids)


def b():
    seen = set(sids)
    for x in range(0b1111111111):
        if x not in seen and x - 1 in seen and x + 1 in seen:
            return x


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
