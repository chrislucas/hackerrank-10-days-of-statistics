'''
http://www.de.ufpb.br/~tarciana/MPIE/Aula7.pdf
Calculadora para testar o processo de bernoulli
https://planetcalc.com/7044/
https://pt.wikipedia.org/wiki/Distribui%C3%A7%C3%A3o_de_Bernoulli
https://planetcalc.com/5390/
'''


def fast_exp(b, e):
    if e == 0:
        return 1
    elif e == 1:
        return b
    elif e < 0:
        b, e = 1/b, -e
    acc = 1
    while e > 0:
        if e & 1 == 1:
            acc *= b
        b *= b
        e >>= 1
    return acc


def ok_ncr(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(0, k):
        res *= (n - i)  # (n * n-1 ... * n-k+1)
        res //= (i + 1)  # dividir de (1 ... k)
    return res


def bernoulli_distribution(events, prob):
    for k_success in range(0, events+1):
        ncr = ok_ncr(events, k_success)
        s = fast_exp(prob, k_success)
        f = fast_exp(1-prob, events-k_success)
        r = ncr * s * f
        print("Numero de sucesso: %d %.8f" % (k_success, r))
    return


def test_exp():
    print(fast_exp(0.5, -3))
    print(fast_exp(10, -3))


bernoulli_distribution(4, 0.5)

if __name__ == '__main__':
    pass
