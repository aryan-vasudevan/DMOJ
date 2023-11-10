case = input()

length = 2 * int(case)
numOfRows = int(case)

def genRow(numOfStars):
    res = ""
    for n in range(1, length + 1):
        if n <= numOfStars or n > length - numOfStars:
            char = "*"
        else:
            char = " "
        
        res += char

    return res

firstHalf = []

for n in range(1, int(case) + 1):
    if 2 * n - 1 <= length / 2:
        numOfStars = 2 * n - 1
        firstHalf.append(numOfStars)
    else:
        numOfStars = firstHalf[numOfRows // 2 - n] # Repeat the first half of the rows in reverse for the second half

    print(genRow(numOfStars))