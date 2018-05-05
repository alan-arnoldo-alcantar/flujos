from rep5 import Grafo, Eliminar
g=Grafo()
e=Eliminar()
n=5
l=1
p=0.02
nodos_ori=set()
coor_ori=list()
pesos_ori=dict()
pesos_p_ori=dict()
vecinos_ori=dict()
g.red(n,l)
nodos_ori, coor_ori, pesos_ori, pesos_p_ori, vecinos_ori = g.aristasp(p)
e.eli_ver(nodos_ori, coor_ori, pesos_ori, pesos_p_ori, vecinos_ori,n)
#print('graficak'+str(n)+'ev'+str(i)+'.plot')