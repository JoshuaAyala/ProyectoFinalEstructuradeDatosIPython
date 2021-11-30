#!/usr/bin/python
#coding: utf-8

# Filename  : proyecto Final.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/ProyectoFinalEstructuradeDatosIPython
# pep8: 100%

def busquedaSecuencial(lista, numero):
	x=0
	for i in range(0, len(lista)):
		x+=1
		if(lista[i]==numero):
			return "El número se encuentra en la lista en la posición: ", x
		elif(x==len(lista)):
			return "El número no se encuentra en la lista."

def busquedaBinaria(lista, dato):
	i = 1
	j = len(lista) - 1
	while(i <= j):
		m = (i + j) // 2
		if(dato == lista[m]):
			return "El elemento se ha encontrado en la posición: ", m+1
		else:
			if(dato < lista[m]):
				j = m - 1
			else:
				i = m + 1

def toASCII(dato):
  clave = 0
  x=0
  for i in dato:
    x+=1
    clave+=(ord(i)*x)
    
  return clave
 
def buscarClave(clave, lista, largo):
  encontrado = False
  for i in range(0, largo):
    if(toASCII(lista[i])==clave):
      encontrado = True
      return "El elemento se ha encontrado en el indice ", i+1
    elif(i==largo and encontrado != True):
      return "El elemento no se encontró"