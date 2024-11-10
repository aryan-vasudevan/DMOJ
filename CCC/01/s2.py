def getPath(start, stop):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    opposites = {
        (0, 1): (0, -1),
        (1, 0): (-1, 0),
        (0, -1): (0, 1),
        (-1, 0): (1, 0)
    }

    path = []
    steps = stop - start + 1
    totalTerms = 0

    current = 0
    multiplier = 1
    sizes = [1, 1]
    counter = 0

    while totalTerms < steps:
        path += [directions[current]] * multiplier
        totalTerms += multiplier

        current = (current + 1) % 4
        counter += 1

        if not counter % 2:
            counter = 0
            multiplier += 1
        
        sizes.append(multiplier)
    
    if directions[current] == (0, -1) or directions[current] == (0, 1):
        dimensions = [sizes[-2], sizes[-1]]
    else:
        dimensions = [sizes[-1], sizes[-2]]
    
    # Path
    path.pop()

    for i in range(len(path)):
        path[i] = opposites[path[i]]

    path.reverse()

    extraSteps = len(path) - steps + 1

    # Start pos
    if len(path) == 0 or path[0] == (1, 0):
        x, y = 0, 0
    elif path[0] == (0, -1):
        x, y = 0, dimensions[1] - 1
    elif path[0] == (0, 1):
        x, y = dimensions[0] - 1, 0
    else:
        x, y = dimensions[0] - 1, dimensions[1] - 1

    return path, extraSteps, dimensions, x, y

def getMaxInCol(grid, column):
    max = 0
    for row in grid:
        if len(str(row[column])) > max:
            max = len(str(row[column]))
    
    return max

def run(start, stop, last):
    path, extraSteps, dimensions, x, y = getPath(start, stop)

    grid = []
    for i in range(dimensions[1]):
        grid.append([" "] * dimensions[0])

    for direction in path[:extraSteps]:
        x, y = x + direction[0], y + direction[1]

    num = stop
    for direction in path[extraSteps:]:
        grid[y][x] = num
        x, y = x + direction[0], y + direction[1]
        num -= 1

    grid[y][x] = num

    for column in range(dimensions[0]):
        maxDigits = getMaxInCol(grid, column)

        for row in range(dimensions[1]):
            grid[row][column] = ((maxDigits - len(str(grid[row][column]))) * " ") + str(grid[row][column])

    for i in range(dimensions[1]):
        row = grid[i]
        if i == dimensions[1] - 1 and not last:
            print(" ".join(x for x in row) + "\n")
        else:
            print(" ".join(x for x in row))

N = int(input())
spirals = []
for _ in range(N):
    start, stop = [int(x) for x in input().split()]
    spirals.append([start, stop])

for i in range(len(spirals)):
    spiral = spirals[i]
    if i == len(spirals) - 1:
        run(spiral[0], spiral[1], True)
    else:
        run(spiral[0], spiral[1], False)