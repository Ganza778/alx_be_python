
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if unit == "f":  
  def convert_to_celsius():
      temperature_in_celsius = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
      print(f"{temperature}°F is {temperature_in_celsius:.2f}°C")  
  convert_to_celsius()
elif unit == "c":
   def convert_to_fahrenheit():
      temperature_in_fahrenheit = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
      print(f"{temperature}°F is {temperature_in_fahrenheit:.2f}°C")  
   convert_to_fahrenheit()
else:
  print("Invalid temperature. Please enter a numeric value.")
