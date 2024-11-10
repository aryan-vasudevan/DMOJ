from math import gcd

def simplify(numerator, denominator):
    divisor = gcd(numerator, denominator)
    numerator /= divisor
    denominator /= divisor

    return int(numerator), int(denominator)

numerator = int(input())
denominator = int(input())

if not numerator % denominator:
    print(int(numerator / denominator))
elif numerator < denominator:
    numerator, denominator = simplify(numerator, denominator)
    print(f"{numerator}/{denominator}")
else:
    wholePart = int(numerator // denominator)
    numerator -= wholePart * denominator
    numerator, denominator = simplify(numerator, denominator)

    print(f"{wholePart} {numerator}/{denominator}")