#apartir de una lista usar la lista para imprimir pares e impares

def ListasPares (x :[])->[]:
    lista=[]
    for elemento in x:
        if elemento%2==0:
            lista.append (elemento)
    return lista

def ListaImpares (x):
    lista=[]
    for elemento in x:
        if elemento%2 ==1:
            lista.append(elemento)
    return lista

if __name__ == '__main__':

    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    pares=ListasPares(numeros)
    impares=ListaImpares(numeros)
    print (f"Numeros pares {pares}")
    print (f"Numeros impares {impares}")
