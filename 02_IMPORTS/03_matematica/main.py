# Importação de blibliotecas PYTHON
import math

# Entrada de dados 
r = float(input("informe o raio do círculo: ").strip().replace(",","."))

# Cálculos
a = math.pi*(r**2)
c = 2*math.pi*r

# Saída de dados 
print(f"Número do pi: {math.pi}")
print(f"Área da circunferância: {a}")
print(f"Tamanho da circunferância: {c}")

