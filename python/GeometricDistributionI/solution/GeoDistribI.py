'''
https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem
https://en.wikipedia.org/wiki/Negative_binomial_distribution
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


def run():
    p, s = map(int, input().split(" "))
    prob = p / s
    tries = int(input())
    return fast_exp(1 - prob, tries - 1) * prob


print("%.3f" % run())

if __name__ == '__main__':
    pass
