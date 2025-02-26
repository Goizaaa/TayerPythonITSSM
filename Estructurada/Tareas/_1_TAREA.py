#Tarea 12 de Febrero del 2025
"""
   Una vez que conociste los tipos de datos de la categoría Collections de Python
   Ahora la tarea consiste en declarar una variabla para cada elemento, ingresa de forma manual, al menos 30 valores para cada elemento,
   y finalmente utiliza un for para imprimir cada uno de sus elementos en pantalla.
   Fecha límite de entrega: Lúunes 17 de febrero del 2025

   ¡Éxito en esta actividad!
"""
# Lista
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
print("Lista:")
for elemento in mi_lista:
    print(elemento)

# Tupla
mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
print("\nTupla:")
for elemento in mi_tupla:
    print(elemento)

# Conjunto
mi_conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
print("\nConjunto:")
for elemento in mi_conjunto:
    print(elemento)

# Diccionario
mi_diccionario = {
    1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco', 6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve', 10: 'diez',
    11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce', 15: 'quince', 16: 'dieciséis', 17: 'diecisiete', 18: 'dieciocho',
    19: 'diecinueve', 20: 'veinte', 21: 'veintiuno', 22: 'veintidós', 23: 'veintitrés', 24: 'veinticuatro', 25: 'veinticinco',
    26: 'veintiséis', 27: 'veintisiete', 28: 'veintiocho', 29: 'veintinueve', 30: 'treinta'
}
print("\nDiccionario:")
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")