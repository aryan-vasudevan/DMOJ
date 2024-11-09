N = int(input())
row = []

for i in range(N):
    value = int(input())
    row.append(value)

while True:
    type = int(input())

    if type == 77:
        break
    
    elif type == 99:
        streamNum = int(input()) - 1
        percentage = int(input())

        stream = row[streamNum]

        split1 = int(stream * percentage / 100)
        split2 = int(stream - split1)

        row = row[:streamNum] + [split1, split2] + row[streamNum + 1:]
        
    elif type == 88:
        streamNum = int(input()) - 1
        stream1 = row[streamNum]
        stream2 = row[streamNum + 1]
        
        row = row[:streamNum] + [stream1 + stream2] + row[streamNum + 2:]

print(" ".join(str(x) for x in row))