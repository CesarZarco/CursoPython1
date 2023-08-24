#Metodo para calcular la segunda derivada
from math import*

def f(x):
	return eval(fo)

def d2(x):
	return eval(do)

#def imprimir_matriz(A):
#	for i in range(len(A)):
#		for j in range(len(A)):
#			print('{:20.15f}'.format(A[i][j]),end=' ')
#		print(

fo=input('f?')
do=input('d2?')
x=eval(input('x?'))
#N=eval(input('N?'))
#h=eval(input('h?'))
me=1
for i in range (32):
	h=1/4**i
	fsa=(f(x+h)-2*f(x)+f(x-h))/h**2
	error=abs(fsa-d2(x))
	if me>error:
		ma=fsa
		j=i
		me=error
	print('{:1.1f}{:20.15f}{:20.15f}{:20.15f}'.format(i,h,fsa,error))
print('La mejor aproximacion es', ma,' en la posicion', j)
	
