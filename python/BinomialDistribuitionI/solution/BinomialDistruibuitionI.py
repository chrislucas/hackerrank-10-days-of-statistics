'''
https://www.hackerrank.com/domains/tutorials/10-days-of-statistics?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=10-days-of-statistics
'''

'''
Distribuicao binomial e uma distribuicao discreta de probabilidade de eventos que derao
certo numa sequencia de n experimentos independentes. Cada evento pode ter uma resposta
de SIM ou NAO.

Um experimento unico cuja resposta eh SIM/NAO eh denominado de Bernoulli Trial
DONE
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


def ok_ncr(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(0, k):
        res *= (n - i)  # (n * n-1 ... * n-k+1)
        res //= (i + 1)  # dividir de (1 ... k)
    return res


def binomial_distribution(trials, k_success, prob):
    trials, k_success = int(trials), int(k_success)
    ncr = ok_ncr(trials, k_success)
    s = fast_exp(prob, k_success)
    f = fast_exp(1 - prob, trials - k_success)
    return ncr * s * f


def run_2(trials):
    for p in range(0, 10):
        for k in range(0, 10):
            print("%f probability: %d success: %f distribution" % (p / 10, k, binomial_distribution(trials, k, p / 10)))
        print("")
    return


def run():
    trials, k_success, prob = tuple(map(float, input().split(" ")))
    return binomial_distribution(trials, k_success, prob)


# https://pt.wikipedia.org/wiki/Distribui%C3%A7%C3%A3o_binomial
def test():
    print(binomial_distribution(3, 2, 1 / 6) + binomial_distribution(3, 3, 1 / 6))


def run_3():
    b, g = tuple(map(float, input().split(" ")))
    p = b/(b+g)
    q = 1 - p
    acc = 0
    for i in range(3, 7):
        acc += ok_ncr(6, i) * fast_exp(p, i) * fast_exp(q, 6-i)
    return "%.3f" % acc

print(run_3())

if __name__ == '__main__':
    pass
