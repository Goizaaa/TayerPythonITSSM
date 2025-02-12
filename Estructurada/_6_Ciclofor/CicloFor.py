import sys


if __name__ == '__main__':
    for i in range (10):
        print (f"{i}", end="")


        print("-----------------")

    for j in range(1,20):
        print (f"{j}", end="") #esto de end" " se usa para anular el salto de linea del print

    sys.stdout.write("Texto sin salto de linea") #funcion utilizada para imrpimir en pantalla son el salto


    print("------------------------")
    lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    #una lista puede contener valores de cualquier tipo
    #ademas una lista es mutable

    for elemento in lista:
        print(elemento)


    lista.add(200) #es lo mutable, se agrega el 200

    for elemento in lista:
        print(elemento)