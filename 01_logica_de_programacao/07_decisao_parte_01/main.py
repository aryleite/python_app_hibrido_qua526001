# Declaração de variáveis

nome = input("informe seu nome:").strip().title()
# O strip é usado para apagar espaços depois do nome 9há usuários que irão colocar o nome e espaço e poderia dar erro.
# Title é usado para deixar as entradas com a letra maiúscula
idade = int (input("informe sua idade: ").strip())
 # O int antes da variável é para transformar string em int (palavra em número inteiro), já que todo input é automaticamente string.

# Decisão
if idade >= 18:
    print(f"{nome} é maior de idade.")
else: 
    print(f"{nome} é menor de idade.")