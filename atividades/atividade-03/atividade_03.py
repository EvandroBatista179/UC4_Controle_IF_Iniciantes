# ATIVIDADE 3 - JOGOS DA NINTENDO
jogos = int(input("Quantidade de jogos: "))
valor = float(input("Valor da compra (R$): "))
pontos = int(input("Pontuação inicial: "))

if jogos >= 3 and valor > 500:
    pontos = pontos + 200

print(f"Pontuação final: {pontos}")
