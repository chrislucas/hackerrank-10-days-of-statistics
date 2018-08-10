'''
https://www.hackerrank.com/challenges/s10-weighted-mean/problem
DONE
'''
def run():
    n = int(input())
    nums = [int(x) for x in input().split(" ")]
    weights = [int(x) for x in input().split(" ")]
    s = sum(weights)
    t = sum(map(lambda x, y: x * y, nums, weights))
    return "%.1f" % (t/s)


print(run())


if __name__ == '__main__':
    pass