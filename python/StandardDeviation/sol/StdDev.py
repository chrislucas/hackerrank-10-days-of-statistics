'''
https://www.hackerrank.com/challenges/s10-standard-deviation/problem

https://www.mathsisfun.com/data/standard-deviation.html
https://www.statcan.gc.ca/edu/power-pouvoir/ch12/5214891-eng.htm

DONE

'''

from math import sqrt


def variance_utils(values, mean, n):
    acc = 0
    for i in values:
        '''
            Pontos interessantes no metodo para calcular o desvio padrao
            Por que usamos o quadrado da diferenca entre o valor i do conjunto
            e a media ?
            Seja S1 um conjunto de N numeros que armazena a diferenca entre i e a media
            e S2 um outro conjunto
            S1 = {4, 4, 4, 4}
            S2 = {7, 1, 6, 2}
            somatorio(S1) / tamanho(S1) = 4
            somatorio(S2) / tamanho(S2) = 4
            Temos valores iguais mesmo a distancia entre que 
            a diferente entre i-esimo valor e a media seja maior em S2 seja
            sempre maior do que em S1.
            A solucao para isso eh calcular um somatorio das diferencas entre
            i e a media ao quadrado.
            somatorio(S1) / tamanho(S1) = 4
            somatorio(S2) / tamanho(S2) = 4.74
        '''
        acc += (i - mean) * (i - mean)
    return acc / n




'''
A razao entre o somatorio da diferenca entre o i-esimo valor do conjunto e a media
e media.

Sigma (i, n) = (values[i] - mean) / mean
'''


def variance(values, n):
    return variance_utils(values, sum(values) / n, n)

'''
O desvio padrao nos diz o quao dispersos estao os valores
O calculo usado nesse arquivo eh o metodo utilizado no
desvio padrao 'populacional', onde usamos a amostra de dados
completa, existe porem o desvio padrao 'amostral' onde utilizamos
um subconjunto da populacao
'''
def std_dev(values, n):
    return sqrt(variance(values, n))


def run():
    n = int(input())
    return std_dev(list(map(int, input().split(" "))), n)

def test():
    _list = [600, 470, 170, 430, 300]
    _n = len(_list)
    stddev = std_dev(_list, _n)
    mean = sum(_list) / _n
    for i in _list:
        print("valor: %d diferenca (i-media): %f stddev: %f" % (i, i - mean, stddev))

'''
print("%.1f" % run())
print(variance([600, 470, 170, 430, 300], 5))
print("%.1f" % std_dev([10, 40, 30, 50, 20], 5))
'''
test()



if __name__ == '__main__':
    pass
