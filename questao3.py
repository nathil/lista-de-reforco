#Questão 03
cotacao = float(input('Informe o valor do dólar:'))
match cotacao:
    case 3.10:
        valorFinal = 15000*3.10
        print('O valor em reais que mariazinha deve guardar é de:' + str(valorFinal))

    case 3.75:
        valorFinal = 15000*3.75
        print('O valor em reais que mariazinha deve guardar é de:' + str(valorFinal))  
    
    case 4:
        valorFinal = 15000*4
        print('O valor em reais que mariazinha deve guardar é de:' + str(valorFinal))
print('Fim...')