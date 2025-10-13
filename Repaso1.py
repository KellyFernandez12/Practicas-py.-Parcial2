

from tkinter import *
from tkinter import messagebox
from Validarrepaso import Validar

class principal():
    def __init__(self):
        self.ven=Tk()
        self.ven.geometry('450x250')
        self.lista = []
        self.valid = Validar()
        


    def inicio(self):    
        Label(self.ven, text="Programa de python con TKInter").place(x=10, y=20)# x columna, y = fila
        Label(self.ven, text="Escribe un dato").place(x=50, y=50)

        self.dato = Entry(self.ven)
        self.dato.place(x=150, y=50, width=150 )#height = alto, width = ancho

        Button(self.ven, text="Validar", command=self.Validardatos).place(x=200, y=90,width=150 )
        self.mostrar = Label(self.ven, text="ejemplo")
        self.mostrar.place(x=20, y=150)
        self.ven.mainloop()

    def Validardatos(self):
        val = self.dato.get()
        if val !="":
         self.revisar(val)
         self.lista.append(val)
         self.dato.delete(0,END)
         #print(self.lista)
         self.mostrar.config(text=f'{self.lista}')
         #respuesta = self.valid.validarAscii(val)
         respuesta = self.valid.validarAscii(val)
         messagebox.showinfo("valida Datos", f'El dato es{respuesta}')
        else:
            messagebox.showerror("Error","Caja de texto vacia") 


    def revisar(self, v): 
        print(v)       
    






if __name__=='__main__':
    app = principal()
    app.inicio()


