#!/usr/bin/python3

import tkinter as tk
from cgitb import text
from textwrap import fill
from tkinter import *
from tkinter import font

from click import command
import PaginaComprobarCorreo
import PaginaComprobarDominio
import PaginaComprobarTelefono

#creamos la ventana y la configuramos
root = Tk()
root.title("Pagina Principal")
#si queremos la ventana redimensionable pondriamos 1,1
root.resizable(0,0)
root.geometry("1280x720")
#para configurar el color de fondo
root.config(bg="#c6c6c6")

#creamos el frame y configuramos el frame
frame = Frame()
frame.pack(fill="both", expand="True")
frame.config(width="960", height="480")
frame.config(bg="#c6c6c6")

#Labels
Label(frame, text="Bienvenido a nuestro programa de OSINT", font=("Calibri, 20")).place(x=360, y=20)
Label(frame, text="Por favor seleccione la opción que desea usar", font=("Calibri, 16")).place(x=360, y=60)

def redirigirCorreo():
    PaginaComprobarCorreo.simular(root)

def redirigirDominio():
    PaginaComprobarDominio.simular(root)
    
def redirigirTelefono():
    PaginaComprobarTelefono.simular(root)

#Botones
BotonTelefono = Button(frame, text="Verificar Número de Teléfono",width=25,bg="#ffb703",height=10,command=redirigirTelefono).place(x=100,y=360)
BotonDominio = Button(frame, text="Verificar Dominio",width=25,height=10,bg="#ffb703", command=redirigirDominio).place(x=520,y=360)
BotonCorreo = Button(frame, text="Verificar Correo Electrónico",width=25,height=10,bg="#ffb703",command=redirigirCorreo).place(x=940,y=360)


#Esta linea siempre debe ir al final
root.mainloop()