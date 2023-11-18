burgers = {
  1: 461,
  2: 431,
  3: 420,
  4: 0
}
sides = {
  1: 100,
  2: 57,
  3: 70,
  4: 0
}
drinks = {
  1: 130,
  2: 116,
  3: 118,
  4: 0
}
deserts = {
  1: 167,
  2: 266,
  3: 75,
  4: 0
}

burger = input()
side = input()
drink = input()
desert = input()

res = burgers[int(burger)] + sides[int(side)] + drinks[int(drink)] + deserts[int(desert)]

print(f"Your total Calorie count is {res}.")