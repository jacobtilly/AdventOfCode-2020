import time

with open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day7/input.txt", "r") as file:
    input = [line.strip() for line in file.readlines() ]

def getNumberBags(color):
    lines = [line for line in input if color in line and line.index(color) != 0]

    allDetectedColors = []

    if len(lines) == 0:
        return []
    else:
        colors = [color for color in [line[:line.index(' bags')] for line in lines] if color not in allDetectedColors ]

        for color in colors:
            allDetectedColors.append(color)
            bags = getNumberBags(color)

            allDetectedColors += bags
    
        uniqueColors = []
        for color in allDetectedColors:
            if color not in uniqueColors:
                uniqueColors.append(color)

        return uniqueColors

def getBagCount(color):
    rule = ''
    for line in input:
        if line[:line.index(' bags')] == color:
            rule = line

    rule = rule[rule.index('contain')+8:].split()

    if "no" in rule:
        return 1

    total = 0
    i = 0

    while i < len(rule):
        count = int(rule[i])
        color = rule[i+1] + " " + rule[i+2]
        total += count * getBagCount(color)
        i += 4

    return total + 1

startTime = time.time()
print("Answer for part 1:",len(getNumberBags("shiny gold")))
print("Answer for part 1:",getBagCount("shiny gold"))
print("Execution time:", time.time()-startTime)