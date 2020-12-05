import re
import time
import random

print("\n"*100)

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

def hexToRGB(h):
    try:
        rgbTuple = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    except:
        rgbTuple = (255,255,255)
    return rgbTuple

RESET = '\033[0m'
def hexColor(hex, background=False):
    rgb = hexToRGB(hex[1:])
    r = rgb[0]
    b = rgb[1]
    g = rgb[2]
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def part2():
    print("\n"*30)
    passportList = getPassportDictionaries("real")
    validPassports = 0
    controlledPassports = 0
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
    hair = ['/-----\\', '.^^^^^.', '.!!!!!.', '///-\\\\\\', '#######', '/~~~~~\\']
    brow = ['| _ _ |', '|^- -^|', '| ~ ~ |', '| = = |', '| - - |']
    eyes = ['     ', '[] []', ' o o ', ' O O ', ' @ @ ', ' x x ']
    nose = ['|  ^  |', '|  V  |', '|  &  |', '|  *  |', '|  v  |']
    lips = [' \ o / ', ' \ O / ', ' \ - / ', ' \ ~ / ', ' \[-]/ ']
    neck = [' | . | ', '  | |  ', ' / $ \ ', ' /^w^\ ',' {-+-} ']
    for passport in passportList:
        if "cid" in passport:
            cid = passport['cid']
        else:
            cid = ""

        eyeColor = "#ffffff"
        eyeColor = "#ffffff"

        byr = passport['byr'] if 'byr' in passport else ""
        iyr = passport['iyr'] if 'iyr' in passport else ""
        eyr = passport['eyr'] if 'eyr' in passport else ""
        hgt = passport['hgt'] if 'hgt' in passport else ""
        hcl = passport['hcl'] if 'hcl' in passport else ""
        ecl = passport['ecl'] if 'ecl' in passport else ""
        pid = passport['pid'] if 'pid' in passport else ""
        cid = passport['cid'] if 'cid' in passport else ""

        if(validateFields(passport,requirements)):
            hairColor = hcl
        else:
            hairColor = "#ffffff"

        ppEyeColor = ecl

        if ppEyeColor == 'amb':
            eyeColor = "#ffbf00"
        elif ppEyeColor == 'blu':
            eyeColor = "#85abce"
        elif ppEyeColor == 'brn':
            eyeColor = "#5e481e"
        elif ppEyeColor == 'gry':
            eyeColor = "#778899"
        elif ppEyeColor == 'grn':
            eyeColor = "#6ca580"
        elif ppEyeColor == 'hzl':
            eyeColor = "#eee8aa"
        elif ppEyeColor == 'oth':
            eyeColor = "#ffffff"
        else:
            eyeColor = "#ffffff"

        print('======================================= PASSPORT ===================================')
        print('||                                                                                ||')
        print('||                                                                                ||')
        print('||                                                                                ||')
        print('||         ----------------                                                       ||')
        print('||         |               |                Passport Number: '+pid+'            ||')
        print('||         |               |                Birth Year: '+byr+'                      ||')
        print('||         |    '+hexColor(hairColor)+hair[random.randint(0,5)]+RESET+'    |                Issue Year: '+iyr+'                      ||')
        print('||         |    '+brow[random.randint(0,4)]+'    |                Expiry Year: '+eyr+'                     ||')
        if(hgt.endswith('cm')):
            print('||         |    |'+hexColor(eyeColor)+eyes[random.randint(0,5)]+RESET+'|    |                Height: '+hgt+25*' '+'||')
        elif(hgt.endswith('in')):
            print('||         |    |'+hexColor(eyeColor)+eyes[random.randint(0,5)]+RESET+'|    |                Height: '+hgt+26*' '+'||')
        print('||         |    '+nose[random.randint(0,4)]+'    |                Hair: '+hcl+'                         ||')
        print('||         |    '+lips[random.randint(0,4)]+'    |                Eye color: '+ecl+'                        ||')
        print('||         |    '+neck[random.randint(0,4)]+'    |                Country ID: '+cid+' '*(26-len(cid))+'||')
        print('||         ----------------                                                       ||')
        print('||                                                                                ||')
        print('||                                                                                ||')
        print('||                                                                                ||')
        print('================================== STAMP BELOW =====================================')
        print('||                                                                                ||')
        controlledPassports += 1
        if checkRequiredFields(passport, requiredFields) == True and validateFields(passport,requirements) == True:
            validPassports += 1
            print('||'+hexColor("#0000FF")+'       █████  ██████  ███    ███ ██ ████████ ████████ ███████ ██████            '+RESET+'||')
            print('||'+hexColor("#0000FF")+'      ██   ██ ██   ██ ████  ████ ██    ██       ██    ██      ██   ██           '+RESET+'||')
            print('||'+hexColor("#0000FF")+'      ███████ ██   ██ ██ ████ ██ ██    ██       ██    █████   ██   ██           '+RESET+'||')
            print('||'+hexColor("#0000FF")+'      ██   ██ ██   ██ ██  ██  ██ ██    ██       ██    ██      ██   ██           '+RESET+'||')
            print('||'+hexColor("#0000FF")+'      ██   ██ ██████  ██      ██ ██    ██       ██    ███████ ██████            '+RESET+'||')
            print('||'+hexColor("#0000FF")+'                                                                                '+RESET+'||')
        else:
            print('||'+hexColor("#FF0000")+'       ██████  ███████ ███    ██ ██ ███████ ██████    ██ ██                     '+RESET+'||')
            print('||'+hexColor("#FF0000")+'       ██   ██ ██      ████   ██ ██ ██      ██   ██   ██ ██                     '+RESET+'||')
            print('||'+hexColor("#FF0000")+'       ██   ██ █████   ██ ██  ██ ██ █████   ██   ██   ██ ██                     '+RESET+'||')
            print('||'+hexColor("#FF0000")+'       ██   ██ ██      ██  ██ ██ ██ ██      ██   ██                             '+RESET+'||')
            print('||'+hexColor("#FF0000")+'       ██████  ███████ ██   ████ ██ ███████ ██████    ██ ██                     '+RESET+'||')
            print('||'+hexColor("#FF0000")+'                                                                                '+RESET+'||')
        print('====================================================================================')
        print('Total Valid Passports:',validPassports)
        print('Total Controlled Passports:',controlledPassports)
        time.sleep(0.02)
            
    return validPassports

part2()