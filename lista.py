#Colores
magenta = '\033[0;35m'
azul = '\033[1;34m'
cyan = '\033[1;36m'
amarillo = "\033[0;33m"
rojo = "\033[0;31m"
quitar = "\033[0;0m"
verde = "\033[0;32m"

#Gotoxy
def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

import time
class Lista:
    
    def __init__(self,datos=[]):
       self.lista = datos
    
    def empty(self):
        return len(self.lista) == 0
        
    def ingresar(self,dato):
        self.lista.append(dato)
        
        
    def eliminar(self):
        if self.empty():
            return print(rojo+"La lista está Vacía......."+amarillo)
              
        else:
            dato = self.lista.pop()
            return dato
    
    def eliminarElemento(self,pos):
        if pos < 0 or pos >= len(self.lista):
            gotoxy(0,2);print(rojo+"No existe esa posición en la Lista"+" "*50+amarillo);time.sleep(1)
            print("\033[3A")
            return print(rojo+"No existe esa posición en la Lista")
        else:    
            self.lista.pop(pos)
            return print("el elemento eliminado es: {}".format(self.lista[pos]))
    
    def ingresarElemento(self,pos,elem):
        if pos < 0 or pos > (len(self.lista)+1):
            gotoxy(39,2);print(rojo+"Posición incorrecta"+amarillo);time.sleep(1);gotoxy(39,2);print(" "*80)
            print("\033[3A")
        else:    
            self.lista.insert(pos,elem)
            print("El elemento insertado fue: "+verde+elem+amarillo+" en la posición:"+verde,pos)
        return 
    
    def buscar(self,buscado):
        op=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                op=True
                break
        if op==True:
            return print(amarillo+"El elemento que buscó se encuentra en la posición: "+verde+"{}".format(pos))
        else:
            return print(rojo+"El elemento que busca no se encuentra en la lista"+amarillo)
    
    def mostrar(self):
        if self.empty():
            return print(rojo+"La lista está Vacía.......")
        else:                    
            return print(amarillo+"la lista es :"+verde+"{}".format(self.lista))
