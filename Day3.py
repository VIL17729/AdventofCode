inputLines = open("Day3Input.txt","r").readlines()

def draw(inputString):
    x = 0
    y = 0
    erg = []
    for segment in inputString:
        i = 0
        if segment[0] == "R":
            while i<int(segment[1:]):
                x += 1
                erg.append([x,y])
                i+=1
        elif segment[0] == "L":
            while i<int(segment[1:]):
                x -= 1
                erg.append([x,y])
                i+=1
        elif segment[0] == "U":
            while i<int(segment[1:]):
                y += 1
                erg.append([x,y])
                i+=1
        elif segment[0] == "D":
            while i<int(segment[1:]):
                y -= 1
                erg.append([x,y])
                i+=1
    return erg

def part1():
    wire1 = draw(inputLines[0].split(','))
    wire2 = draw(inputLines[1].split(','))
    crossings = [point for point in wire1 if point in wire2]
    distance = [abs(x)+abs(y) for [x,y] in crossings]

    return min(distance)

print(part1())

def part2():
    wire1 = draw(inputLines[0].split(','))
    wire2 = draw(inputLines[1].split(','))
    crossings = [point for point in wire1 if point in wire2]
    distance = [wire1.index(point)+wire2.index(point) for point in crossings]

    return min(distance)+2

print(part2())