def getInput(filename):
        return open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day6/"+filename, "r").read().replace('\n\n',',').replace("\n"," ").split(",")

def countAnswers(input):
	totalUnique, totalAgreed = 0, 0

	for row in input:
		totalUnique += len(''.join(set(row)).replace(' ',''))
		personAnswers = row.split(' ')
		choices = 'abcdefghijklmnopqrstuvwxyz'
		for answer in personAnswers:
			choices = ''.join(set(choices).intersection(''.join(set(answer))))
		totalAgreed += len(choices)
	return totalUnique, totalAgreed

input = getInput("input.txt")

print(countAnswers(input))