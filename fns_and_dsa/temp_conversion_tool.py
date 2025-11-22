CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_fahrenheit(temperature):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return temperature * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def convert_to_celsius(temperature):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

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
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

