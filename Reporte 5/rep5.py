from math import fabs
import random
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
					if q==0:
						self.coor.append((j,i,7))
						print(j,i,7,file=n)
					if q==self.nn-1:
						self.coor.append((j,i,22))
						print(j,i,22,file=n)
					else:
						self.coor.append((j,i,0))
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
							self.pesos[(i,self.coor.index((x,y_s)))]=1							
							print(self.coor[i][0],self.coor[i][1],x,y_s,file=a)
							if not i in self.vecinos:
								self.vecinos[i] = set()
							self.vecinos[i].add(self.coor.index((x,y_s)))
						if ((x,y_i)) in self.coor:
							self.pesos[(i,self.coor.index((x,y_i)))]=1							
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
									self.pesos_p[(i,j)]=1
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
			print('plot "'+filename1+'" u 1:2 w points pt 7 lc "gray", "'+filename2+'" u 1:2:($3-$1):($4-$2) w vectors nohead lc "black", "'+filename3+'" u 1:2:($3-$1):($4-$2) w vectors head lw 2 lc "red"',file=grafica)

		return self.nodos, self.coor, self.pesos, self.pesos_p, self.vecinos

class Eliminar():
	def __init__(self):
		self.nodos=set()
		self.coor=list()
		self.pesos=dict()
		self.pesos_p=dict()
		self.vecinos=dict()
		self.n=int()
		self.nn=int()
		self.comodin=set()
		self.comodin2=set()
		self.grafo_completo=dict()

	def eli_ver(self,nodos_ori,coor_ori,pesos_ori,pesos_p_ori,vecinos_ori,k):
		for i in range (1,k**2-1):
			self.comodin.add(i)
		for i in range(k**2):
			self.comodin2.add(i)
		self.nodos=nodos_ori
		self.coor=coor_ori
		self.pesos=pesos_ori
		self.pesos_p=pesos_p_ori
		self.vecinos=vecinos_ori
		self.n=k
		self.nn=k**2
		print(self.comodin)
		quitar_ver=random.sample(self.comodin,k**2-2)
		print(quitar_ver)
		print(self.vecinos)
		p=1
		for i in quitar_ver:
			for j in range(self.nn):
				print(i,j)
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
				if u in self.vecinos:
					if len(self.vecinos[u]) == 0:
						self.nodos.remove(u)
						del self.vecinos[u]
			print(self.vecinos)
			print(self.nodos)

			self.grafo_completo.clear()

			for (i,j) in self.pesos_p:
				self.grafo_completo[(i,j)]=self.pesos_p[(i,j)]
			for (i,j) in self.pesos:
				self.grafo_completo[(i,j)]=self.pesos[(i,j)]

			filename1='aristaspk'+str(k)+'ev'+str(p)+'.csv'
			filename2='nodosk'+str(k)+'ev'+str(p)+'.csv'
			filename3='aristask'+str(k)+'ev'+str(p)+'.csv'
			filename4='graficak'+str(k)+'ev'+str(p)+'.plot'
			with open (filename1,'w') as g:
				for (i,j) in self.pesos_p:
					print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=g)
			with open(filename2,'w') as v:
				for i in self.nodos:
					print(self.coor[i][0],self.coor[i][1],file=v)
			with open(filename3,'w') as g:
				for i in range(self.nn-1):
					for j in range(i+1,self.nn):
						if ((i,j)) in self.pesos:
							print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=g)

			with open(filename4,'w') as grafica:
				print('set term eps',file=grafica)
				print('set output "grafok'+str(k)+'ev'+str(p)+'.eps"',file=grafica)
				print('set xrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
				print('set yrange[-0.1:'+str(self.n-1)+'.1]',file=grafica)
				print('unset border',file=grafica)
				print('unset xtics',file=grafica)
				print('unset ytics',file=grafica)
				print('unset key',file=grafica)
				if len(self.pesos_p) > 0:
					print('plot "'+filename2+'" u 1:2 w points pt 7 lc "gray", "'+filename3+'" u 1:2:($3-$1):($4-$2) w vectors nohead lc "black", "'+filename1+'" u 1:2:($3-$1):($4-$2) w vectors head lw 2 lc "red"',file=grafica)
				else:
					print('plot "'+filename2+'" u 1:2 w points pt 7 lc "gray", "'+filename3+'" u 1:2:($3-$1):($4-$2) w vectors nohead lc "black", "',file=grafica)
			p=p+1

	def eli_ari(self,nodos_ori,coor_ori,pesos_ori,pesos_p_ori,vecinos_ori,k,p):
		self.nodos=nodos_ori
		self.coor=coor_ori
		self.pesos=pesos_ori
		self.pesos_p=pesos_p_ori
		self.vecinos=vecinos_ori
		self.n=k
		self.nn=k**2
		q=0
		while q < p:
			(i,j)=random.sample(range(self.nn),2)
			if ((i,j)) in self.pesos:
				del self.pesos[(i,j)]
				del self.pesos[(j,i)]
				self.vecinos[i].remove(j)
				self.vecinos[j].remove(i)
				if len(self.vecinos[i]) == 0:
					self.nodos.remove(i)
					del self.vecinos[i]
				if len(self.vecinos[j]) == 0:
					self.nodos.remove(j)
					del self.vecinos[j]
				q=q+1

		with open ('aristasp2.csv','w') as g:
			for (i,j) in self.pesos_p:
				self.pesos[(i,j)]=self.pesos_p[(i,j)]
				print(self.coor[i][0],self.coor[i][1],self.coor[j][0],self.coor[j][1],file=g)
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
			print('plot "nodos2.csv" u 1:2 w points pt 7 lc "gray", "aristas2.csv" u 1:2:($3-$1):($4-$2) w vectors nohead lc "black", "aristasp2.csv" u 1:2:($3-$1):($4-$2) w vectors head lw 2 lc "red"',file=grafica)
