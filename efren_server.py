#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#we import the library to work with sockets
import socket

#we import a module to work with system funtions
import sys

#we generate a funtion to set and up the server
def upserver():
    #globals variables
    host = "127.0.0.1"
    puerto = 511
    global servidor
    global ip
    global target
    #our type IP and form connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        #we configure the server in to listen in...
        servidor.bind((host, puerto))
        #we set the server in listening mode
        #we write the number of subscribers
        servidor.listen(5)
        #show a ok message
        print("Servidor corriendo pot puerto: {}".format(puerto))
        #accep any connection
        target, ip = servidor.accept()
        #show who connected to our server
        print("Cliente {} conectado",format(str(ip[0])))

if __name__ == '__main__':
    #we try to call our funtion
    try:
        #call our funtion to begin the server
        upserver()
    #if the user push ctrl + c , close all
    except KeyboardInterrupt:
        #close the server
        servidor.close()
        #get out of our code
        sys.exit()
