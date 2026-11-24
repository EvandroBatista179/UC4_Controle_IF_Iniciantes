# ATIVIDADE 8 - EXTENSÃO DE RAP DO VS CODE
execucoes = int(input("Quantidade de execuções: "))
musicas = int(input("Músicas disponíveis no início: "))

if execucoes >= 10:
    musicas = musicas + 5

print(f"Quantidade final de músicas: {musicas}")
