'''
https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
'''


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


def distribution(p, n):
    return fast_exp(1 - p, n - 1) * p


def solution1(tries, prob):
    acc = 0
    for i in range(1, tries + 1):
        acc += distribution(prob, i)
    return acc


'''
O problema proposto eh:

A probabilidade de se produzir uma peça defeituosa eh de 1/3. Qual a probabilidade
de a primeira peça defeitusa estar entre as 5 primeiras peças inspecionadas P(x <= 5) ?
X = [1,2,3,4,5] -> pecas inspecionadas
P(X) = (1 - (probabilidade de defeito)) ^ (X - 1) * (probabilidade de defeito)

Solucao proposta no forum de discussoes sem usar um somatorio, poupando processamento:

Primeiro calcula-se a probabilidade de encontrar um defeito apos as 5 inspecoes
P(x > 5), ou seja as 5 primeiras pecas nao possuem defeito

Usando a ideia de complemento (1 - p) podemos chegar a probabilidade de achar uma
peca defeituosa nas primeiras 5 inspecoes P(x <= 5) com a formula - 1 - P(x > 5)

P(x > 5) = (1 - probabilidade de sucesso) ^ 5 ou 'T'
P(x <= 5) = 1 - T

'''


def solution2(tries, prob):
    return 1 - (fast_exp(1 - prob, tries))


def run():
    p, s = map(int, input().split(" "))
    prob = p / s
    tries = int(input())
    return solution2(tries, prob)


print("%.3f" % run())

if __name__ == '__main__':
    pass
