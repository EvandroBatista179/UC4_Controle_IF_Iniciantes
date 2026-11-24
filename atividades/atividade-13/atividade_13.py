# ATIVIDADE 13 - BRENO E ARTUR NO SENAC
laboratorios = int(input("Laboratórios visitados: "))
pontos = laboratorios * 10

if laboratorios >= 4:
    pontos = pontos + 20

print(f"Pontuação final: {pontos}")
