velocidadeCarro = int(input("Qual a veloc do carro?"))    
velocidadeMaxima = 80

if velocidadeCarro <= velocidadeMaxima : 
    print("Não levou multa!")
elif velocidadeCarro > velocidadeMaxima and velocidadeCarro <= (velocidadeMaxima + 10): 
    print(" Levou multa leve.")
elif velocidadeCarro > (velocidadeMaxima + 10) and velocidadeCarro < (velocidadeMaxima + 20){
    print("Levou multa grave.")
else : 
    print("Levou multa gravíssima.")
 



# esse código esta no replit
# verificar se carro levou multa
##veloc_maxima  = 80
#multa_leve >= velocidade_maxima + 10
#multa_grave >= velocidade_maxima + 11
#multa_gravissima > velocidade_maxima + 20

#1)dados entrada: velocidade carro e velocidade maxim
#2)o que fazer com esses dados: comparar
#3)quais as restricoes : numero recebido deve ser positivo e inteiro
#4)resultado esperado : comparar os valore e mostrar mensagem conforme a comparcao
#5)qual a sequencia de passos a ser feita para chegar ao resultado esperado?
# a) verifica a velocidade do carro
# b) faz um if para cada intervalo de velocidade e mensagem conforme a veloc
#  b1) loop de 1 a numero
#        fatorial = fatorial * numeroQestaInterandoNaHora (ou i)
# C)printar na tela a msg correspondente