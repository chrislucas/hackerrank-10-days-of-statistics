'''
https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
'''

# https://en.wikipedia.org/wiki/Normal_distribution
# https://en.wikipedia.org/wiki/Cumulative_distribution_function
# https://se.mathworks.com/help/matlab/ref/erf.html
from math import erf

def cdf(x, mean, stddev):
    return .5 * (1 + erf((x - mean) / (stddev * 2 ** .5)))

def run():
    mean, stddev = tuple(map(int, input().split(" ")))
    less = float(input())
    print("%.3f" % cdf(less, mean, stddev))
    a, b = tuple(map(float, input().split(" ")))
    '''
        a equacao da curva normal utiliza 2 parâmetra: a media e o desvio padrao
        Denota-se N(m, dp) a curva normal com media 'm' e desvio padrao 'dp'
        A media refere-se ao centro da distribuicao e o desvio padrao ao achatamento da curva
        A distribuicao normal é simétrica em torno da média o que implica que a media,
        a mediana e a moda sao iguais
    '''
    # z1 = ((a - mean) / stddev)
    # z2 = ((b - mean) / stddev)
    print("%.3f" % (cdf(b, mean, stddev) - cdf(a, mean, stddev)))


run()

if __name__ == '__main__':
    pass
