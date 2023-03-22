import tradutor_binario
from tradutor_binario import *

#variaveis de um outro arquivo devem ser mencionadas como nome_do_arquivo.nome_da_variavel
sum = tradutor_binario.sum
sum2 = tradutor_binario.sum2


SumDecimal = int(sum)+int(sum2)
print("A soma dos numeros binarios em decimal é : "+str(SumDecimal))