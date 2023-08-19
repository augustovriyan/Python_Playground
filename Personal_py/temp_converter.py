def temperature_converter():
    print("Temperature Converter")
    while True:
        print("\nSelect the temperature unit you want to input:")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")
        print("0. Exit")
        choice = input("Enter your choice (0-3): ")

        try:
            choice = int(choice)
            if choice == 0:
                print("Exiting the program...")
                break
            elif choice in [1, 2, 3]:
                temperature = float(input("Enter temperature: "))
                
                if choice == 1:
                    celsius = temperature
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    kelvin = celsius_to_kelvin(celsius)
                elif choice == 2:
                    fahrenheit = temperature
                    celsius = fahrenheit_to_celsius(fahrenheit)
                    kelvin = fahrenheit_to_kelvin(fahrenheit)
                else:
                    kelvin = temperature
                    celsius = kelvin_to_celsius(kelvin)
                    fahrenheit = kelvin_to_fahrenheit(kelvin)
                
                print("Temperature in Celsius:", round(celsius, 2))
                print("Temperature in Fahrenheit:", round(fahrenheit, 2))
                print("Temperature in Kelvin:", round(kelvin, 2))
            else:
                print("Invalid choice! Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    temperature_converter()
