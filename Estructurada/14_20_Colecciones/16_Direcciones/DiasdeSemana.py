def dia_de_la_semana(numero_dia:int)->str:
    dias_semana={

        1: "lunes",
        2: "martes",
        3: "Miercoles",
        4:"jueves",
        5:"viernes",
        6:"sabado",
        7:"domingo",

    }
    #return dias_semana[numero_dia] este es el bug
    return dias_semana.get(numero_dia,"dia no valido")

if __name__ == '__main__':
    numero=3
    print(dia_de_la_semana(numero))
