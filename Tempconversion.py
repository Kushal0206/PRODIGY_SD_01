def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (Celsius, Fahrenheit, or Kelvin): ").lower()

    if unit == "celsius":
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
    elif unit == "fahrenheit":
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
    elif unit == "kelvin":
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
    else:
        print("Invalid unit of measurement. Please enter Celsius, Fahrenheit, or Kelvin.")
        return

    print(f"{temperature} {unit} is equivalent to:")
    if "celsius" in unit:
        print(f"{fahrenheit:.2f} Fahrenheit")
        print(f"{kelvin:.2f} Kelvin")
    elif "fahrenheit" in unit:
        print(f"{celsius:.2f} Celsius")
        print(f"{kelvin:.2f} Kelvin")
    elif "kelvin" in unit:
        print(f"{celsius:.2f} Celsius")
        print(f"{fahrenheit:.2f} Fahrenheit")

if __name__ == "__main":
    main()
