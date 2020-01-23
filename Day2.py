import array as arr

inputtext=open("Day2Input.txt","r").readline()
inputarraystring=inputtext.split(',')

def reset(inputarray):
    inputarray = arr.array('l',[])
    for zahl in inputarraystring:
        inputarray.append(int(zahl))
    return inputarray

def addition(pos, inputarray):
    pos1 = inputarray[inputarray[pos+1]]
    pos2 = inputarray[inputarray[pos+2]]
    inputarray[inputarray[pos+3]] = pos1+pos2

def multiplikation(pos, inputarray):
    pos1 = inputarray[inputarray[pos+1]]
    pos2 = inputarray[inputarray[pos+2]]
    inputarray[inputarray[pos+3]] = pos1*pos2

def mathThing(arrayThing):
    i=0
    erg = arrayThing
    while i<len(arrayThing):
        if arrayThing[i] == 99:
            return erg
        if arrayThing[i] == 1:
            addition(i, arrayThing)
        if arrayThing[i] == 2:
            multiplikation(i, arrayThing)
        i=i+4
    return erg

def part1(inputarray):
    inputarray = reset(inputarray)
    inputarray[1] = 12
    inputarray[2] = 2
    return mathThing(inputarray)

print(part1(arr.array('l',[]))[0])

def part2(inputarray):
    inputarray = reset(inputarray)
    for noun in range(100):
        for verb in range(100):
            inputarray = reset(inputarray)
            inputarray[1] = noun
            inputarray[2] = verb
            inputarray = mathThing(inputarray)
            if inputarray[0]==19690720:
                return 100*noun+verb
    return 'f'


print(part2(arr.array('l',[])))