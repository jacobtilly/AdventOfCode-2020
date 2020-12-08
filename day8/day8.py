with open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day8/input.txt", "r") as file:
    input = [{"operation":line.strip().split(" ")[0],"argument":line.strip().split(" ")[1]} for line in file.readlines() ]

pointer = 0
allVisitedInstructions = []

def calculateAccumulator(instructionId,accumulator):
    operation = input[instructionId]["operation"]
    argument = int(input[instructionId]["argument"])
    # print("Currently accumulator is",accumulator,". Current instruction ID is",instructionId,". Current instruction reads",input[instructionId]["operation"]+input[instructionId]["argument"])
    if(instructionId in allVisitedInstructions):
        print("Loop detected. Value of accumulator is",accumulator)
        return
    if(operation == "nop"):
        allVisitedInstructions.append(instructionId)
        calculateAccumulator(instructionId+1,accumulator)
    elif(operation == "jmp"):
        allVisitedInstructions.append(instructionId)
        calculateAccumulator(instructionId+argument,accumulator)
    elif(operation == "acc"):
        allVisitedInstructions.append(instructionId)
        accumulator += argument
        calculateAccumulator(instructionId+1,accumulator)

calculateAccumulator(0,0)