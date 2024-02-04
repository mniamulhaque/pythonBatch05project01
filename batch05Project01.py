weight = float(input("Type Your weight in Kg: "))
height = float(input("Type Your height in Meters : "))

BMI = weight/height ** 2
if BMI < 18.5:
    print("Under Weight")
elif BMI < 25:
    print("Healthy Weight")
else:
    print("Over Weight")