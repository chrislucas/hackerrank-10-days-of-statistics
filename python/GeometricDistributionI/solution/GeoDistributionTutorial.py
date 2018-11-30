'''
https://www.hackerrank.com/challenges/s10-geometric-distribution-1/tutorial
https://pt.wikipedia.org/wiki/Distribui%C3%A7%C3%A3o_geom%C3%A9trica
https://en.wikipedia.org/wiki/Geometric_distribution

Constituida por duas funcoes de probabilidade discreta

* distribuicao de probabildade do numero X de experimentos de bernoulii
necessarios para obter 1 resultado de sucesso

* a distribuicao de probabilidade Y = X-1 de falhas antes do primerio ceusso

calculadora de distribuicao geometrica
http://www.elektro-energetika.cz/calculations/distrgeo.php

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


'''
Probabilidade de alcancar um sucesso apos n-1 falhas
g(n, p)
n - numero de tentativas
p - probabilidade de sucesso em cada tentativa
1-p = probailidade de falha
n-1 = numero de falhas maximo (n testes, n-1 testes resultando em falha e o n-esimo em sucesso)
q = 1-p
P(X) = q ^ (n-1) * p
'''


def geo_distribution_success(n, p):
    return fast_exp(1 - p, n - 1) * p


'''
probabilidade de obter n falhas ate o primeiro sucesso
n = numero de falhas
p = probabilidade de sucesso a cada teste
q = 1-p -> probabilidade de falha a cada teste

P(X) = q ^ (n) * p
'''


def geo_distribution_failure(n, p):
    return fast_exp(1 - p, n) * p


'''
a probabilidade de sucesso de cada evento eh 0.7
qual a probabilidade de se obter o primero sucesso na quinta tentativa ?
'''
print(geo_distribution_success(5, 0.7))
print(geo_distribution_success(10, 0.3))
print(geo_distribution_success(11, 0.3))

'''
a probabilidade de sucesso de cada evento eh 0.7
qual a probabilidade de se obter o primeiro sucesso apos 5 falhas ?
'''
print("qual a probabilidade de se obter o primeiro sucesso apos 5 falhas ? %f" % geo_distribution_failure(5, 0.7))

# apos 4 falhas espera-se que o resultado seja o mesmo da pergunta 1
print(geo_distribution_failure(4, 0.7))
# idem para 2
print(geo_distribution_failure(9, 0.3))
# idem para 3
print(geo_distribution_failure(10, 0.3))

if __name__ == '__main__':
    pass
