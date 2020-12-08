with open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day8/input.txt", "r") as file:
    input = [{"operation":line.strip().split(" ")[0],"argument":line.strip().split(" ")[1]} for line in file.readlines() ]

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
        return
    elif(operation == "jmp"):
        allVisitedInstructions.append(instructionId)
        calculateAccumulator(instructionId+argument,accumulator)
        return
    elif(operation == "acc"):
        allVisitedInstructions.append(instructionId)
        accumulator += argument
        calculateAccumulator(instructionId+1,accumulator)
        return

calculateAccumulator(0,0)

allVisitedInstructions = []

def checkForCorruptLine(instructionId,accumulator):
    # print("Received task to check the following list:",input)
    # listan är inte korrupt om instructionId är utanför listan. (>= eftersom indexet utgår från 0 men listans längd utgår från 1)
    if instructionId >= len(input):
        print("Tried to call outside list, meaning file not corrupt.")
        print("Current accumulator value:",accumulator)
        return False
    operation = input[instructionId]["operation"]
    argument = int(input[instructionId]["argument"])
    # print("Currently accumulator is",accumulator,". Current instruction ID is",instructionId,". Current instruction reads",input[instructionId]["operation"]+input[instructionId]["argument"])
    if(instructionId in allVisitedInstructions):
        return True # listan är korrupt om den bildar en loop
    if(operation == "nop"):
        allVisitedInstructions.append(instructionId)
        checkForCorruptLine(instructionId+1,accumulator)
        return
    elif(operation == "jmp"):
        allVisitedInstructions.append(instructionId)
        checkForCorruptLine(instructionId+argument,accumulator)
        return
    elif(operation == "acc"):
        allVisitedInstructions.append(instructionId)
        accumulator += argument
        checkForCorruptLine(instructionId+1,accumulator)
        return
    return False

def getAllPossibleCorruptionLines(input):
    possiblyCorruptedInstructionLines = []
    possiblyCorruptedOperations = ["nop", "jmp"]
    i = 0
    for instruction in input:
        if(instruction["operation"] in possiblyCorruptedOperations):
            possiblyCorruptedInstructionLines.append(i)
        i += 1
    return possiblyCorruptedInstructionLines

# Plan för del 2
# Gå igenom inputlistan. Byt ut första jmp->nop eller nop->jump. Testa om filen är korrupt. Om inte, ändra tillbaka, gå igenom igen och ändra nästa jump/nop. osv

# listan possibleCorruptions innehåller ID för alla instruktioner som skulle kunna vara korrupta, dvs för alla som ska testa att bytas (och anropa checkForCorruption)
possibleCorruptions = getAllPossibleCorruptionLines(input)

for line in possibleCorruptions:
    if input[line]["operation"] == "nop":
        input[line]["operation"] = "jmp"
    elif input[line]["operation"] == "jmp":
        input[line]["operation"] = "nop"

    allVisitedInstructions = []
    if checkForCorruptLine(0,0) == False:
        print("Change instruction with id",line,"for normal function!")
    else:
        if input[line]["operation"] == "nop":
            input[line]["operation"] = "jmp"
        elif input[line]["operation"] == "jmp":
            input[line]["operation"] = "nop"