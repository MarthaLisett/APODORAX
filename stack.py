'''
Implementacion de la clase STACK (lifo) el ultimo elemento que se agrega es el primero que sale.
Codigo de: https://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html
'''
class Stack:
    '''inicializacion de la lista variable para los elementos del stack'''
    def __init__(self):
        self.items = []
    '''regresa verdadero si el stack esta vacio; falso en caso contrario'''
    def isEmpty(self):
        return self.items == []
    '''agrega un elemento al stack, (por seguir un esquema lifo) el elemento queda hasta arriba del stack'''
    def push(self, item):
        self.items.append(item)
    '''regresa el elemento que se encuentra hasta arriba del stack (el ultimo que se agrego.
        El elemento se elimina del stack'''
    def pop(self):
        return self.items.pop()
    '''regresa el elemento que se encuentra hasta arriba del stack (el ultimo que se agrego).
        El elemento se queda en el stack (no se elimina)'''
    def peek(self):
        return self.items[len(self.items)-1]
    '''regresa la cantidad de elementos presentes en el stack'''
    def size(self):
        return len(self.items)