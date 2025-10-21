# Declaração de variáveis 

nome = input("informe o nome:").strip().title()
# O strip é usado para apagar espaços depois do nome. Há usuários que irão colocar o nome e espaço e poderia dar erro.
# Title é usado para deixar as entradas com a letra maiúscula
idade = int (input("informe sua idade: ").strip())
 # O int antes da variável é para transformar string em int (palavra em número inteiro), já que todo input é automaticamente string.
altura = float(input("Informe a altura: ").strip().replace(",","."))

# Verificação das condições
if idade>= 12 and altura >= 1.15:
    print(f"Entrada de {nome} autorizada.")
else:
    print(f"Entrada de {nome} não autorizada.")
