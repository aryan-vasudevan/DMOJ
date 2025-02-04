n, m = [int(x) for x in input().split()]

grid = [[0 for i in range(m)] for i in range(n)]

if n == 1 and m == 1:
    print(1)
    print(1)

elif n == 1 or m == 1:
    print(2)
    i = 0
    tiling = [1, 2]
    for row in range(n):
        for column in range(m):
            grid[row][column] = tiling[i % 2]
            i += 1

    for row in grid:
        print(" ".join(str(x) for x in row))

else:
    print(4)
    i = 0
    j = 0
    tilings = [[1, 2], [3, 4]]
    for row in range(n):
        tiling = tilings[j % 2]
        for column in range(m):
            grid[row][column] = tiling[i % 2]
            i += 1
        
        j += 1

    for row in grid:
        print(" ".join(str(x) for x in row))