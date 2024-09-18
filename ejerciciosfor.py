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
#ejercicio4 ()

def numeros_impares():
    numero=int(input("ingrese el numero: "))

    for i in range(0,numero+1,2):
        print("numero:", numero)
        print(i,end=",")
        time.sleep(1)
#numeros_impares() 

def numeros_impares():
    numero=int(input("ingrese el numero: "))
    for i in range(1,numero+1,1):
        print(i,end=",")
#numeros_impares(6) 

def numeros_impares():
    numero=int(input("ingrese el numero: "))
    for i in range(1,numero+1,1):
        time.sleep(1)
        print(i)
        if i==15:
            break;
#numeros_impares() ejercico7

def reloj_segundos():
    numero=int(input("ingrese los segundos: "))
    for i in range(1,60,1):
        print(i, "segundos")
        time.sleep(1)
        if i==numero:
            print("tiempo maximo")
            break
#reloj_segundos()

def interes():
    cantidad=int(input("ingrese la cantidad: "))
    interes_anual=int(input("ingrese el interes anual: "))
    tiempo=int(input("ingrese el tiempo de inversion: "))
    valor=cantidad
    for i in range(tiempo):
        calculo1=(valor*interes_anual)/100
        calculo2=valor+calculo1
        valor=calculo2
        time.sleep(1)
        print("el año ",i+1," ",valor)
    print ("\33[42m" + "las ganancias en ",tiempo," años son: ",valor," " + "\33[0m")
#interes()

def print_piramide(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '8' * (2 * i + 1))
print_piramide(5)
