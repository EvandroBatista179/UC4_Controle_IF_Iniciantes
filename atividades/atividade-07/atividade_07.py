# ATIVIDADE 7 - MÚSICA DE WANDERCYRA
reproducoes = int(input("Número de reproduções: "))
curtidas = int(input("Número de curtidas: "))
valor = float(input("Valor já arrecadado (R$): "))

if reproducoes > 1000 or curtidas > 200:
    valor = valor + 150

print(f"Valor final: R$ {valor:.2f}")
