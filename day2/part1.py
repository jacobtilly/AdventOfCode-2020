import re

f = open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day2/input.txt", "r")
input = f.read().split('\n')
validPasswords = []
for row in input:
    # format: x-y z: pass
    # z needs to appear in pass more than x times and less than y times
    # if z.count > x AND z.count < Y - add to valid passwords
    numbers = re.findall('\d+', row)
    min = int(numbers[0])
    max = int(numbers[1])
    text = row.split(":")
    passw = text[1].strip()
    key = text[0].strip()[-1]
    count = passw.count(key)
    if(count >= min and count <= max): validPasswords.append(passw)

print(len(validPasswords))