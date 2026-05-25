class conversor_de_temperatura:
    def __init__(self):
        pass

    def celsius_para_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def fahrenheit_para_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9