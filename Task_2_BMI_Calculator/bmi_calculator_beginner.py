
# TASK 2 · BMI Calculator

# Objective: Build a Python program that calculates a user's Body Mass Index (BMI) and classifies it into health categories. Beginners build a command-line tool; advanced builds a full GUI application with data persistence and trend visualisation.

# Tech Stack — Beginner: Python, input(), basic arithmetic 




# Feature Checklist — Beginner Tier:
# [ ] Prompt user for weight (kg) and height (m) via command line
# [ ] Calculate BMI using the formula: BMI = weight / (height²)
# [ ] Classify result into standard categories: Underweight (< 18.5), Normal (18.5–24.9), Overweight (25–29.9), Obese (≥ 30)
# [ ] Display the BMI value rounded to 2 decimal places and the category
# [ ] Input validation: reject non-numeric input and negative values with a helpful error message



# Self-Sourcing Guideline: Search "Python BMI calculator command line tutorial" for the beginner approach. 

##  Beginner Tier  ##


def input_validation(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num == 0:
                print("Invalid input! \nInputs can't be  equal to zero. ")
                continue
            if num < 0:
                print("Invalid input! \nInputs can't be negative value. ")
                continue
            return num
        
        except ValueError:
            print("Invalid Input! \n Enter numbers only \n Please try again..")

weight = input_validation("Enter your weight (kg): ")
height = input_validation("Enter your height(m): ")
bmi = weight / (height**2)

if bmi < 18.5 :
    category = "Under weight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25 <= bmi <= 29.9 :
    category = "Over weight"
else:
    category = "Obese"


print(f"""
================================
        BMI CALCULATOR
================================

Enter your weight (kg): {weight}
Enter your height (m): {height}

--------------------------------
BMI       : {round(bmi,2)}
Category  : {category}
--------------------------------

""")