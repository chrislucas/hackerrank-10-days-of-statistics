'''
https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem
DONE
'''


def lsr(points):
    sum_x, sum_y, sum_xx, sum_xy = 0, 0, 0, 0
    for p in points:
        sum_xx += p[0] * p[0]  # x ^ 2
        sum_xy += p[0] * p[1]  # x * y
        sum_x += p[0]
        sum_y += p[1]

    n = len(points)
    # coeficiente angular
    m = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_xx) - (sum_x * sum_x))
    # equacao da reta = y = mx + b
    b = (sum_y - (m * sum_x)) / n

    return m, b


from math import floor
def run():
    points = [0] * 5
    for i in range(0, 5):
        points[i] = tuple(map(int, input().split(" ")))
    m, b = lsr(points)
    return round((m * 80 + b) * 10) / 10


print(run())

if __name__ == '__main__':
    pass
