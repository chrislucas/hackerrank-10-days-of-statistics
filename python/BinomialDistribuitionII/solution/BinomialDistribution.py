'''
https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
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


def fast_ncr(n, r):
    if r > n - r:
        r = n - r
    acc = 1
    for i in range(0, r):
        acc *= (n - i)
        acc //= (i + 1)
    return acc


def run():
    prob_fail, q_production = tuple(map(int, input().split(" ")))
    p = prob_fail / 100
    '''
        b(x, n, p)
        x = numero de sucessos esperados apos N tentativas
        n = numero de tentativas
        p = probabilidade de sucesso em cada tentativa individual
    '''
    # probabilidade de nao mais do que 2 pecas falharem
    prob_1 = 0
    for i in range(0, 3):
        prob_1 += fast_ncr(q_production, i) * fast_exp(p, i) * fast_exp(1 - p, q_production - i)

    prob_2 = 0
    for i in range(2, q_production+1):
        prob_2 += fast_ncr(q_production, i) * fast_exp(p, i) * fast_exp(1 - p, q_production - i)

    print("%.3f\n%.3f" % (prob_1, prob_2))


run()

if __name__ == '__main__':
    pass
