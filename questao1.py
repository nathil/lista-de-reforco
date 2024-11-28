#questão 01 lista de reforço
gasolina = float(input('Informe o valor da gasolina:'))

match gasolina:
    case 4.1:
        autonomia = 312/8.5
        valorFinal = 4.1*autonomia
        print(f'O valor final é:{valorFinal:,.2f}')
    
    case 3.51:
        autonomia = 312/10
        valorFinal = 3.51*autonomia
        print(f'O valor final é:{valorFinal:,.2f}')
    
    case 3:
        autonomia = 312/9.36
        valorFinal = 3*autonomia
        print(f'O valor final é:{valorFinal:,.2f}')
    
print('Fim...')
    