# DESAFIO 2 - PROMOÇÃO ESPECIAL DA LIZANDRA
valor = float(input("Valor da compra (R$): "))

if valor >= 200:
    desconto = 40
else:
    desconto = 10

final = valor - desconto
print(f"Valor a pagar: R$ {final:.2f}")
