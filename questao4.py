#questão 04
for i in range(3):

    caso = int(input('Informe o valor da fatura que deseja calcular a taxa: \n1 - 1500 \n2 - 938.50 \n3 - 1000 \n'))

    match caso:
        case 1:
            taxa = 1500*0.02
            faturaTaxa = 1500 + taxa
            valorFinal = faturaTaxa*3.10
            print(f'O valor final que será pago em dólar é de {valorFinal:,.2f}')
        
        case 2:
            taxa = 938.50*0.02
            faturaTaxa = 938.50 + taxa
            valorFinal = faturaTaxa*3.75
            print(f'O valor final que será pago em dólar é de {valorFinal:,.2f}')
        
        case 3:
            taxa = 1000*0.02
            faturaTaxa = 1000 + taxa
            valorFinal = faturaTaxa*4
            print(f'O valor final que será pago em dólar é de {valorFinal:,.2f}')
print('Fim...')