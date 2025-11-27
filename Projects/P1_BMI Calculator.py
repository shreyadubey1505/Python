print("Welcome to the BMI Calculator")

gender = input("Enter your gender (male/female): ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height**2)
print("Your BMI is:", round(bmi, 2))

if gender == "male":
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 25:
        print("You have a normal weight.")
    elif 25 <= bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

elif gender == "female":
    if bmi < 18:
        print("You are underweight.")
    elif 18 <= bmi < 24:
        print("You have a normal weight.")
    elif 24 <= bmi < 29:
        print("You are overweight.")
    else:
        print("You are obese.")
else:
    print("Invalid gender entered. Please type 'male' or 'female'.")

# OUTPUT
# Welcome to the BMI Calculator
# Enter your gender (male/female): male
# Enter your weight in kilograms: 70
# Enter your height in meters: 1.75
# Your BMI is: 22.86
# You have a normal weight.
# OR
# Welcome to the BMI Calculator
# Enter your gender (male/female): female
# Enter your weight in kilograms: 60
# Enter your height in meters: 1.65
# Your BMI is: 22.04
# You have a normal weight.
