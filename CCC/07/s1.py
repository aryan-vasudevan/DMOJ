numOfFriends = int(input())

pairs = {}

for i in range(numOfFriends):
    pair = input()
    pair = pair.split()
    pairs[int(pair[0])] = int(pair[1])

checkPairs = {}
done = False
while not done:
    pair = input()
    if pair != "0 0":
        pair = pair.split()
        checkPairs[int(pair[0])] = int(pair[1])
    else:
        done = True


for n in checkPairs:
    seen = {}
    print("n = ", n)
    def findLoop(number):
        print(number)
        
            
        if pairs[number] in pairs:
            if number in seen:
                if number == checkPairs[n]:
                    print("Yes")
                    return 0
                else:
                    print("No")
                    return 0
            else:
                seen[number] = 1
            newNumber = pairs[number]
            findLoop(newNumber)
        else:
            print("No")
            return 0
    findLoop(n)