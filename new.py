from random import random
from math import sqrt
import time

class Grafo:

	def __init__(self):
		self.meta_data = list() #aqui van las coordenadas de cada punto y la temperatura del punto
		self.vertices = set()	#son la etiqueta de cada nodo (numero de cada punto)
		self.aristas = dict()	#aristas que forman el grafo
		self.vecinos = dict()	#vecinos de cada nodo (aristas que conectan cada nodo con los demas)

	#GENERAR PUNTOS Y TEMPERATURAS
	def nodos(self, n, t):		#'n' es el numero de nodos y 't' es la temperatura maxima del sistema
		with open('nodos.csv', 'w') as nodos:
			for i in range(n):
				x = random()
				y = random()
				self.meta_data.append((x, y, y*t))	#guardar las coordenadas y temperatura
				self.vertices.add(i)				#guardar la etiqueta (numero del nodo)
				print(x, y, y*t, file = nodos)

	#CONECTAR LOS PUNTOS PARA FORMAR EL GRAFO
	def conectar(self, n, modo):		#'n' es el numero de nodos y 'modo' puede ser 'simple', 'dirigido', 'ponderado' (siempre debe ponerse entre comillas simples)
		with open('aristas.csv', 'w') as aristas:
			if modo == 'simple' or modo == 'ponderado':
				for i in range(n-1):
					for j in range(i+1,n):
						dis = sqrt((self.meta_data[j][0]-self.meta_data[i][0])**2+(self.meta_data[j][1]-self.meta_data[i][1])**2)
						w = int(self.meta_data[i][2]+self.meta_data[j][2])
						if random() <= dis:
							self.aristas[(i,j)] = (w)
							print(self.meta_data[i][0],self.meta_data[i][1],self.meta_data[j][0],self.meta_data[j][1],w, file = aristas)
							if not i in self.vecinos:
								self.vecinos[i] = set()
							if not j in self.vecinos:
								self.vecinos[j] = set()
							self.vecinos[i].add(j)
							self.vecinos[j].add(i)
			elif modo == 'dirigido' or modo == 'campechano':
				for i in range(n):
					for j in range(n):
						dis = sqrt((self.meta_data[j][0]-self.meta_data[i][0])**2+(self.meta_data[j][1]-self.meta_data[i][1])**2)
						w = int(self.meta_data[i][2]+self.meta_data[j][2])
						if random() <= dis:
							self.aristas[(i,j)] = (w)
							print(self.meta_data[i][0],self.meta_data[i][1],self.meta_data[j][0],self.meta_data[j][1],w, file = aristas)
							if not i in self.vecinos:
								self.vecinos[i] = set()
							if not j in self.vecinos:
								self.vecinos[j] = set()
							self.vecinos[i].add(j)
							self.vecinos[j].add(i)

	#GRAFICAR GRAFO
	def grafica(self, modo):		#'modo' puede ser 'simple', 'dirigido', 'ponderado' (siempre debe ponerse entre comillas simples)
		with open('grafica.plot', 'w') as grafica:
			print('set term png', file = grafica)
			print('set key off', file = grafica)
			print('set xrange[-0.1:1.1]', file = grafica)
			print('set yrange[-0.1:1.1]', file = grafica)
			print('plot ', file = grafica)
			if modo == 'simple':
				print('set output "simple.png"', file = grafica)
				print('plot "aristas.csv" u 1:2:($3-$1):($4-$2):5 w vectors head filled lc palette, "nodos.csv" with points palette pt 7 ps 2', file = grafica)
				print('quit()', file = grafica)

############################################################
############################################################
#CODIGO DE LA PROFE
	def camino(self, s, t, f):
		cola = [s]
		usados = set()
		camino = dict()
		while len(cola) > 0:
			u = cola.pop(0)
			usados.add(u)
			for (x, y) in self.aristas:
				if x == u and y not in cola and y not in usados:
					actual = f.get((u,y), 0)
					dif = self.aristas[(u,y)] - actual
					if dif > 0:
						cola.append(y)
						camino[y] = (u,dif)
		if t in usados:
			return camino
		else: #no se alcanzo
			return None

	def ford_fulkerson(self, s, t):		#'s' es el nodo como fuente y 't' es el nodo sumidero
		inicio = time.clock()
		if s == t:
			return 0
		maximo = 0
		f = dict()
		while True:
			aum = self.camino(s, t, f)
			if aum is None:
				break #ya no hay
			incr = min(aum.values(), key = (lambda k: k[1]))[1]
			u = t
			while u in aum:
				v = aum[u][0]
				actual = f.get((v,u), 0) #cero si no hay
				inverso = f.get((u,v), 0)
				f[(v,u)] = actual + incr
				f[(u,v)] = inverso - incr
				u = v
			maximo += incr
		final = time.clock()
		tiempo = final - inicio
		return maximo, tiempo

	def floy_warshall(self):			#no se le da de comer 
		inicio = time.clock()
		d = {}
		for v in self.vertices:
			d[(v,v)] = 0 #la distancia reflexiva es cero
			for u in self.vecinos[v]: #para vecinos, la distancia es el peso
				if (v,u) in self.aristas:
					d[(v,u)] = self.aristas[(v,u)]
				else:
					d[(v,u)] = self.aristas[(u,v)]
		for intermedio in self.vertices:
			for desde in self.vertices:
				for hasta in self.vertices:
					di = None
					if (desde, intermedio) in d:
						di = d[(desde,intermedio)]
					ih = None
					if (intermedio,hasta) in d:
						ih = d[(intermedio,hasta)]
					if di is not None and ih is not None:
						c = di + ih #largo del camino via "i"
						if (desde,hasta) not in d or c < d[(desde,hasta)]:
							d[(desde,hasta)] = c #mejora al camino actual
		final = time.clock()
		tiempo = final - inicio
		return d, tiempo