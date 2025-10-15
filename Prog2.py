from Validaciones import Validaciones 
val = Validaciones()

class Principal():
    def __init__(self):
        # Lista donde se guardarán las calificaciones
        # List where grades will be stored
        self.lista = []

        # Contador de cuántas calificaciones se han ingresado
        # Counter for how many grades have been entered
        self.num = 0

        # Variable temporal para guardar la entrada del usuario
        # Temporary variable to store the user's input
        self.a = ""

    def inicio(self):
        # Solicita una calificación al usuario
        # Asks the user to enter a grade
        self.a = input('Escribe una calificación: \n')

        # Verifica si la entrada es un número válido usando la clase Validaciones
        # Checks if the input is a valid number using the Validaciones class
        if val.validarnumeros(self.a):
            
            # Convierte la entrada a entero y la agrega a la lista
            # Converts the input to an integer and adds it to the list
            self.num += 1
            self.lista.append(int(self.a))

            # Si ya se ingresaron 5 calificaciones, muestra la lista y el promedio
            # If 5 grades have been entered, shows the list and the average
            if self.num >= 5:   
                print("\nCalificaciones ingresadas:", self.lista)
                print(f'El promedio es: {val.promedio(self.lista)}') 
            else:
                # Si aún no se han ingresado 5, vuelve a pedir otra calificación
                # If fewer than 5 have been entered, asks for another one
                self.inicio()
        else:
            # Si la entrada no es válida, muestra un mensaje de error y repite
            # If the input is invalid, shows an error message and repeats
            print("Error: Ingresa solo números válidos.")
            self.inicio()


# Punto de inicio del programa
# Program entry point
if __name__ == '__main__':
    app = Principal()
    app.inicio()
