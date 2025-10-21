# Entrada de dados 

aluno = input("informe o nome do aluno:").strip().title()
nota = float(input("informe a nota:").strip().replace(",","."))
# O strip é usado para apagar espaços depois do nome. Há usuários que irão colocar o nome e espaço e poderia dar erro.
# Title é usado para deixar as entradas com a letra maiúscula

# Verificação da nota do aluno

if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f" {aluno} está aprovado.")
    elif nota >= 5:
        print(f" {aluno} está de recuperação.")
    else:
        print(f"{aluno} está reprovado.")
   
else:
    print(f"nota do {aluno} inválida.")