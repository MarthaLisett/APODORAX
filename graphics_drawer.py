 from graphics import *
class Graphics():
	def __init__(self):
		"""Inicializacion y creacion de la ventana que servira de canvas"""
		self.win = GraphWin("APODORAX", 800, 600)

	def build_figure(self, name, parameter_lst):
		"""Dibuja la figura especificada en funcion del valor de los parametros 
		dados por el programador.
		Args:
			name: Nombre de la figura.
			parameter_lst: Lista de parametros"""
		"""
		for param in parameter_lst:
			print "llego el parametro:" + str(param)
		"""
		# Variables que representan a los dibujos de cada tipo
		self.c = None
		self.l = None
		self.r = None
		self.t = None
		self.p = None
		self.o = None
		self.tri = None
		self.point_list = []

		# Dibujamos el circulo de acuerdo a los parametros especificados y las restricciones de la libreria
		# Parametros: coordx, coordy, radio, colorFondo, colorOrilla, grosor
		if name == "insertaCirculo":
			self.c = Circle(Point(float(parameter_lst[0]), float(parameter_lst[1])), float(parameter_lst[2]))
			self.c.setFill(self.get_color_name(parameter_lst[3]))
			self.c.setOutline(self.get_color_name(parameter_lst[4]))
			self.c.setWidth(str(float(parameter_lst[5])))
			self.c.draw(self.win)
		
		# Dibujamos la linea de acuerdo a los parametros especificados y las restricciones de la libreria
		# Parametros: coordx1, coordy1, coordx2, coordy2, color, grosor
		elif name == "insertaLinea":
			self.l = Line(Point(float(parameter_lst[0]), float(parameter_lst[1])),
				Point(float(parameter_lst[2]), float(parameter_lst[3])))
			self.l.setFill(self.get_color_name(parameter_lst[4]))
			self.l.setWidth(str(parameter_lst[5]))
			self.l.draw(self.win)

		# Dibujamos la linea de acuerdo a los parametros especificados y las restricciones de la libreria
		# Parametros: coordx1, coordy1, coordx2, coordy2, colorFondo, colorOrilla, grosor
		elif name == "insertaRectangulo":
			self.r = Rectangle(Point(float(parameter_lst[0]), float(parameter_lst[1])),
				Point(float(parameter_lst[2]), float(parameter_lst[3])))
			self.r.setFill(self.get_color_name(parameter_lst[4]))
			self.r.setOutline(self.get_color_name(parameter_lst[5]))
			self.r.setWidth(str(parameter_lst[6]))
			self.r.draw(self.win)

		# Escribe texto en la pantalla de acuerdo a los parametros especificados y las restricciones de la libreria
		# Parametros: coordx, coordy, color, tamanio
		elif name == "insertaTexto":
			texto = parameter_lst[3].replace('"', "")
			self.t = Text(Point(float(parameter_lst[0]), float(parameter_lst[1])), texto)
			self.t.setFill(self.get_color_name(parameter_lst[2]))
			self.t.setSize(parameter_lst[4])
			self.t.setFace("courier")
			self.t.setStyle("bold italic")
			self.t.draw(self.win)

		# Dibujamos un punto en la pantalla de acuerdo a los parametros especificados y las restricciones de la libreria
		# Parametros coordx, coordy, color
		elif name == "insertaPunto":
			self.p = Point(float(parameter_lst[0]), float(parameter_lst[1]))
			self.p.setFill(self.get_color_name(str(parameter_lst[2])))
			self.p.draw(self.win)

		# Dibujamos un ovalo en la pantalla de acuerdo a los parametros especificados y las restricciones de la libreria
		# Parametros: coordx1, coordy1, coordx2, coordy2, colorFondo, colorOrilla, grosor
		elif name == "insertaOvalo":
			self.o = Oval(Point(float(parameter_lst[0]), float(parameter_lst[1])),
				Point(float(parameter_lst[2]), float(parameter_lst[3])))
			self.o.setFill(self.get_color_name(parameter_lst[4]))
			self.o.setOutline(self.get_color_name(parameter_lst[5]))
			self.o.setWidth(str(parameter_lst[6]))
			self.o.draw(self.win)

		# Dibujamos un triangulo en la pantalla de acuerdo a los parametros especificados y las restricciones de la libreria
		# Parametros: coordx1, coordy1, coordx2, coordy2, coordx3, coordy3, colorFondo, colorOrilla, grosor
		elif name == "insertaTriangulo":
			self.tri = Polygon(Point(float(parameter_lst[0]), float(parameter_lst[1])),
				Point(float(parameter_lst[2]), float(parameter_lst[3])),
				Point(float(parameter_lst[4]), float(parameter_lst[5])))
			self.tri.setFill(self.get_color_name(parameter_lst[6]))
			self.tri.setOutline(self.get_color_name(parameter_lst[7]))
			self.tri.setWidth(str(parameter_lst[8]))
			self.tri.draw(self.win)
		
		# Dibujamos una curva en la pantalla de acuerdo a los parametros especificados y las restricciones de la libreria
		# Parametros: coordx1, coordy1, coordx2, coordy2, color
		elif name == "insertaCurva":
			c1 = Point(float(parameter_lst[0]), float(parameter_lst[1]))
			c1x = c1.getX()
			c1y = c1.getY()
			c2 = Point(float(parameter_lst[2]), float(parameter_lst[3]))
			c2x = c2.getX()
			c2y = c2.getY()

			curvx = 300
			curvy = 400
			
			# Hecha con la curva de Bezier: https://en.wikipedia.org/wiki/B%C3%A9zier_curve
			cont = 0.0
			while cont < 1:
				# Calculamos las coordenadas de inicio de la curva
				x = (1-cont)*(1-cont)*c1x + 2*(1-cont)*cont*curvx+cont*cont*c2x
				y = (1-cont)*(1-cont)*c1y + 2*(1-cont)*cont*curvy+cont*cont*c2y
				# Se dibuja un punto en esas coordenadas
				self.auxc = Point(x,y)
				# Se asigna un color
				self.auxc.setOutline(self.get_color_name(parameter_lst[4]))
				# Se pinta la figura
				self.auxc.draw(self.win)
				# Se utiliza la razon de cambio para variar las coordenadas y se repite el proceso
				cont += 0.001

	def display_graphics(self):
		"""Cierra la ventana con los dibujos por el medio especificado en el metodo"""
		self.win.getKey()
		self.win.close()

	def get_color_name(self, color_esp):
		"""Mapea los nombres de los colores especificados por el usuario en espanol 
		a ingles para que sean manejables por la libreria.
		Args:
			color_esp: Color en espanol.
		Regresa:
			Nombre en ingles del color."""
		colors_eng = {
			'"rojo"'   : "red"   ,'"amarillo"': "yellow",
			'"azul"'   : "blue"  , '"rosa"'   : "pink"  ,
			'"naranja"': "orange", '"verde"'  : "green" ,
			'"negro"'  : "black" , '"gris"'   : "gray"  ,
		}
		return colors_eng.get(color_esp)