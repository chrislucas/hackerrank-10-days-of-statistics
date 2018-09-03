'''
https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/
'''

'''
C(n, k) = n! / (n-k)! * k!
ou
C(M, k) = n * ... (n-k+1) / (k * k-1 * k-2 ... * 1)
ou
C(n, k) = C(n, n-k) = 

(n * n-1 ... * n-k+1)  / (k * k-1 * ... * 1)
'''


def ok_ncr(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(0, k):
        res *= (n - i)  # (n * n-1 ... * n-k+1)
        res //= (i + 1)  # dividir de (1 ... k)
    return res


def run():
    n, k = tuple(map(int, input().split()))
    print(ok_ncr(n, k))


run()

if __name__ == '__main__':
    pass
