from rep4 import Grafo
from new import Grafo
from scipy import stats
import numpy as np

a = [20,40,60,80,100,120,140,160,180,200] #200
tiempos_avgdist = dict()
k=3
p=0.95
with open('tiempos.csv', 'w') as a:
	for n in a:
		tiempos_avgdist[n] = list()
		for k in range(10):
			g=Grafo()
			g.nodos(n)
			g.conectar(n,k,p)
			tiempos_avgdist[n].append(g.avgdist(n,k,p)[1])
		print(n)
		print(n, tiempos_avgdist[n], file=a)
#print('tiempos avgdist')
#print(tiempos_avgdist)

with open('error_avgdist.csv', 'w') as e:
	for n in i:
		print(n,np.percentile(tiempos_avgdist[n],0),np.percentile(tiempos_avgdist[n],25),np.median(tiempos_avgdist[n]),np.percentile(tiempos_avgdist[n],75),np.percentile(tiempos_avgdist[n],100), file=e)

with open('error_avgdist.plot', 'w') as avgdist:
	print('set term eps', file=avgdist)
	print('set output "error_avgdist.eps"', file=avgdist)
	print('set boxwidth 5.0 absolute', file=avgdist)
	print("set ylabel 'Tiempo (segundos)'", file=avgdist)
	print("set xlabel 'Número de nodos'",file=avgdist)
	print('g(x) = a*x**3+b*x**2+c*x+d', file=avgdist)
	print("fit g(x) 'error_avgdist.csv' u 1:4 via a, b, c, d", file=avgdist)
	print("plot 'error_avgdist.csv' u 1:3:2:6:5 w candlesticks lt 3 lw 2 notitle whiskerbars, '' u 1:4:4:4:4 w candlesticks lt -1 lw 2 notitle, g(x) lc 7 lw 2 notitle", file=avgdist)