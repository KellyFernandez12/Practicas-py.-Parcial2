
from tkinter import *
from tkinter import messagebox

class Principal:
    def __init__(self):
        self.ven = Tk()
        self.ven.title('Preexamen')
        self.ven.geometry('550x450')

        self.lista = []  # Lista interna para guardar los elementos
        self.crear_interfaz()

    def crear_interfaz(self):
        # Etiquetas
        Label(self.ven, text="Minúsculas").place(y=30, x=30)
        Label(self.ven, text="Mayúsculas").place(y=30, x=180)
        Label(self.ven, text="Números").place(y=30, x=350)

        # Cajas de texto
        self.n1 = Entry(self.ven)
        self.n1.place(x=30, y=50)
        self.n2 = Entry(self.ven)
        self.n2.place(x=180, y=50)
        self.n3 = Entry(self.ven)
        self.n3.place(x=350, y=50)

        # Botones
        Button(self.ven, text="Validar", command=self.validar).place(x=180, y=150)
        Button(self.ven, text="Agregar", command=self.agregar).place(x=280, y=150)

        # Listbox y etiqueta contador
        self.listbox = Listbox(self.ven, width=60)
        self.listbox.place(x=50, y=220)
        self.lbl_contador = Label(self.ven, text="Elementos en la lista: 0")
        self.lbl_contador.place(x=180, y=380)

        self.ven.mainloop()

    def validar(self):
        # Obtener valores
        val1 = self.n1.get()
        val2 = self.n2.get()
        val3 = self.n3.get()

        # Validaciones
        if not val1.islower() or not val1.isalpha():
            messagebox.showerror("Error", "La primera caja solo debe contener letras minúsculas")
            self.n1.delete(0, END)
            return False

        if not val2.isupper() or not val2.isalpha():
            messagebox.showerror("Error", "La segunda caja solo debe contener letras mayúsculas")
            self.n2.delete(0, END)
            return False

        if not val3.isdigit():
            messagebox.showerror("Error", "La tercera caja solo debe contener números")
            self.n3.delete(0, END)
            return False

        messagebox.showinfo("Correcto", "Validación exitosa")
        return True

    def agregar(self):
        # Solo agrega si la validación es correcta
        if self.validar():
            texto = self.n1.get() + self.n2.get() + self.n3.get()
            self.lista.append(texto)
            self.listbox.insert(END, texto)

            # Actualizar contador
            self.lbl_contador.config(text=f"Elementos en la lista: {len(self.lista)}")

            # Limpiar entradas
            self.n1.delete(0, END)
            self.n2.delete(0, END)
            self.n3.delete(0, END)

# Ejecución principal
if __name__ == '__main__':
    app = Principal()
