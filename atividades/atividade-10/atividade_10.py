# ATIVIDADE 10 - COMPRAS DE KAUANE E KAUANY
livros = int(input("Quantidade de livros: "))
jogos = int(input("Quantidade de jogos: "))
valor = float(input("Valor da compra (R$): "))

if livros >= 2 or jogos >= 3:
    valor = valor - 25

print(f"Valor final: R$ {valor:.2f}")
