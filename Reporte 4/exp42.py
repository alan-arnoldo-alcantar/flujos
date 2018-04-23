from rep4 import Grafo
from scipy import stats
import numpy as np

avgdist = list()
cluster = list()
k=3
n=50
with open('coef.csv', 'w') as t:
	for p in range(20):
		g=Grafo()
		g.nodos(n)
		g.conectar(n,k,p/20)
		d = g.cluster(n)
		cluster.append(d)
		f = g.avgdist(n,k,p/20)[0]
		avgdist.append(f)
		print(n)
		print(p/20, f, d, file=t)
#print('tiempos avgdist')
#print(tiempos_avgdist)

with open('coef.plot', 'w') as avgdist:
	print('set term eps', file=avgdist)
	print('set output "coef.eps"', file=avgdist)
	print("set ylabel 'Distancia mas corta promedio'", file=avgdist)
	print("set y2label 'Coeficiente de clustering'", file=avgdist)
	print("set xlabel 'Probabilidad'",file=avgdist)
	print('set xrange [-0.1:1.0]',file=avgdist)
	print("plot 'coef.csv' u 1:2 w lines lt 7 lw 2 title 'D', '' u 1:3 w lines lt 5 lw 2 title 'Coef. cluster'", file=avgdist)