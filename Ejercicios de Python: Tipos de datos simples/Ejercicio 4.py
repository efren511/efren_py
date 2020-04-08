#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Escribir un programa que pregunte el nombre
#del usuario en la consola y después de que
#el usuario lo introduzca muestre por pantalla
#la cadena ¡Hola <nombre>!, donde <nombre> es
#el nombre que el usuario haya introducido.

def main():
    number = int(input("¿Cuantas veces quires mostrar tu nombre? "))
    name = input("¿Como te llamas? ")
    for value in range(number):
        print('\n'+name)

if __name__ == '__main__':
    main()
