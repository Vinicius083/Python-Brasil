#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas = float(input ("quantas horas você trabalhou por mês?"))
valor_hora = float(input ("quanto custa a hora do seu trabalho?"))
sálario = horas * valor_hora
print ("seu salaio é de:", "R$", sálario,)