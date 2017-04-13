#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------
#
#  Jose Gonzalez Ayerdi - A01036121
#  Martha Benavides - A01280115
#  Proyecto Final, Diseño de Compiladores
#  Puntos Extras
# ------------------------------------------------------------
from Tkinter import *
import subprocess, os

ventana = Tk()
ventana.geometry("700x600")
ventana.title("Compilador APODORAX")

def obtenerCodigo():
    codigoAgregado = codigo.get("1.0",'end-1c')
    with open("codigoUsuario.txt", "w") as f:
    	f.write(codigoAgregado) 
	subprocess.Popen('python parser_apodorax.py codigoUsuario.txt')
    #os.chmod('python parser_apodorax.py codigoUsuario.txt',0755)
    #print (codigoAgregado)

lblApodorax = Label(text="APODORAX",font=("Times New Roman",24,"bold"), fg = "red").place(x=260,y=10)
run = Button(ventana, text ="Compilar",font=("Times New Roman",14,"bold"), relief=RAISED, cursor="arrow", command = obtenerCodigo).place(x=300,y=50)

codigo = Text(width = 78, height = 25, wrap = WORD,  bg ="black", fg = "white", insertbackground = "white")
codigo.place(x = 30, y = 95)

lineaCodigo =  StringVar()
lblInstruccion = Label(text="Ingresa Instrucción: ",font=("Times New Roman",12, "bold")).place(x=30,y=520)
txtUsuario = Entry(ventana,textvariable = lineaCodigo, width = 65, bg ="black", fg = "white", insertbackground = "white").place(x=173,y=525)
runLinea = Button(ventana, text ="Ejecutar",font=("Times New Roman",12,"bold"), relief=RAISED, cursor="arrow").place(x=580,y=518)

ventana.mainloop()