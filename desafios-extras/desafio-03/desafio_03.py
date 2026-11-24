# DESAFIO 3 - ORÇAMENTO DO SHOW DO BTS
dinheiro = float(input("Dinheiro disponível (R$): "))
custo = 900 + 600 + 400  # Ingresso + passagem + hospedagem

if dinheiro >= custo:
    sobra = dinheiro - custo
    print("Mikaelly vai realizar seu sonho!")
    print(f"Dinheiro que sobrará: R$ {sobra:.2f}")
else:
    falta = custo - dinheiro
    print("Ainda falta economizar!")
    print(f"Dinheiro que falta: R$ {falta:.2f}")
