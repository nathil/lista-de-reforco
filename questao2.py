#questão 02
import math

def cm_para_m(x):
    return x/100

continuar = 'S'

while continuar != 'N':
    tamanho_sala = input('Informe a largura e o comprimeto da sala: ')
    tamanho_lajota = input('Informe o a largura e o comprimento da lajota: ')

    largura_sala, comprimento_sala = list(map(float, tamanho_sala.split()))
    tamanho_lajota_cm = list(map(float, tamanho_lajota.split()))


    largura_lajota, comprimento_lajota = list(map(cm_para_m, tamanho_lajota_cm))


    quantidade_minima = math.ceil((largura_sala/largura_lajota))*math.ceil((comprimento_sala/comprimento_lajota))

    print(f'A quantidade mínima é de {quantidade_minima} lajotas')
    continuar = input('Deseja continuar?:')
print('Fim...')
knllkjlkjlkj






