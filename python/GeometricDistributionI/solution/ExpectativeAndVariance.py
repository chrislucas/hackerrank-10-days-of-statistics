'''
https://en.wikipedia.org/wiki/Geometric_distribution
'''
from pip._vendor.distlib.util import proceed

'''
a expectativa de numero de falhas antes do primeiro sucesso e dada pela formula
E(Y) = (1 - p) / p
onde p = probabilidade de sucesso

Tambem conhecido pela media de numero de falhas antes do primerio sucesso
'''


def expected(prob_success):
    return (1 - prob_success) / prob_success


def expected_value(prob_success):
    return 1 / prob_success


'''
Valor experado da distribuicao geometrica cuja funcao de probabilidade de massa seja
P(X) = (1 -p)^n * p - Funcao de probabilidade para falhas
A formula para variancia continua a mesma
'''


def expected_value_failure(prob_success):
    return (1 - prob_success) / prob_success


def variance(prob_success):
    return (1 - prob_success) / (prob_success * prob_success)


if __name__ == '__main__':
    pass
