import tradutor_binario
#import tradutor_decimal
#from tradutor_decimal import traducao_dec_to_bin
from tradutor_binario import *
import time 
from time import sleep 

#variaveis de um outro arquivo devem ser mencionadas como nome_do_arquivo.nome_da_variavel
num1 = tradutor_binario.num1
num2 = tradutor_binario.num2

traducao_bin_to_dec()

SumDecimal = int(num1)+int(num2)
print("A soma dos numeros binarios em decimal é : "+str(SumDecimal))


def traducao_dec_to_bin(SumDecimal):
    
     
    # array to store
    # binary number
    binaryNum = [0] * SumDecimal
 
    # counter for binary array
    i = 0
    while (SumDecimal > 0):
 
        # storing remainder
        # in binary array
        binaryNum[i] = SumDecimal % 2
        SumDecimal = int(SumDecimal / 2)
        i += 1
 
    # printing binary array
    # in reverse order
    
    
    
    print(f'O numero decimal {SumDecimal} em binário é : {str(binaryNum[::-1])}')
    
 
# Driver Code
traducao_dec_to_bin(SumDecimal)

#de decimal de volta pra binario :
#resultado_em_binario() :
    #pega o resultado da soma e transforma de volta em binario
    #traducao_dec_to_bin()
    