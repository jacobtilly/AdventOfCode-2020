import re
import time

def getPassportDictionaries(stage):
    if stage == "real":
        f = open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day4/input.txt", "r")
    else:
        f = open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day4/input-test.txt", "r")
    input = f.read()
    formattedInput = input.replace(" ", '\n')
    formattedInput = input.replace("\n\n", ',')
    passports = formattedInput.split(",")
    passportList = []
    for passport in passports:
        passport = passport.replace("\n", " ")
        passportContents = passport.split(' ')
        passportDictionary = {}
        for row in passportContents:
            row = row.split(':')
            passportDictionary[row[0]] = row[1]
        passportList.append(passportDictionary)
    return passportList

def validateFields(passport,requirements):
    invalid = [field for field in requirements if (not(field in passport)) or (not(re.compile(requirements[field] if requirements[field] != '' else '^.+$').match(passport[field])))]
    return True if len(invalid) == 0 else False

def part1(): return len([passport for passport in getPassportDictionaries("real") if validateFields(passport,{'byr':'','iyr':'','eyr':'','hgt':'', 'hcl':'', 'ecl':'', 'pid':''})])

def part2():
    requirements = {
        'byr': '^[1][9][2-9][0-9]$|[2][0][0][0-2]$',
        'iyr': '^[2][0][1][0-9]$|[2][0][2][0]$',
        'eyr': '^[2][0][2][0-9]$|[2][0][3][0]$',
        'hgt': '^[1][5-8][0-9](cm)$|^[1][9][0-3](cm)$|^[5][9](in)$|^[6][0-9](in)$|^[7][0-6](in)$',
        'hcl': '^#[0-9a-f]{6}$',
        'ecl': '^(amb)$|^(blu)$|^(brn)$|^(gry)$|^(grn)$|^(hzl)$|^(oth)$',
        'pid': '^\d{9}$'
    }
    return len([passport for passport in getPassportDictionaries("real") if validateFields(passport,requirements)])

start = time.time()

print(part1())
#print(part2())

diff = time.time() - start
print("Execution Time:",diff,"seconds")