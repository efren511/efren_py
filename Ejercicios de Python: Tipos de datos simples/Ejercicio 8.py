#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Escribir un programa que lea un
#entero positivo, n, introducido
#por el usuario y después muestre
#en pantalla la suma de todos los
#enteros desde 1 hasta n. La suma
#de los n primeros enteros positivos
#puede ser calculada de la siguiente forma:

num = int(input("Ingresa un numero: "))

suma = int((num*(num+1))/2)

print("La suma desde 1 hasta {}: {}".format(num, suma))
