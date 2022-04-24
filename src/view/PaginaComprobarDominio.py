#!/usr/bin/python3

from cgitb import text
from textwrap import fill
from tkinter import *
from tkinter import font
import tkinter as tk
import functools
import os, sys

p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p) #Esto es para que detecte el paquete controller

from controller.DNS_verification  import DNSDomain

def simular(parent):
    
    #creamos la ventana y la configuramos
    top =tk.Toplevel(parent)
    top.title("Verificación de Dominio")
    #si no queremos la ventana redimensionable pondriamos 0,0
    top.resizable(0,0)
    top.geometry("960x480")
    #para configurar el color de fondo
    top.config(bg="#c6c6c6")

    #Labels
    Label(top, text="Introduzca el dominio", font=("Calibri, 12")).place(x=320, y=30)
    top.protocol("WM_DELETE_WINDOW", functools.partial(volver,parent,top))
    
    def codigoBorrar():
        entry.delete(0, END)
    
    def codigoBuscar():
        dominio = DNSDomain.comprobar_dominio(entry.get())
        print(dominio)
    
    #Entries
    entry = Entry(top)
    entry.place(x=320, y= 60)

    #Botones
    BotonBuscar = Button(top, text="Buscar", command=codigoBuscar).place(x=320,y=100)
    BotonBorrer = Button(top, text="Borrar", command=codigoBorrar).place(x=420, y=100)
    BotonVolver = Button(top, text="Volver a ventana principal", command=functools.partial(volver,parent,top)).place(x=600, y=400)
    
    #Listboxes
    list = Listbox(top,width=40)
    list.place(x=315, y=160)
    
    parent.withdraw()
       
def volver(parent,top):
    parent.deiconify()
    top.destroy()