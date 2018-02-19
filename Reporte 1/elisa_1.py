###################################################################################################################################################
#CONSTRUIR UN GRAFO CON PUNTOS AL AZAR Y CON ARISTAS CON PROBABILIDAD
from random import random
from math import sqrt

#pedir el numero de nodos
n = 15
id = 1
q = 0
alpha = 0.9
temp = 100

#crear una lista para guardar las coordenadas
nodos = []

#crear lista para aristas
aristas = []
y_min = 1.0
y_max = 0.1
# generar de forma aleatoria n puntos con colores diferentes 
for i in range(n):
	x = random()
	y = random()
	if y < y_min:
		y_min = y
		mi = i
	if y > y_max:
		y_max = y
		ma = i
	nodos.append((x,y))

#abrir archivo para guardar las aristas de conexion
with open("aristas.csv", "w") as g:
	for i in range(n):
		for j in range(n):
			p = y_min/nodos[i][1]*alpha
			#dos puntos debes de tener una probabilidad random menor a p
			if i == j:
				continue
			else:
				d = sqrt((nodos[i][0]-nodos[j][0])**2 + (nodos[i][1]-nodos[j][1])**2)
				if d <= p:
					print(nodos[i][0], nodos[i][1], nodos[j][0], nodos[j][1], file = g)
					aristas.append((nodos[i][0], nodos[i][1], nodos[j][0], nodos[j][1]))
					#contador de aristas para cada nodo
					q = q + 1

#abrir archivo para guardar las coordenadas color y tamaño
with open("nodos.csv", "w") as w:
	for i in range(n):
		print(nodos[i][0], nodos[i][1], y_min/nodos[i][1]*temp, file = w)

with open("regiones.csv", "w") as w:
	print(nodos[mi][0],nodos[mi][1],alpha, file = w)
	print(nodos[ma][0],nodos[ma][1],nodos[mi][1]/nodos[ma][1]*alpha, file = w)

with open ("nodos.plot", 'w') as salida: #Archivo para poder generar mi grafica de salida.
	print ('set term pngcairo size 1000,1000', file = salida) 
	#png para formato de salida de mi grafica
	print ('set output "nodos.png"', file = salida) 
	print ('set size square', file = salida)
	#Keyoff es para que la marca de agua que sale en la parte superior der. no se vea.
	print ('set key off', file = salida)
	#El rango x y y son para el tamanio en que va a salir mi grafica.
	print ('set xrange [-.1:1.1]', file = salida)
	print ('set yrange [-.1:1.1]', file = salida)
	print('set xlabel "Longitud (m)"', file = salida)
	print('set ylabel "Longitud (m)"', file = salida)
	for i in range(q):
		print ('set arrow', id, 'from', aristas[i][0], ',',aristas[i][1],'to', aristas[i][2], ',', aristas[i][3], file = salida)
		id = id + 1
	#print ('plot "nodos.dat" using 1:2:($3*256):4 with points pt 7 lc var ps var')
	print ('plot "nodos.csv" with points palette pt 7 ps 4', file = salida)
	print("quit()", file = salida)

with open ("regiones.plot", 'w') as salida: #Archivo para poder generar mi grafica de salida.
	print ('set term pngcairo size 1000,1000', file = salida) 
	#png para formato de salida de mi grafica
	print ('set output "regiones.png"', file = salida) 
	print ('set size square', file = salida)
	#Keyoff es para que la marca de agua que sale en la parte superior der. no se vea.
	print ('set key off', file = salida)
	#El rango x y y son para el tamanio en que va a salir mi grafica.
	print ('set xrange [-.1:1.1]', file = salida)
	print ('set yrange [-.1:1.1]', file = salida)
	print('set xlabel "Longitud (m)"', file = salida)
	print('set ylabel "Longitud (m)"', file = salida)
	print("set style fill  transparent solid 0.35 border", file = salida)
	#print ('plot "nodos.dat" using 1:2:($3*256):4 with points pt 7 lc var ps var')
	print ('plot "nodos.csv" w points palette pt 7 ps 4, "regiones.csv" u 1:2:3 w circles', file = salida)
	print("quit()", file = salida)