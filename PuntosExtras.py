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
	from graphics import *
	linea = lineaCodigo.get()
	# Quitar espacios en blanco
	linea = linea.replace(" ", "")
	# Separar parametros
	linea = re.split('[(),]', linea)
	nombreFuncion = linea[0]
	
	# insertaTexto(300.0, 300.0, "rojo", "hola mundo", 12);
	# insertaTriangulo(600, 200, 500, 300, 700, 300, "rojo", "amarillo", 12);
	# insertaRectangulo(500, 400, 780, 500, "rojo", "amarillo", 12);
	# insertaCirculo(300, 300, 50.3, "rojo", "amarillo", 4);
	# insertaOvalo(100, 500, 250, 300, "gris", "rosa", 12);
	# insertaPunto(290, 75, "azul");
	# insertaLinea(300, 300, 500, 100, "azul", 13);
	# insertaCurva(10, 100, 400, 200, "verde");

	if (nombreFuncion == "insertaCirculo"):
		parametro1 = float(linea[1])
		parametro2 = float(linea[2])
		radio = float(linea[3])
		color1 = str(linea[4])
		color1 = color1.replace('"', "")
		
		if color1 == "rojo":
			color1 = "red"
		elif color1 == "amarillo":
			color1 = "yellow"
		elif color1 == "azul":
			color1 = "blue"
		elif color1 == "rosa":
			color1 = "pink"
		elif color1 == "naranja":
			color1 = "orange"
		elif color1 == "negro":
			color1 = "black"
		elif color1 == "verde":
			color1 = "green"
		elif color1 == "gris":
			color1 = "gray"

		color2 = linea[5]
		color2 = color2.replace('"', "")

		if color2 == "rojo":
			color2 = "red"
		elif color2 == "amarillo":
			color2 = "yellow"
		elif color2 == "azul":
			color2 = "blue"
		elif color2 == "rosa":
			color2 = "pink"
		elif color2 == "naranja":
			color2 = "orange"
		elif color2 == "negro":
			color2 = "black"
		elif color2 == "verde":
			color2 = "green"
		elif color2 == "gris":
			color2 = "gray"
		
		grosor = linea[6]
		win = GraphWin("APODORAX", 800, 600)
		c = Circle(Point(parametro1,parametro2), radio)
		c.setFill(str(color1))
		c.setOutline(str(color2))
		c.setWidth(str(grosor))
		c.draw(win)

	elif (nombreFuncion == "insertaRectangulo"):
		coordx1 = float(linea[1])
		coordy1 = float(linea[2])
		coordx2 = float(linea[3])
		coordy2 = float(linea[4])
		color1 = str(linea[5])
		color1 = color1.replace('"', "")

		if color1 == "rojo":
		   color1 = "red"
		elif color1 == "amarillo": 
		   color1 = "yellow"
		elif color1 == "azul":
		   color1 = "blue"
		elif color1 == "rosa":
		   color1 = "pink"
		elif color1 == "naranja":
		   color1 = "orange"
		elif color1 == "negro":
		   color1 = "black"
		elif color1 == "verde":
		   color1 = "green"
		elif color1 == "gris":
		   color1 = "gray"

		color2 = linea[6]
		color2 = color2.replace('"', "")

		if color2 == "rojo":
			color2 = "red"
		elif color2 == "amarillo":
			color2 = "yellow"
		elif color2 == "azul":
			color2 = "blue"
		elif color2 == "rosa":
			color2 = "pink"
		elif color2 == "naranja":
			color2 = "orange"
		elif color2 == "negro":
			color2 = "black"
		elif color2 == "verde":
			color2 = "green"
		elif color2 == "gris":
			color2 = "gray"
		
		grosor = int(linea[7])
		win = GraphWin("APODORAX", 800, 600)
		r = Rectangle(Point(coordx1,coordy1), Point(coordx2,coordy2))
		r.setFill(str(color1))
		r.setWidth(grosor)
		r.setOutline(str(color2))
		r.draw(win)

	elif (nombreFuncion == "insertaTexto"):
		parametro1 = float(linea[1])
		parametro2 = float(linea[2])
		color1 = str(linea[3])
		color1 = color1.replace('"', "")
		
		if color1 == "rojo":
			color1 = "red"
		elif color1 == "amarillo":
			color1 = "yellow"
		elif color1 == "azul":
			color1 = "blue"
		elif color1 == "rosa":
			color1 = "pink"
		elif color1 == "naranja":
			color1 = "orange"
		elif color1 == "negro":
			color1 = "black"
		elif color1 == "verde":
			color1 = "green"
		elif color1 == "gris":
			color1 = "gray"

		texto = linea[4]
		texto = texto.replace('"', "")
		grosor = int(linea[5])

		win = GraphWin("APODORAX", 800, 600)
		t = Text(Point(parametro1,parametro2), str(texto))
		# Tamano de la letra
		t.setSize(grosor)
		# Font (helvetica, courier, times roman, arial)
		t.setFace("courier")
		t.setFill(str(color1))
		# Style (normal, bold, italic, bold italic)
		t.setStyle("bold italic")
		t.draw(win)

	elif (nombreFuncion == "insertaTriangulo"):
		coordx1 = float(linea[1])
		coordy1 = float(linea[2])
		coordx2 = float(linea[3])
		coordy2 = float(linea[4])
		coordx3 = float(linea[5])
		coordy3 = float(linea[6])
		color1 = str(linea[7])
		color1 = color1.replace('"', "")
		
		if color1 == "rojo":
			color1 = "red"
		elif color1 == "amarillo":
			color1 = "yellow"
		elif color1 == "azul":
			color1 = "blue"
		elif color1 == "rosa":
			color1 = "pink"
		elif color1 == "naranja":
			color1 = "orange"
		elif color1 == "negro":
			color1 = "black"
		elif color1 == "verde":
			color1 = "green"
		elif color1 == "gris":
			color1 = "gray"

		color2 = linea[8]
		color2 = color2.replace('"', "")

		if color2 == "rojo":
			color2 = "red"
		elif color2 == "amarillo":
			color2 = "yellow"
		elif color2 == "azul":
			color2 = "blue"
		elif color2 == "rosa":
			color2 = "pink"
		elif color2 == "naranja":
			color2 = "orange"
		elif color2 == "negro":
			color2 = "black"
		elif color2 == "verde":
			color2 = "green"
		elif color2 == "gris":
			color2 = "gray"
		
		grosor = int(linea[9])
		win = GraphWin("APODORAX", 800, 600)
		tri = Polygon(Point(coordx1,coordy1), Point(coordx2,coordy2), Point(coordx3,coordy3))
		tri.setFill(str(color1))
		tri.setWidth(grosor)
		tri.setOutline(str(color2))
		tri.draw(win)

	elif (nombreFuncion == "insertaOvalo"):
		coordx1 = float(linea[1])
		coordy1 = float(linea[2])
		coordx2 = float(linea[3])
		coordy2 = float(linea[4])
		color1 = str(linea[5])
		color1 = color1.replace('"', "")
		
		if color1 == "rojo":
			color1 = "red"
		elif color1 == "amarillo":
			color1 = "yellow"
		elif color1 == "azul":
			color1 = "blue"
		elif color1 == "rosa":
			color1 = "pink"
		elif color1 == "naranja":
			color1 = "orange"
		elif color1 == "negro":
			color1 = "black"
		elif color1 == "verde":
			color1 = "green"
		elif color1 == "gris":
			color1 = "gray"

		color2 = linea[6]
		color2 = color2.replace('"', "")

		if color2 == "rojo":
			color2 = "red"
		elif color2 == "amarillo":
			color2 = "yellow"
		elif color2 == "azul":
			color2 = "blue"
		elif color2 == "rosa":
			color2 = "pink"
		elif color2 == "naranja":
			color2 = "orange"
		elif color2 == "negro":
			color2 = "black"
		elif color2 == "verde":
			color2 = "green"
		elif color2 == "gris":
			color2 = "gray"
		
		grosor = int(linea[7])
		win = GraphWin("APODORAX", 800, 600)
		o = Oval(Point(coordx1,coordy1), Point(coordx2,coordy2))
		o.setWidth(grosor)
		o.setFill(str(color1))
		o.setOutline(str(color2))
		o.draw(win)

	elif (nombreFuncion == "insertaPunto"):
		parametro1 = float(linea[1])
		parametro2 = float(linea[2])
		color1 = str(linea[3])
		color1 = color1.replace('"', "")
		
		if color1 == "rojo":
			color1 = "red"
		elif color1 == "amarillo":
			color1 = "yellow"
		elif color1 == "azul":
			color1 = "blue"
		elif color1 == "rosa":
			color1 = "pink"
		elif color1 == "naranja":
			color1 = "orange"
		elif color1 == "negro":
			color1 = "black"
		elif color1 == "verde":
			color1 = "green"
		elif color1 == "gris":
			color1 = "gray"

		win = GraphWin("APODORAX", 800, 600)
		p = Point(parametro1,parametro2)
		p.setFill(str(color1))
		p.draw(win)

	elif (nombreFuncion == "insertaLinea"):
		coordx1 = float(linea[1])
		coordy1 = float(linea[2])
		coordx2 = float(linea[3])
		coordy2 = float(linea[4])
		color1 = str(linea[5])
		color1 = color1.replace('"', "")

		if color1 == "rojo":
		   color1 = "red"
		elif color1 == "amarillo": 
		   color1 = "yellow"
		elif color1 == "azul":
		   color1 = "blue"
		elif color1 == "rosa":
		   color1 = "pink"
		elif color1 == "naranja":
		   color1 = "orange"
		elif color1 == "negro":
		   color1 = "black"
		elif color1 == "verde":
		   color1 = "green"
		elif color1 == "gris":
		   color1 = "gray"
		
		grosor = int(linea[6])
		win = GraphWin("APODORAX", 800, 600)
		l = Line(Point(coordx1,coordy1), Point(coordx2,coordy2))
		l.setWidth(grosor)
		l.setFill(str(color1))
		l.draw(win)

	elif (nombreFuncion == "insertaCurva"):
		coordx1 = float(linea[1])
		coordy1 = float(linea[2])
		coordx2 = float(linea[3])
		coordy2 = float(linea[4])
		color1 = str(linea[5])
		color1 = color1.replace('"', "")

		if color1 == "rojo":
		   color1 = "red"
		elif color1 == "amarillo": 
		   color1 = "yellow"
		elif color1 == "azul":
		   color1 = "blue"
		elif color1 == "rosa":
		   color1 = "pink"
		elif color1 == "naranja":
		   color1 = "orange"
		elif color1 == "negro":
		   color1 = "black"
		elif color1 == "verde":
		   color1 = "green"
		elif color1 == "gris":
		   color1 = "gray"
		
		win = GraphWin("APODORAX", 800, 600)
		curvx = 300
		curvy = 400
		# Hecha con la curva de Bezier: https://en.wikipedia.org/wiki/B%C3%A9zier_curve
		cont = 0.0
		while cont < 1:
			x = (1-cont)*(1-cont)*coordx1 + 2*(1-cont)*cont*curvx+cont*cont*coordx2
			y = (1-cont)*(1-cont)*coordy1 + 2*(1-cont)*cont*curvy+cont*cont*coordy2
			auxc = Point(x,y)
			auxc.setOutline(str(color1))
			auxc.draw(win)
			cont += 0.001



lblApodorax = Label(text="APODORAX",font=("Times New Roman",24,"bold"), fg = "red").place(x=260,y=10)
run = Button(ventana, text ="Compilar",font=("Times New Roman",14,"bold"), relief=RAISED, cursor="arrow", command = obtenerCodigo).place(x=300,y=50)

codigo = Text(width = 78, height = 25, wrap = WORD,  bg ="black", fg = "white", insertbackground = "white")
codigo.place(x = 30, y = 95)

lineaCodigo =  StringVar()
lblInstruccion = Label(text="Ingresa Instrucción: ",font=("Times New Roman",12, "bold")).place(x=30,y=520)
txtUsuario = Entry(ventana,textvariable = lineaCodigo, width = 65, bg ="black", fg = "white", insertbackground = "white").place(x=173,y=525)
runLinea = Button(ventana, text ="Ejecutar",font=("Times New Roman",12,"bold"), relief=RAISED, cursor="arrow", command = obtenerInstruccion).place(x=580,y=518)

ventana.mainloop()