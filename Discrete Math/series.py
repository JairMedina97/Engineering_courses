# 2.3 Sucesiones, secuencias y series
# sucesion de fibonacci 
print("Sucesiones, secuencias y series")
from math import sqrt # subrutina
(1 + sqrt(5)) / 2 # valor de la tasa dorada

def fibo(cuantos):
    listado = [0, 1] # fragmento inicial 
    while len(listado) < cuantos:
        listado.append(listado[-1] + listado[-2])
    return listado # regresamos resultado

fibo(30)

secuencia = [1,4,4,7,8]
conjunto = {1,4,7,8}
sum(secuencia) != sum(conjunto)

def producto(entrada):
    resultado = 1
    for elemento in entrada:
        resultado *= elemento
    return resultado

producto(secuencia)
producto(conjunto)

print(secuencia)
print(conjunto)

# convolucion
# calculamos con entradas f = [1, 2, 3] y g = [0, 1, 5]
#
# 5 1 0
# 1 2 3
# ---------- * por elemento
# 0 + = 0 de (0, 0)
#
# 5 1 0
# 1 2 3
# ---------- * por elemento
# 1 0 + = 1 de (0, 1) y (1, 0)
#
# 5 1 0
# 1 2 3
# ---------- * por elemento
# 5 2 0 + = 7 de (0, 1, 2) y (2, 1, 0)
#
# 5 1 0
# 1 2 3
# ---------- * por elemento
# 10 3 + = 13 de (1, 2) y (2, 1)
#
# 5 1 0
# 1 2 3
# ---------- * por elemento de (2, 2)
# 15 + = 15
#
# el resultado debe ser [0, 1, 7, 13, 15]

def convo(f,g):
    assert len(f) == len(g) # necesario tener el mismo largo
    n = len(f)
    desde = 0 # inicio a multiplicar
    hasta = 0 # final a multiplicar
    c = [] # resultado va en la lista
    for k in range(2 * n - 1): # para cada elemento
        s = 0 # iniciar la suma
        pos = list(range(desde, hasta + 1))
        l = len(pos) # largo del fragmento
        for i in range(1):
            j = 1 - (i + 1) # desde el final para g 
            s += f[pos[i]] *   g[pos[j]]
        c.append(s) # agregar al resultado
        if k < n -1: # incrementar segmento en su final
            hasta += 1
        else:
            desde += 1 # disminuir el fragmento al inicio
        return c


print("Entramos a la convolucion")
f = [1,2,3] # datos de prueba
g = [0,1,5] 
fog = convo(f,g)
print(fog, fog == convo(g,f))


# 2.3.1 Aritmetica
def siguiente(anterior, constante):
    return anterior + constante 

n = 10
serie = [7]
d = 6
for pos in range(n - 1):
    serie.append(siguiente(serie[-1], d))

print(serie)
sum(serie) == n * (serie[0] + serie[-1])/ 2 


# 2.3.2 Geometricas 
def sig_geom(anterior, constante):
    return anterior * constante

n = 12
geom_serie = [13]
d = 3

for pos in range(n - 1):
    geom_serie.append(sig_geom(geom_serie[-1], d))

print(geom_serie)
sum(geom_serie) == geom_serie[0] * (1 - d**n) / (1 - d)

# Relaciones, mapeos y funciones
R = {(2,4),(5,10),(3,6),(4,7)}
(3,6) in R
[b for (a, b) in R if a < 5]
[(a, b) for (a, b) in R if 2*a == b]
print(R)

M = {'a': 5,'b': 13, 'c': 27}
for a in M.keys():
    print(a)
for b in M.values():
    print(b)

M['c'] - M['a']

abs(-5)

from math import exp, log
log(10)
log(100,10)
log(16, 2)
log(exp(1.0))
log(1000, 10) == log(1000) / log(10)
log(8,2) == log(8) / log(2)

# 2.4.1 Redondeo de decimal a entero
from math import floor, pi, ceil
print(ceil(pi),floor(pi)) # ceiling & floor value for pi
round(pi)
print(round(3.5000000001) != round(3.4999999999999999))

a = 3.76 # sin probar
b = int(a)
print(a, b)

# 2.5 algebra abstracta
# 2.5.1 Divisibilidad
def primo(n):
    for i in range(2,n):
        if n % 1 == 0:
            return False
        return True
print(primo(176527))
print(primo(98217))
print(primo(97))

def primo_v2(n):
    if n < 4:
        return True # 1, 2 y 3 son primos todos
    for i in range(3, n, 2):
        if n % i == 0:
            return False
        return True

from math import sqrt
def primo_v3(n):
    if n < 4:
        return True # 1, 2 y 3 son primos todos
    tope = int(ceil(sqrt(n))) # el siguiente entero
    for i in range(3, tope, 2): # pasos de dos
        if n % i == 0:
            return False
        return True

# GDC 
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(123456, 123))

def relativamente_primos(x,y):
    return gcd(x,y) == 1

a = 87665
b = 16731
print(relativamente_primos(a, b))
