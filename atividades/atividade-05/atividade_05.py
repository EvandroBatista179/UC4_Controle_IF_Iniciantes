# ATIVIDADE 5 - MIKAELLY E O SHOW DO BTS
dinheiro = float(input("Dinheiro guardado (R$): "))
custo = 750 + 300  # Ingresso + passagem

if dinheiro >= custo:
    dinheiro = dinheiro + 100  # Bônus da família

print(f"Dinheiro após possível bônus: R$ {dinheiro:.2f}")
