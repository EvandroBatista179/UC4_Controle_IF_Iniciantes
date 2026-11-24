# ATIVIDADE 9 - PALESTRA SOBRE CASAMENTO
inscritos = int(input("Quantidade de inscritos: "))
cadeiras = int(input("Quantidade de cadeiras disponíveis: "))

if inscritos > 80 and cadeiras < inscritos:
    cadeiras = cadeiras + 30

print(f"Quantidade final de cadeiras: {cadeiras}")
