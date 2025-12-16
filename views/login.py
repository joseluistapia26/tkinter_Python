from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Combobox


class LoginLv:

    def __init__(self, titulo=None):
        self.marca_user = "Ingrese su usuario"
        self.marca_password = "Ingrese su password"
        self.__getWindow(titulo)

    def __getWindow(self, titulo=None):
        self.ven = tk.Tk()
        self.ven.title(titulo)
        #self.ven.geometry(f"{400}x{450}")
        self.__centrado(self.ven,400,450)
        self.ven.config(bg="#546E7A")
        self.ven.resizable(0, 0)

        # marco interno
        frame_ancho = 300
        frame_alto = 370
        input_ancho = 240
        self.login_frame = tk.Frame(self.ven, bg="white", relief="flat")
        frame_x = (400 - frame_ancho) / 2
        frame_y = (450 - frame_alto) / 2

        input_x = (frame_ancho - input_ancho) / 2

        self.login_frame.place(x=frame_x, y=frame_y, width=frame_ancho,
                               height=frame_alto)
        # Etiquetas
        lb1 = tk.Label(self.login_frame, text="Inicio de sesión",
                       fg="#19335A", bg="white",  # Color de título mejorado
                       font=("Roboto", 18, "bold")).place(relx=0.5, y=40, anchor="center")  # Ajuste Y

        # CORRECCIÓN: Posición input_x
        lb2 = tk.Label(self.login_frame, text="Usuario",
                       fg="#6C757D", bg="white",
                       font=("Roboto", 9)).place(x=input_x, y=95)  # Ajuste Y

        # Entradas
        self.usuario = tk.Entry(self.login_frame,
                                font=("Roboto", 11),
                                fg="#A0A0A0", bg="#F4F4F4",  # Colores iniciales de placeholder y fondo
                                relief="flat", bd=0)  # CORRECCIÓN: Estilo plano (bd=0)

        self.usuario.place(x=input_x, y=120, width=input_ancho,
                           height=35)

        self.usuario.insert(0, self.marca_user)
        self.usuario.bind("<FocusIn>", self.__clear_placeholder_user)
        self.usuario.bind("<FocusOut>", self.__add_placeholder_user)

        # Password
        lb3 = Label(self.login_frame,text="Password",
                bg="white",font=("Roboto",9)).place(
            x=input_x,y=155
        )
        self.password = Entry(self.login_frame,font=("Roboto",11),
                        fg="#333333",bg="#E9ECEF", show="*",
                              relief="flat", bd=5)
        self.password.place(x=input_x,y=180,
                        width=input_ancho,height=35)
        #Botones
        btn1 = Button(self.login_frame,relief="flat",
                      text="Iniciar Sesión",bg="#3A5A9A",
                      fg="white",font=("Roboto",12,"bold"),
                      command=self.__validacion,
                      cursor="hand2"
                      )
        btn1.place(x=input_x,y=250,width=input_ancho,height=40)

        btn2 = Button(self.login_frame,relief="flat",
                      text="Cancelar",fg="white",bg="#3A5A9A",font=("Roboto",12,"bold"),
                      command=self.ven.destroy,
                      cursor="hand2",bd=0
                      )
        btn2.place(relx=0.5,y=335,width=input_ancho,height=40,anchor="center")

        self.ven.mainloop()

    def __validacion(self):
        if self.usuario.get()=="Live14" and self.password.get()=="1234":
           self.ven.destroy()
           dash = Dashboard()
        else:
            messagebox.showerror("Inicio de Sesión",
                                 "Credenciales Inválidas!")

    def __add_placeholder_user(self, event):
        if not self.usuario.get():
            self.usuario.insert(0, self.marca_user)
            self.usuario.config(fg="#A0A0A0")

    def __clear_placeholder_user(self, event):
        if self.usuario.get() == self.marca_user:
            self.usuario.delete(0, 'end')
            self.usuario.config(fg="#333333")

    def __centrado(self,obV,ancho,alto):
        y_alto= alto
        x_ancho = ancho
        screen_x = obV.winfo_screenwidth()
        screen_y = obV.winfo_screenheight()
        x_coord = int((screen_x/2)-(x_ancho/2))
        y_coord = int((screen_y/2)- (y_alto/2))
        obV.geometry(f"{x_ancho}x{y_alto}+{x_coord}+{y_coord}")

class Dashboard:

    def __init__(self,obj=None):
        self.ruta="C:/Users/Usuario/PycharmProjects/TecLemas/img/Curso_Programacion.png"
        self.__getWindow("")
        self.__getMenu()
        self.__getImage(self.ruta,120,30,21)

    def __getMenu(self):
        self.menu = Menu(self.ven)
        self.ven.config(menu=self.menu)
        #Cascada
        item1 = Menu(self.menu)
        self.menu.add_cascade(label="Archivo",menu=item1)
        item1.add_command(label="Registro",command=self.__registro)
        item1.add_command(label="Gestion de usuarios")
        item1.add_separator()
        item1.add_command(label="Salir", command=self.ven.destroy)

        item2 = Menu(self.menu)
        self.menu.add_cascade(label="Ayuda",menu=item2)
        item2.add_separator()
        item2.add_command(label="About",command=self.__about)
    def __getWindow(self,obj=None):
        self.ven = Tk()
        self.ven.title("")
        self.ven.config(bg="purple")
        self.ven.geometry(f"{1000}x{570}")
        self.ven.resizable(0,0)

    def __registro(self):
        reg = Registro("Registro de Usuarios")



    def __about(self):
        messagebox.showinfo("About",
                            "Desarrollado en el Live 15 de Python",
                            parent=self.ven)

    def __getImage(self,ruta,x,y,tam):
        img = PhotoImage(file=ruta)
        img = img.zoom(tam)
        img = img.subsample(35)
        panel = Label(self.ven,image=img).place(x=x,y=y)
        self.ven.mainloop()

class Registro:

    def __init__(self,obj=None):
        self.__getWindow()
        self.__getLabels()
        self.__getInputs()
        self.__getButtons()
        self.ven1.mainloop()
    def __getWindow(self,obj=None):
        self.ven1 = Toplevel()
        self.ven1.title(obj)
        self.ven1.config(bg="orange")
        self.ven1.geometry(f"{700}x{490}")
        self.ven1.resizable(0, 0)


    def __getLabels(self):
        posX=120
        lb1 = Label(self.ven1,text="Registro de Usuarios",
                    bg="orange",font=("Arial",18,"bold")).place(
            x=370,y=40,anchor="center")
        lb2 = Label(self.ven1,text="Usuario",
                    bg="orange",font=("Arial",18,"bold")).place(
            x=posX,y=100)
        lb3 = Label(self.ven1,text="Password",
                    bg="orange",font=("Arial",18,"bold")).place(
            x=posX,y=150)
        lb4 = Label(self.ven1,text="Nombres",
                    bg="orange",font=("Arial",18,"bold")).place(
            x=posX,y=200)
        lb5 = Label(self.ven1,text="Apellido",
                    bg="orange",font=("Arial",18,"bold")).place(
            x=posX,y=250)
        lb6 = Label(self.ven1,text="Correo",
                    bg="orange",font=("Arial",18,"bold")).place(
            x=posX,y=300)
        lb7 = Label(self.ven1,text="Profesion",
                    bg="orange",font=("Arial",18,"bold")).place(
            x=posX,y=350)

    def __getInputs(self):
        posX = 380
        self.usuario = Entry(self.ven1,font=("Arial",16),
                             fg="#333333",bg="#E9ECEF",
                             relief="flat",bd=5)
        self.usuario.place(x=posX,y=100,width=200,height=25)
        self.password = Entry(self.ven1,font=("Arial",18),
                             fg="#333333",bg="#E9ECEF",
                             relief="flat",bd=5,show="*")
        self.password .place(x=posX,y=150,width=200,height=25)
        self.nombres = Entry(self.ven1,font=("Arial",16),
                             fg="#333333",bg="#E9ECEF",
                             relief="flat",bd=5)
        self.nombres.place(x=posX,y=200,width=200,height=25)
        self.apellidos = Entry(self.ven1,font=("Arial",16),
                             fg="#333333",bg="#E9ECEF",
                             relief="flat",bd=5)
        self.apellidos.place(x=posX,y=250,width=200,height=25)
        self.correo = Entry(self.ven1,font=("Arial",16),
                             fg="#333333",bg="#E9ECEF",
                             relief="flat",bd=5)
        self.correo.place(x=posX,y=300,width=200,height=25)
        self.profesion = Combobox(self.ven1,state="readonly",
                                values=["Estudiante","Docente",
                                        "Programador","Otro"])
        self.profesion.place(x=posX,y=350,width=200,height=25)

    def __getButtons(self):
        btn1= Button(self.ven1,relief="flat",
                      text="Registrar",bg="#3A5A9A",
                      fg="white",font=("Roboto",12,"bold"),
                      #command=self.__registrar,
                      cursor="hand2"
                      ).place(x=200,y=420,width=110,height=40)
        btn2= Button(self.ven1,relief="flat",
                      text="Cancelar",bg="#3A5A9A",
                      fg="white",font=("Roboto",12,"bold"),
                      command=self.ven1.destroy,
                      cursor="hand2"
                      ).place(x=360,y=420,width=110,height=40)



if __name__ == '__main__':
    #form1 = Registro("Registro de Usuarios")
    ventana = LoginLv("Login Live")

    #dash = Dashboard()
