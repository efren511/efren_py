#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Escribir un programa que pregunte el nombre del
#usuario en la consola y después de que el usuario
#lo introduzca muestre por pantalla <NOMBRE> tiene <n>
#letras, donde <NOMBRE> es el nombre de usuario en mayúsculas
#y <n> es el número de letras que tienen el nombre.

def main():
    name = input("¿Como te llamas? ")
    name = name.upper()
    cont = str(len(name))
    print("El nombre {} tiene {} letras".format(name, cont))

if __name__ == '__main__':
    main()
