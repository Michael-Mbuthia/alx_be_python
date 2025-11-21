CELSIUS_TO_FAHRENHEIT = 9/5
FAHRENHEIT_TO_CELSIUS = 5/9

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT
    return celsius * CELSIUS_TO_FAHRENHEIT + 32

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature value")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif unit == 'F':
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}C°")
    else:
        print("Invalid choice. Enter 'C' or 'F'.")

if __name__ == "__main__":
    main()

