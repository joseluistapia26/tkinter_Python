from tkinter import *

import tkinter as tk
class LoginLv:

    def __init__(self, titulo=None):
        self.marca_user = "Ingrese su usuario"
        self.marca_password = "Ingrese su password"
        self.__getWindow(titulo)

    def __getWindow(self, titulo=None):
        self.ven = tk.Tk()
        self.ven.title(titulo)
        self.ven.geometry(f"{400}x{450}")
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
        self.ven.mainloop()

    def __add_placeholder_user(self, event):
        if not self.usuario.get():
            self.usuario.insert(0, self.marca_user)
            self.usuario.config(fg="#A0A0A0")

    def __clear_placeholder_user(self, event):
        if self.usuario.get() == self.marca_user:
            self.usuario.delete(0, 'end')
            self.usuario.config(fg="#333333")

if __name__ == '__main__':
    ventana = LoginLv("Login Live")