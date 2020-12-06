def getInput(debug = ""):
    if(debug != "debug"):
        declarationFormGroups = open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day6/input.txt", "r").read().split("\n\n")
    else:
        declarationFormGroups = open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day6/input-test.txt", "r").read().split("\n\n")

    return [declarationForm.split('\n') for declarationForm in declarationFormGroups]

def getUniqueAnswers(groupAnswers):
    groupUniqueAnswers = []
    for group in groupAnswers:
        for person in group:
            for question in person:
                if question not in groupUniqueAnswers:
                    groupUniqueAnswers.append(question)
    return groupUniqueAnswers

def getNumberOfUniqueAnswers(groupUniqueAnswers):
    totalUniqueAnswers = 0
    for uniqueGroupAnswer in groupUniqueAnswers:
        totalUniqueAnswers += len(uniqueGroupAnswer)
    return totalUniqueAnswers

input = getInput("debug")

for group in input:
    print("Gruppens svar:",group)
    for person in group:
        print("Individsvar i gruppen:",person)

# print("Input:",input)