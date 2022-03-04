'''
desafio: 
#calcular fatorial de um numero 
#regra para todo fatorial: para calcular fatorial, o numero tem q ser positivo e inteiro
METODO 5Qs
1)dados entrada: numero recebido
2)o que fazer com esses dados: calcular o fatorial
3)quais as restricoes : numero recebido deve ser positivo e inteiro
4)resultado esperado : mostrar o fatorial do numero recebido
5)qual a sequencia de passos a ser feita para chegar ao resultado esperado?
 a) verifica se numero recebido eh inteiro e positivo
 b)fatorial inicia em 1 e vai até o numero recebido
  b1) loop de 1 a numero
        fatorial = fatorial * numeroQestaInterandoNaHora (ou i)
 C)printar na tela o resultado 
    print(fatorial)

'''

numero = int(input('digite um numero'))
if numero > 0: 
    fatorial =1
    for item in range (1, numero +1):
        fatorial = fatorial * item
    print(fatorial)