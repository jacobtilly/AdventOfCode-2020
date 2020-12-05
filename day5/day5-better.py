def openInput():
    return [seatrow for seatrow in open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day5/input.txt", "r").read().split('\n')]

def getSeatID(input):
    return int(input.translate(input.maketrans("FBLR", "0101")),2)

def part1():
    return max([getSeatID(seat) for seat in openInput()])

def part2():
    slist = [getSeatID(seat) for seat in openInput()]
    return [seat for seat in range(min(slist),max(slist)) if seat not in slist and seat+1 in slist and seat-1 in slist][0]

print(part1(),part2())