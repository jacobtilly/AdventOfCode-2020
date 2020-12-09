with open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day9/input.txt", "r") as file:
    input = [line for line in file.read().splitlines()]

summableNumbers = []
notSummableNumbers = []
preamble = 25

for i, number in enumerate(input):
    if i > preamble:
        targetList = input[i-preamble:i]
        for a in targetList:
            for b in targetList:
                if(int(number)-int(a)-int(b) == 0 and number not in summableNumbers): summableNumbers.append(number)

for i, number in enumerate(input):
    if i > preamble:
        if number not in summableNumbers: notSummableNumbers.append(number)

print(notSummableNumbers)