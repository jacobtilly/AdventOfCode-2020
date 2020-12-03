import math
import time

def openInput(stage):
    if stage == "real":
        f = open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day3/input.txt", "r")
        input = f.read().split('\n')
        return input
    else:
        inputString = """..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#"""
        inputString = inputString.replace(" ", "")
        inputString = inputString.replace("   ", "")
        input = inputString.split('\n')
        return input

def createInputMap(input, rightStep, downStep):
    inputMap = []
    currentrow = 0
    multiple = math.ceil(float(rightStep * (len(input) // downStep))/float(len(input[0])))
    for row in input:
        inputMap.append([])
        inputMap[currentrow].append(row*multiple)
        currentrow += 1
    return inputMap

def calculateTrees(stage, rightStep, downStep):
    if stage == "real":
        input = openInput("real")
    else:
        input = openInput("test")

    input = createInputMap(input, rightStep, downStep)

    pointerRight = 0
    pointerDown = 0
    totalTrees = 0

    while pointerDown < len(input)-1:
        pointerRight += rightStep
        pointerDown += downStep
        if(input[pointerDown][0][pointerRight] == "#"):
            totalTrees += 1
    
    return totalTrees

print("\n"*30)
print("Advent of Code")
print("Jacob Tilly, day 3")

while True:
    run = input("Type 1 or 2 for part 1 or part 2\n» ")
    print("\n")
    starttime = time.time()
    if(run == str(1)):
        trees = calculateTrees("real", 3, 1)
        print("Total Trees for slope in input:", trees)
    elif(run == str(2)):
        #trees = part2("real")
        totalTrees = calculateTrees("real", 1, 1) * calculateTrees("real", 3, 1) * calculateTrees("real", 5, 1) * calculateTrees("real", 7, 1) * calculateTrees("real", 1, 2)
        print("Total Trees in part 2:", totalTrees)
    else:
        print("Invalid choice! Please try again.")

    finishtime = time.time()
    print("Execution time:",finishtime-starttime)
    print("\n")
