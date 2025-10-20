# Declaração de variáveis 

nome = input("informe seu nome:").strip().title()
# O strip é usado para apagar espaços depois do nome 9há usuários que irão colocar o nome e espaço e poderia dar erro.
# Title é usado para deixar as entradas com a letra maiúscula
idade = int(input("informe sua idade:"))
 # O int antes da variável é para transformar string em int (palavra em número inteiro), já que todo input é automaticamente string.
altura = float(input("informe sua altura:").strip().replace(",","."))
# O float antes da variável é para transformar string em int (palavra em número número deciamal), já que todo input é automaticamente string.

# Saída de dados 

print(f"Nome do usuário: {nome}. Tipo: {type(nome)}")
print(f"idade: {idade}. Tipo: {type(idade)}")
print(f"altura: {altura}. Tipo: {type(altura)}")
#Tipo: {type(variável)} é usado para saber que tipo de variável se trata