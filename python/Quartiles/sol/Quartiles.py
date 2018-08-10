'''
https://www.hackerrank.com/challenges/s10-quartiles/problem

https://en.wikipedia.org/wiki/Quartile
https://en.wikipedia.org/wiki/Quantile

DONE

'''

def calc_q1(n, nums):
    half = (n // 2)
    if n > 4:
        # se ao cortar o array na metade temos 2 metades impares
        if (half & 1) == 1:
            # dividimos novamente ao meio
            t = nums[half//2]
            q1 = t
        # senao, pegamos o elemento na posicao de 1/4 do array e o elemento a sua direita
        else:
            t = nums[half//2-1] + nums[half//2]
            q1 = t // 2
    else:
        # se o array tiver 2 elementos pegamos os 2 elementos mesmo
        q1 = (nums[0] + nums[1]) // 2
    return q1


def calc_q3(n, nums):
    half = (n // 2)
    if n > 4:
        m = (n-half)//2+half
        if (half & 1) == 1:
            t = nums[m]
            q3 = t
        else:
            if (n & 1) == 0:
                m -= 1
            t = nums[m] + nums[m+1]
            q3 = t // 2
    else:
        q3 = (nums[0] + nums[1]) // 2
    return q3


def run():
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    q1 = calc_q1(n, nums)
    q2 = nums[n // 2] if (n & 1) == 1 else (nums[n//2] + nums[n//2-1]) // 2
    q3 = calc_q3(n, nums)
    return "%d\n%d\n%d" % (q1, q2, q3)


'''
9
3 7 8 5 12 14 21 13 18

11
6 7 15 36 39 40 41 42 43 47 49

6
7 15 36 39 40 41

10
3 7 8 5 12 14 21 15 18 14


12
4 17 7 14 18 12 3 16 10 4 4 12
'''

print(run())
if __name__ == '__main__':
    pass
