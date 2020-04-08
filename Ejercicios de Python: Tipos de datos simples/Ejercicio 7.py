#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Escribir un programa que pregunte al usuario por el número
#de horas trabajadas y el coste por hora. Después debe
#mostrar por pantalla la paga que le corresponde.

def main():
    hours = float(input("¿Cuantas horas trabajaste? "))
    cost = float(input("¿Cuanto ganas por hora? "))
    salary = hours * cost
    print("Tu paga será de: {} pesos".format(salary))

if __name__ == '__main__':
    main()
