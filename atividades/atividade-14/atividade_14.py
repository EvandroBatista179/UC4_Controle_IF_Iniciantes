# ATIVIDADE 14 - PROMESSA DE ESFIHAS DA PROF. RUTH
alunos = int(input("Total de alunos: "))
presentes = int(input("Alunos presentes: "))
media = float(input("Média geral da turma: "))
custo = 0

if presentes == alunos and media >= 8:
    custo = alunos * 5  # Uma esfiha por aluno

print(f"Custo total das esfihas: R$ {custo:.2f}")
