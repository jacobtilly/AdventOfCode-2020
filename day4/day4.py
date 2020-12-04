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

def checkRequiredFields(passport: dict, requiredFields: list):
    valid = True
    for field in requiredFields:
        if not field in passport: valid = False
    return valid

def validateFields(passport,requirements):
    valid = True
    for field in passport:
        if field in requirements:
            regexRequirement = re.compile(requirements[field])
            if not regexRequirement.match(passport[field]): valid = False
    return valid

def part1():
    passportList = getPassportDictionaries("real")
    validPassports = 0
    for passport in passportList:
        requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
        if checkRequiredFields(passport, requiredFields) == True:
            validPassports += 1
    return validPassports

def part2():
    passportList = getPassportDictionaries("real")
    validPassports = 0
    requirements = {
        'byr': '^[1][9][2-9][0-9]$|[2][0][0][0-2]$',
        'iyr': '^[2][0][1][0-9]$|[2][0][2][0]$',
        'eyr': '^[2][0][2][0-9]$|[2][0][3][0]$',
        'hgt': '^[1][5-8][0-9](cm)$|^[1][9][0-3](cm)$|^[5][9](in)$|^[6][0-9](in)$|^[7][0-6](in)$',
        'hcl': '^#[0-9a-f]{6}$',
        'ecl': '^(amb)$|^(blu)$|^(brn)$|^(gry)$|^(grn)$|^(hzl)$|^(oth)$',
        'pid': '^\d{9}$'
    }
    requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for passport in passportList:
        if checkRequiredFields(passport, requiredFields) == True and validateFields(passport,requirements) == True:
            validPassports += 1
    return validPassports

start = time.time()

#print(part1())
print(part2())

diff = time.time() - start
print("Execution Time:",diff,"seconds")