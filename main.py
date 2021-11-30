#!/usr/bin/python
#coding: utf-8

# Filename  : proyecto Final.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/ProyectoFinalEstructuradeDatosIPython
# pep8: 100%

# --- Importaciones ---
from packages.deOrdenacion import *
from packages.deBusqueda import *
from packages.menus import *

import os, time, random

def banner():
	os.system('cls')
	print("""
		\n
		============================================================================
		 ___    _               _                      _       ___       _          
		| __|__| |_ _ _ _  _ __| |_ _  _ _ _ __ _   __| |___  |   \ __ _| |_ ___ ___
		| _|(_-<  _| '_| || / _|  _| || | '_/ _` | / _` / -_) | |) / _` |  _/ _ (_-<
		|___/__/\__|_|  \_,_\__|\__|\_,_|_| \__,_| \__,_\___| |___/\__,_|\__\___/__/
		============================================================================
	\n\n""")

gotData = False
lista = []

def main():

	banner()
	mainMenu(gotData, lista)

main()