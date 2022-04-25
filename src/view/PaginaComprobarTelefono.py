#!/usr/bin/python3

from cgitb import text
import imp
from textwrap import fill
from tkinter import *
from tkinter import font
import tkinter as tk
import os, sys
import functools

p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p) #Esto es para que detecte el paquete controller

from controller.phone_verification  import phone_info

TLFN_INFO = ""

def simular(parent):
    
    #creamos la ventana y la configuramos
    top = tk.Toplevel(parent)
    top.title("Verificación de Número de Teléfono")
    #si no queremos la ventana redimensionable pondriamos 0,0
    top.resizable(0,0)
    top.geometry("960x480")
    #para configurar el color de fondo
    top.config(bg="#c6c6c6")

    #Labels
    Label(top, text="Introduzca el número de teléfono", font=("Calibri, 12")).place(x=320, y=30)
    top.protocol("WM_DELETE_WINDOW", functools.partial(volver,parent,top))
    
    def codigoBorrar():
        entry.delete(0, END)
        
    def codigoBuscar():
        telefono = phone_info(entry.get())

        if list.size() != 0:
            list.delete(0,(list.size()-1))
        list.insert(0,telefono.phone_format())
        list.insert(1,telefono.phone_provider())
        list.insert(2,telefono.phone_region())
        list.insert(3,telefono.phone_timezone())
        list.insert(4,telefono.phone_validation())        
        list.place(x=260, y=160)

    
    #Entries
    entry = Entry(top)
    entry.place(x=320, y= 60)
    #Listboxes
    list = Listbox(top,width=70)
    
    #Botones
    BotonBuscar = Button(top, text="Buscar", command=codigoBuscar).place(x=320,y=100)
    BotonBorrer = Button(top, text="Borrar", command=codigoBorrar).place(x=420, y=100)
    BotonVolver = Button(top, text="Volver a ventana principal", command=functools.partial(volver,parent,top)).place(x=600, y=400)

    parent.withdraw()
    
def volver(parent,top):
    parent.deiconify()
    top.destroy()    