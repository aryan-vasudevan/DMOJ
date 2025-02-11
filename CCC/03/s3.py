def bfs(r, c, grid):
    queue = [(r, c)]
    res = 0
    grid[r][c] = "I"
    
    while queue != []:
        node = queue.pop(0)
        res += 1

        neighbours = [
            (node[0] + 1, node[1]), 
            (node[0] - 1, node[1]), 
            (node[0], node[1] + 1), 
            (node[0], node[1] - 1)
        ]

        for (y, x) in neighbours:
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
                continue
            if grid[y][x] == "I":
                continue

            queue.append((y, x))

        grid[node[0]][node[1]] = "I"

    return res

flooring = int(input())
r, c = int(input()), int(input())

grid = []
for _ in range(r):
    row = list(input())
    grid.append(row)

print(bfs(2, 1, grid))

# rooms = []
# for row in range(r):
#     for col in range(c):
#         size, area = bfs(row, col, grid)
#         rooms.append(size)

# print(rooms)