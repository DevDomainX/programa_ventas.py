#!/usr/bin/env python3
#create by: Hans saldias
#programa de ventas ingresar datos ventas, ingresar fecha, poder ir viendo lista de productos ingresados y todo queda registrado enun archivo.txt
from colorama import init, Fore, Back, Style

def ventas():
    print(Fore.YELLOW+'''
Yb    dP 888888 88b 88 888888    db    .dP"Y8
 Yb  dP  88__   88Yb88   88     dPYb   `Ybo."
  YbdP   88""   88 Y88   88    dP__Yb  o.`Y8b
   YP    888888 88  Y8   88   dP""""Yb 8bodP'
''')
    print(Fore.GREEN+"\t**** programa de ventas ****\t\n")
    print("=-="*20, '\n')
    
    while True :
        
        archivo = open("ventas.txt", "a")   
        print("Regresar a menu digite: atras")
        venta=input("Ingrese venta: ")
        precio=input("Ingrese precio: ")
        archivo.write(f"producto: {venta}, precio ${precio}\n")
        archivo.close()
        print("=-="*20, '\n')
        volver = input("Digite => atras <= si quiere volver a menu principal:\n para seguir ingresando productos solo precione Enter:")
        
        if volver == "atras":
            menu()
        else:
            print("Ingrese una opcion valida")
    

def ingresarFecha():
       print(Fore.RED+'''
888888 888888  dP""b8 88  88    db
88__   88__   dP   `" 88  88   dPYb
88""   88""   Yb      888888  dP__Yb
88     888888  YboodP 88  88 dP""""Yb
''')
       while True:               
               print(Fore.GREEN+" ** Ingresar fecha actual **")
               print("=-="*20)
               archivo = open("ventas.txt", "a")
               fecha = input("Ingrese fecha: ")
               archivo.write(f"La fecha es: {fecha}\n")
               print("=-="*20, '\n')
               print("volver a menu principal digite 0:\npara ingresar fecha nuevamente digite 1: ")
               salir = input("Digite opcion: :")
               print("=-="*20, '\n')
               if salir == "0":
                   menu()
               elif salir == "1":
                   ingresarFecha()
               else:
                   print("opcion no valida")
    
def verVentas():
    print(Fore.BLUE+'''
### ###  ### ###  ### ##
 ##  ##   ##  ##   ##  ##
 ##  ##   ##       ##  ##
 ##  ##   ## ##    ## ##
 ### ##   ##       ## ##
  ###     ##  ##   ##  ##
   ##    ### ###  #### ##
''')
    print(Fore.GREEN+"** Lista de ventas **\n")   
    print("=-="*20, '\n')   
    
    archivo = open ('ventas.txt','r')
    mensaje = archivo.read()
    print(mensaje, "\n ")
    archivo.close()
    print("** vista total de ventas **")
    print("=-="*20, '\n')
    print("para volver a menu principal digite: 0")
    print("=-="*20)
    salir = input("Digite opcion:")
    print("=-="*20, '\n')
    if salir == "0":
                menu()
                print("=-="*20)
    else:
             print("opcion no valida")
    
def menu():
    print(Fore.GREEN+"**** ventas 3 y 4, A ****\n")
    print('''
88888   Yb  dP     dP88    .o.      db
  .dP    YbdP     dP 88    `"'     dPYb
o `Yb     8P     d888888   .o.    dP__Yb
YbodP    dP          88    `"'   dP""""Yb
''')
    print('''
     Programa para curso 3 y 4 A, año 2023\n\nby: Hans   saldias... \n\nProfesor: Alvaro Vergara\n''')
    print("=-="*20, '\n')
    
    print("[ 1 ] - Ingresar fecha \n")
    print("=-="*20, '\n')
    print("[ 2 ] - Ingresar ventas \n")
    print("=-="*20, '\n')
    print("[ 3 ] - ver ventas totales \n")
    print("=-="*20, '\n')
    print("para salir escribe: [salir]\n")
    print("=-="*20, '\n')
    op = input("Ingrese opcion: ")
    while op != "salir":
        if op == "1":
            ingresarFecha()
        elif op == "2":
            ventas()
        elif op == "3":
            verVentas()
        elif op == "salir":
            break
          
menu() 
      
    