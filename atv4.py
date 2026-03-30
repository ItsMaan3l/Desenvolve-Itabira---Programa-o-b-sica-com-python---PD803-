# Lê o valor inteiro em reais
valor = int(input())

# Calcula a quantidade de notas de 100 e atualiza o valor restante
n100 = valor // 100
valor = valor % 100

# Calcula a quantidade de notas de 50 e atualiza o valor restante
n50 = valor // 50
valor = valor % 50

# Calcula a quantidade de notas de 20 e atualiza o valor restante
n20 = valor // 20
valor = valor % 20

# Calcula a quantidade de notas de 10 e atualiza o valor restante
n10 = valor // 10
valor = valor % 10

# Calcula a quantidade de notas de 5 e atualiza o valor restante
n5 = valor // 5
valor = valor % 5

# Calcula a quantidade de notas de 2 e atualiza o valor restante
n2 = valor // 2
valor = valor % 2

# Calcula a quantidade de notas de 1
n1 = valor

# Imprime a quantidade de cada nota exatamente no formato solicitado
print(f"{n100} nota(s) de R$100,00")
print(f"{n50} nota(s) de R$50,00")
print(f"{n20} nota(s) de R$20,00")
print(f"{n10} nota(s) de R$10,00")
print(f"{n5} nota(s) de R$5,00")
print(f"{n2} nota(s) de R$2,00")
print(f"{n1} nota(s) de R$1,00")