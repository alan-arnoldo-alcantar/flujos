from math import sqrt
from random import random

class Grafo:

    def __init__(self):
        self.nodos = dict()     #la etiqueta es el nodo y el contenido son las coordenadas
        self.aristas = dict()   #la etiqueta es el par de nodos conectados y el contenido es el tama;o de la arista
        self.vecinos = dict()   #la etiqueta es un nodo y el contenido son todos los nodos con los que tiene conexion

    def vertices(self, i, t):
    	for j in range(i):
    		y = random()
    		self.nodos[j] = (random(), y, y*t)

    def graficar(self, modo):
    	with open('nodos.csv', 'w') as p:
    		for i in self.nodos:
    			print(self.nodos[i][0], self.nodos[i][1], self.nodos[i][2], file =p)
    	id = 1

    	with open('nodos.plot', 'w') as q:
    		print('set term png', file = q)
    		print('set size square', file = q)
    		print('set key off', file =q)
    		print('set xrange[-.1:1.1]', file = q)
    		print('set yrange[-.1:1.1]', file = q)
    		print('set xlabel "Longitud(m)"', file = q)
    		print('set ylabel "Longitud(m)"', file = q)
    		if modo == 'simple':
    			print('set output "simple.png"', file = q)
    			for (x,y) in self.aristas:
    				print('set arrow', id, 'from', self.nodos[x][0], ',', self.nodos[x][1], 'to', self.nodos[y][0], ',', self.nodos[y][1], 'nohead', file = q )
    				id = id + 1
    		elif modo == 'ponderado':
    			print('set output "ponderado.png"', file = q)
    			for (x,y) in self.aristas:
    				print('set arrow', id, 'from', self.nodos[x][0], ',', self.nodos[x][1], 'to', self.nodos[y][0], ',', self.nodos[y][1], 'nohead', file = q )
    				print('set label', "'", int(self.aristas[(x,y)][2]), "'", 'at', self.aristas[(x,y)][0], ',', self.aristas[(x,y)][1], file = q)
    				id = id + 1
    		elif modo == 'dirigido':
    			print('set output "dirigido.png"', file = q)
    			for (x,y) in self.aristas:
    				print('set arrow', id, 'from', self.nodos[x][0], ',', self.nodos[x][1], 'to', self.nodos[y][0], ',', self.nodos[y][1], 'head filled size 0.1,10,5', file = q )
    				id = id + 1
    		elif modo == 'campechano':
    			print('set output "campechano.png"', file = q)
    			for (x,y) in self.aristas:
    				print('set arrow', id, 'from', self.nodos[x][0], ',', self.nodos[x][1], 'to', self.nodos[y][0], ',', self.nodos[y][1], 'head filled size 0.07,10,5', file = q )
    				print('set label', "'", int(self.aristas[(x,y)][2]), "'", 'at', self.aristas[(x,y)][0], ',', self.aristas[(x,y)][1], file = q)
    				id = id + 1
    		print('plot "nodos.csv" with points palette pt 7 ps 3', file = q)
    		print('quit()', file = q)

    def unir(self, i, alpha):
	    for k in range(i-1):
	    	for l in range(k+1, i):
	    		d = sqrt((self.nodos[l][0] - self.nodos[k][0])**2 + (self.nodos[l][1] - self.nodos[k][1])**2)
	    		if d <= self.nodos[k][1]*alpha:
	    			xm = (self.nodos[l][0] + self.nodos[k][0])/2 
	    			ym = (self.nodos[l][1] + self.nodos[k][1])/2
	    			w = (self.nodos[l][2] + self.nodos[k][2])/10
	    			self.aristas[(k,l)] = (xm, ym, w)
	    			if not k in self.vecinos:
	    				self.vecinos[k] = set()
	    			if not l in self.vecinos:
	    				self.vecinos[l] = set()
	    			self.vecinos[k].add(l)
	    			self.vecinos[l].add(k)