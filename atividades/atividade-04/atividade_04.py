# ATIVIDADE 4 - MARATONA DE SÉRIES
# Digite 1 para disponível ou 0 para indisponível.
caua = int(input("Cauã está disponível? (1/0): "))
miguel = int(input("Miguel está disponível? (1/0): "))
joao = int(input("João Victor está disponível? (1/0): "))
jonatha = int(input("Jonatha está disponível? (1/0): "))

if caua == 1 and miguel == 1 and joao == 1 and jonatha == 1:
    print("Maratona confirmada! Preparem a pipoca!")
else:
    print("A maratona não foi confirmada.")
