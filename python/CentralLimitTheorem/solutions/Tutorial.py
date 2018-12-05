'''
https://support.minitab.com/pt-br/minitab/18/help-and-how-to/statistics/basic-statistics/supporting-topics/data-concepts/about-the-central-limit-theorem/
https://pt.wikipedia.org/wiki/Teorema_central_do_limite
https://www.investopedia.com/terms/c/central_limit_theorem.asp

https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/tutorial

Descricao:
https://en.wikipedia.org/wiki/Central_limit_theorem

Na teoria da probabilidate The Central Limit Theorem estabelece que em algumas situacoes quando somamos variaeis
aleatorias independentes a soma devidamente normalizada tende em direcao a distribuicao normal, mesmo
se as variaveis originalmente nao estavam numa distribuicao normal.

O teorema eh um conceito chave na teoria de probabilidade pois implica que metodos probabilisticos e estatiscos
que funcionam na distribuicao normal podem ser aplicados a muitos problemas que envolvem outros tipos de
distribuicao.

Exemplo:

Suponha um conjunoto que contem um grande numero de observacoes em que cada uma foi randomicamente
gerada e uma indepentede da outra e que foi retirada a media aritmetica desse conjunto. Se esse
processo for realizado muitas vezes, o teorema central de limite diz que a distribuicao da media sera
bem proximo da distribuicao normal

'''

'''
Exemplo da wiki

Seja a variavel aleatoria X = "resultado de um dado nao viciado" que pode
assumir os valores de 1 a 6.
'''


# valor esperado populacional
def expected_value():
    return sum(range(1, 7)) / 6


'''
v = lambda x: x ** 2
variancia populacional
Var[X] = E(X^2) - [E(X)] ^ 2
'''


def p_variance():
    return sum([x ** 2 * (1 / 6) for x in range(1, 7)]) - (sum([x / 6 for x in range(1, 7)])) ** 2


def fn_variance(n):
    return p_variance() / n


'''
https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem
'''

# print(expected_value())
# print(p_variance())
# print(fn_variance(6))

# https://en.wikipedia.org/wiki/Normal_distribution
# https://www.hackerrank.com/challenges/s10-normal-distribution-1/tutorial

from math import pi, e, erf, sqrt


def prob_density_normal_distrib(x, mean, variance):
    return (1 / sqrt(2 * pi * variance)) * (e ** (-(x - mean) ** 2 / 2 * variance))


# https://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function
# http://mathworld.wolfram.com/Erf.html
def cumulative_distribution_function(x, mean, stddev):
    p = 1 + erf((x - mean) / (stddev * sqrt(2)))
    return round(0.5 * p, 4)


def fn():
    max_total = int(input())
    boxes = int(input())
    mean = int(input())
    stddev = int(input())
    u = boxes * mean
    stddev2 = sqrt(boxes) * stddev
    print(cumulative_distribution_function(max_total, u, stddev2))

fn()


if __name__ == '__main__':
    pass
