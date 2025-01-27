def generateAlleles(parent1, parent2):
    possibleAlleles = set()
    for allele1 in parent1:
        for allele2 in parent2:
            possibleAlleles.add(''.join(sorted(allele1 + allele2)))
    return possibleAlleles

def isPossibleBaby(mother, father, baby):
    for i in range(len(baby)):
        possibleAlleles = generateAlleles(mother[i], father[i])
        if baby[i] not in possibleAlleles:
            return False
    return True

mother = input()
father = input()
x = int(input())

babies = [input() for _ in range(x)]

motherAlleles = [mother[i:i+2] for i in range(0, len(mother), 2)]
fatherAlleles = [father[i:i+2] for i in range(0, len(father), 2)]

for baby in babies:
    babyAlleles = [baby[i] for i in range(len(baby))]
    if isPossibleBaby(motherAlleles, fatherAlleles, babyAlleles):
        print("Possible baby.")
    else:
        print("Not their baby!")