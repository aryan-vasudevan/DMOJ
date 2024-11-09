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
    
    path.pop()

    for i in range(len(path)):
        path[i] = opposites[path[i]]

    path.reverse()

    extraSteps = len(path) - steps + 1

    return path, extraSteps, dimensions

start, stop = [int(x) for x in input().split()]

path, extraSteps, dimensions = getPath(start, stop)

grid = []
for i in range(dimensions[1]):
    grid.append([0] * dimensions[0])

x, y = 0, 0

for direction in path[:extraSteps]:
    x, y = x + direction[0], y + direction[1]

num = stop
for direction in path[extraSteps:]:
    grid[y][x] = num
    x, y = x + direction[0], y + direction[1]
    num -= 1

grid[y][x] = num

print(grid)