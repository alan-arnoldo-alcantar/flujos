from math import sqrt

class Grafo:

    def __init__(self):
        self.nodos = dict()     #la etiqueta es el nodo y el contenido son las coordenadas
        self.aristas = dict()   #la etiqueta es el par de nodos conectados y el contenido es el tama;o de la arista
        self.vecinos = dict()   #la etiqueta es un nodo y el contenido son todos los nodos con los que tiene conexion

    def vertices(self, i, x, y, t):
    	self.nodos[i] = (x, y, t)

    def unir(self, i, j, q):
        d = sqrt((self.nodos[j][0] - self.nodos[i][0])**2 + (self.nodos[j][1] - self.nodos[i][1])**2)
        if d <= self.nodos[i][1]*q:
            self.agregar(i, j)

    def agregar(self, i, j, w = 0):
        self.aristas[(i,j)] = w
        if not i in self.vecinos:
            self.vecinos[i] = set()
        if not j in self.vecinos:
            self.vecinos[j] = set()
        self.vecinos[i].add(j)
        self.vecinos[j].add(i)

