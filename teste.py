from temperatura import conversor_de_temperatura
import sys

falhou = False

def testar(descricao, resultado, esperado, tolerancia=0.01):
    if abs(resultado - esperado) <= tolerancia:
        print(f"  PASSOU - {descricao}")
    else:
        print(f"  FALHOU - {descricao} | Esperado: {esperado} | Obtido: {resultado}")
        falhou = True

converter = conversor_de_temperatura()

print("\n=== Testes: Fahrenheit para Celsius ===")
testar("32F deve ser 0C",   converter.fahrenheit_para_celsius(32),  0.0)
testar("212F deve ser 100C", converter.fahrenheit_para_celsius(212), 100.0)

print("\n=== Testes: Celsius para Fahrenheit ===")
testar("0C deve ser 32F",   converter.celsius_para_fahrenheit(0),   32.0)
testar("100C deve ser 212F", converter.celsius_para_fahrenheit(100), 212.0)

if falhou:
    sys.exit(1)