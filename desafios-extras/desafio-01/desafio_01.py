# DESAFIO 1 - CAMPEONATO DE GAMES DA NINTENDO
pontos = int(input("Pontuação do jogador: "))
vitorias = int(input("Número de vitórias: "))

if pontos >= 500 and vitorias >= 3:
    print("Classificado para a final!")
else:
    print("Continue treinando para o próximo campeonato!")
