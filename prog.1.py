''' 
Programa que solicita 5 calificaciones al usuario y las guarda en una lista.
Al final, muestra todas las calificaciones ingresadas.
Program that asks the user for 5 grades and stores them in a list.
At the end, it displays all the entered grades.
'''

def inicio(num):
    # Función que pide una calificación al usuario y controla la cantidad de entradas
    # Function that asks the user for a grade and keeps track of the number of entries
    a = int(input('Escribe una calificación:\n'))

    # Aumenta el contador para saber cuántas calificaciones se han ingresado
    # Increases the counter to know how many grades have been entered
    num += 1

    # Agrega la calificación a la lista global
    # Adds the grade to the global list
    lista.append(a)

    # Si ya se ingresaron 5 calificaciones, muestra la lista
    # If 5 grades have been entered, show the list
    if num >= 5:
        print("Calificaciones ingresadas:", lista)
    else:
        # Si aún no son 5, vuelve a pedir otra calificación
        # If fewer than 5, ask for another grade
        inicio(num)


# Lista vacía donde se guardarán las calificaciones
# Empty list where grades will be stored
lista = []

# Inicializa el contador en 0
# Initializes the counter at 0
num = 0

# Punto de inicio del programa
# Program entry point
if __name__ == '__main__':
    inicio(num)
