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

def calculateTrees(inputMap, rightStep, downStep):
    pointerRight = 0
    pointerDown = 0
    totalTrees = 0
    while pointerDown < len(inputMap)-1:
        pointerRight += rightStep
        pointerDown += downStep
        if(inputMap[pointerDown][0][pointerRight] == "#"):
            totalTrees += 1
    return totalTrees


# UI, the code will run from below
print("\n"*30)
print("Advent of Code")
print("Jacob Tilly, day 3")

while True:
    run = input("Type 1 or 2 for part 1 or part 2\n» ")
    print("\n")
    starttime = time.time()
    if(run == str(1)):
        inputMap = createInputMap(openInput("real"), 3, 1)
        trees = calculateTrees(inputMap, 3, 1)
        print("Total Trees for slope in input:", trees)
    elif(run == str(2)):
        slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
        inputMap = createInputMap(openInput("real"), 14, 2)
        totalTrees = 1 # init as 1 for multiplication purposes... 0*x = 0
        for slope in slopes:
            totalTrees = totalTrees * calculateTrees(inputMap, slope[0], slope[1])
        print("Total Trees in part 2:", totalTrees)
    else:
        print("Invalid choice! Please try again.")

    finishtime = time.time()
    print("Execution time:",finishtime-starttime)
    print("\n")
