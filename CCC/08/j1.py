weight = float(input())
height = float(input())

bmi = weight / pow(height, 2)

if bmi < 18.5:
    print("Underweight")
elif bmi > 25:
    print("Overweight")
else:
    print("Normal weight")
