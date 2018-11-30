'''
https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem
'''

from math import e as E


def factorial(n):
    acc = 1
    for i in range(n, 1, -1):
        acc *= i
    return acc


def poisson_distribution(success, avg):
    return ((avg ** success) * (E ** (-avg))) / factorial(success)


'''
a = 0.88
b = 1.55
'''


def run():
    a, b = map(float, input().split(" "))
    ca = 160 + 40 * (a + a * a)
    cb = 128 + 40 * (b + b * b)
    print("%.3f\n%.3f" % (ca, cb))


run()

if __name__ == '__main__':
    pass
