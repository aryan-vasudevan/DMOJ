first = True
low = 0
res = ""
while True:
    city, temp = input().split()
    temp = int(temp)
    if first:
        low = temp
        res = city
        first = False
    else:
        if temp < low:
            res = city
            low = temp

    if city == "Waterloo":
        break

print(res)
