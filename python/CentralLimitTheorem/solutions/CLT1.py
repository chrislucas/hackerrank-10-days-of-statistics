
from math import  erf, sqrt
# DONE

# https://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function
# http://mathworld.wolfram.com/Erf.html
def cumulative_distribution_function(x, mean, stddev):
    p = 1 + erf((x - mean) / (stddev * sqrt(2)))
    return round(0.5 * p, 4)


def fn():
    max_total = int(input())
    boxes = int(input())
    mean = int(input())
    stddev = int(input())
    u = boxes * mean
    stddev2 = sqrt(boxes) * stddev
    print(cumulative_distribution_function(max_total, u, stddev2))


if __name__ == '__main__':
    fn()