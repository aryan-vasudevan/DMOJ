T, N = [int(x) for x in input().split()]

strings = []
for _ in range(T):
    string = input()
    strings.append(string)

for string in strings:
    counts = {}
    for i in range(N):
        if string[i] in counts:
            counts[string[i]] = "heavy"
        else:
            counts[string[i]] = "light"

    prev = counts[string[0]]

    valid = True
    for c in string[1:]:
        if counts[c] == prev:
            valid = False
            break
        else:
            prev = counts[c]
    
    if valid:
        print("T")
    else:
        print("F")