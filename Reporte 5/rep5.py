from math import fabs
import random
class Grafo():
	def __init__(self):
		self.nodos=set()
		self.coor=list()
		self.pesos=dict()
		self.n=int()
		self.nn=int()

	def red(self,k,l):
		#NODOS
		self.n=k
		self.nn=k**2
		q=0
		with open('nodos1.csv','w') as n:
			for i in range(k-1,-1,-1):
				for j in range(k):
					self.nodos.add(q)
					self.coor.append((i,j))
					print(i,j,file=n)
					q=q+1
		#ARISTAS
		with open('aristas1.csv','w') as a:
			for i in self.nodos:
				for p in range(1,l+1):
					for j in range(p,-p-1,-1):
						x=self.coor[i][0]+j
						y_s=self.coor[i][1]+p-fabs(j)
						y_i=self.coor[i][1]+fabs(j)-p
						if ((x,y_s)) in self.coor:
							self.pesos[(i,self.coor.index((x,y_s)))]=1							
							print(self.coor[i][0],self.coor[i][1],x,y_s,file=a)
						if ((x,y_i)) in self.coor:
							self.pesos[(i,self.coor.index((x,y_i)))]=1							
							print(self.coor[i][0],self.coor[i][1],x,y_i,file=a)

	def aristasp(self,p):
		with open('aristasp.csv','w') as b:
				for i in range(self.nn):
					for j in range(self.nn):
						if i != j:
							if random.random() <= p:
								if ((i,j)) not in self.pesos:
									self.pesos[(i,j)]=1
									print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=b)
		#GRAFICA
		with open('grafica1.plot','w') as grafica:
			print('set term eps',file=grafica)
			print('set output "grafo1.eps"',file=grafica)
			print('set xrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
			print('set yrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
			print('unset border',file=grafica)
			print('unset xtics',file=grafica)
			print('unset ytics',file=grafica)
			print('unset key',file=grafica)
			print('plot "nodos1.csv" u 1:2 w points pt 7 lc "gray", "aristas1.csv" u 1:2:($3-$1):($4-$2) w vectors nohead lc "black", "aristasp.csv" u 1:2:($3-$1):($4-$2) w vectors head lw 2 lc "red"',file=grafica)

	def eli_ver(self,p):
		quitar_ver=random.sample(self.nodos,int(self.nn*p/100))
		print(quitar_ver)
		for i in quitar_ver:
			for j in range(self.nn):
				if ((i,j)) in self.pesos:
					del self.pesos[(i,j)]
				if ((j,i)) in self.pesos:
					del self.pesos[(j,i)]
			print(self.pesos)
			self.nodos.remove(i)
			print(self.nodos)

	def eli_ari(self,p):
		print(int(len(self.pesos)/2*p/100))
		k=0
		while k < int(len(self.pesos)/2*p/100):
			(i,j)=random.sample(range(self.nn),2)
			if ((i,j)) in self.pesos:
				del self.pesos[(i,j)]
				del self.pesos[(j,i)]
				k=k+1

		with open('nodos2.csv','w') as v:
			for i in self.nodos:
				print(self.coor[i][0],self.coor[i][1],file=v)
		with open('aristas2.csv','w') as g:
			for i in range(self.nn-1):
				for j in range(i+1,self.nn):
					if ((i,j)) in self.pesos:
						print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=g)

		with open('grafica2.plot','w') as grafica:
			print('set term eps',file=grafica)
			print('set output "grafo2.eps"',file=grafica)
			print('set xrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
			print('set yrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
			print('unset border',file=grafica)
			print('unset xtics',file=grafica)
			print('unset ytics',file=grafica)
			print('unset key',file=grafica)
			print('plot "nodos2.csv" u 1:2 w points pt 7 lc "gray", "aristas2.csv" u 1:2:($3-$1):($4-$2) w vectors nohead lc "black", "aristasp.csv" u 1:2:($3-$1):($4-$2) w vectors head lw 2 lc "red"',file=grafica)
