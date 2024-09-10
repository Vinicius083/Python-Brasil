'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

#Código
from math import ceil

lata = 18
valor_lata = 80
galao = 3.6
valor_galao = 25


area = float(input("Qual a área da sua parede? (em metros²): "))
litros = area / 6 
litros_folga = litros * 1.1

#Opção 1
quantidade_latas = ceil(litros / lata)
valor_a_pagar = quantidade_latas * valor_lata
print("====================Latas de 18 Litros====================")
print(f"Quantidade de latas: {quantidade_latas} e valor a pagar: R${valor_a_pagar}")

#Opção 2
quantidade_galoes = ceil(litros / galao)
valor_a_pagar = quantidade_latas * valor_galao
print("===================Galões de 3,6 Litros===================")
print(f"Quantidade de Galões: {quantidade_galoes} e valor a pagar: R${valor_a_pagar}")

#Opção 3
mistura_lata = int(litros_folga / lata)
mistura_galao = int((litros_folga - (mistura_lata * 18)) / 3.6)
if (litros_folga - (mistura_lata * 18) % 3.6 != 0):
    mistura_galao += 1
valor_a_pagar_mistura_lata = mistura_lata * 80
valor_a_pagar_mistura_galao = mistura_galao * 18
valor_total = valor_a_pagar_mistura_galao + valor_a_pagar_mistura_lata

print("===================Latas e Galões===================")
print(f"Quantidade de latas: {mistura_lata} | Quanidade de galões: {mistura_galao} | valor a pagar: R${valor_total}")