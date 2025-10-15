from tkinter import * 
from tkinter import messagebox

def Ventana():
    # Función que crea la ventana principal / Function that creates the main window
    def revisar():
        # Función que valida el usuario y contraseña / Function that validates username and password
        try:
            u = str(us.get())  # Obtiene el texto ingresado en la caja de usuario / Gets text from username entry
            p = str(pas.get()) # Obtiene el texto ingresado en la caja de contraseña / Gets text from password entry

            # Validación de usuario y contraseña / Username and password validation
            if u == 'admin' and p == '12345':
                messagebox.showinfo('Validación', 'Usuario y contraseña correctos')  
            else:
                messagebox.showerror('Error', 'Usuario y/o contraseña incorrecta')
        except ValueError:
            messagebox.showerror('Error', 'Introduce datos válidos')
       
    ven = Tk()  # Crea la ventana principal / Creates the main window
    ven.title('Programa 1 con Ventanas')  # Título de la ventana / Window title
    ven.geometry('400x400')  # Tamaño de la ventana / Window size

    Label(ven, text='Usuario').pack(pady=10)  # Etiqueta "Usuario" / "Username" label

    us = Entry(ven)  # Caja de texto para el usuario / Textbox for username
    us.pack(pady=3)

    Label(ven, text='Contraseña').pack(pady=10)  # Etiqueta "Contraseña" / "Password" label

    pas = Entry(ven, show='*')  # Caja de texto para contraseña / Password entry box
    pas.pack(pady=3)

    boton = Button(ven, text='Aceptar', command=revisar)  # Botón para validar / Button to validate
    boton.pack(pady=3)

    ven.mainloop()  # Inicia el bucle principal de la ventana / Starts the main window loop


# Condición para ejecutar el programa principal / Condition to run the main program
if __name__ == '__main__':
    Ventana()
