n = int(input())

machines = []
for _ in range(3):
    machines.append(int(input()))

res = 0
curMachine = 0
while n != 0:
    n -= 1
    machines[curMachine] += 1
    res += 1
    
    if machines[0] == 35:
        n += 30
        machines[0] = 0
    if machines[1] == 100:
        n += 60
        machines[1] = 0
    if machines[2] == 10:
        n += 9
        machines[2] = 0    

    curMachine = (curMachine + 1) % 3
print(f"Martha plays {res} times before going broke.")
