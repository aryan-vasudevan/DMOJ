from math import sqrt

c = []

while True:
    C = int(input())
    
    if C != 0:
        c.append(C)
    else:
        break

def dimensions(area):
    n = int(sqrt(area))

    for i in range(1, n + 1):
        if area % i == 0:
            d = [i, int(area/i)]
    
    return d

for C in c: 
    d = dimensions(C)
    print(f"Minimum perimeter is {d[0] * 2 + d[1] * 2} with dimensions {d[0]} x {d[1]}")