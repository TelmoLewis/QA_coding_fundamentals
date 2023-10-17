def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("enter the temperature in celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}C is equal to {fahrenheit: .2f}F")
