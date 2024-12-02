def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

fahrenheit = 50
celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)