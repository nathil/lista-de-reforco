#questão 06
menor_valor = 0
continuar = 'S'

while continuar != 'N':
    valores = input('Informe os valores das peças:')

    valor1, valor2, valor3 = list(map(int, valores.split()))

    if(valor1 < valor2 and valor1 < valor3):
        print(menor_valor)
    if(valor2 < valor1 and valor2 < valor3):
        menor_valor = valor2
        print(menor_valor)
    if(valor3 < valor1 and valor3 < valor2):
        menor_valor = valor3

    total = valor1 + valor2 + valor3
    desconto = menor_valor
    valor_pago = total - desconto

    print(f'O valor total da compra é de R${total}')
    print(f'O valor do desconto é de R${desconto}')
    print(f'O valor pago foi de R${valor_pago}')
    input('Deseja continuar?(S?/N):')
    


