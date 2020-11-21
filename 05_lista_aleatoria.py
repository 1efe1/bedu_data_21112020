# Generear una lista con valores aleatorios

from random import randint

# Lista vacia que contendra

lista_aleatoria = []

elementos = input('cuantos elemenots necesitas?')
elementos = int(elementos)



contador = 1

while contador <= elementos:

    # Generamos un valor aleatorio

    matriz = randit(1,100)
    


    valor = matriz * elementos
    print(valor)

    # guardar valor aleatorio en la lista

    lista_aleatoria(valor)

    # Sumar valor a contador para la siguiente vuelta

    contador = contador + 1

print(lista_aleatoria)


# ciclo while o ciclo mientras