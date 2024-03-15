
import random

def generar_ficha():
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    ficha = ''.join(random.sample(letras, 3)) + ''.join(random.sample(numeros, 3)) + ''.join(random.sample(simbolos, 3))
    return ficha

def main():
    ficha = generar_ficha()
    print("Memoriza esta ficha:", ficha)
    input("Presiona Enter cuando estés listo para ingresar la ficha: ")
    
    ingreso = input("Ingresa la ficha que memorizaste: ")
    
    if ingreso == ficha:
        print("¡Correcto! Has memorizado la ficha correctamente.")
    else:
        print("Incorrecto. La ficha correcta era:", ficha)

if "_main_":
    main()