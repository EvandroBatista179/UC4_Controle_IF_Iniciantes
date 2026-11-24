# ATIVIDADE 11 - IZABELA NO SHOW DE DJAVAN
curtidas = int(input("Curtidas da publicação: "))
comentarios = int(input("Comentários da publicação: "))
pontos = int(input("Pontuação inicial: "))

if curtidas >= 100 and comentarios >= 30:
    pontos = pontos + 50

print(f"Pontuação final: {pontos}")
