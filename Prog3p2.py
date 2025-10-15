from tkinter import * 
from tkinter import messagebox

class Ventana():
  def __init__(self):  # CORRECCIÓN: debe ser __init__, no _init_
        # Crear la ventana principal / Create the main window
      self.ven = Tk()
      self.ven.title('Programa 1 con Ventanas')  # Título de la ventana / Window title
      self.ven.geometry('400x400')  # Tamaño de la ventana / Window size
      self.inicio()  # Llamar al método que construye la interfaz / Call the method that builds the interface

  def inicio(self):
       # Etiqueta para el usuario / Label for username
      Label(self.ven, text='Usuario').pack(pady=10)

      # Caja de texto para el usuario / Entry box for username
      self.us = Entry(self.ven)
      self.us.pack(pady=3)
        # Etiqueta para la contraseña / Label for password
      Label(self.ven, text='Contraseña').pack(pady=10)

        # Caja de texto para la contraseña / Entry box for password
      self.pas = Entry(self.ven, show='*')  # 'show="*"' oculta la contraseña / hides password input
      self.pas.pack(pady=3)

        # Botón que ejecuta la validación / Button that triggers validation
      Button(self.ven, text='Aceptar', command=self.revisar).pack(pady=3)

        # Inicia el bucle principal de la ventana / Starts the window main loop
      self.ven.mainloop()

  def revisar(self):
      # Método que valida el usuario y la contraseña / Method that validates username and password
      try:

        u = str(self.us.get())  # Obtiene el texto del campo usuario / Gets username input
        p = str(self.pas.get())  # Obtiene el texto del campo contraseña / Gets password input

        # Validación simple / Simple validation
        if u == 'admin' and p == '12345':
            messagebox.showinfo('Validación', 'Usuario y contraseña correctos')
        else:
            messagebox.showerror('Error', 'Usuario y/o contraseña incorrecta')
      except ValueError:
            messagebox.showerror('Error', 'Introduce datos válidos')


if __name__ == '__main__':
    Ventana()
