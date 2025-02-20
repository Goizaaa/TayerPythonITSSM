from typing import List

#List es la lista avanzada tipada y necesita ser importada
#lista normal nativa de python

if __name__ == '__main__':

    lista_Tipada:List [int]= [5,12,25,33,47,58,63,77,82,91,4,1]

    lista_Tipada.append(1000)

    print("imprimiendo de forma tradicional")
    for elemento in lista_Tipada:
        print (elemento, end=", ")
