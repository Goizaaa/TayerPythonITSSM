def contar_hasta(n)->tuple[str,int]:
    count=1
    potencia=0
    while count <=n:
        potencia:int=count**2
        valor:str=f"valor: {count}"
        yield (valor, potencia)# refleja dos valores o en
        count +=1

if __name__ == '__main__':

    for numero,potencia in contar_hasta(5):
        print(f"Para {numero} su potencia es {potencia}")
        input("parando el proceso")#este puede detener el while
