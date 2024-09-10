'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

mega_bytes = float(input("Digite o tamanho do seu arquivo: "))
mega_bits_por_segundo = float(input("Digite a velocidade da sua internet: "))

mega_bits = mega_bytes * 8
velocidade_segundos = int(mega_bits / mega_bits_por_segundo)
velocidade_minutos = int(velocidade_segundos / 60)

print(f"Levará aproximadamente {velocidade_minutos} minutos para realizar o download do arquivo")