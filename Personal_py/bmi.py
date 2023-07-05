def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert height from centimeters to meters
    bmi = weight / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Main program
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

bmi = calculate_bmi(weight, height)
category = interpret_bmi(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"Interpretation: {category}")
