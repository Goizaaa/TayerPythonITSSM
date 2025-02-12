#nos muestra la potencia de un numero X a la Y
if __name__ == '__main__':
    print("El programa calculoa la potencia de x a la y ")
    x=int (input("Proporciona el valor de la base"))
    y=int (input("Proporciona el valor de la potencia"))

    i=1; resultado=1
    while i<=y:
        print (f"conteo{i}")
        resultado*=x #este es el acumulador
        i+=1

    print (f"el resultado de {x} a la {y} es {resultado}")

