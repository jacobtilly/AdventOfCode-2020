def openInput():
    return [seatrow for seatrow in open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day5/input.txt", "r").read().split('\n')]

def getSeatID(input):
    input = input.translate(input.maketrans("FBLR", "0101"))
    return int(input,2)

def part1():
    return max([getSeatID(seat) for seat in openInput()])

def part2():
    seatIDList = [getSeatID(seat) for seat in openInput()]
    return [seat for seat in range(min(seatIDList),max(seatIDList)) if seat not in seatIDList and seat+1 in seatIDList and seat-1 in seatIDList][0]
print(part1(),part2())