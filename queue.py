'''
Implementacion de la clase QUEUE (fifo), el primer elemento que se agrega es el primero que sale (es una fila).
Codigo de: http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html
'''
class Queue:
    '''inicializacion de la lista variable con los elementos de la queue'''
    def __init__(self):
        self.items = []
    '''regresa verdadero si la queue esta vacia; falso en caso contrario'''
    def isEmpty(self):
        return self.items == []
    '''se agrega a la queue un elemento, (como el esquema es fifo)
    el elemento se agrega en la primera posicion de la lista'''
    def enqueue(self, item):
        self.items.insert(0, item)
    '''regresa el primer elemento que se agrego, este se elimina de la lista'''
    def dequeue(self):
        return self.items.pop()
    '''regresa la cantidad de elementos en la queue'''
    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]