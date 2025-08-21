def celcius_to_fahrenheit(celcius):
    fahrenheit = celcius * (9/5) + 32
    return fahrenheit
celcius = float(input("Enter temperature in celcius: "))
fahrenheit = celcius_to_fahrenheit(celcius)
print("Tempearture in fahrenheit is", fahrenheit)