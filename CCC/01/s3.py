
def dfs(graph, p, q):
    stack = ["A"]
    seen = set()
    res = False
    while stack != []:
        node = stack.pop()
        seen.add(node)

        if node == "B":
            res = True
            break

        neighbours = graph[node]
        for n in neighbours:
            if n in seen:
                continue
            if (node == p and n == q) or (node == q and n == p):
                continue
            stack.append(n)

    return res

graph = {}
roads = []
while True:
    r1, r2 = list(input())
    roads.append(r1 + r2)
    if r1 == "*":
        break

    if r1 in graph:
        graph[r1].append(r2)
    else:
        graph[r1] = [r2]
    
    if r2 in graph:
        graph[r2].append(r1)
    else:
        graph[r2] = [r1]

res = 0
for road in roads:
    if not dfs(graph, road[0], road[1]):
        print(road)
        res += 1

print(f"There are {res} disconnecting roads.")