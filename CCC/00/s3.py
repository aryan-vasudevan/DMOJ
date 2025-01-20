import re

def surf(start, target, links):
    seen = set()
    queue = links[start]
    while queue != []:
        cur = queue.pop(0)
        if cur in seen:
            continue
        else:
            seen.add(cur)
            if len(seen) == len(links):
                return False

        if cur == target:
            return True
        else:
            queue += links[cur]
    
    return False

n = int(input())

links = {}

for i in range(n):
    url = input()
    subUrls = []
    body = ""
    while True:
        body = input()
        if body == "</HTML>":
            break
        matches = re.finditer('HREF="[^"]+">', body)

        for m in matches:
            start, stop = m.span()
            start += 6
            stop -= 2
            subUrls.append(body[start:stop])
    
    links[url] = subUrls

queries = []
while True:
    start = input()
    if start == "The End":
        break
    target = input()
    queries.append([start, target])

for url in links:
    for subUrl in links[url]:
        print(f"Link from {url} to {subUrl}")

for query in queries:
    start, target = query
    if surf(start, target, links):
        print(f"Can surf from {start} to {target}.")
    else:
        print(f"Can't surf from {start} to {target}.")