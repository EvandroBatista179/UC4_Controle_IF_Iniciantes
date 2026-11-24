# DESAFIO 5 - FESTIVAL DE TALENTOS DA TURMA
participantes = int(input("Quantidade de participantes inscritos: "))
orcamento = float(input("Orçamento disponível (R$): "))

if participantes >= 20 and orcamento >= 500:
    orcamento = orcamento + 200
    print("Festival aprovado!")
else:
    print("Festival não aprovado.")

print(f"Orçamento final: R$ {orcamento:.2f}")
