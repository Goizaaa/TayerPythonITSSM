#crear un metodo llamado agregar, paso un valor entero, lista.appen y retornar, imprimir 10 veces el metodo
def Lista(a:int)->list:
    lista=[]
    lista.append(a)
    return lista


if __name__ == '__main__':

    l=Lista("10")
    l=Lista("6")
    l=Lista("17")
    l=Lista("54")
    l=Lista("15")
    l=Lista("30")
    l=Lista("18")
    l=Lista(19)
    l=Lista(48)
    l=Lista(68)

    print("********* Lista original *********")
    for l in Lista:
        print(l)
