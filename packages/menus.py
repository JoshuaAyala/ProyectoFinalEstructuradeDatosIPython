#!/usr/bin/python
#coding: utf-8

# Filename  : proyecto Final.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/ProyectoFinalEstructuradeDatosIPython
# pep8: 100%

# Importaciones
from packages.deOrdenacion import *
from packages.deBusqueda import *

import os, time, random

def mainMenu(gotData, lista):
	opcion = int(input("\n  +- Métodos de Ordenamiento\n\n  [+] Burbuja.\n  [+] Radix Sort.\n  [+] Quicksort.\n  [+] Shell Sort\n  [+] Mezcla Directa.\n  [+] Mezcla Natural.\n  [+] Intercalación.\n\n  +- De Búsqueda.\n  \n  [+] Secuencial.\n  [+] Binaria.\n  [+] Hash.\n\nElige una opción:\n\n  [01] Testear métodos de ordenamiento.\n  [02] Testear métodos de busqueda.\n\n  [00] Salir.\n\n>: "))
	if(opcion==1):
		ordTest(gotData, lista)
	elif(opcion==2):
		busquedaTest(gotData, lista)
	else:
		exit()

def faster(tiempos):
	return sorted(tiempos)

def gotomM(gotData, lista):
	q = str(input("\n¿Desea regresar al menú principal? (S/n)\n>: "))
	if(q.upper() == "S"):
		mainMenu(False, lista = [])
	else:
		exit()

def ordTest(gotData, lista):
	os.system('cls')
	print("""
		\n
		====================================================================
		      ▄▄▄  ·▄▄▄▄  ▄▄▄ . ▐ ▄  ▄▄▄· • ▌ ▄ ·. ▪  ▄▄▄ . ▐ ▄ ▄▄▄▄▄      
		▪     ▀▄ █·██▪ ██ ▀▄.▀·•█▌▐█▐█ ▀█ ·██ ▐███▪██ ▀▄.▀·•█▌▐█•██  ▪     
 		▄█▀▄ ▐▀▀▄ ▐█· ▐█▌▐▀▀▪▄▐█▐▐▌▄█▀▀█ ▐█ ▌▐▌▐█·▐█·▐▀▀▪▄▐█▐▐▌ ▐█.▪ ▄█▀▄ 
		▐█▌.▐▌▐█•█▌██. ██ ▐█▄▄▌██▐█▌▐█ ▪▐▌██ ██▌▐█▌▐█▌▐█▄▄▌██▐█▌ ▐█▌·▐█▌.▐▌
		 ▀█▄▀▪.▀  ▀▀▀▀▀▀•  ▀▀▀ ▀▀ █▪ ▀  ▀ ▀▀  █▪▀▀▀▀▀▀ ▀▀▀ ▀▀ █▪ ▀▀▀  ▀█▄▀▪
		====================================================================
		\n\n""")
	if(gotData == False):
		print("[!] Para empezar a testear la velocidad de ordenamiento de los métodos de ordenamiento es necesario crear una lista de elemntos primero.")
		op = int(input("¿Desea generar una lista de datos aleatorios o desea ingresar sus propios datos?\n\n  [01] Generar lista aleatoria.\n  [02] Introducir datos.\n\n>: "))
		if(op==1):
			lista = []
			for i in range(0, random.randint(5, 50)):
				lista.append(random.randint(0,1000))
			gotData = True
			ordTest(gotData, lista)
		elif(op==2):
			cant = int(input("¿Cuántos datos desea ingresar?\n >:"))
			lista = []
			for i in range(0, cant):
				lista.append(int(input("\nIngresa >: ")))

			gotData = True
			ordTest(gotData, lista)
		else:
			print("    [!] Opción inválida.")
			ordTest(gotData, lista)
	else:
		tiempos = {}
		print("Lista de datos: ", lista)
		# ORDENAMIENTO BURBUJA
		inicio = time.time()
		print("\n\n  [+] Burbuja.")
		print("  ", Burbuja(lista))
		fin = time.time()
		print("  Tiempo: ", fin-inicio)
		tiempos['Burbuja'] = fin-inicio
		inicio, fin = 0, 0
		# RADIX SORT
		inicio = time.time()
		print("\n\n  [+] Radix Sort.")
		print("  ", RadixSort(lista))
		fin = time.time()
		print("  Tiempo: ", fin-inicio)
		tiempos['RadixSort'] = fin-inicio
		inicio, fin = 0, 0
		# Quick SORT
		inicio = time.time()
		print("\n\n  [+] QuickSort.")
		print("  ", QuickSort(lista))
		fin = time.time()
		print("  Tiempo: ", fin-inicio)
		tiempos['QuickSort'] = fin-inicio
		inicio, fin = 0, 0
		# SHELL SORT
		inicio = time.time()
		print("\n\n  [+] Shell Sort.")
		print("  ", ShellSort(lista, len(lista)))
		fin = time.time()
		print("  Tiempo: ", fin-inicio)
		tiempos['ShellSort'] = fin-inicio
		inicio, fin = 0, 0
		# Mezcla Directa
		inicio = time.time()
		print("\n\n  [+] Mezcla Directa.")
		print("  ", mezclaDirecta(lista))
		fin = time.time()
		print("  Tiempo: ", fin-inicio)
		tiempos['Mezcla Directa'] = fin-inicio
		inicio, fin = 0, 0
		# Mezcla Natural
		inicio = time.time()
		print("\n\n  [+] Mezcla Natural.")
		print("  ", split_listaN(lista))
		fin = time.time()
		print("  Tiempo: ", fin-inicio)
		tiempos['Mezcla Natural'] = fin-inicio
		inicio, fin = 0, 0
		# Intercalación
		inicio = time.time()
		print("\n\n  [+] Intercalación")
		print("  ", Intercalacionsort(lista))
		fin = time.time()
		print("  Tiempo: ", fin-inicio)
		tiempos['Intercalación'] = fin-inicio
		inicio, fin = 0, 0
		tiemposS = sorted(tiempos)
		print("\n 	+- Tabla de posiciones: ")
		for i in range(0, len(tiemposS)):
			print("		[",i+1,"] ", tiemposS[i])
		gotomM(gotData, lista)


def busquedaTest(gotData, lista):
	os.system('cls')
	print("""
		\n
		=======================================================================================
		 ______     __  __     ______     ______     __  __     ______     _____     ______    
		/\  == \   /\ \/\ \   /\  ___\   /\  __ \   /\ \/\ \   /\  ___\   /\  __-.  /\  __ \   
		\ \  __<   \ \ \_\ \  \ \___  \  \ \ \/\_\  \ \ \_\ \  \ \  __\   \ \ \/\ \ \ \  __ \  
		 \ \_____\  \ \_____\  \/\_____\  \ \___\_\  \ \_____\  \ \_____\  \ \____-  \ \_\ \_\ 
		  \/_____/   \/_____/   \/_____/   \/___/_/   \/_____/   \/_____/   \/____/   \/_/\/_/ 
		=======================================================================================
		\n\n""")
	if(gotData == False):
		print("[!] Para empezar a testear la velocidad de ordenamiento de los métodos de ordenamiento es necesario crear una lista de elemntos primero.")
		op = int(input("¿Desea generar una lista de datos aleatorios o desea ingresar sus propios datos?\n\n  [01] Generar lista aleatoria.\n  [02] Introducir datos.\n\n>: "))
		if(op==1):
			lista = []
			for i in range(0, random.randint(5, 50)):
				lista.append(random.randint(0,1000))
			gotData = True
			busquedaTest(gotData, lista)
		elif(op==2):
			cant = int(input("¿Cuántos datos desea ingresar?\n >:"))
			lista = []
			for i in range(0, cant):
				lista.append(int(input("\nIngresa >: ")))

			gotData = True
			busquedaTest(gotData, lista)
		else:
			print("    [!] Opción inválida.")
			busquedaTest(gotData, lista)
	else:
		tiempos = {}
		print("Lista de datos: ", lista)
		n = int(input("¿Qué número deseas buscar?\n>: "))
		# BUSQUEDA SECUENCIAL
		inicio = time.time()
		print("\n\n  [+] Busqueda Secuencial.")
		print("  ", busquedaSecuencial(lista, n))
		fin = time.time()
		print("  Tiempo: ", fin-inicio)
		tiempos['Secuencial'] = fin-inicio
		inicio, fin = 0, 0
		# BUSQUEDA BINARIA
		inicio = time.time()
		print("\n\n  [+] Busqueda Binaria. (Diferente lugar a los demás debido a que primero se ordena la lista y luego se busca.)")
		print("  ", busquedaBinaria(sorted(lista), n))
		fin = time.time()
		print("  Tiempo: ", fin-inicio)
		tiempos['Binaria'] = fin-inicio
		inicio, fin = 0, 0
		# BUSQUEDA HASH
		inicio = time.time()
		print("\n\n  [+] Hash.")
		listaStr = []
		for i in range(0, len(lista)):
	  		listaStr.append(str(lista[i]))

		print("  ", buscarClave(toASCII(str(n)), listaStr, len(lista)))
		fin = time.time()
		print("  Tiempo: ", fin-inicio)
		tiempos['Hash'] = fin-inicio
		tiemposS = sorted(tiempos)
		print("\n 	+- Tabla de posiciones: ")
		for i in range(0, len(tiemposS)):
			print("		[",i+1,"] ", tiemposS[i])
		gotomM(gotData, lista)
