from graphics import *
class Graphics():
	def build_figure(self, name, parameter_lst):
		self.win = GraphWin("APODORAX", 800, 600)

		"""
		for param in parameter_lst:
			print "llego el parametro:" + str(param)
		"""

		if name == "insertaCirculo":
			# insertaCirculo(1.0, 4.0, 8.0, "rojo", "amarillo", 5);
			c = Circle(Point(parameter_lst[0], parameter_lst[1]), parameter_lst[2])
			c.setFill(self.get_color_name(parameter_lst[3]))
			c.setOutline(self.get_color_name(parameter_lst[4]))
			c.setWidth(str(float(parameter_lst[5])))
			c.draw(self.win)
	
		elif name == "insertaLinea":
			l = Line(Point(parameter_lst[0], parameter_lst[1]), Point(parameter_lst[3], parameter_lst[4]))
			l.setFill(self.get_color_name(parameter_lst[5]))
			l.setWidth(str(parameter_lst[6]))
			l.draw(self.win)

		elif name == "insertaRectangulo":
			r = Rectangle(Point(parameter_lst[0], parameter_lst[1]), Point(parameter_lst[2], parameter_lst[3]))
			r.setFill(parameter_lst[4])
			r.setOutline(parameter_lst[5])
			r.setWidth(str(parameter_lst[6]))
			r.draw(win)

		elif name == "insertaTexto":
			t = Text(Point(parameter_lst[0], parameter_lst[1]), parameter_lst[3])
			t.setFill(parameter_lst[2])
			t.setSize(parameter_lst[4])
			t.setFace("courier")
			t.setStyle("bold italic")
			t.draw(win)

		elif name == "insertaPunto":
			p = Point(parameter_lst[0], parameter_lst[1])
			p.setFill(str(parameter_lst[2]))
			p.draw(win)

		elif name == "insertaOvalo":
			o = Oval(Point(parameter_lst[0], parameter_lst[1]), Point(parameter_lst[2], parameter_lst[3]))
			o.setFill(parameter_lst[4])
			o.setOutline(parameter_lst[5])
			o.setWidth(str(parameter_lst[6]))
			o.draw(win)

		elif name == "insertaTriangulo":
			tri = Polygon(Point(parameter_lst[0], parameter_lst[1]),
				Point(parameter_lst[2], parameter_lst[3]),
				Point(parameter_lst[4], parameter_lst[5]))
			tri.setFill(parameter_lst[6])
			tri.setOutline(parameter_lst[7])
			tri.setWidth(str(parameter_lst[8]))
			tri.draw(win)

		elif name == "insertaCurva":
			c1 = Point(parameter_lst[0], parameter_lst[1])
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
				auxc = Point(x,y)
				auxc.setOutline(parameter_lst[4])
				auxc.draw(win)	
				cont += 0.001

	def pause_execution(self):
		self.win.getMouse()

	def get_color_name(self, color_esp):
		colors_eng = {
			'"rojo"'   : 'red'   ,'"amarillo"': "yellow",
			"azul"     : "blue"  , '"rosa"'   : "pink"  ,
			'"naranja"': "orange", '"verde"'  : "green" ,
			'"negro"'  : "black" , '"gris"'   : "gray"  ,
		}
		return colors_eng.get(color_esp)
