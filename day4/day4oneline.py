import re, time

def validateFields(passport,requirements):
    return True if len([field for field in requirements if (not(field in passport)) or (not(re.compile(requirements[field] if requirements[field] != '' else '^.+$').match(passport[field])))]) == 0 else False

def part1(): return len([passport for passport in [{row.split(':')[0] : row.split(':')[1] for row in passport.replace("\n", " ").split(' ')} for passport in open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day4/input.txt", "r").read().replace(" ", '\n').split("\n\n")] if validateFields(passport,{'byr':'','iyr':'','eyr':'','hgt':'', 'hcl':'', 'ecl':'', 'pid':''})])

def part2():
    return len([passport for passport in [{row.split(':')[0] : row.split(':')[1] for row in passport.replace("\n", " ").split(' ')} for passport in open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day4/input.txt", "r").read().replace(" ", '\n').split("\n\n")] if validateFields(passport,{'byr': '^[1][9][2-9][0-9]$|[2][0][0][0-2]$','iyr': '^[2][0][1][0-9]$|[2][0][2][0]$','eyr': '^[2][0][2][0-9]$|[2][0][3][0]$','hgt': '^[1][5-8][0-9](cm)$|^[1][9][0-3](cm)$|^[5][9](in)$|^[6][0-9](in)$|^[7][0-6](in)$','hcl': '^#[0-9a-f]{6}$','ecl': '^(amb)$|^(blu)$|^(brn)$|^(gry)$|^(grn)$|^(hzl)$|^(oth)$','pid': '^\d{9}$'})])

print("Valid passports according to part 1 rules:",part1())

print("Valid passports according to part 2 rules:",part2())