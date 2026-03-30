# Lê o comprimento do terreno como número inteiro
comprimento = int(input("Digite o comprimento do terreno: "))

# Lê a largura do terreno como número inteiro
largura = int(input("Digite a largura do terreno: "))

# Lê o preço do metro quadrado como número de ponto flutuante
preco_m2 = float(input("Digite o preço do metro quadrado: "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Imprime o resultado formatado com duas casas decimais e separador de milhar
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")