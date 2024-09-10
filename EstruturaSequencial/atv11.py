'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

int1 = int(input("Insira um número inteiro"))
int2 = int(input("Insira um número inteiro"))
real = float(input("Insira um número real"))
A = (int1 * 2) * (int2 / 2)
B = (int1 * 3) + real
C = real ** 2
print ("a.", A)
print ("b.", B)
print ("c.", C)