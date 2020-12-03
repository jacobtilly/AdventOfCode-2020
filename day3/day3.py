import math

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
    # goal: to have the map look like map[vertical][horizontal], i.e. map is array of arrays containing horizontal chars
    # python – string can automatically be used as "array" (i think...)
    # the map need to continue enough to the right for all the steps. If right step is 3 and down is 1, the pointer will move 3 steps
    # right for every step to the right, i.e. the map needs to be 3*(rows) wide
    inputWidth = len(input[0])
    inputHeight = len(input)
    countHeight = inputHeight // downStep
    requiredWidth = rightStep * countHeight
    multiple = math.ceil(float(requiredWidth)/float(inputWidth))
    currentrow = 0
    for row in input:
        inputMap.append([])
        inputMap[currentrow].append(row*multiple)
        currentrow += 1
    return inputMap

def part1(stage, rightStep, downStep):
    # get the input
    if stage == "real":
        input = openInput("real")
    else:
        input = openInput("test")

    # convert input to a map
    input = createInputMap(input, rightStep, downStep)

    # start looping through map
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