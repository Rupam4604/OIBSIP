weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / (height**2)

if bmi < 18.5 :
    category = "Under weight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25 <= bmi <= 29.9 :
    category = "Over weight"
else:
    category = "Obese"


print(round(bmi,2))
print(category)