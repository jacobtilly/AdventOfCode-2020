import math
import time

starttime = time.time()

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

def part1(stage, rightStep, downStep):
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

trees = part1("real", 3, 1)
print("Total Trees for slope in input:", trees)

finishtime = time.time()
print("Execution time: ",finishtime-starttime, "seconds")