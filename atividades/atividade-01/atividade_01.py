# ATIVIDADE 1 - A LOJINHA DE LIZANDRA
valor = float(input("Valor da compra (R$): "))

if valor > 150:
    valor = valor - 30

print(f"Valor a pagar: R$ {valor:.2f}")
