'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

print ("Calcule seu peso ideal!")
alt = float(input("Insira sua altura em metros:"))
pih = (72.7 * alt) - 58
pim = (62.1* alt) - 44.7
print ("Caso você seja homem, seu peso ideal é:", pih)
print ("Caso você seja mulher, seu peso ideal é:", pim)