
from tkinter import *
from tkinter import messagebox


def Ventana():
    def revisar():
        try:
           u = str(us.get())
           p = S(pas.get())
           if u == 'admin' and p == '12345':
            messagebox.showinfo('Validacion', 'Usuario y Contraseña correctos')
           else:
            messagebox.showerror('Error', 'Usuaruio y/o contraseaña incorrectos')
        except ValueError:
         messagebox.showerror('Error', 'Introduce datos')

    ven=Tk()
    ven.title('Programa 1 con ventanas')
    ven.geometry('400x200')
    Label(ven, text='Usuario').pack(pady=10)
    us = Entry(ven)
    us.pack(pady=3)
    Label(ven, text='Password').pack(pady=10)
    pas = Entry(ven)
    pas.pack(pady=3)
    boton = Button(ven, Text='Aceptar', command=revisar).pack(pady=3)




    ven.mainloop()


if __name__=='__main__':
     Ventana()
    