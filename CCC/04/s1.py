def prefixFree(words):
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[j].startswith(words[i]):
                return False
    return True

n = int(input())

for _ in range(n):
    words = []
    for _ in range(3):
        words.append(input())
    
    if prefixFree(words) and prefixFree([word[::-1] for word in words]):
        print("Yes")
    else:
        print("No")