from statistics import mean

if __name__ == '__main__':
    materias=["Español","Matematicas", "quimica","fisica","Computaciom"]
    calificaciones=[]

    nombre= input("escribe tu nombre: ")

    for asignatura in materias:
        calif=float (input(f"dame la calificacion de {asignatura}"))
        calificaciones.append(calif)

    prome=mean (calificaciones)
    print(f"el promedio de {nombre} es {round(prome, 1)}")
