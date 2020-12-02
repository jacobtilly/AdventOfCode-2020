import re

f = open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day2/input.txt", "r")
input = f.read().split('\n')
validPasswords = []
for row in input:
    numbers = re.findall('\d+', row)
    first = int(numbers[0])-1
    second = int(numbers[1])-1
    text = row.split(":")
    passw = text[1].strip()
    if(passw[first] == key and passw[second] != key):
        validPasswords.append(passw)
    elif(passw[second] == key and passw[first] != key):
        validPasswords.append(passw) +1 

        print(hej)


print(len(validPasswords))