'''
https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
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


def factorial(n):
    acc = 1
    for i in range(n, 1, -1):
        acc *= i
    return acc


def poisson_distribution(succees, avg_success):
    return (fast_exp(avg_success, succees) * E ** -avg_success) / factorial(succees)


def run():
    avg = float(input())
    s = int(input())
    print("%.3f" % poisson_distribution(s, avg))


run()

if __name__ == '__main__':
    pass
