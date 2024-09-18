import time
def ejercicio1 ():
    palabra= str(input("por favor ingresar palabra: "))
    for i  in range(10):
        print("valor de la variable i: ",i+1)
        time.sleep(1)
        print(palabra)
    return
#ejercicio1 ()

import time
def ejercicio2 ():
    palabra= str(input("por favor ingresar palabra: "))
    cantidad= int (input("ingrese la cantidad de veces: "))
    for i  in range(cantidad):
        print("valor de la variable i: ",i+1)
        time.sleep(1)
        print(palabra)
    return
#ejercicio2 ()

import time
def ejercicio3 ():
    edad= str(input("por ingresar edad: "))
    cantidad= int (input("cantidad de años que tiene: "))
    for i  in range(cantidad):
        print("valor de la edad i:",i+1)
        time.sleep(1)
        print(i+1)
    return
#ejercicio3 ()

import time
def ejercicio4 ():
    cantidad1=int(input("ingrese su año de nacimento: "))
    cantidad2= int (input("cantidad de años que tiene: "))
    cantidad3=cantidad2-cantidad1
    print("la edad es: ",cantidad3)
    for i  in range(cantidad3+1):
        print("los años son:",cantidad1+i)
        time.sleep(1)
        print(i)
    return
ejercicio4 ()

