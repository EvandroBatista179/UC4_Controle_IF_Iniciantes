# ATIVIDADE 12 - FELIPE E AS TRANÇAS DE MILENA
distancia = float(input("Distância a percorrer (km): "))
valor = 180  # Preço do serviço

if distancia > 10:
    valor = valor + 25

print(f"Total a pagar: R$ {valor:.2f}")
