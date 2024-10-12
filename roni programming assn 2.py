# Roni Kulkarni Programming Assn 2 9-7-22


# This program converts degrees Kelvin to degrees Celsius and degrees Fahrenheit.

# Convert degrees Kelvin to degrees Celsius and degrees Fahrenheit
# Input-temperature in degrees Kelvin
# Output-temperature in degrees Celsius and degrees Fahrenheit

# Get the temperature in degrees Kelvin
degreesKelvin = input("What is the temperature in degrees Kelvin?")
degreesKelvin = float(degreesKelvin)

# Calculate and display the temperature in degrees Celsius
degreesCelsius = degreesKelvin - 273.15
print("The temperature is", degreesCelsius, "Celsius")

# Calculate and display the temperature in degrees Fahrenheit
degreesFahrenheit = (degreesCelsius * 9/5) + 32
print("The temperature is", degreesFahrenheit, "Fahrenheit")

