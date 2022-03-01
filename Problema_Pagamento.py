'''Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
uma mensagem explicativa, conforme exemplo.'''

n = str(input("Nome: "))
v = float(input("Valor por hora: "))
h = int(input("Horas trabalhadas: "))

total = v * h

print(f"O pagamento para {n} deve ser de R${total:.2f}")
