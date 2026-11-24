# DESAFIO 4 - GRANDE PEDIDO DE ESFIHAS
quantidade = int(input("Quantidade de esfihas: "))

if quantidade >= 30:
    preco = 4
else:
    preco = 5

total = quantidade * preco
print(f"Total da compra: R$ {total:.2f}")
