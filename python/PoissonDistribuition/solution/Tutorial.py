'''
https://www.hackerrank.com/challenges/s10-poisson-distribution-1/tutorial
'''

from math import e as E


def fast_exp(b, e):
    if e == 0:
        return 1
    elif e == 1:
        return b
    elif e < 0:
        b, e = 1 / b, -e
    acc = 1
    while e > 0:
        if e & 1 == 1:
            acc *= b
        b *= b
        e >>= 1
    return acc


def fast_ncr(n, r):
    if r > n - r:
        r = n - r
    acc = 1
    for i in range(0, r):
        acc *= (n - i)
        acc //= (i + 1)
    return acc


'''
https://pt.wikipedia.org/wiki/Distribui%C3%A7%C3%A3o_de_Poisson
Experimento de poisson deriva de um caso da distribuicao binomial

Experimento de poisson
    + resultado de cada teste pode ser V/F (variavel de bernoulli)
    + a media de numero de ocorrencias de sucesso (lambda) ocorre numa especifica regiao conhecida
    + a quantidade de eventos considerados um sucesso e proporcional ao tamanho da regiao
    + a probabilidade de um evento de sucesso ocorrer numa regiao pequena e virtualmente 0
'''


def factorial(n):
    acc = 1
    for i in range(n, 1, -1):
        acc *= i
    return acc


def poisson_distribution(succees, avg_success):
    return (fast_exp(avg_success, succees) * (E ** -avg_success) ) / factorial(succees)


'''
Exemplo:
Uma data empresa vende em 2 casas por dia. Qual a probabilidade que tal empresa
venda 3 casas amanha
'''


def example_1():
    print(poisson_distribution(3, 2))


def example_2():
    acc = 0
    for i in range(0, 4):
        acc += poisson_distribution(i, 5)
    print(acc)


example_2()

'''
Seja X uma variavel Poisson Randomico.

Seja E[X] a experenca de X

Seja Var(X) a variancia de X, se uma variavel aleatoria
tiver uma distribuicao de poisson

E[X] = a media de sucessos de um dado evento (lambda)
Var(X) = Idem


Var(X) = E[x^2] - (E[X]) ^2
E[x^2] = Var(X) + E[x^2] 

E[x^2] = lambda + lambda ^2

'''

# print(E, fast_exp(E, 5))

if __name__ == '__main__':
    pass
