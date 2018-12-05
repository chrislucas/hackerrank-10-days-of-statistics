'''
https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/tutorial
https://pt.wikipedia.org/wiki/Coeficiente_de_correla%C3%A7%C3%A3o_de_Pearson
'''

from math import sqrt


def covariance(data_x, data_y):
    mean_x = sum(data_x) / len(data_x)
    mean_y = sum(data_y) / len(data_y)
    acc = 0
    for i in range(0, len(data_x)):
        acc += (data_x[i] - mean_x) * (data_y[i] - mean_y)
    return acc * (1 / len(data_x))


def pearson_correlation_coefficient_2(data_x, data_y, stddev_x, stddev_y):
    mean_x = sum(data_x) / len(data_x)
    mean_y = sum(data_y) / len(data_y)
    acc = 0
    for i in range(0, len(data_x)):
        acc += (data_x[i] - mean_x) * (data_y[i] - mean_y)
    return acc * (1 / len(data_x))  / (stddev_x * stddev_y)


def pearson_correlation_coefficient(data_x, data_y, stddev_x, stddev_y):
    return covariance(data_x, data_y) / (stddev_x * stddev_y)


def stddev(data):
    mean = sum(data) / len(data)
    acc = 0
    for i in data:
        acc += (i - mean) * (i - mean)
    return sqrt(1 / len(data) * acc)


def fn():
    v = int(input().strip())
    val_x = list(map(float, input().strip().split(" ")))
    val_y = list(map(float, input().strip().split(" ")))
    print("%.3f" % pearson_correlation_coefficient(val_x, val_y, stddev(val_x), stddev(val_y)))


if __name__ == '__main__':
    fn()
