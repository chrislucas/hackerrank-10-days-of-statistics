'''
https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/tutorial
https://pt.wikipedia.org/wiki/Coeficiente_de_correla%C3%A7%C3%A3o_de_postos_de_Spearman
DONE
'''

from math import sqrt


def stddev(data):
    mean = sum(data) / len(data)
    acc = 0
    for v in data:
        acc += (v - mean) * (v - mean)
    return sqrt(1 / len(data) * acc)


def pearson_correlation(rank_x, rank_y):
    sdx = stddev(rank_x)
    sdy = stddev(rank_y)
    mean_x = sum(rank_x) / len(rank_x)
    mean_y = sum(rank_y) / len(rank_y)
    acc = 0
    for i in range(0, len(rank_x)):
        acc += (rank_x[i] - mean_x) * (rank_y[i] - mean_y)
    return acc * (1 / len(rank_x)) / (sdx * sdy)


from copy import deepcopy


def make_rank(data):
    rank = [1] * len(data)
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            rank[i] += rank[i - 1]
        else:
            rank[i] = rank[i - 1]
    return rank


def pearson_correlation_unique_values(data_x, data_y):
    cpx = deepcopy(data_x)
    cpx.sort()
    rank_x = make_rank(cpx)

    map_rank_x = {}
    for i in range(0, len(cpx)):
        map_rank_x[cpx[i]] = rank_x[i]

    cpy = deepcopy(data_y)
    cpy.sort()
    rank_y = make_rank(cpy)
    map_rank_y = {}
    for i in range(0, len(cpy)):
        map_rank_y[cpy[i]] = rank_y[i]

    acc, n = 0, len(data_x)
    for i in range(0, n):
        acc += (map_rank_x[data_x[i]] - map_rank_y[data_y[i]]) * (map_rank_x[data_x[i]] - map_rank_y[data_y[i]])
    return 1 - (6 * acc / (n ** 3 - n))


def fn():
    v = int(input().strip())
    val_x = list(map(float, input().strip().split(" ")))
    val_y = list(map(float, input().strip().split(" ")))
    print("%.3f" % pearson_correlation_unique_values(val_x, val_y))


'''
10
106 86 100 101 99 103 97 113 112 110
7 0 27 50 28 29 20 12 6 17

'''

if __name__ == '__main__':
    fn()
