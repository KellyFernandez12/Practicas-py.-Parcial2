
class Validaciones():
    def __init__(self):
        # Variable para almacenar la suma total de las calificaciones
        # Variable to store the total sum of the grades
        self.suma = 0

        # Variable para guardar el promedio calculado
        # Variable to store the calculated average
        self.promedio = 0.0


    def validarnumeros(self, valor):
        # Verifica si el valor ingresado es un número entero positivo
        # Checks if the entered value is a positive integer
        if valor.isdigit():
            return True
        else:
            return False


    def promedio(self, lista):
        # Reinicia la suma antes de calcular un nuevo promedio
        # Resets the sum before calculating a new average
        self.suma = 0

        # Recorre la lista sumando todos los valores
        # Iterates through the list adding up all values
        for i in lista:
            self.suma += i

        # Calcula el promedio dividiendo la suma entre el número de elementos
        # Calculates the average by dividing the sum by the number of elements
        self.promedio = self.suma / len(lista)

        # Devuelve el resultado del promedio
        # Returns the average result
        return self.promedio


        