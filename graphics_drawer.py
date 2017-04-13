from graphics import *
class Graphics():
	def build_figure(self, name, parameter_lst):
		win = GraphWin("APODORAX", 800, 600)
		if name == "insertaCirculo":
			# Circulo
			# insertaCirculo(1.0, 4.0, 8.0, "rojo", "amarillo", 5);
			c = Circle(Point(parameter_lst[0], parameter_lst[1]), parameter_lst[2])
			c.setFill("red")
			c.setOutline("yellow")
			c.setWidth(str(float(parameter_lst[5])))
			c.draw(win)
