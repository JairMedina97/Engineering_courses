# Discrete Math in python

# Capitulo 1 Logica
print(('hola '+'mundo ') * 2)
# Operaciones basicas en python
3 + 5 #sumar
9 - 3 #restar
4 * 6 #multiplicar
2 ** 3 # dos elevado a la potencia tres
a = 1234567 # guardamos un valor en una variable
b = 17 # guardamos otro valor
a // b # cuantas veces b cabe en a
a % b # cuanto es el residuo
a % b == 0 # si a es divisible entre b
# Los valores guardado se pueden imprimir 
print(a)
print(a,b)
nombre = 'Jair'
print('hola, {:s}'.format(nombre))
from math import pi
pi
print('pi vale {:f}'.format(pi))

# 1.1 Notacion matematica
# 1.1.1 Conjuntos
# Diagrama Venn
A = {'a','b','c'} # un conjunto
len(A) # Cardinalidad
'a' in A # comprobar existencia
'd' in A
'b' not in A # comprobar que no pertenezca
'e' not in A

A = {1,2,3}
B = {'x','y','z'}
A.union(B)
A|B #Lo mismo que union()
C = {1,3,5}
A.intersection(C)
A & C # lo mismo que intersection()
A.difference(C)
A - C # lo mismo que difference()


# Subconjuntos
a = {0,1,2,3,4,5,6,7,8}
b == set(range(9)) # un conjunto de 0 hasta 8
a == b
c = {1,3,5}
c.issubset(a) # si c es un subconjunto de A
# b.issuperset(c)  si C es un subconjunto de b

# E cuantificacion existencial A cuantificacion universal
A = {1,3,5,7}
all(a % 2 == 1 for a in A) # si todos son impares
all(a % 5 == 0 for a in A) # si por lo menos uno es divisible

# 1.2 representacion digital en bit
for potencia in range(37):
    print(2**potencia)
# 1.2.1 Unidades de informacion byte
x = 250
bin(x) #binario
oct(x) #octal
hex(x) #hexadecimal
a = 0.6/0.2
b = int(a)
print(a)
print(b)

# Logica booleana
b = not (9 == 6)
c = a and b
d = a or b

# Definimos subrutinas para and, or & xor
def xor(a,b):
    return (a or b) and not (a and b)

xor(True, False)
xor(True, False)

def impl(a,b):
    return (not a) or b

impl(True, False)
impl(False, False)
impl(True, True)

def equi(a,b):
    return impl(a,b) and impl(b,a)

equi(True, False)
equi(False, False)

# 1.3. Aritmetica binaria
a = 1000
b = 7
#˜a los ceros a unos y vice versa
a & b # y binario
a | b # o binario
#a ˆ b o-exclusivo binario
a << b # agregar b ceros a la derecha
a >> b # quitar b bits a la izquierda
