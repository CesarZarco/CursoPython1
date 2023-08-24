#Metodo para calcular integrales
from math import*

def f(x):
	return eval(fo)

#def d2(x):
#	return eval(do)

#def imprimir_matriz(A):
#	for i in range(len(A)):
#		for j in range(len(A)):
#			print('{:20.15f}'.format(A[i][j]),end=' ')
#		print(

fo=input('f?')
#do=input('d2?')
#x=eval(input('x?'))
n=eval(input('n?'))
#h=eval(input('h?'))
#m=[0]*n
#M=[0]*n
L=0
U=0
h=1/n
for i in range (n):
	L=f((i+1)/n)+L
	U=f(i/n)+U
	#m[i]=f(i+1/n)
	#M[i]=f((i)/n)
	
L=L*h
U=U*h
P=(L+U)/2
print('{:20.15f}{:20.15f}{:20.15f}'.format(L,U,P))
#print('La mejor aproximacion es', ma,' en la posicion', j)
	
