import soma_binario
from soma_binario import SumDecimal

decimal = soma_binario.SumDecimal

def traducao_dec_to_bin():
    #pega o decimal
    l = []
    while (decimal // 2 != 1):
        x = decimal%2  #armazenar o valor dessa divisão
        l.append(x)
        if(decimal//2 == 1):
            y = decimal//2 == 1
            l.append(y)
            break
    print(f'O valor {decimal} em binário é {l}')