from rep5 import Grafo, Eliminar
import numpy as np
tiempos_v=list()
tiempos_a=list()
arreglo=dict()
n=10
l=2
p=0.01
for i in range(10):
	print(i)
	g=Grafo()
	g.red(n,l)
	nodos_ori, coor_ori, pesos_ori, pesos_p_ori, vecinos_ori = g.aristasp(p)
	e=Eliminar(nodos_ori, coor_ori, pesos_ori, pesos_p_ori, vecinos_ori,n)
	#tiempos_v=e.eli_ver()+tiempos_v
	tiempos_a=e.eli_ari(10)+tiempos_a
	

#print(tiempos_a)
for (i,j,k) in tiempos_a:
	if i not in arreglo:
		arreglo[i]=list()
	if i in arreglo:
		arreglo[i].append(k)
t=[x for x in range(0,201,10)]
with open('desviacion.csv', 'w') as e:
	for n in arreglo:
		if n in t:
			print(n,arreglo[n])
			print(n,np.percentile(arreglo[n],0),np.percentile(arreglo[n],25),np.median(arreglo[n]),np.percentile(arreglo[n],75),np.percentile(arreglo[n],100), file=e)

with open('desviacion.plot', 'w') as avgdist:
	print('set term eps', file=avgdist)
	print('set output "desviacion.eps"', file=avgdist)
	print('set boxwidth 3.5 absolute', file=avgdist)
	print("set ylabel 'Tiempo (segundos)'", file=avgdist)
	print("set xlabel 'Número de nodos'",file=avgdist)
	print("plot 'desviacion.csv' u 1:3:2:6:5 w candlesticks lt 3 lw 2 notitle whiskerbars, '' u 1:4:4:4:4 w candlesticks lt -1 lw 2 notitle", file=avgdist)