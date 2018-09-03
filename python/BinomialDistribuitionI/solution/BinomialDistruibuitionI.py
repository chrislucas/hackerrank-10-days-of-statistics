'''
https://www.hackerrank.com/domains/tutorials/10-days-of-statistics?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=10-days-of-statistics
'''


'''
Distribuicao binomial e uma distribuicao discreta de probabilidade de eventos que derao
certo numa sequencia de n experimentos independentes. Cada evento pode ter uma resposta
de SIM ou NAO.

Um experimento unico cuja resposta eh SIM/NAO eh denominado de Bernoulli Trial
'''


def fast_exp(b, e):
    if e == 0:
        return 1
    elif e == 1:
        return b
    elif e < 0:
        b, e = 1/b, -e
    acc = 1
    while e > 0:
        if e & 1 == 1:
            acc *= b
        b *= b
        e >>= 1
    return acc

def ok_ncr(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(0, k):
        res *= (n - i)  # (n * n-1 ... * n-k+1)
        res //= (i + 1)  # dividir de (1 ... k)
    return res


def binomial_distribution(events, prob):
    return


def run():
    return

if __name__ == '__main__':
    pass