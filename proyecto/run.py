from archivos.ficheros import *
class Run:

    def __init__(self):
        self.usuarios=[]
        self.arch = Archivo()
        self.ruta="C:/Users/Usuario/PycharmProjects/TecLemas/proyecto.csv"
        self.usuarios=self.arch.leerArchivoCsv(self.ruta)
        self.start()

    def start(self):
        opc=("Registro","Buscar","Actualizar","Eliminar",
             "Listar","Salir",)
        op=self.getMenu(opc)
        match op:
            case 1:
                    self.registro()
                    self.start()
            case 2:
                    self.buscar()
                    self.start()
            case 3:
                    self.actualizar()
                    self.start()
            case 4:
                    self.eliminar()
                    self.start()
            case 5:
                    self.listado()
                    self.start()
            case __:
                    print("Gracias por su visita")

    def registro(self):
        print("Registro de usuario")
        usuario = input("Usuario:")
        self.usuarios= self.arch.leerArchivoCsv(self.ruta)
        obj= self.getUser(self.usuarios,usuario)
        if obj==None:
            nombre = input("Nombre:")
            apellido = input("Apellido:")
            edad = int(input("Edad:"))
            cad = f"{usuario};{nombre};{apellido};{edad};\n"
            self.arch.create(self.ruta,cad,"a")
        else:
            print("Usuario ya existe!!")
        input("Pulsar <Enter> para continuar...")
    def buscar(self):
        print("Consulta de usuarios")
        self.usuarios = self.arch.leerArchivoCsv(self.ruta)
        usuario = input("Usuario a buscar:")
        obj = self.getUser(self.usuarios,usuario)
        if obj==None:
            print("El usuario no existe!!")
        else:
            print("Usuario encontrado!")
            print(f"Nombre   :{obj.nombre}")
            print(f"Apellido :{obj.apellido}")
            print(f"Edad     :{obj.edad}")
        input("Pulsar <Enter> para continuar...")

    def actualizar(self):
        print("Actualizacion de datos del usuario")
        usuario = input("Usuario a actualizar:")
        self.usuarios= self.arch.leerArchivoCsv(self.ruta)
        index = self.getUserId(self.usuarios,usuario)
        if index>=0:
            print(f"Nombre:{self.usuarios[index].nombre}\n"
                  f"Apellido:{self.usuarios[index].apellido}\n"
                  f"Edad:{self.usuarios[index].edad}")
            print("Ingrese los nuevos datos....")
            nombre = input("Nuevo nombre:")
            apellido = input("Nuevo apellido:")
            edad = int(input("Nueva edad:"))
            self.usuarios[index].nombre=nombre
            self.usuarios[index].apellido=apellido
            self.usuarios[index].edad=edad
            msg = ""
            for i in range(len(self.usuarios)):
                msg = msg +f"{self.usuarios[i].usuario};{self.usuarios[i].nombre};" \
                           f"{self.usuarios[i].apellido};{self.usuarios[i].edad};\n"
            #print(msg)
            self.arch.create(self.ruta,msg,"w")
            print(f"Usuario:{usuario} actualizado!")
        else:
            print("Usuario no existe!!")
        input("Pulsar <Enter> para continuar...")

    def eliminar(self):
        print("Eliminar usuarios.")
        usuario= input("Usuario a eliminar:")
        self.usuarios= self.arch.leerArchivoCsv(self.ruta)
        index = self.getUserId(self.usuarios,usuario)
        if index>=0:
            print(f"Nombre:{self.usuarios[index].nombre}")
            print(f"Apellido:{self.usuarios[index].apellido}")
            print(f"Edad:{self.usuarios[index].edad}")
            x = input("Deseas eliminar[S-N]:").upper()
            if x == "S":
                self.usuarios.pop(index)
                msg = ""
                for i in range(len(self.usuarios)):
                    msg = msg+f"{self.usuarios[i].usuario};" \
                              f"{self.usuarios[i].nombre};" \
                              f"{self.usuarios[i].apellido};" \
                              f"{self.usuarios[i].edad};\n"
                #print(msg)
                self.arch.create(self.ruta,msg,"w")
                print(f"El usuario {usuario} ha sido eliminado!")
        else:
            print("Usuario no existe!")
        input("Pulsar <Enter> para continuar...")
    def getUserId(self,lista,valor):
        pos = -1
        for i in range(len(lista)):
            if valor == lista[i].usuario:
                pos = i
                break
        return pos


    def getUser(self,lista,usuario):
        obj = None
        for i in range(len(lista)):
            if usuario==lista[i].usuario:
                obj= lista[i]
                break
        return obj


    def listado(self):
        print("Lista de usuarios")
        self.usuarios = self.arch.leerArchivoCsv(self.ruta)
        for i in range(len(self.usuarios)):
            print(f"{self.usuarios[i].usuario} {self.usuarios[i].nombre} "
                  f"{self.usuarios[i].apellido} {self.usuarios[i].edad}")
        input("Pulsar <Enter> para continuar...")



    def getMenu(self,opc):
        for i in range(len(opc)):
            print(f"{i+1}.- {opc[i]}")
        op = 0
        while op<=0 or op>len(opc):
            op = int(input(f"Ingrese una opcion[1-{len(opc)}]:"))
        return op


if __name__ == '__main__':
    run = Run()


