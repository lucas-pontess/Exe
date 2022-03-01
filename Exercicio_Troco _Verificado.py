'''Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
valor restante conforme exemplo.'''

p = float(input("Preço unitario do produto: "))
q = int(input("Quantidade comprada: "))
d = float(input("Dinheiro recebido: "))

if d >= (p  * q):
    troco = d - p * q
    print(f"TROCO = {troco:.2f}")
else:
    resto = p * q - d
    print(f"Dinheiro insuficiente. Faltam R${resto:.2f}")



