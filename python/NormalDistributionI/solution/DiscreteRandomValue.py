def E(x, values):
    return x * sum(values)


def variance(k, values):
    p = sum(list(map(lambda x: x * x, values)))
    q = ((sum(values) ** 2) / k)
    return (1 / k) * (p - q)


from math import sqrt


def stddev(k, values):
    return sqrt(variance(k, values))


print(E(1 / 6, [1, 2, 3, 4, 5, 6]))
print(variance(6, [1, 2, 3, 4, 5, 6]))
print(stddev(6, [1, 2, 3, 4, 5, 6]))

if __name__ == '__main__':
    pass
