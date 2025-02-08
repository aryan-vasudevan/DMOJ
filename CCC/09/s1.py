start = int(input())
end = int(input())

res = 0

for i in range(start, end + 1):
    if (i ** (1/3)).is_integer() and (i ** (1/2)).is_integer():
        res += 1

print(res)