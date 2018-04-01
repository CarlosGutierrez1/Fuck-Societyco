from termcolor import colored
import colorama
import win32console
import win32gui
import pythoncom,pyHook
import time
import smtplib
import os
import sys
import getpass
import urllib
import urllib.request


colorama.init()
num = 0




desc = "\033[1;33m"+'''
        +=========================================+
        |...........SomethingSpecial..............|
        +-----------------------------------------+
        |#Author: Apolus12                        |
        |#Contact: apolus12@outlook.com           |
        |#Date: 26/03/18                          |
        |#I take no responsibilities for the      |
        |  use of this tool!                      |
        +=========================================+
        |...........SomethingSpecial..............|
        +-----------------------------------------+
'''+"\033[0;0m"




def public_ip():
	lista = "0123456789."
	ip=""
	dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
	for x in str(dato):
		if x in lista:
			ip += x
	return ip

def send_email(eldue,destinatario,usuario,lacontra,message,smtp):

    try:


        fromaddr = eldue
        toaddrs = destinatario
        username = usuario
        password = lacontra
        serv = smtp
        server = smtplib.SMTP(serv)
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, message)
        server.quit()
        os.system("cls")
        print("")
        print("")
        print("                                                      \033[1;34m"+"Perfecto, enviado!"+"\033[0;0m")

    except:
        os.system("cls")
        print("")
        print("")
        e= ("                                        \033[1;31m"+"Error al enviar el correo, intente de nuevo :/"+"\033[0;0m")
        print(e)



def casos(unnumero):
    if(unnumero=="1"):
        print("Esta opcion aun no esta desarrollada\r\n"+"Coming soon")
    elif(unnumero=="2"):
        print("Abriendo Shodan.io")
        os.system('start https://www.shodan.io/')
        os.system("cls")
        print("")
        print("")
    elif(unnumero=="3"):
        """print("Abriendo pagina web -Cual es mi ip publica- ")
        os.system('start https://www.cual-es-mi-ip.net/')"""
        os.system("cls")
        print("")
        print("")
        print("                                     Su ip publica es: "+"\033[1;34m"+ public_ip()+"\033[0;0m")
        print("")
        print("")

    elif(unnumero=="4"):
        print("Servicios de mensajeria")
        print("\033[1;31m"+"[1]"+"\033[0;0m" + "\033[1;37m"+"Gmail"+"\033[0;0m")
        print("\033[1;31m"+"[2]"+"\033[0;0m" + "\033[1;37m"+"cooming"+"\033[0;0m")
        print("\033[1;31m"+"[3]"+"\033[0;0m" + "\033[1;37m"+"Smtp personalizado"+"\033[0;0m")
        sel = input("Que servicio de mensajeria desea utilizar, seleccione una opcion:  ")
        if sel=="1":
            try:
                primcorreo = input("Ingrese el asunto: ")
                eldes = input("Ingrese el correo destinatario:  ")
                elus = input("Ingrese el usuario de la cuenta: ")
                lacon = getpass.getpass("Ingrese la contraseña de la cuenta:  ")
                elmen = input("Ingrese el mensaje del correo: ")
                smtp0 = "smtp.gmail.com:587"
                send_email(primcorreo, eldes, elus, lacon, elmen,smtp0)

                print("")
                print("")
            except:
                print("Error en los datos")
        elif(sel=="cooming"):
            primercorreo = input("Ingrese el correo desde el cual se enviara: ")
            eldestino = input("Ingrese el correo destinatario:  ")
            elusuario = input("Ingrese el usuario de la cuenta:  ")
            lacontraseña = getpass.getpass('Ingrese la contraseña de la cuenta:')
            elmensaje = input("Ingrese el mensaje del correo: ")
            smtp1 = "smtp-mail.outlook.com:587"
            send_email(primercorreo, eldestino, elusuario, lacontraseña, elmensaje,smtp1)

            print("")
            print("")
        elif(sel=="3"):
            primercorreo = input("Ingrese el correo desde el cual se enviara: ")
            eldestino = input("Ingrese el correo destinatario:  ")
            elusuario = input("Ingrese el usuario de la cuenta:  ")
            lacontraseña = getpass.getpass('Ingrese la contraseña de la cuenta:')
            elmensaje = input("Ingrese el mensaje del correo: ")
            smtp2 = input("Ingrese el smtp - " +"ejemplo(smtp.mail.com:234)" )
            send_email(primercorreo, eldestino, elusuario, lacontraseña, elmensaje,smtp2)
            print("")
            print("")
    elif(unnumero=="5"):
        site = input("Ingrese el sitio, ejemplo(www.google.com):  ")
        coman = ("ping " + site)
        os.system(coman)
    elif(unnumero=="6"):
        os.system("cls")
        sys.exit()
    else:
        print("Ingrese una opcion valida")


while True:
    print(desc)
    print("\033[1;31m"+"[1]"+"\033[0;0m" + "\033[1;37m"+"Windows Keylogger(Made in python)"+"\033[0;0m")
    print("\033[1;31m"+"[2]"+"\033[0;0m"+ "\033[1;37m"+"Open Shodan"+"\033[0;0m")
    print("\033[1;31m"+"[3]"+"\033[0;0m"+ "\033[1;37m"+"Know ip public"+"\033[0;0m")
    print("\033[1;31m"+"[4]"+"\033[0;0m"+ "\033[1;37m"+"Send e-mail"+"\033[0;0m")
    print("\033[1;31m"+"[5]"+"\033[0;0m"+ "\033[1;37m"+"Use command ºpingª"+"\033[0;0m")
    print("\033[1;31m"+"[6]"+"\033[0;0m"+ "\033[1;37m"+"Exit"+"\033[0;0m")
    print("")
    num = input("type an option: ")
    casos(num)
