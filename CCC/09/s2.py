R = int(input())
L = int(input())
grid = []

def xor(row1, row2):
    res = []
    for i in range(L):
        res.append(row1[i] ^ row2[i])
    
    return res

for i in range(R):
    row = [int(x) for x in input().split()]
    grid.append(row)

options = [[grid[0]]]

for i in range(1, R):
    curRow = grid[i]
    prevOptions = options[-1]
    newOptions = [curRow]
    
    for curOption in prevOptions:
        x = [curRow]
        newOption = xor(curOption, x[-1])
        if newOption in newOptions:
            continue
        else:
            x.append(newOption)
        newOptions += x[1:]

    print(newOptions)
    options.append(newOptions)

print(len(options[-1]))