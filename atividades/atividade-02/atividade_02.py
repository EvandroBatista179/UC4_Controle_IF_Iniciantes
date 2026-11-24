# ATIVIDADE 2 - ANNA BEATRIZ E GIULIANY
anna = float(input("Gasto de Anna Beatriz (R$): "))
giuliany = float(input("Gasto de Giuliany (R$): "))
total = anna + giuliany

if total > 80:
    total = total + 20

print(f"Valor final: R$ {total:.2f}")
