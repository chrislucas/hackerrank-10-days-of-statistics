'''
https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem
DONE
'''

from math import erf


# cumulative_distribution_function
def cdf(x, mean, stddev):
    return 0.5 * (1 + erf((x - mean) / (stddev * (2 ** .5))))


def run():
    mean, stddev = 70, 10
    a = 1 - cdf(80, mean, stddev)
    b = 1 - cdf(60, mean, stddev)
    c = cdf(60, mean, stddev)
    print("%.2f\n%.2f\n%.2f" % (a*100, b*100, c*100))

run()

if __name__ == '__main__':
    pass
