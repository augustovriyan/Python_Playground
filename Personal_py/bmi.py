# Function to calculate BMI based on weight in kilograms and height in centimeters
def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100  # Convert height from centimeters to meters
    return weight_kg / (height_m ** 2)

# Function to interpret BMI into categories
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Function to get numeric input from the user
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Main function to drive the program
def main():
    print("BMI Calculator")
    weight = get_numeric_input("Please enter your weight in kilograms: ")
    height = get_numeric_input("Please enter your height in centimeters: ")

    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Interpretation: {category}")

# Entry point of the program
if __name__ == "__main__":
    main()
