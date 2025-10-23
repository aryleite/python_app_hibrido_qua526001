# Importação de blibliotecas PYTHON

import os

# LOOP 
while True:
    # Limpeza de console (terminal)
    os.system("cls")

    # Tratamento de exceção 
    try:
        nome = input("informe o nome:").strip().title()
        email = input("informe o e-mail:").strip().lower()
        cpf = input("informe o cpf:").strip()

# Limpeza de console (terminal)
        os.system("cls")

        #Saída de dados
        print(f"nome: {nome}")
        print(f"e-mail: {email}")
        print(f"cpf: {cpf}")

        # Menu
        print("1- Inserir novos dados") 
        print("2- Sair do programa")

        opcao = input("Opção desejada:").strip()
        
        # Verifica a opção escolhida
        match opcao:
            case "1":
                continue
            case "2":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                break
        
    except:print("não foi possível receber informações.")