from graphics import *

def main():
    win = GraphWin("APODORAX", 800, 600)

    # Circulo
    # insertaCirculo(1.0, 4.0, 8.0, "rojo", "amarillo", 5);
    c = Circle(Point(1.0,4.0), 8.0)
    c.setFill("red")
    c.setOutline("yellow")
    c.setWidth("5")
    c.draw(win)

    # Linea
    l = Line(Point(300,300), Point(500,100))
    l.setWidth("3")
    l.setFill("blue")
    # Para agregar formato de flecha: first, last, both. El default es none
    #l.setArrow("last")
    l.draw(win)

    # Rectangulo
    r = Rectangle(Point(500,420), Point(780,500))
    r.setFill("green")
    r.setWidth("8")
    r.setOutline("gray")
    r.draw(win)

    # Texto
    t = Text(Point(640,460), "APODORAX Compiler")
    # Tamano de la letra
    t.setSize(12)
    # Font (helvetica, courier, times roman, arial )
    t.setFace("courier")
    t.setFill("orange")
    # Style (normal, bold, italic, bold italic)
    t.setStyle("bold italic")
    t.draw(win)

    # Punto
    p = Point(290,75)
    p.setFill("blue")
    p.draw(win)

    p = Point(310,75)
    p.setFill("gray")
    p.draw(win)

    # Ovalo (forma ovalo en box invisible)
    o = Oval(Point(100,500), Point(250,300))
    o.setWidth("2")
    o.setFill("yellow")
    o.setOutline("black")
    o.draw(win)

    # Triangulo
    tri = Polygon(Point(600,200), Point(500,300), Point(700,300))
    tri.setFill("pink")
    tri.setWidth("20")
    tri.setOutline("green")
    tri.draw(win)

    # Imagen (solo gif)
    # img = Image(Point(400,500), "spongebob.gif")
    # img.draw(win)

    #Curva (no debe haber una diferencia muy grande entre puntos)
    c1 = Point(10,100)
    c1x = c1.getX()
    c1y = c1.getY()
    c2 = Point(400,200)
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
    	auxc.setOutline("red")
    	auxc.draw(win)	
    	cont += 0.001

    # Quitar el dibujo
    #t.undraw()
    # Mover objeto  
    #l.move(100,100)
    win.getMouse() # Pausar para ver el resultado
    win.close()    # Cerrar la ventana

main()