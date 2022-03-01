'''Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
mensagem "REPROVADO", conforme exemplos.'''


n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota: "))

nfinal = n1 + n2

if nfinal < 60:
    print("REPROVADO")

print(f"NOTA FINAL = {nfinal:.1f}")

