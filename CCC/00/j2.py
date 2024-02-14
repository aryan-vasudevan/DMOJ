def isPalindrome(i):
    num = str(i)
    l, r = 0, len(num) - 1
    numbers = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    while l < r:
        if num[l] not in numbers or num[r] not in numbers or num[l] != numbers[num[r]]:
            return False
        
        l += 1
        r -= 1         

    return True


m, n = int(input()), int(input())
res = 0

for i in range(m, n + 1):
    if isPalindrome(i):
        print(i)
        res += 1

print(res)