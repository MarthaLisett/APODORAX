from graphics import *
class Graphics():
	def __init__(self):
		self.win = GraphWin("APODORAX", 800, 600)

	def build_figure(self, name, parameter_lst):
		"""
		for param in parameter_lst:
			print "llego el parametro:" + str(param)
		"""
		self.c = None
		self.l = None
		self.r = None
		self.t = None
		self.p = None
		self.o = None
		self.tri = None
		self.point_list = []

		if name == "insertaCirculo":
			# insertaCirculo(1.0, 4.0, 8.0, "rojo", "amarillo", 5);
			self.c = Circle(Point(float(parameter_lst[0]), float(parameter_lst[1])), float(parameter_lst[2]))
			self.c.setFill(self.get_color_name(parameter_lst[3]))
			self.c.setOutline(self.get_color_name(parameter_lst[4]))
			self.c.setWidth(str(float(parameter_lst[5])))
			self.c.draw(self.win)
			
		elif name == "insertaLinea":
			self.l = Line(Point(float(parameter_lst[0]), float(parameter_lst[1])),
				Point(float(parameter_lst[2]), float(parameter_lst[3])))
			self.l.setFill(self.get_color_name(parameter_lst[4]))
			self.l.setWidth(str(parameter_lst[5]))
			self.l.draw(self.win)

		elif name == "insertaRectangulo":
			self.r = Rectangle(Point(float(parameter_lst[0]), float(parameter_lst[1])),
				Point(float(parameter_lst[2]), float(parameter_lst[3])))
			self.r.setFill(self.get_color_name(parameter_lst[4]))
			self.r.setOutline(self.get_color_name(parameter_lst[5]))
			self.r.setWidth(str(parameter_lst[6]))
			self.r.draw(self.win)

		elif name == "insertaTexto":
			texto = parameter_lst[3].replace('"', "")
			self.t = Text(Point(float(parameter_lst[0]), float(parameter_lst[1])), texto)
			self.t.setFill(self.get_color_name(parameter_lst[2]))
			self.t.setSize(parameter_lst[4])
			self.t.setFace("courier")
			self.t.setStyle("bold italic")
			self.t.draw(self.win)

		elif name == "insertaPunto":
			self.p = Point(float(parameter_lst[0]), float(parameter_lst[1]))
			self.p.setFill(self.get_color_name(str(parameter_lst[2])))
			self.p.draw(self.win)

		elif name == "insertaOvalo":
			self.o = Oval(Point(float(parameter_lst[0]), float(parameter_lst[1])),
				Point(float(parameter_lst[2]), float(parameter_lst[3])))
			self.o.setFill(self.get_color_name(parameter_lst[4]))
			self.o.setOutline(self.get_color_name(parameter_lst[5]))
			self.o.setWidth(str(parameter_lst[6]))
			self.o.draw(self.win)

		elif name == "insertaTriangulo":
			self.tri = Polygon(Point(float(parameter_lst[0]), float(parameter_lst[1])),
				Point(float(parameter_lst[2]), float(parameter_lst[3])),
				Point(float(parameter_lst[4]), float(parameter_lst[5])))
			self.tri.setFill(self.get_color_name(parameter_lst[6]))
			self.tri.setOutline(self.get_color_name(parameter_lst[7]))
			self.tri.setWidth(str(parameter_lst[8]))
			self.tri.draw(self.win)

		elif name == "insertaCurva":
			c1 = Point(float(parameter_lst[0]), float(parameter_lst[1]))
			c1x = c1.getX()
			c1y = c1.getY()
			c2 = Point(parameter_lst[2], parameter_lst[3])
			c2x = c2.getX()
			c2y = c2.getY()

			curvx = 300
			curvy = 400
			
			# Hecha con la curva de Bezier: https://en.wikipedia.org/wiki/B%C3%A9zier_curve
			cont = 0.0
			while cont < 1:
				x = (1-cont)*(1-cont)*c1x + 2*(1-cont)*cont*curvx+cont*cont*c2x
				y = (1-cont)*(1-cont)*c1y + 2*(1-cont)*cont*curvy+cont*cont*c2y
				self.auxc = Point(x,y)
				self.auxc.setOutline(self.get_color_name(parameter_lst[4]))
		    	self.auxc.draw(self.win)	
		    	cont += 0.001



	def display_graphics(self):
		self.win.getKey()
		self.win.close()

	def get_color_name(self, color_esp):
		colors_eng = {
			'"rojo"'   : "red"   ,'"amarillo"': "yellow",
			'"azul"'   : "blue"  , '"rosa"'   : "pink"  ,
			'"naranja"': "orange", '"verde"'  : "green" ,
			'"negro"'  : "black" , '"gris"'   : "gray"  ,
		}
		return colors_eng.get(color_esp)














