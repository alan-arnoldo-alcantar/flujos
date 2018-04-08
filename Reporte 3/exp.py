from new import Grafo
from scipy import stats
import numpy as np

i = [20,40,60,80,100,120,140,160,180,200] #200
tiempos_ford = dict()
tiempos_floy = dict()
p_ford = list()
p_floy = list()
tem=100
modo='simple'
id=0
with open('tiempos.csv', 'w') as a:
	for n in i:
		s=0
		t=n-1
		tiempos_ford[n] = list()
		tiempos_floy[n] = list()
		for k in range(15):
			g=Grafo()
			g.nodos(n,tem)
			g.conectar(n,modo)
			tiempos_ford[n].append(g.ford_fulkerson(s,t)[1]) 
			tiempos_floy[n].append(g.floy_warshall()[1])
		print(n)
		print(n, tiempos_ford[n], file=a)
		print(n, tiempos_floy[n], file=a)
#print('tiempos ford')
#print(tiempos_ford)
#print('tiempos floy')
#print(tiempos_floy)
id=0
with open('p_value.csv', 'w') as t:
	for n in i:
		p_ford.append((n,stats.shapiro(tiempos_ford[n])[1]))
		p_floy.append((n,stats.shapiro(tiempos_floy[n])[1]))
		print(n, p_ford[id][1], p_floy[id][1], file=t)
		id=id+1

with open('error_ford.csv', 'w') as e:
	for n in i:
		print(n,np.percentile(tiempos_ford[n],0),np.percentile(tiempos_ford[n],25),np.median(tiempos_ford[n]),np.percentile(tiempos_ford[n],75),np.percentile(tiempos_ford[n],100), file=e)

with open('error_floy.csv', 'w') as e:
	for n in i:
		print(n,np.percentile(tiempos_floy[n],0),np.percentile(tiempos_floy[n],25),np.median(tiempos_floy[n]),np.percentile(tiempos_floy[n],75),np.percentile(tiempos_floy[n],100), file=e)

with open('error_ford.plot', 'w') as ford:
	print('set term eps', file=ford)
	print('set output "error_ford.eps"', file=ford)
	print('set boxwidth 0.2 absolute', file=ford) 
	print("plot 'error_ford.csv' u 1:3:2:6:5 w candlesticks lt 3 lw 2 notitle whiskerbars, '' u 1:4:4:4:4 w candlesticks lt -1 lw 2 notitle", file=ford)

with open('error_floy.plot', 'w') as floy:
	print('set term eps', file=floy)
	print('set output "error_floy.eps', file=floy)
	print('set boxwidth 0.2 absolute', file=floy)
	print("plot 'error_floy.csv' u 1:3:2:6:5 w candlesticks lt 3 lw 2 notitle whiskerbars, '' u 1:4:4:4:4 w candlesticks lt -1 lw 2 notitle", file=floy)