'''Fazer um programa para ler a quantidade de glicose
no sangue de uma pessoa e depois mostrar na tela a
classificação desta glicose de acordo com a tabela de
referência ao lado.'''



g = float(input("Digite a medida da glicose: "))

if g <= 100:
    print("NORMAL")
elif (g > 100) and (g <= 140):
    print("ALTERADO")
else:
    print("DIABETES")
