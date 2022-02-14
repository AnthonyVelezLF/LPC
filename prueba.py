from repeticion import Helper
from lista import Lista
from pila import Pila
from cola import Cola
import os
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

#Repite el listado
helper = Helper()
lista = [amarillo+"1) Listas"+magenta,"2) Pilas"+cyan,"3) Colas"+quitar,"4) Salir"+verde]
opcion=""

#Menu principal
while opcion != "4":
  os.system("cls")
  opcion = helper.menu(lista,azul+"*"*20+" MENÚ PRINCIPAL "+"*"*20)
  
  #Menu Lista
  if opcion == "1":
    opc1=""
    while opc1 != "7":
      os.system("cls")
      opc1 = helper.menu([amarillo+"1) Ingresar ","2) Borrar","3) Mostrar","4) Eliminar","5) Insertar","6) Buscar","7) Salir"+verde],azul+"*"*20+" MENÚ LISTA "+"*"*20)
      os.system("cls")
      datos = Lista()

      #ingreso de elementos
      if opc1 == "1":
        print(azul+"*"*20,"INGRESO DE ELEMENTO(S) EN LA LISTA:","*"*20+amarillo)
        # num = int(input("Cuántos elementos desea en la lista?: "))
        # num=0.00
        # while True:
        #   try:
        #     num = int(input("Cuántos elementos desea en la lista?: "))
        #     break
        #   except ValueError:
        #     gotoxy(39,2);print(rojo+"Ingrese solo números."+amarillo);time.sleep(1);gotoxy(39,2);print(" "*80)
        #     print("\033[3A")
        # os.system("cls")
        # for i in range(num):
        valor = input("Ingrese el elemento: ")
        datos.ingresar(valor)
        input(verde+"Elemento(s) ingresado(s) satisfactoriamente, presione una tecla para continuar...")
        
      #eliminar ultimo elemento
      elif opc1 == "2":
        print(azul+"*"*20,"ELIMINAR UN ELEMENTO","*"*20+amarillo)
        if len(datos.lista) == 0:
              print(rojo+"La lista está Vacía......."+amarillo)
              print("")
        else:
          print("Borrando el ultimo elemento...");time.sleep(1)
          gotoxy(0,2);print("El elemento eliminado fué: "+verde+datos.eliminar());gotoxy(60,2);print(" "*80)
          print("\033[3A")
          # print("Borrando el ultimo elemento.......");time.sleep(1);os.system("cls")
          # print("El elemento eliminado fué: {}".format(datos.eliminar()))
          # print(datos.lista)
          print("\033[0B")
        # print("\033[0B")
        input(verde+"Presione una tecla para continuar...")
        
      
      #mostrar elementos de la lista
      elif opc1 == "3":
        print(azul+"*"*20,"MOSTRAR UN ELEMENTO","*"*20+amarillo)
        datos.mostrar()
        print("")
        input(verde+"Presione una tecla para continuar...")   
      
      #eliminar dicho elemento
      elif opc1 == "4":
        print(azul+"*"*20,"ELIMINAR UN ELEMENTO","*"*20+amarillo)
        if len(datos.lista) == 0:
              print(rojo+"La lista está Vacía......."+amarillo)
              print("")
        else:
          while True:
              try:
                elimi=int(input("Ingrese la posición del elemento que desea eliminar: "))
                datos.eliminarElemento(elimi)
                #print("El elemento eliminado fué: {}".format(datos.lista[elimi]))
                break
              except ValueError:
                gotoxy(54,2);print(rojo+"Ingrese solo números."+amarillo);time.sleep(1);gotoxy(54,2);print(" "*80)
                print("\033[3A")    
              #print("\033[0B")
        input(verde+"Presione una tecla para continuar...")
        print("\033[A")  
      
      #agregar dicho elemento
      elif opc1 == "5":
        print(azul+"*"*20,"AGREGAR UN ELEMENTO","*"*30+amarillo)
        if len(datos.lista) == 0:
          print(rojo+"La lista está Vacía......."+amarillo)
          print("")
        else:
          while True:
            try:
              pos=int(input("Ingrese la posición en la que desea agregar el elemento: "))
              if pos < 0 or pos > (len(datos.lista)+1):
                gotoxy(0,2);print(rojo+"Esa posición no exite......."+" "*60+amarillo);time.sleep(1)#;gotoxy(0,2);print(" "*100)
                print("\033[3A")
              else:
                ele=input("Ingrese el nuevo elemento: ")
                datos.ingresarElemento(pos,ele)
              break
            except ValueError:
              gotoxy(58,2);print(rojo+"Ingrese solo números"+amarillo);time.sleep(1);gotoxy(58,2);print(" "*100)
              print("\033[3A")        
          # if pos < 0 or pos > (len(datos.lista)+1):
          #   print("No puedes agregarlo en esa posición")
          # else:
          #   ele=input("Ingrese el nuevo elemento: ")
          #   datos.ingresarElemento(pos,ele)
          # print("El elemento insertado fue: '{}' en la posición: {}".format(ele,pos))
        input(verde+"Presione una tecla para continuar...")
        print("\033[A") 
        
      
      #buscar elemento      
      elif opc1 == "6":
        print(azul+"*"*20,"BUSCAR UN ELEMENTO","*"*20+amarillo)
        if len(datos.lista) == 0:
              print(rojo+"La lista está Vacía......."+amarillo)
              print("")
              
        else:
          ele=input("Ingrese el elemento que desea buscar: ")
          datos.buscar(ele)
        input(verde+"Presione una tecla para continuar...") 

  #Menu pila      
  elif opcion == "2":       
    opc2=""
    os.system("cls")
    print(azul+"*"*20,"MENÚ PILA","*"*20,magenta)
    while True:
      try:
        lim=int(input("Cuantos elementos tendrá la pila?: ")) 
        break
      except ValueError:
        gotoxy(36,2);print(rojo+"Ingrese solo números.");time.sleep(1);gotoxy(36,2);print(" "*80+magenta)
        print("\033[3A")
    datos=Pila(lim)
    os.system("cls")
    while opc2 != "6":
      os.system("cls")
      opc2 = helper.menu([magenta+"1) Ingresar","2) Eliminar","3) Mostrar","4) Buscar","5) Longitud","6) Salir"],azul+"*"*20+" MENÚ PILA "+"*"*20)
      os.system("cls")

      #ingreso un elemento
      if opc2 == "1":
        nombre= ""
        os.system("cls")
        print(azul+"*"*20,"INGRESAR ELEMENTO A LA PILA","*"*20)
        datos.ingresar()
        input(verde+"Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      
      #eliminar ultimo elemento
      elif opc2 == "2":
        print(azul+"*"*20,"ELIMINAR EL ÚLTIMO ELEMENTO","*"*20)
        datos.eliminar()
        print("\033[0B")
        input(verde+"Presione una tecla para continuar...")
      
      #mostrar elementos
      elif opc2 == "3":
        print(azul+"*"*20,"MOSTRAR PILA","*"*20)
        datos.mostrar()
        print("")
        input(verde+"Presione una tecla para continuar...")
      
      #buscar elementos  
      elif opc2 == "4":
        print(azul+"*"*20,"BUSCAR ELEMENTO EN LA PILA","*"*20)
        if len(datos.lista) == 0:
              print(rojo+"La Pila está Vacía.......")
        else:
          ele=input(magenta+"Ingrese el elemento que desea buscar: ")
          datos.buscar(ele)
        input(verde+"Presione una tecla para continuar...")
      
      #longitud
      elif opc2 == "5":
        print(azul+"*"*20,"LONGITUD DE LA PILA","*"*20)
        datos.longitud()
        input(verde+"Presione una tecla para continuar...")
  
  #Menu Cola
  elif opcion == "3":       
    opc3=""
    os.system("cls")
    print(azul+"*"*20,"MENÚ COLA","*"*20)
    while True:
          try:
            lim=int(input(cyan+"Cuántos elementos tendrá la cola?: "))
            break
          except ValueError:
            gotoxy(39,2);print(rojo+"Ingrese solo números.");time.sleep(1);gotoxy(39,2);print(" "*80+cyan)
            print("\033[2A")
    datos=Cola(lim)
    os.system("cls")
    while opc3 != "6":
      os.system("cls")
      opc3 = helper.menu([cyan+"1) Ingresar","2) Eliminar","3) Mostrar","4) Buscar","5) Longitud","6) Salir"],azul+"*"*20+" MENÚ COLA "+"*"*20)
      os.system("cls")

      #ingreso
      if opc3 == "1":
        nombre= ""
        os.system("cls")
        print(azul+"*"*20,"INGRESAR ELEMENTO A LA COLA","*"*20)
        datos.ingresar()
        input(verde+"Datos ingresados satisfactoriamente, presione una tecla para continuar...")
      
      #eliminar primer elemento
      elif opc3 == "2":
        print(verde+"*"*20,"ELIMINAR EL PRIMER ELEMENTO","*"*20)
        datos.eliminar()
        # print(cyan+"El elemento eliminado fué: {}".format(datos.eliminar()))
        input(verde+"Presione una tecla para continuar...")

      #mostrar cola  
      elif opc3 == "3":
        print(azul+"*"*20,"MOSTRAR COLA","*"*20)
        datos.mostrar()
        print("")
        input(verde+"Presione una tecla para continuar...")
       
      #buscar elementos  
      elif opc3 == "4":
        print(azul+"*"*20,"BUSCAR ELEMENTO EN LA COLA","*"*20)
        if len(datos.lista) == 0:
              print(rojo+"La Cola está Vacía.......")
        else:
          ele=input(cyan+"Ingrese el elemento que desea buscar: ")
          datos.buscar(ele)
        input(verde+"Presione una tecla para continuar...")
      
      #longitud
      elif opc3 == "5":
        print(azul+"*"*20,"LONGITUD DE LA COLA","*"*20)
        datos.longitud()
        input(verde+"Presione una tecla para continuar...")
        
print(amarillo+"GRACIAS POR USAR ESTE SOFTWARE")
print("VUELVA PRONTO")
        
        
        
       
    
        

