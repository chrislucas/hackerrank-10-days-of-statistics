'''

https://brilliant.org/wiki/poisson-distribution/#conditions-for-use

Condicoes
* Um evento pode ocorrer um numero qualquer de vezes num periodo de tempo
* eventos sao independentes
* a taxa de ocorrencia eh constante. Ela nao mudacom base no tempo
* a probailidade de um evento ocorrer e proporcional ao tamanho do periodo. exemplo
eh 2x mais provavel de um evento ocorrer em 2 horas do que 1 evento ocorrer em 1h
.
'''

'''
A distribuicao de poisson eh apropriada para modelar o numero de ligacoes
que um esritorio pode receber ao meio-dia sabendo que a media de ligacoes
nesse periodo eh de 4 chamadas 
'''

from math import e as E


def factorial(n):
    acc = 1
    for i in range(n, 1, -1):
        acc *= i
    return acc


def poisson_distribution(success, avg):
    return ((avg ** success) * (E ** (-avg))) / factorial(success)


def example_1():
    # 4 ligacoes, probabilidade de receber uma ligacao 50%
    return poisson_distribution(4, 0.5)


'''
A media de gols por jogo num determinado campeonato eh de 0.25
modelar a probabilidade de ocorrer k gols num determinado jogo
'''


def example_2():
    acc = 0
    for k_goals in range(0, 10):
        pd = poisson_distribution(k_goals, 2.5)
        print("%d %f" % (k_goals, pd))
        acc += pd
    return acc


'''
https://brilliant.org/problems/fast-food-customers/

Um estatisticos registra uma media de 2.8 clientes realizando cadastros
a cada minuto.

Assumindo que o numero de clientes realiznaod o seu cadatros segue
uma distribuicao de poisson, qual a probabilidade de 4 clientes se
cadastrarem no proximo minuto
'''


def example_3():
    return round(poisson_distribution(4, 2.8), 3)


'''

Rule of sum
https://brilliant.org/wiki/probability-rule-of-sum/

Probability - by complement
https://brilliant.org/wiki/probability-by-complement/

A distribuicao de possion nos permite calcular a probabilidade de sucesso ou fracasso
de 0 a x eventos ocorrerem ou de mais do que x eventos ocorrerem (denominado respectivamente de
 "menor ou igual a" X ocorrencias ou "maior que" X ocorrencias) usando propriedades de regras de soma
 e de complemento de probabilidade
'''

'''
Um estatistico observou que a media de carros que atravessam um cruzamento eh de 1.6 a cada minuto

Quala probabilidade de 3 ou mais carros atravessarems um cruzamento em 1 min

Como nao a um limite superior para calcular essa probabilidade, uma vez que queremos
saber o resultado para 3 ou mais carros, precisamos calcula-la de forma indireta, usando o complemento

P(x >= 3) = 1 - P(x <= 2)

'''


def example_4():
    acc = 0
    for i in range(0, 3):
        acc += poisson_distribution(i, 1.6)
    return 1 - acc

'''
https://brilliant.org/wiki/poisson-distribution/#conditions-for-use'''

def example_5():
    return

if __name__ == '__main__':
    pass
