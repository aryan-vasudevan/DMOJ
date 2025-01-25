square = 1

sl = {
    9: 34,
    40: 64,
    67: 86,
    54: 19, 
    90: 48,
    99: 77
}

terminate = False
while square != 100:
    move = int(input())
    if move == 0:
        terminate = True
        break

    if square + move > 100:
        square += 0
    else:
        square += move

    if square in sl:
        square = sl[square]
    
    print(f"You are now on square {square}")

if not terminate:
    print("You Win!")
else:
    print("You Quit!")