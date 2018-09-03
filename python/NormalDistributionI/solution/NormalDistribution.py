'''
https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
'''


def run():
    mean, stddev = tuple(map(int, input().split(" ")))
    #less = float(input())
    a, b = tuple(map(int, input().split(" ")))
    '''
        a equacao da curva normal utiliza 2 parâmetra: a media e o desvio padrao
        Denota-se N(m, dp) a curva normal com media 'm' e desvio padrao 'dp'
        A media refere-se ao centro da distribuicao e o desvio padrao ao achatamento da curva
        A distribuicao normal é simétrica em torno da média o que implica que a media,
        a mediana e a moda sao iguais
    '''
    z1 = 1 - (abs(a - mean) / stddev)
    z2 = 1 - (abs(b - mean) / stddev)

    print(z1 + z2)

run()

if __name__ == '__main__':
    pass