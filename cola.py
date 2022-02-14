import time

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

class Cola:                
    def __init__(self,tamanio):
        self.lista=[]
        self.tope=0
        self.size=tamanio
        
    def empty(self):
        return self.tope == 0
    
    def ingresar(self):
        while self.tope < self.size:
            self.lista += []
            self.tope += 1 
            nombre=input(cyan+"ingresa un elemento: ")
            self.lista.append(nombre)
            return True
        return print(rojo+"La Cola está Llena.......")
    
    def eliminar(self):
        if self.empty():
            return print(rojo+"La Cola está Vacía.......")
        else:
            top = self.lista[0]
            self.tope -= 1
            self.lista = self.lista[1::1]
            print(magenta+"Borrando el ultimo elemento.......");time.sleep(1)
            gotoxy(0,2);print("El elemento eliminado fué: "+verde+top);gotoxy(40,2);print(" "*80)
            print("\033[3A")
            # return print(cyan+"El elemento eliminado fué:"+verde+" {}".format(top))
            
    def longitud(self):
        return print(cyan+"La longitud es: "+verde+"[{}/{}]".format(self.tope,self.size))
        
    def mostrar(self):
        if self.empty():
            return print(rojo+"La Cola está Vacía.......")
        else:                    
            print(cyan+"COLA")
            for tope in range(self.tope-1,-1,-1):
                print(verde+"[{}]".format(self.lista[tope]))   
    
    def buscar(self,buscado):
        op=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                op=True
                break
        if op==True:
            return print(cyan+"El elemento que buscó se encuentra en la posición: "+verde+"{}".format(pos))
        else:
            return print(rojo+"El elemento que buscó no se encuentra en la Cola")