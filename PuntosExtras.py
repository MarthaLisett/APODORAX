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
# from graphics import *
import subprocess, os, re
#from graphics import *

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


def obtenerInstruccion():
	linea = lineaCodigo.get()
	# Quitar espacios en blanco
	linea = linea.replace(" ", "")
	# Separar parametros
	linea = re.split('[(),]', linea)
    
    # insertaTexto(2.0, 3.0, "rojo", "hola mundo", 12);
	# insertaTriangulo(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, "rojo", "amarillo", 12);
	# insertaRectangulo(1.0, 2.0, 3.0, 4.0, "rojo", "amarillo", 12);
	# insertaCirculo(1.0, 4.0, 8.0, "rojo", "amarillo", 12);
	# insertaOvalo(1.0, 4.0, 8.0, 9.0, "rojo", "amarillo", 12);
	# insertaPunto(1.0, 2.0, "azul");
	# insertaLinea(1.0, 2.0, 3.0, 4.0, "azul", 13);
	# insertaCurva(1.0, 2.0, 3.0, 4.0, "verde");

	nombreFuncion = linea[0]
	print (nombreFuncion)
	parametro1 = linea[1]
	print (parametro1)
	parametro2 = linea[2]
	print (parametro2)
	radio = linea[3]
	print (radio)
	color1 = linea[4]
	print (color1)
	color2 = linea[5]
	print (color2)
	grosor = linea[6]
	print (grosor)

	if (nombreFuncion == "insertaCirculo"):
		print (nombreFuncion)


lblApodorax = Label(text="APODORAX",font=("Times New Roman",24,"bold"), fg = "red").place(x=260,y=10)
run = Button(ventana, text ="Compilar",font=("Times New Roman",14,"bold"), relief=RAISED, cursor="arrow", command = obtenerCodigo).place(x=300,y=50)

codigo = Text(width = 78, height = 25, wrap = WORD,  bg ="black", fg = "white", insertbackground = "white")
codigo.place(x = 30, y = 95)

lineaCodigo =  StringVar()
lblInstruccion = Label(text="Ingresa Instrucción: ",font=("Times New Roman",12, "bold")).place(x=30,y=520)
txtUsuario = Entry(ventana,textvariable = lineaCodigo, width = 65, bg ="black", fg = "white", insertbackground = "white").place(x=173,y=525)
runLinea = Button(ventana, text ="Ejecutar",font=("Times New Roman",12,"bold"), relief=RAISED, cursor="arrow", command = obtenerInstruccion).place(x=580,y=518)

ventana.mainloop()