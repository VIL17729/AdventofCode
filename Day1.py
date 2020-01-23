inputtext=open("Day1Input.txt","r").readlines()
def mathThing(x):
    zerg = int(int(x)/3)
    zerg = zerg-2
    return zerg

def part1():
    erg=0
    for x in inputtext:
        erg = erg + mathThing(x)
    print(erg)
part1()
def part2():
    erg=0
    for x in inputtext:
        zerg=mathThing(x)
        while zerg>0:
            erg = erg+zerg
            zerg=mathThing(zerg)
    print(erg)
part2()