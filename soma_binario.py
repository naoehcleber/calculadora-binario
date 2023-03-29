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
x = SumDecimal



    
 
# Driver Code
traducao_dec_to_bin(x)

#de decimal de volta pra binario :
#resultado_em_binario() :
    #pega o resultado da soma e transforma de volta em binario
    #traducao_dec_to_bin()
    