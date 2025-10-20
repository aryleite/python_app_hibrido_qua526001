# declaração da variável
nome = "Ary Leite"
idade = 27

# concatenação de valores
# forma 1 - abrindo aspas 
print("Boa tarde, meu nome é " + nome + " e tenho " + str(idade)+ " anos de idade.")

# forma 2 - usando vírgulas 
print("Boa tarde, meu nome é", nome, "e tenho", idade, "anos de idade.")

# forma 3 - usando format
print("Boa tarde, meu nome é {} e tenho {} anos de idade.".format(nome, idade))

# forma 4 - usando f-string (A MAIS USADA)
print(f"Boa tarde, meu nome é {nome} e tenho {idade} anos de idade.")
