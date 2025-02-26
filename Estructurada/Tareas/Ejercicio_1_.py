#crear un metodo llamado agregar, paso un valor entero, lista.appen y retornar, imprimir 10 veces el metodo
"""
 Al revisar el código observo que tienes unas pequeñas observaciones. Bien finalemnte lo he corregido para que lo revises.
 Calificación 8
"""
def Lista(a,lista:list):
    lista.append(a)

if __name__ == '__main__':
    lista=[] #Comenzamos con una lista vacía.

    Lista("10",lista) #Aprovecha la fortaleza de la referencia a objeto.
    Lista("6",lista)
    Lista("17",lista)
    Lista("54",lista)
    Lista("15",lista)
    Lista("30",lista)
    Lista("18",lista)
    Lista(19,lista)
    Lista(48,lista)
    Lista(68,lista)

    print("********* Lista original *********")
    for l in lista:
        print(l)
