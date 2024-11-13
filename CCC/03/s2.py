N = int(input())

def getLastSyllable(word):
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(word)):
        if word[::-1][i] in vowels:
            return (word[::-1][:i + 1])[::-1]
        
    return word

res = []
for i in range(N):
    lastSyllables = []

    for j in range(4):
        line = input().lower().split()
        lastSyllables.append(getLastSyllable(line[-1]))
    
    perfect = True
    for i in range(len(lastSyllables)):
        if lastSyllables[i] != lastSyllables[i - 1]:
            perfect = False
            break

    if perfect:
        res.append("perfect")
    elif lastSyllables[0] == lastSyllables[1] and lastSyllables[2] == lastSyllables[3]:
        res.append("even")
    elif lastSyllables[0] == lastSyllables[2] and lastSyllables[1] == lastSyllables[3]:
        res.append("cross")
    elif lastSyllables[1] == lastSyllables[2] and lastSyllables[0] == lastSyllables[3]:
        res.append("shell")
    else:
        res.append("free")

for rhyme in res:
    print(rhyme)