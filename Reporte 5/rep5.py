from math import fabs
import random
import time
class Grafo():
	def __init__(self):
		self.nodos=set()
		self.coor=list()
		self.pesos=dict()
		self.pesos_p=dict()
		self.vecinos=dict()
		self.n=int()
		self.nn=int()

	def red(self,k,l):
		#NODOS
		self.n=k
		self.nn=k**2
		q=0
		filename1='nodosk'+str(self.n)+'.csv'
		with open(filename1,'w') as n:
			for i in range(k-1,-1,-1):
				for j in range(k):
					self.nodos.add(q)
					self.coor.append((j,i))
					if q ==0:
						print(j,i,2,file=n)
					elif q ==self.nn-1:
						print(j,i,22,file=n)
					else:
						print(j,i,0,file=n)
					q=q+1
		#ARISTAS
		filename2='aristask'+str(self.n)+'.csv'
		with open(filename2,'w') as a:
			for i in self.nodos:
				for p in range(1,l+1):
					for j in range(p,-p-1,-1):
						x=self.coor[i][0]+j
						y_s=self.coor[i][1]+p-fabs(j)
						y_i=self.coor[i][1]+fabs(j)-p
						if ((x,y_s)) in self.coor:
							self.pesos[(i,self.coor.index((x,y_s)))]=int(random.normalvariate(6,1))
							print(self.coor[i][0],self.coor[i][1],x,y_s,file=a)
							if not i in self.vecinos:
								self.vecinos[i] = set()
							self.vecinos[i].add(self.coor.index((x,y_s)))
						if ((x,y_i)) in self.coor:
							self.pesos[(i,self.coor.index((x,y_i)))]=int(random.normalvariate(6,1))
							print(self.coor[i][0],self.coor[i][1],x,y_i,file=a)
							if not i in self.vecinos:
								self.vecinos[i] = set()
							self.vecinos[i].add(self.coor.index((x,y_i)))

	def aristasp(self,p):
		filename1='nodosk'+str(self.n)+'.csv'
		filename2='aristask'+str(self.n)+'.csv'
		filename3='aristaspk'+str(self.n)+'.csv'
		with open(filename3,'w') as b:
				for i in range(self.nn):
					for j in range(self.nn):
						if i != j:
							if random.random() <= p:
								if ((i,j)) not in self.pesos:
									self.pesos_p[(i,j)]=int(random.expovariate(0.1))+1
									print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=b)
									self.vecinos[i].add(j)
		#GRAFICA
		filename4='graficak'+str(self.n)+'.plot'
		with open(filename4,'w') as grafica:
			print('set term eps',file=grafica)
			print('set output "grafok'+str(self.n)+'.eps"',file=grafica)
			print('set xrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
			print('set yrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
			print('unset border',file=grafica)
			print('unset xtics',file=grafica)
			print('unset ytics',file=grafica)
			print('unset key',file=grafica)
			print('plot "'+filename1+'" u 1:2:3 w points pt 7 ps 2 lc var, "'+filename2+'" u 1:2:($3-$1):($4-$2) w vectors nohead lw 7 lc "black", "'+filename3+'" u 1:2:($3-$1):($4-$2) w vectors head lw 2 lc "red"',file=grafica)

		return self.nodos, self.coor, self.pesos, self.pesos_p, self.vecinos

class Eliminar():
	def __init__(self,nodos_ori,coor_ori,pesos_ori,pesos_p_ori,vecinos_ori,k):
		self.nodos=nodos_ori
		self.coor=coor_ori
		self.pesos=pesos_ori
		self.pesos_p=pesos_p_ori
		self.vecinos=vecinos_ori
		self.n=k
		self.nn=k**2
		self.comodin=set()
		self.comodin2=set()
		self.grafo_completo=dict()

	def eli_ver(self):
		tiempos=[]
		for i in range (1,self.nn-1):
			self.comodin.add(i)
		for i in range(self.nn):
			self.comodin2.add(i)
		quitar_ver=random.sample(self.comodin,self.nn-2)
		p=1
		for i in quitar_ver:
			for j in range(self.nn):
				if ((i,j)) in self.pesos:
					del self.pesos[(i,j)]
					self.vecinos[i].remove(j)
				if ((j,i)) in self.pesos:
					del self.pesos[(j,i)]
					self.vecinos[j].remove(i)
				if ((i,j)) in self.pesos_p:
					del self.pesos_p[(i,j)]
					self.vecinos[i].remove(j)
				if ((j,i)) in self.pesos_p:
					del self.pesos_p[(j,i)]
					self.vecinos[j].remove(i)
			for u in self.comodin2:
				if u != 0 and u != (self.nn-1):
					if u in self.vecinos:
						if len(self.vecinos[u]) == 0:
							self.nodos.remove(u)
							del self.vecinos[u]

			self.grafo_completo.clear()

			for (i,j) in self.pesos_p:
				self.grafo_completo[(i,j)]=self.pesos_p[(i,j)]
			for (i,j) in self.pesos:
				self.grafo_completo[(i,j)]=self.pesos[(i,j)]

			flujo, tiempo = self.ford_fulkerson()
			tiempos.append((p,flujo,tiempo))

			filename1='aristaspk'+str(self.n)+'ev'+str(p)+'.csv'
			filename2='nodosk'+str(self.n)+'ev'+str(p)+'.csv'
			filename3='aristask'+str(self.n)+'ev'+str(p)+'.csv'
			filename4='graficak'+str(self.n)+'ev'+str(p)+'.plot'
			with open (filename1,'w') as g:
				for (i,j) in self.pesos_p:
					print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=g)
			with open(filename2,'w') as v:
				for i in self.nodos:
					if i==0:
						print(self.coor[i][0],self.coor[i][1],2,file=v)
					elif i==self.nn-1:
						print(self.coor[i][0],self.coor[i][1],22,file=v)
					else:
						print(self.coor[i][0],self.coor[i][1],0,file=v)
			with open(filename3,'w') as g:
				for i in range(self.nn-1):
					for j in range(i+1,self.nn):
						if ((i,j)) in self.pesos:
							print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=g)

			with open(filename4,'w') as grafica:
				print('set term eps',file=grafica)
				print('set output "grafok'+str(self.n)+'ev'+str(p)+'.eps"',file=grafica)
				print('set xrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
				print('set yrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
				print('unset border',file=grafica)
				print('unset xtics',file=grafica)
				print('unset ytics',file=grafica)
				print('unset key',file=grafica)
				if len(self.pesos_p) > 0:
					print('plot "'+filename2+'" u 1:2:3 w points pt 7 ps 2 lc var, "'+filename3+'" u 1:2:($3-$1):($4-$2) w vectors nohead lw 7 lc "black", "'+filename1+'" u 1:2:($3-$1):($4-$2) w vectors head lw 2 lc "red"',file=grafica)
				else:
					print('plot "'+filename2+'" u 1:2:3 w points pt 7 ps 2 lc var, "'+filename3+'" u 1:2:($3-$1):($4-$2) w vectors nohead lw 7 lc "black", "',file=grafica)
			p=p+1

			if flujo==0:
				break
		return tiempos

	def eli_ari(self,p):
		tiempos=[]
		flujo=1
		q=0
		while flujo!=0:
			a=0
			while a <p:
				(i,j)=random.sample(range(self.nn),2)
				if ((i,j)) in self.pesos:
					b=0
					c=0
					del self.pesos[(i,j)]
					del self.pesos[(j,i)]
					self.vecinos[i].remove(j)
					self.vecinos[j].remove(i)
					a=a+1
					for t in self.nodos:
						if i in self.vecinos[t]:
							b=1
					if len(self.vecinos[i]) == 0 and b==0:
						self.nodos.remove(i)
						del self.vecinos[i]
					for t in self.nodos:
						if j in self.vecinos[t]:
							c=1
					if len(self.vecinos[j]) == 0 and c==0:
						self.nodos.remove(j)
						del self.vecinos[j]
			q=q+p
			self.grafo_completo.clear()

			for (i,j) in self.pesos_p:
				self.grafo_completo[(i,j)]=self.pesos_p[(i,j)]
			for (i,j) in self.pesos:
				self.grafo_completo[(i,j)]=self.pesos[(i,j)]

			flujo, tiempo = self.ford_fulkerson()
			tiempos.append((q,flujo,tiempo))

			filename1='aristaspk'+str(self.n)+'ea'+str(q)+'.csv'
			filename2='nodosk'+str(self.n)+'ea'+str(q)+'.csv'
			filename3='aristask'+str(self.n)+'ea'+str(q)+'.csv'
			filename4='graficak'+str(self.n)+'ea'+str(q)+'.plot'

			with open (filename1,'w') as g:
				for (i,j) in self.pesos_p:
					print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=g)
			with open(filename2,'w') as v:
				for i in self.nodos:
					if i==0:
						print(self.coor[i][0],self.coor[i][1],2,file=v)
					elif i==self.nn-1:
						print(self.coor[i][0],self.coor[i][1],22,file=v)
					else:
						print(self.coor[i][0],self.coor[i][1],0,file=v)
			with open(filename3,'w') as g:
				for i in range(self.nn-1):
					for j in range(i+1,self.nn):
						if ((i,j)) in self.pesos:
							print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=g)
			with open(filename4,'w') as grafica:
				print('set term eps',file=grafica)
				print('set output "grafok'+str(self.n)+'ea'+str(q)+'.eps"',file=grafica)
				print('set xrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
				print('set yrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
				print('unset border',file=grafica)
				print('unset xtics',file=grafica)
				print('unset ytics',file=grafica)
				print('unset key',file=grafica)
				if len(self.pesos_p) > 0:
					print('plot "'+filename2+'" u 1:2:3 w points pt 7 ps 2 lc var, "'+filename3+'" u 1:2:($3-$1):($4-$2) w vectors nohead lw 7 lc "black", "'+filename1+'" u 1:2:($3-$1):($4-$2) w vectors head lw 2 lc "red"',file=grafica)
				else:
					print('plot "'+filename2+'" u 1:2:3 w points pt 7 ps 2 lc var, "'+filename3+'" u 1:2:($3-$1):($4-$2) w vectors nohead lw 7 lc "black", "',file=grafica)
		return tiempos

	def camino(self, f):
		cola = [0]
		usados = set()
		camino = dict()
		while len(cola) > 0:
			u = cola.pop(0)
			usados.add(u)
			for (x, y) in self.grafo_completo:
				if x == u and y not in cola and y not in usados:
					actual = f.get((u,y), 0)
					dif = self.grafo_completo[(u,y)] - actual
					if dif > 0:
						cola.append(y)
						camino[y] = (u,dif)
		if self.nn-1 in usados:
			return camino
		else: #no se alcanzo
			return None

	def ford_fulkerson(self):		#'s' es el nodo como fuente y 't' es el nodo sumidero
		inicio = time.clock()
		if 0 == self.nn-1:
			return 0
		maximo = 0
		f = dict()
		while True:
			aum = self.camino(f)
			if aum is None:
				break #ya no hay
			incr = min(aum.values(), key = (lambda k: k[1]))[1]
			u = self.nn-1
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