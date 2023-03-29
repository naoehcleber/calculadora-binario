import tradutor_binario
from tradutor_binario import *

#variaveis de um outro arquivo devem ser mencionadas como nome_do_arquivo.nome_da_variavel
num1 = tradutor_binario.num1
num2 = tradutor_binario.num2

traducao_bin_to_dec()

SubDecimal = int(num1)-int(num2)
print("A subtração dos numeros binários em decimal é : "+str(SubDecimal))
x = SubDecimal
#se o resultado der negativo ele não tá conseguinfo transformar em binario NEGATIVO, resolver isso dps
traducao_dec_to_bin(x)

