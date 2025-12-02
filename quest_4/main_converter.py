from conversor_temp_1 import converter_temperatura as f
from conversor_temp_2 import converter_temperatura as k

celsius = 50

fahrenheit = f(celsius)
kelvin = k(celsius)

print(f"{celsius}°C em Fahrenheit: {f(celsius)} °F")
print(f"{celsius}°C em Kelvin: {k(celsius)} K")

