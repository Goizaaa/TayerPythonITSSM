def suma(a:int, b:int, lista:list):
    lista.append(a)
    lista.append(b)

def otraSuma(a:int, b:int, suma, int):
    suma=a+b

def metodovacio():
    pass

if __name__ == '__main__':

    miLista=[]

    suma(3,10,miLista)

    print (miLista)

    suma=0
    otraSuma(3,10,suma)
    print(suma)