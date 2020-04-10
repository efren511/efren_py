#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Escribir un programa que pida al usuario dos números
#enteros y muestre por pantalla la <n> entre <m> da
#un cociente <c> y un resto <r> donde <n> y <m> son
#los números introducidos por el usuario, y <c> y <r> son
#el cociente y el resto de la división entera respectivamente.

def main():
    val1 = int(input("Ingresa un numero: "))
    val2 = int(input("Ingresa otro numero: "))
    cociente = val1 // val2
    residuo = val1 % val2
    print("""El numero {} entre {},
da un cociente de {}
y un residuo de {}""".format(val1, val2, cociente, residuo))

if __name__ == '__main__':
    main()
