# 4) Crie dois módulos diferentes: 'conversor_temp_1.py' com uma função 'converter(celsius)' que converte Celsius para Fahrenheit (C * 9/5 + 32), 
# e 'conversor_temp_2.py' com uma função 'converter(celsius)' que converte Celsius para Kelvin (C + 273.15). Em um arquivo 'main_converter.py', 
# importe ambos os módulos (usando nomes diferentes ou aliases para evitar conflito) e use cada função para converter 50 graus Celsius, imprimindo ambos os resultados.

def converter_temperatura(celsius: float):
    return celsius * 9/5 + 32

