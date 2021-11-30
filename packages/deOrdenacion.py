#!/usr/bin/python
#coding: utf-8

# Filename  : proyecto Final.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/ProyectoFinalEstructuradeDatosIPython
# pep8: 100%

# Importaciones
from functools import reduce

def ndigitos(lista):
    digitoMax = 0
    for num in lista:
        digitoMax = max(digitoMax, num)
    return len(str(digitoMax))
 

def flatten(lista):
    return reduce(lambda x, y: x + y, lista)
 
def RadixSort(lista):
    digitos = ndigitos(lista)
    for digito in range(0, digitos):
        t = [[] for i in range(10)]
        for elemento in lista:
            num = (elemento // (10 ** digito)) % 10
            t[num].append(elemento)
        lista = flatten(t)
    return lista

def ShellSort(lista, l):

    k = l // 2
    while(k > 0):
        for i in range(k, l):
            x = lista[i]
            y = i
            while(y >= k and lista[y - k] > x):
                lista[y] = lista[y - k]
                y -= k

            lista[y] = x

        k = k // 2
    return lista

def split_listaN(lista):
    if len(lista)<=1:
        return lista
    mitad = len(lista)//2
    izquierda, derecha = split_listaN(lista[:mitad]), split_listaN(lista[mitad:])
    return mezclaNatural(izquierda, derecha, lista)

def split_listaD(lista):
    if len(lista)<=1:
        return lista
    mitad = len(lista)//2
    izquierda, derecha = split_listaD(lista[:mitad]), split_listaD(lista[mitad:])
    return lista[:mitad], lista[mitad:]

def Burbuja(lista):
    num = len(lista)
    i = 0
    while(i < num):
        x = i
        while (x < num):
            if (lista[i] > lista[x]):
                aux = lista[i]
                lista[i] = lista[x]
                lista[x] = aux
            x = x + 1
        i = i + 1

    return lista

def QuickSort(lista):
    if(len(lista) > 1):
        pivot = lista[0]
        listaIz = []
        listaDe = []
        listaPi = []
        for i in range(0, len(lista)):
            if(lista[i] < pivot):
                listaIz.append(lista[i])
            elif(lista[i] == pivot):
                listaPi.append(lista[i])
            else:
                listaDe.append(lista[i])
        return QuickSort(listaIz) + listaPi + QuickSort(listaDe)
    else:
        return lista

def mezclaDirecta(lista):
    if len(lista)>1:
        #Dividimos la lista dada en 2 listas
        listaA, listaB = split_listaD(lista)
        mezclaDirecta(listaA)
        mezclaDirecta(listaB)
        i, x, iListOrd = 0, 0, 0
        while(i<len(listaA) and x<len(listaB)):
            if(listaA[i] < listaB[x]):
                lista[iListOrd] = listaA[i]
                i+=1
            else:
                lista[iListOrd] = listaB[x]
                x+=1
            iListOrd+=1

        while(i<len(listaA)):
            lista[iListOrd]=listaA[i]
            i+=1
            iListOrd+=1

        while(x<len(listaB)):
            lista[iListOrd] = listaB[x]
            x+=1
            iListOrd+=1
    return lista

def mezclaNatural(izq, der, lista):
    izq_a, der_a = 0, 0
    while izq_a < len(izq) and der_a < len(der):
        if izq[izq_a] <= der[der_a]:
            lista[izq_a + der_a]=izq[izq_a]
            izq_a += 1
        else:
            lista[izq_a + der_a] = der[der_a]
            der_a += 1
            
    for izq_a in range(izq_a, len(izq)):
        lista[izq_a + der_a] = izq[izq_a]
        
    for der_a in range(der_a, len(der)):
        lista[izq_a + der_a] = der[der_a]

    return lista

def Intercalacionsort(lista):
    for i in range(0, len(lista)):
        aux = lista[i]
        izq = 0
        der = i - 1

        while(izq <= der):
            mitad = (izq+der)//2
            if(aux <= lista[mitad]):
                der = mitad - 1
            else:
                izq = mitad + 1

        j = i - 1

        while(j >= izq):
            lista[j+1]=lista[j]
            j-=1

        lista[izq] = aux

    return lista