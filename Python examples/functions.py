# these functions can be very complicated
def complicated_function(x,y):  # definimos nombre de la funcion
    lenx = len(x)               # Calculamos longitud
    print(lenx) 
    leny = len(y)
    print(leny)
    z = [0]*(lenx*leny)         # z es un vector de muchos ceros y su longitud sera multiplicando a las longitudes para crear vector 0 de sus longitudes multiplicadas
    print(z) # imprimimos un vector para visualizar lenx*leny
    
    counter = 0 # Iniciamos contador desde cero

    for i in x: # Vamos a iniciar un for de i tomando los valores de x
        for j in y: # Vamos a iniciar un for de i tomando los valores de y
            z[counter] = i*j # el contador va de 0 (en este caso empieza con el numero 34) en la posicion del vector 0 va a multiplicar el 1 x 34 = 34 en la posicion cero de nuestro vector z
            counter = counter + 1 # sigue contando para multiplicar los lenx*leny valores (en este caso 16)
    return z # regresame el nuevo valor de z

output = complicated_function([1,2,3,4],[34,234,31,888]) # ejemplo de primer vector x,y con 4 valores cada uno
print(output) # imprime output que corresponde a la funcion complicated_function
