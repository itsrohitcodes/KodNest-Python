# Transform Data

def celsius_to_fahrenheit(celsius):
    # TODO: Implement logic to convert Celsius to Fahrenheit
    return (celsius * 9/5) + 32

# TODO: Use map() to convert celsius_temperatures to Fahrenheit
celsius_temperatures = list(map(float, input().split()))
# Hardcoded list of temperatures for conversion

fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))

print (fahrenheit_temperatures)