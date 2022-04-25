#!/usr/bin/python3

from cgitb import text
from curses.panel import top_panel
from importlib.metadata import entry_points
from textwrap import fill
from tkinter import *
from tkinter import font
import tkinter as tk
from unittest import result
import functools
import os, sys

p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p) #Esto es para que detecte el paquete controller

from controller.email_verification  import email_info

        
def simular(parent):
    #creamos la ventana y la configuramos
    top = tk.Toplevel(parent)
    top.title("Verificación de Corre Electrónico")
    #si no queremos la ventana redimensionable pondriamos 0,0
    top.geometry("960x480")
    top.resizable(0,0)
    #para configurar el color de fondo
    top.config(bg="#c6c6c6")

    #Labels
    Label(top, text="Introduzca el correo electrónico", font=("Calibri, 12")).place(x=320, y=30)
    
    def codigoBorrar():
        entry.delete(0, END)
    
    def codigoBuscar():
        correo = email_info().email_verification(entry.get())
        if list.size() != 0:
            list.delete(0,(list.size()-1))

        for i in range(len(correo)):
            list.insert(i, correo.pop(0))
        
        list.place(x=270, y=160)
    
    #Entries
    entry = Entry(top)
    entry.place(x=320, y= 60)
    
    top.protocol("WM_DELETE_WINDOW", functools.partial(volver,parent,top))
    
    #Botones
    BotonBuscar = Button(top, text="Buscar", command=codigoBuscar).place(x=320,y=100)
    BotonBorrer = Button(top, text="Borrar", command=codigoBorrar).place(x=420, y=100)
    BotonVolver = Button(top, text="Volver a ventana principal", command=functools.partial(volver,parent,top)).place(x=600, y=400)

    #Listboxes
    list = Listbox(top,width=70)
    
    parent.withdraw()

def volver(parent,top):
    parent.deiconify()
    top.destroy()
    
