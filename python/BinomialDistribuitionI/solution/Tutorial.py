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
    acc = 1
    while e > 0:
        if e & 1 == 1:
            b *= b
        acc *= b
        e >>= 1
    return acc


def binomial_coefficient(n, k):
    memo = [0] * (k + 1)
    memo[0] = 1
    for i in range(0, n):
        for j in range(min(i, k), 0, -1):
            memo[j] += memo[j - 1]
    return memo[k]


'''
    n = numero de sucessos
    k = numero de tentativas
'''

# https://stattrek.com/online-calculator/binomial.aspx
def binomial_probability(n, k, prob):
    coefficient = binomial_coefficient(n, k)
    return coefficient * fast_exp(prob, k) * fast_exp(1 - prob, n - k)


print(fast_exp(12, 4))

print(binomial_probability(10, 15, 0.5))

if __name__ == '__main__':
    pass
