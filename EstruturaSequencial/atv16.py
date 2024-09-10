'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
'''
from math import ceil

area = float(input("Qual a área da sua parede? (em metros²)"))
latas = area / 3 
valor_lata = 80
capacidade_lata = 18
quantidade_latas = latas / capacidade_lata
valor = ceil(quantidade_latas) * valor_lata
print ("Quantidade de latas necessárias:", ceil(quantidade_latas))
print ("Preço total: R$", ceil(valor))