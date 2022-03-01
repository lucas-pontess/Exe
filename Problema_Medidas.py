'''Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C'''

a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C:"))

q = a * a
t = a * b / 2
tp = (a + b) * c / 2

print(f"AREA DO QUADRADO = {q:.4f}")
print(f"AREA DO TRIANGULO = {t:.4f}")
print(f"AREA DO TRAPEZIO = {tp:.4f}")
