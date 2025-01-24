def points(cards):
    res = 0

    if len(cards) == 0:
        res += 3
    elif len(cards) == 1:
        res += 2
    elif len(cards) == 2:
        res += 1    
    
    cardValues = {
        "A": 4,
        "K": 3,
        "Q": 2,
        "J": 1
    }

    for card in cards:
        if card in cardValues:
            res += cardValues[card]

    return res

hand = input()

handSuits = {
    "C": [],
    "D": [],
    "H": [],
    "S": []
}
suitPoints = []
curSuit = "C"
for card in hand[1:]:
    if card == "D":
        curSuit = "D"
    elif card == "H":
        curSuit = "H"
    elif card == "S":
        curSuit = "S"
    else:
        handSuits[curSuit].append(card)

for suit in handSuits:
    suitPoints.append(points(handSuits[suit]))

print("Cards Dealt" + " " * 14, end="")
print("Points")

s = "Clubs " + " ".join(handSuits["C"])
print(s + " " * (25 - len(s)), end="")
print(f"{suitPoints[0]}".rjust(6))

s = "Diamonds " + " ".join(handSuits["D"])
print(s + " " * (25 - len(s)), end="")
print(f"{suitPoints[1]}".rjust(6))

s = "Hearts " + " ".join(handSuits["H"])
print(s + " " * (25 - len(s)), end="")
print(f"{suitPoints[2]}".rjust(6))

s = "Spades " + " ".join(handSuits["S"])
print(s + " " * (25 - len(s)), end="")
print(f"{suitPoints[3]}".rjust(6))

print(f"Total {sum(suitPoints)}".rjust(31))