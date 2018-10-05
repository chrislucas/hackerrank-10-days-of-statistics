'''
https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem
https://en.wikipedia.org/wiki/Negative_binomial_distribution
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

if __name__ == '__main__':
    pass