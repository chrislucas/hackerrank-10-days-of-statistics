'''
https://pt.wikipedia.org/wiki/Distribui%C3%A7%C3%A3o_binomial_negativa


A distribuicao binomial negativa eh a distribuicao de probabilidade discreta de um
numero de sucessos numa sequencia de identicos e independentes experimentos de bernoulli
antes de um especifico numero de resultados de falha ocorrer


indica o numero de tentativas necessarias para obter K-eventos de sucesso de
igual probabilidade X ao fim de N experimentos de bernoulli

a funcao de probabilidade eh:

b(n, k, p)
n - numero de evetos
k - sucessos (ou o k-esimo sucesso)
p - probabilidade de sucesso de cada eventos_

C(n-1, k-1) * p^k * (1-p)^(n-k)

'''

def fast_exp(b, e):
    if e == 0:
        return 1
    elif e == 1:
        return b
    elif e < 0:
        b, e = 1 / b, -e
    acc = 1
    while e > 0:
        if e & 1 == 1:
            acc *= b
        b *= b
        e >>= 1
    return acc


def fast_ncr(n, r):
    if r > n - r:
        r = n - r
    acc = 1
    for i in range(0, r):
        acc *= (n - i)
        acc //= (i + 1)
    return acc


'''
Negative Binomial Distribution - nbd

O experimento binomial negativo (NBE) eh um experimento com as seguintes propriedades

* consistem em n testes repetidos
* tentativas sao independentes
* o resultado da tentativa so pode ser sucesso ou fracasso {0, 1}
* a probabilidade de sucesso P(s) eh sempre a mesma
* o experimento continua ate x sucessos serem atingidos

'''

'''
x - numero de sucessos que se quer obter
n - numero de tentativas reaçozadas
p - probabilidade de sucesso
'''


def nbd(x, n, p):
    c = fast_ncr(n - 1, x - 1)
    s = fast_exp(p, x)
    f = fast_exp(1 - p, n - x)
    return c * s * f


'''
s - numero de sucesso
f - numero de fracassos
p - probabilidade de sucesso
'''
def nbd_2(s, f, p):
    ss = fast_exp(p, s)
    ff = fast_ncr(1-p, f)
    return fast_ncr(s+f-1,s) * ff * ss


if __name__ == '__main__':
    pass
