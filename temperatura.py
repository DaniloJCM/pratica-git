class conversor_de_temperatura:
    def __init__(self):
        pass

    def celsius_para_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def fahrenheit_para_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

celsius = 0
print(f"Celsius {celsius} para Fahrenheit:")
print(conversor_de_temperatura().celsius_para_fahrenheit(celsius))  # Deve imprimir 32.0

fahrenheit = 32
print(f"Fahrenheit {fahrenheit} para Celsius:")
print(conversor_de_temperatura().fahrenheit_para_celsius(fahrenheit))  # Deve imprimir 0.0