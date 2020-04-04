#!/usr/bin/env python3
## -*- coding: utf-8 -*-

#company logo
logo = """
here                                               ▄▄▄▄▄▄`
    you                                         ▄██▀▀╙╙▀▀██▄
        can                                   ▄███        ╙██
            generate                       ,▄██└└▀██,      ▐█▌
                    custom               ,██▀─     ███▄    ▐█▌
                        word           ▄██▀     ,▄█▀└▀██▄ ▄██
                    lists            ▄██▀     ╓██▀     ▀███└
                  to               ▄██▀     ▄██▀     ,▄█▀┴
             brute              ,▄█▀─     ▄██▀     ,██▀
        force                 ,▄█▀'     ▄██┘     ▄██▀
 attacks                    ▄██▀     ,▄█▀└     ▄██▀
by                        ▄██▀     ,██▀      ▄██░
                        ▄██▀     ▄██▀     ,▄█▀└
Efren                 ▄██▄     ▄██▀     ,██▀
                     ▐█▌▀▀██▄▄██└     ▄██▀
Garcia               ██     ▐██     ▄██▀
                    ║█▌       ██⌂ ▄██┴
UwU                ╓███▄      L███▀┘
                   ██┐▐███████▀▀▀`
                  ▐███▀▀▀╙-                           »
"""

#we create a funtion to ask questions
def ask(data_list, value):
    print("\npreciona enter para pasar a la siguiente pregunta")
    if input("Usar {}?: ".format(value)):
        while True:
            information = input("\nIngresa {}: ".format(value))
            if information != "":
                data_list.append(information)
            else:
                break

#we generate a main funtion
def main():
    #we show our logo
    print(logo)
    #we start our list of data
    data = []
    #parameter list
    asks = ["nombre", "apellido", "edad", "dia de cumpleaños",
    "mes de cumpleaños", "año de nacimiento", "nombre de pareja",
    "apellido de pareja", "edad de pareja", "dia de cumpleaños de pareja",
    "mes de cumpleaños de pareja", "año de nacimiento de pareja",
    "dia de aniversario", "mes de aniversario", "año de aniversario"]
    #we begin with the asks to generate the word list
    for topic in asks:
        ask(data, topic)
    #show our word list
    print(data)
#we create an access point
if __name__ == '__main__':
    main()
