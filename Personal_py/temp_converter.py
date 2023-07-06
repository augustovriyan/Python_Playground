def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def temperature_converter():
    print("Temperature Converter")
    while True:
        print("\nSelect the temperature unit you want to input:")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        print("0. Exit")
        choice = int(input("Enter your choice (0-3): "))

        if choice == 0:
            print("Exiting the program...")
            break
        elif choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
            print("Temperature in Fahrenheit:", fahrenheit)
            print("Temperature in Kelvin:", kelvin)
        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print("Temperature in Celsius:", celsius)
            print("Temperature in Kelvin:", kelvin)
        elif choice == 3:
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print("Temperature in Celsius:", celsius)
            print("Temperature in Fahrenheit:", fahrenheit)
        else:
            print("Invalid choice! Please enter a number between 0 and 3.")

temperature_converter()
