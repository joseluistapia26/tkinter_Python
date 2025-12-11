"""
num=0
try:
    num = float(input("Peso:"))
except:
    print("Error de digitacion")
print(f"El numero es:{num}")
print("fin de ejecucion")
"""
class Usuario:

    def __init__(self,usuario, nombre, apellido,edad):
        self.usuario = usuario
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
class Archivo:
    def create(self,ruta,contenido,modo):
        archivo = open(ruta,modo)
        archivo.write(contenido)
        archivo.close()

    def leerArchivo(self,ruta):
        try:
            archivo = open(ruta,"r",encoding="utf-8")
            contenido = archivo.read()
            return contenido
        except FileNotFoundError:
            return f"Error: El fichero en {ruta} tiene un error!"

    def leerArchivoCsv(self,ruta):
        lista = []
        try:
            archivo = open(ruta,"r",encoding="utf-8")
            for linea in archivo.readlines():
                tupla = linea.split(";")
                obj = Usuario(tupla[0],tupla[1],tupla[2],
                              int(tupla[3]))
                lista.append(obj)
        except FileNotFoundError:
            print(f"Error: La ruta del archivo {ruta}, tiene un error!")
        return lista

if __name__ == '__main__':
    ruta ="C:/Users/Usuario/PycharmProjects/TecLemas/usuarios.csv"
    arch = Archivo()
    usuario = input("Usuario:")
    nombre = input("Nombre:")
    apellido = input("Apellido:")
    edad = int(input("Edad:"))
    contenido = f"{usuario};{nombre};{apellido};{edad}\n"
    arch.create(ruta,contenido,"a")
    print("*************")
    lista = arch.leerArchivoCsv(ruta)
    for i  in range(len(lista)):
        print(f"{lista[i].usuario} {lista[i].nombre}"
              f" {lista[i].apellido} {lista[i].edad}")




    """ 
    ruta ="C:/Users/Usuario/PycharmProjects/TecLemas/fichero.txt"
    arc = Archivo()
    texto = input("Escriba el contenido del archivo:")
    arc.create(ruta,texto+" \n","a")
    conte = arc.leerArchivo(ruta)
    print(conte)
    
    
    08:30pm Ecuador, Colombia, Peru
    Clase: Proyecto en Python
    Desarrollo de un CRUD
    con Ficheros 
    """





