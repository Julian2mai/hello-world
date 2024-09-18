def suma_dos_valores(a, b):
    global resultado
    resultado = a + b
    
    return resultado 

# suma_dos_valores(5, 7) 
# print("primera suma")
# print(resultado)
# suma_dos_valores(1, 2)
# print("segunda suma")
# print(resultado)

# def calculadora_dos_valores(numero1,numero2,operador):
#     global resultado
#     if operador ==1: #si el operador es 1 es suma
#         resultado =numero1 + numero2
#         return resultado
#     elif operador == 2:
#         resultado =numero1 - numero2
#         return resultado
#     elif operador ==3:
#         resultado =numero1 * numero2
#         return resultado
#     elif operador==4:
#         resultado =numero1 / numero2
#         return resultado
#     else: #si el operador es otro numero
#         print("el numero ingresado no es valido")
#         return resultado    

# calculadora_dos_valores(1,2,1)
# print(resultado)

# def pitagoras(a, b):
#     global c 
#     c=(a**2+b**2)**0.5
#     return c

# #pitagoras(3,4)
# #print("pitagoras",c)

#import random




import random

def jugar():
    opciones = ['piedra', 'papel', 'tijeras']     # Opciones
    jugador = input("Elige piedra, papel o tijeras: ").lower()    # Jugador elige
    if jugador not in opciones:   # Validar entrada del jugador
        print("Opción no válida. Intenta de nuevo.")
        return
    computadora = random.choice(opciones) # Computadora elige
    print(f"La computadora eligió: {computadora}")
    if jugador == computadora: # Determinar ganador
        print("Es un empate!")
    elif (jugador == 'piedra' and computadora == 'tijeras') or \
        (jugador == 'papel' and computadora == 'piedra') or \
        (jugador == 'tijeras' and computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("Perdiste.")
jugar()
