# Functions to handle the math
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kilometers_to_miles(km):
    return km * 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

# The main part of the program
print("--- Simple Unit Converter ---")
print("1. Celsius to Fahrenheit")
print("2. Kilometers to Miles")
print("3. Kilograms to Pounds")

choice = input("\nChoose a conversion (1, 2, or 3): ")

if choice == '1':
    val = input("Enter temperature in Celsius: ")
    # Convert the text input into a number (float)
    val_float = float(val) 
    result = celsius_to_fahrenheit(val_float)
    print(val + "°C is equal to " + str(result) + "°F")

elif choice == '2':
    val = input("Enter distance in Kilometers: ")
    val_float = float(val)
    result = kilometers_to_miles(val_float)
    print(val + " km is equal to " + str(result) + " miles")

elif choice == '3':
    val = input("Enter weight in Kilograms: ")
    val_float = float(val)
    result = kilograms_to_pounds(val_float)
    print(val + " kg is equal to " + str(result) + " lbs")

else:
    print("Invalid choice! Please run the program again.")