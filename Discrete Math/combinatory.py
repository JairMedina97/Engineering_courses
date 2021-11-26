# Combinatory
from math import factorial
factorial(5) # subrutina existente
f = 1
for i in range(1,20):
    f *= i;
    print('{:d}! = {:d}'.format(i,f))

from itertools import permutations
p = list(permutations(['a','b','c','d']))
l = len(p)
print(l)

# coeficiente binomial
def binom(n,k):
    value = 1
    for factor in range(max(k, n - k) + 1, n + 1):
        value *= factor
    return value // factorial(min(k, n - k))

binom(10,2) == factorial(10) // factorial(10 - 2) * factorial(2)
print(binom(10,2))

from itertools import combinations
A = ['a','b','c','d']
for subconjunto in combinations(A,3):
    print(subconjunto)

from itertools import chain
k = 7
A = range(7)
contador = 0
c = chain.from_iterable(combinations(A, r) for r in range(k + 1))
for subconjunto in c:
    print(subconjunto)
    contador += 1

contador = 2**k
