n = int(input())

for i in range(n):
    link = input()

    body = ""

    while body != "</HTML>":
        body = input()
        if "HREF=" in body:
            print(True)
            start = body.index("HREF=") + 5
            stop = body[start:].index(">")
            print(body[start:stop])