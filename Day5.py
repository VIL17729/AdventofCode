inputtext=open("Day5Input.txt","r").readline().split(',')
inputArray = []
for zahl in inputtext:
        inputArray.append(int(zahl))

def addition(value1,value2,position):
    inputArray[position] = value1 + value2

def multiplikation(value1,value2,position):
    inputArray[position] = value1 * value2

def output(position):
    print(inputArray[position])

def takeIn(position):
    inputArray[position] = int(input())

def part1():
    i=0
    
    while True:
        imediate = str(int(inputArray[i]/100))
        if inputArray[i]%100 == 99:
            return inputArray
        elif inputArray[i]%100 == 1:
            position1 = inputArray[i+1] if imediate[len(imediate)-1] == '1' else i+1
            position2 = inputArray[i+2] if imediate[len(imediate)-2] == '1' else i+2
            addition(inputArray[position1],inputArray[position2],inputArray[i+3])
            i += 4
        elif inputArray[i]%100 == 2:
            position1 = inputArray[i+1] if imediate[len(imediate)-1] == '0' else i+1
            position2 = inputArray[i+2] if imediate[len(imediate)-2] == '0' else i+2
            multiplikation(inputArray[position1],inputArray[position2],inputArray[i+3])
            i += 4
        elif inputArray[i]%100 == 3:
            position1 = inputArray[i+1] if imediate[len(imediate)-1] == '0' else i+1
            takeIn(position1)
            i += 2
        elif inputArray[i]%100 == 4:
            position1 = inputArray[i+1] if imediate[len(imediate)-1] == '0' else i+1
            output(position1)
            i += 2

part1()