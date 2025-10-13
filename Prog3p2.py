from tkinter import * 
from tkinter import messagebox

class Ventana():
    def _init_(self):
      self.ven = Tk() #Libreria
      self.ven.title('Programa 1 con Ventanas')#Titulo de la ventana
      self.ven.geometry('400x400') #Tamaño de la ventana
      self.inicio()

    def inicio(self):
      Label(self.ven, text='Usuario').pack(pady=10) #Texto

      self.us = Entry(self.ven)
      self.us.pack(pady=3)#Caja de texto

      Label(self.ven, text='Contraseña').pack(pady=10) #Texto

      self.pas = Entry(self.ven)
      self.pas.pack(pady=3) #Caja de Texto
  
      boton = Button(self.ven,text='Aceptar',command=self.revisar).pack(pady=3) #Boton 

      self.ven.mainloop()

    def revisar(self):
       try:
            u = str(self.us.get())
            p = str(self.pas.get())

            if u == 'admin' and p == '12345':
                messagebox.showinfo('Validacion','Usuario','Contraseña correcta')
            else:
                messagebox.showerror('Error','Usuario y/o contraseña incorrecta')
       except ValueError:
            messagebox.showerror('Error','Introduce datos')
if __name__=='main_':
    Ventana()