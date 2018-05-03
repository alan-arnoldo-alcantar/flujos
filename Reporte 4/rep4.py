from math import pi, sin, cos, log, exp
from random import random
import time
#tenemos que hacer un cagadero
#grafo redondo
#conectar de grafo con los parametros n, k>= 1
#avgdist(g) calcular la distancia promedio entre dos vertices del grafo
	#Average path length is a concept in network topology that is defined as the 
	#average number of steps along the shortest paths for all possible pairs of network nodes. 
	#It is a measure of the efficiency of information or mass transport on a network
#desarrollar una funcion que me de una cota superior para la distancia maxima posible en un grafo que dependa de los parametros n, k
#normalizar el avgdist con la cota superior maxima
#clustcoef(g) densidad de conexiones entre los vecinos de un vertices, al quitar el vertice, es el promedi???????????????
##########################################################################################################################
##########################################################################################################################
#vamo aser el grafo redonde
class Grafo():
	def __init__(self):
		self.vertices=set()
		self.coor=list()
		self.aristas=dict()
		self.comodin=list()
		self.vecinos=dict()

	def nodos(self,n):
		#numero de nodos
		theta=2*pi/n
		with open('nodos.csv','w') as nodos:
			for i in range(n):
				print(cos(i*theta),sin(i*theta),file=nodos)
				self.coor.append((cos(i*theta),sin(i*theta)))
				self.vertices.add(i)

	def grafica(self):
		with open('grafica.plot','w') as grafica:
			print('set term eps',file=grafica)
			print('set output "grafo.eps"',file=grafica)
			print('set xrange[-1.2:1.2]',file=grafica)
			print('set yrange[-1.2:1.2]',file=grafica)
			print('unset xtics',file=grafica)
			print('unset ytics',file=grafica)
			print('unset key',file=grafica)
			print('plot "nodos.csv" u 1:2 w points pt 7 lt 1, "aristas.csv" u 1:2:($3-$1):($4-$2) w vectors nohead lt 7, "aristasp.csv" u 1:2:($3-$1):($4-$2) w vectors nohead lt 22',file=grafica)
#vamo a conectar
	def conectar(self,n,k,q):
		with open('aristas.csv','w') as a:
			for p in range(n):
				for j in range(1,k+1):
					if ((p,p+j)) not in self.aristas:
						self.aristas[(p,(p+j)%n)] = 1
						self.aristas[((p+j)%n,p)] = 1
						print(self.coor[p][0],self.coor[p][1],self.coor[(p+j)%n][0],self.coor[(p+j)%n][1],file=a)
						if not p in self.vecinos:
							self.vecinos[p] = set()
						if not ((p+j)%n) in self.vecinos:
							self.vecinos[(p+j)%n] = set()
						self.vecinos[p].add((p+j)%n)
						self.vecinos[(p+j)%n].add(p)
		with open('aristasp.csv','w') as b:
			for i in range(n-1):
				for j in range(i+1,n):
					if random() >= q: 
						if ((i,j)) not in self.aristas:
							self.aristas[(i,j)]=1
							self.aristas[(j,i)]=1
							print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=b)
							self.vecinos[i].add(j)
							self.vecinos[j].add(i)
	#coeficiente de cluster
	def cluster(self,n):
		clu = 0
		for i in self.vertices:
			t=len(self.vecinos[i])
			con=0
			for j in self.vecinos[i]:
				for k in self.vecinos[j]:
					if k in self.vecinos[i]:
						con=con+1
			clu = clu + con/(t*(t-1))
		return clu/n
	#distancia minima entre dos nodos
	def avgdist(self,n,k,p):			#no se le da de comer 
		h=0
		inicio = time.clock()
		d = {}
		for v in self.vertices:
			d[(v,v)] = 0 #la distancia reflexiva es cero
			for u in self.vecinos[v]: #para vecinos, la distancia es el peso
				d[(v,u)] = self.aristas[(v,u)]				
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
		sdm = 0 #suma de las distancias minimas entre cualquier nodo
		for (i,j) in d:
			sdm=sdm+d[(i,j)]	#sumando las distancias minimas entre todos los pares de nodos
		adm = sdm/(n*(n-1))	#distancia minima promedio
		final = time.clock()
		tiempo = final - inicio
		return adm, tiempo