def openInput():
    return [(seatrow[:7],seatrow[7:]) for seatrow in open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day5/input.txt", "r").read().split('\n')]

def getDecimal(input):
    # input is tuple, row = input[0], column = input[1]
    rows = range(0,127)
    cols = range(0,7)
    decimal = {}
    for letter in input[0][:6]:
        rows = rows[len(rows)//2+1:] if letter == "B" else rows[:len(rows)//2]
    decimal['row'] = rows[0] if input[0][-1] == "F" else rows[0]+1

    for letter in input[1][:2]:
        cols = cols[len(cols)//2+1:] if letter == "R" else cols[:len(cols)//2]
    decimal['col'] = cols[0] if input[1][-1] == "L" else cols[0]+1

    return decimal

def getSeatID(obj):
    return (obj['row'] * 8) + obj['col']

def part1():
    return max([getSeatID(getDecimal(row)) for row in openInput()])

def part2():
    seatIDList = [getSeatID(getDecimal(row)) for row in openInput()]
    return [seat for seat in range(min(seatIDList),max(seatIDList)) if seat not in seatIDList and seat+1 in seatIDList and seat-1 in seatIDList][0]

print("Highest seat ID in airplane is",part1())
print("Empty seat where ID above and below exists is",part2())