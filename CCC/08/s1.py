lowest = float('inf')

while True:
    city, temp = input().split()
    temp = int(temp)

    if temp < lowest:
        lowest = temp
        res = city

    if city == "Waterloo":
        break

print(res)