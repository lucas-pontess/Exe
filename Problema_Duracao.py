'''Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
formato horas:minutos:segundos.'''

d = int(input("Digite a duração em seguntos: "))

hora = d // 3600
resto = d % 3600
min = resto // 60
seg = resto % 60

print(f"{hora}:{min}:{seg}")
