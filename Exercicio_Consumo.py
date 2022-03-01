'''Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
médio do carro, com três casas decimais.'''


d = int(input("Distancia percorrida: "))
c = float(input("Combustivel gasto: "))

media = d / c

print(f"Consumo medio = {media:.3f}")

