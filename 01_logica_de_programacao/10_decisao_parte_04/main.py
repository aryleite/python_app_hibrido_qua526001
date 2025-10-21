# Declaração de variáveis 

x = float(input("informe o 1º número: ").strip().replace(",","."))
y= float(input("informe o 2 número: ").strip().replace(",","."))

# Menu

print("1 - Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
operador = input("informe a operação desejada: ").strip()

# Decisão

match operador:
    case "1":
        print(f"A Soma é {x+y}")
    case "2":
        print(f"A Subtração é {x-y}")
    case "3":
        print(f"A multuplicação é {x*y}")
    case "4":
        print(f"A Divisão é {x/y}")
    case _:
        print(f"Operação inválida.")

 