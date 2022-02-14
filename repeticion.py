#Colores
magenta = '\033[0;35m'
azul = '\033[1;34m'
cyan = '\033[1;36m'
amarillo = "\033[0;33m"
rojo = "\033[0;31m"
quitar = "\033[0;0m"
verde = "\033[0;32m"

#Para repetir listado
class Helper:
  def __init__(self):
    # x=10
    pass
  def menu(self,opciones,titulo):
    print(titulo)
    for opcion in opciones:
      print(opcion)
    opc = input(verde+"Elija Opcion[1...{}]: ".format(len(opciones)))
    return opc 