import logging
import soma_binario
from soma_binario import *

logging.debug("debugando")

numero_binario1 = input("digite o primeiro numero ")
logging.debug("o primeiro numero binario inserido foi : " + numero_binario1)
#pra transformar cada numero em um elemento de array : list(numero_binario1)
numero_binario1_list = list(numero_binario1)
numero_binario2 = input("digite o segundo numero ")
numero_binario2_list = list(numero_binario2)



def traducao_bin_to_dec() :
    
    global sum
    global sum2
    #o sum =0 foi declarado no inicio da função pq senão ele dava erro de execução
    #UnboundLocalError: local variable 'sum2' referenced before assignment
    sum = 0
    sum2 = 0

    #numero 1 :
    print("numero separado em array " + str(numero_binario1_list))
    #tamanho do array : len()
    numero_binario1_inverso = numero_binario1[::-1]
    for n in range(len(numero_binario1_list)):
        
        #numero_binario1_inverso = numero_binario1[::-1]
        logging.debug(numero_binario1_inverso[n])
        
        #(elemento do array) * 2**n; sendo n o numero do elemento (começando em 0)
    
    for m in range(len(numero_binario1_inverso)):
    # while m <= len(numero_binario1_inverso) :
        multiplic = int(numero_binario1_inverso[m]) * (2**m)
        sum += 0
        sum = sum + multiplic
        #transformacao =+ multiplic
        
        

    print("o primeiro numero decimal : "+ str(sum))

    #numero 2 :
    print("numero separado em array " + str(numero_binario2_list))
    numero_binario2_inverso = numero_binario2[::-1]
    for n in range(len(numero_binario2_list)):
        
        #numero_binario1_inverso = numero_binario2[::-1]
        logging.debug(numero_binario2_inverso[n])
        
        #(elemento do array) * 2**n; sendo n o numero do elemento (começando em 0)
        
    for m in range(len(numero_binario2_inverso)):
        multiplic2 = int(numero_binario2_inverso[m]) * (2**m)
        sum2+=0
        sum2 = sum2+multiplic2
        #transformacao =+ multiplic2
        

    print("o segundo numero decimal : "+ str(sum2))
    
traducao_bin_to_dec()

def traducao_dec_to_bin():
    SumDecimal = soma_binario.SumDecimal
    while(SumDecimal%2 != 1):
        SumDecimal%2
        destranf += 0
        destranf =
