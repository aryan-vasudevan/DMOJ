ticketValues = []
for _ in range(4):
    ticketValues.append(int(input()))

target = int(input())

combinations = []
minNum = 0
for pink in range(target // ticketValues[0] + 1):
    for green in range(target // ticketValues[1] + 1):
        for red in range(target // ticketValues[2] + 1):
            for orange in range(target // ticketValues[3] + 1):
                total = pink * ticketValues[0] + green * ticketValues[1] + red * ticketValues[2] + orange * ticketValues[3]

                if total == target:
                    combinations.append([pink, green, red, orange])
                    if minNum == 0:
                        minNum = sum(combinations[-1])
                    else:
                        minNum = min(minNum, sum(combinations[-1]))

for c in combinations:
    print(f"# of PINK is {c[0]} # of GREEN is {c[1]} # of RED is {c[2]} # of ORANGE is {c[3]}")

print(f"Total combinations is {len(combinations)}.")
print(f"Minimum number of tickets to print is {minNum}.")