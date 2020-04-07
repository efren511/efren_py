#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#we import the module to work with colors
from termcolor import colored

#company logo
logo = colored("""
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
""", "yellow")

#we create a funtion to ask questions
def ask(data_list, value):
    #we show a message if you want to skip the cuestion
    print(colored("\npreciona enter para pasar a la siguiente pregunta", "red"))
    #if the user didn't skip the cuestion
    if input(colored("Usar {}?: ".format(value), "green")):
        while True:
            #we ask information
            information = input(colored("\nIngresa {}: ".format(value), "blue"))
            #if the information isn't empty
            if information != "":
                #we add the information
                data_list.append(information)
            #if no
            else:
                #get out of the bluce
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
        #we ask the information
        ask(data, topic)
    #show our word list
    print(data)
#we create an access point
if __name__ == '__main__':
    #we call our main funtion
    main()
