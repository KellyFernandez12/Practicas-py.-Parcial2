
from tkinter import *                # Importa todas las funciones de la librería tkinter / Imports all functions from the tkinter library
from tkinter import messagebox        # Importa la función para mostrar mensajes emergentes / Imports messagebox for pop-up messages

class principal():                    # Define la clase principal del programa / Defines the main class of the program
    def __init__(self):               # Constructor de la clase / Class constructor
        self.ven = Tk()               # Crea la ventana principal / Creates the main window
        self.ven.title('Programa 5 con ventanas')  # Establece el título de la ventana / Sets the window title
        self.ven.geometry('450x250')  # Define el tamaño de la ventana / Sets the window size
        self.lista = []               # Crea una lista vacía para guardar promedios / Creates an empty list to store averages
        self.inicio()                 # Llama al método que construye los elementos de la ventana / Calls the method that builds the window UI

    def sumar(self):                  # Método para sumar los valores de la lista / Method to sum the list values
        s = 0                         # Inicializa la variable suma / Initializes sum variable
        for i in self.lista:          # Recorre cada elemento en la lista / Loops through each item in the list
            s += i                    # Suma cada elemento / Adds each item
        return s                      # Retorna la suma total / Returns the total sum    

    def promediar(self):              # Método para calcular el promedio / Method to calculate the average
        try:
            a = float(self.n1.get())  # Obtiene el valor del primer cuadro de texto y lo convierte a número / Gets and converts the first entry to a number
            b = float(self.n2.get())  # Obtiene el valor del segundo cuadro de texto / Gets the second entry value
            c = float(self.n3.get())  # Obtiene el valor del tercer cuadro de texto / Gets the third entry value
            d = float(self.n4.get())  # Obtiene el valor del cuarto cuadro de texto / Gets the fourth entry value
            pro = (a + b + c + d) / 4 # Calcula el promedio / Calculates the average
            self.l6.config(text=str(pro))  # Muestra el promedio en la etiqueta / Displays the average on the label
            self.lista.append(pro)         # Agrega el promedio a la lista / Adds the average to the list
            self.l7.config(text=str(self.lista))  # Muestra la lista de promedios / Displays the list of averages

            # Limpia las cajas de texto / Clears the input boxes
            self.n1.delete(0, END)
            self.n2.delete(0, END)
            self.n3.delete(0, END)
            self.n4.delete(0, END)

            suma = self.sumar()             # Llama al método sumar / Calls the sum method
            p = suma / len(self.lista)      # Calcula el promedio general / Calculates the general average
            self.l8.config(text=f' promedio general: {str(p)}')  # Muestra el promedio general / Displays the general average

        except ValueError:  # Si hay un error al convertir a número / If there's an error converting to number
            messagebox.showerror("Error", "Algun dato no es numero")  # Muestra mensaje de error / Shows error message
            # Limpia las cajas de texto en caso de error / Clears input boxes in case of error
            self.n1.delete(0, END)
            self.n2.delete(0, END)
            self.n3.delete(0, END)
            self.n4.delete(0, END)

    def salir(self):                   # Método para cerrar la ventana / Method to close the window
        self.ven.destroy()             # Cierra la ventana / Destroys the window    

    def inicio(self):                  # Método que construye la interfaz / Method that builds the interface
        l1 = Label(self.ven, text="Escribe un numero").place(y=10, x=20)  # Etiqueta 1 / Label 1
        l2 = Label(self.ven, text="Escribe un numero").place(y=50, x=20)  # Etiqueta 2 / Label 2
        self.n1 = Entry(self.ven)      # Caja de texto 1 / Textbox 1
        self.n1.place(y=10, x=150)     # Posición de la caja 1 / Position of textbox 1
        self.n2 = Entry(self.ven)      # Caja de texto 2 / Textbox 2
        self.n2.place(y=50, x=150)     # Posición de la caja 2 / Position of textbox 2

        l3 = Label(self.ven, text="Escribe un numero").place(y=90, x=20)  # Etiqueta 3 / Label 3
        l4 = Label(self.ven, text="Escribe un numero").place(y=130, x=20) # Etiqueta 4 / Label 4
        self.n3 = Entry(self.ven)      # Caja de texto 3 / Textbox 3
        self.n3.place(y=90, x=150)     # Posición de la caja 3 / Position of textbox 3
        self.n4 = Entry(self.ven)      # Caja de texto 4 / Textbox 4
        self.n4.place(y=130, x=150)    # Posición de la caja 4 / Position of textbox 4

        l5 = Label(self.ven, text="Promedio").place(y=150, x=130)  # Etiqueta para promedio / Label for average
        self.l6 = Label(self.ven, text="0.0")                      # Etiqueta que muestra promedio individual / Label showing individual average
        self.l6.place(y=150, x=200)

        b1 = Button(self.ven, text="Promedio", command=self.promediar).place(y=50, x=300)  # Botón para calcular promedio / Button to calculate average
        b2 = Button(self.ven, text="Salir", command=self.salir).place(y=90, x=300)         # Botón para salir / Button to exit

        self.l7 = Label(self.ven, text="[]")                     # Etiqueta que muestra la lista de promedios / Label showing list of averages
        self.l7.place(y=170, x=200)
        self.l8 = Label(self.ven, text="Promedio general: 0.0")  # Etiqueta para mostrar el promedio general / Label showing general average
        self.l8.place(y=190, x=150)

        self.ven.mainloop()   # Ejecuta el ciclo principal de la ventana / Runs the main loop for the window


if __name__ == '__main__':   # Punto de entrada del programa / Program entry point
    app = principal()        # Crea una instancia de la clase principal / Creates an instance of the main class
