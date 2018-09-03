'''
https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial
'''

'''
Variavel Randomica
https://en.wikipedia.org/wiki/Four-sided_die
https://en.wikipedia.org/wiki/Random_variable
https://pt.wikipedia.org/wiki/Vari%C3%A1vel_aleat%C3%B3ria

'''

'''
probability mass function
https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_massa_de_probabilidade
https://en.wikipedia.org/wiki/Probability_mass_function
https://en.wikipedia.org/wiki/Binomial_distribution#Probability_mass_function
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


def binomial_coefficient(n, k):
    memo = [0] * (k + 1)
    memo[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            memo[j] += memo[j - 1]
    return memo[k]


def ok_ncr(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(0, k):
        res *= (n - i)  # (n * n-1 ... * n-k+1)
        res //= (i + 1)  # dividir de (1 ... k)
    return res

'''
    n = numero de sucessos
    k = numero de tentativas
    prob = probabilidade de um evento dar certo dentro do conjunto
'''


# https://stattrek.com/online-calculator/binomial.aspx
def binomial_probability(trials, k_success, prob):
    coefficient = ok_ncr(trials, k_success)
    return coefficient * fast_exp(prob, k_success) * fast_exp(1 - prob, trials - k_success)


def e(n, p):
    return n * p

def variance(n, p):
    return n * p * (1-p)

def cumulative_probability():
    return

# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial
def solve_problem_tutorial():
    print(binomial_probability(10, 5, 0.5))
    acc = 0
    for x in range(0, 6):
        acc += binomial_probability(10, x, 0.5)
    print(acc)
    acc = 0
    for x in range(5, 11):
        acc += binomial_probability(10, x, 0.5)
    print(acc)
    return

solve_problem_tutorial()

print(binomial_coefficient(5, 5))

print(binomial_probability(15, 10, 0.5))

if __name__ == '__main__':
    pass
