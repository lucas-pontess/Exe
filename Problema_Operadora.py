'''Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.'''


m = int(input("Digite a quantidade de minutos: "))

valorpago = 50.0

if m > 100:
    valorpago = valorpago + 2 * (m - 100)

print(f"Valor a pagar = R${valorpago:.2f}")
