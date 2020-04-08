#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Escribir un programa que pregunte el nombre del
#usuario en la consola y después de que el usuario
#lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
#donde <nombre> es el nombre que el usuario haya introducido.

def main():
    name = input("¿Como te llamas? ")
    print("¡Hola! {}".format(name))

if __name__ == '__main__':
    main()
