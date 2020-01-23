inputLines = open("Day4Input.txt","r").readline().split('-')
beginning = int(inputLines[0])
end = int(inputLines[1])

def isPasswordPart1(password):
    strPassword = str(password)
    hasDoubles = False
    position = 0
    previous = 0
    while position<len(strPassword):
        if previous>int(strPassword[position]):
            return False
        previous=int(strPassword[position])
        position+=1

    for digit in strPassword:
        count = strPassword.count(digit)
        if count == 2:
            hasDoubles = True

    if hasDoubles:
        return True
    return False


def part1():
    start = beginning
    possibiliyties = 0
    while start<=end:
        if isPasswordPart1(start):
            possibiliyties+=1
        start+=1
    return possibiliyties

print(part1())

def isPasswordPart2(password):
    strPassword = str(password)
    hasDoubles = False
    position = 0
    previous = -1
    while position<len(strPassword):
        if previous>int(strPassword[position]):
            return False
        previous=int(strPassword[position])
        position+=1
    
    for digit in strPassword:
        count = strPassword.count(digit)
        if count == 2:
            hasDoubles = True

    if hasDoubles:
        return True
    return False

def part2():
    start = beginning
    possibiliyties = 0
    while start<=end:
        if isPasswordPart2(start):
            possibiliyties+=1
        start+=1
    return possibiliyties

print(part2())