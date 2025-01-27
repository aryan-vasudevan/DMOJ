n = int(input())
for _ in range(n):
    y, m, d = [int(x) for x in input().split()]
    if y < 1989 or (y == 1989 and (m < 2 or (m == 2 and d <= 27))):
        print("Yes")
    else:
        print("No")
