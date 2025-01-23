graph = {}
while True:
    r1, r2 = list(input())
    if r1 == "*":
        break

    if r1 in graph:
        graph[r1].append(r2)
    else:
        graph[r1] = [r2]

seen = set()
path = {}
prev = "0"
stack = ["A"]

while stack != []:
    cur = stack.pop()
    path.append(cur + prev)
    if cur in 
    else:
        stack.append(graph[cur])




    
