if __name__ == '__main__':

    diccionario ={}

    diccionario [("Ana",25)] ="Estudiantes"
    diccionario [("Luis",30)] ="Ingeniero"
    diccionario [("Carlos",40)] ="Abogado"

    #accede a los valores del diccionario usando la tupla
    ocupacion_ana =diccionario[("Ana",25)]
    ocupacion_luis =diccionario[("Luis",30)]

    print (f"Ana es: {ocupacion_ana}")
    print (f"Luis es: {ocupacion_luis}")


