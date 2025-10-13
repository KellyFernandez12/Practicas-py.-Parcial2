
class Validar():
    def __init__(self):
        self.index=0

    def validarAscii(self, valor):
        con = 0
        con2 =0
        for i in valor:
            if ord(i) >= 48 and ord(i)<=57:
                con += 1
            if (ord(i) > 65 and ord(i)<=90) or (ord(i) > 97 and ord(i)<=122):
                con2 += 1

        if con == len(valor):
            return "Numeros"
        elif con2 == len (valor):
            return " letras"
        else:
            return "Letras y Numeros"


    def Validarerrros(self, valor):
        a = 0
        b = 0.0
        try:
             a = int(valor)
             return "numeros"

        except ValueError:
            return "Letras o numeros"
       # try:
            b=flo


        except ValueError:   
            pass 

    def validarconstring (self, valor):
      if self.index < len(valor):
       if valor[index] == "@":
          return "si es un correa"
      else:
          if self.index < len(valor):
           self.index += 1
           self.validarconstring(valor)
          else:
              return "no es un correo"
        

