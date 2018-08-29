'''
https://www.mathsisfun.com/data/standard-deviation-formulas.html

Bessel's correction
https://en.wikipedia.org/wiki/Bessel%27s_correction

'''


def sample_mean(values, n):
    return sum(values) / n

'''
O calculo eh o mesmo usado para o desvio padrao 'populacional'
porem encontramos formulas que usam simbolos diferentes para
o valor da media do conjunto de valores. A segunda diferenca
na formula a razao do somatorio pelo quantidade de valores
na amostra -1
'''
def sample_variance(values, n):
    mean = sample_mean(values, n)
    acc = 0
    for i in values:
        acc += (i - mean) * (i - mean)
    return acc / (n-1)

def variance(values, n):
    mean = sample_mean(values, n)
    acc = 0
    for i in values:
        acc += (i - mean) * (i - mean)
    return acc / n


from math import sqrt


def sample_stddev(values, n):
    return sqrt(sample_variance(values, n))


_list = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]
stddev = sqrt(variance(_list, len(_list)))

_list = [9,2,5,4,12,7]
sstddev = sample_stddev(_list, len(_list))

print("%.10f %.10f %.10f" % (stddev, sstddev, stddev / sstddev))


if __name__ == '__main__':
    pass
