#El programa debería contener:
    #Al menos 4 funciones que mezclen texto.
    #Pedir al usuario que introduzca una palabra
    #Generar un número aleatorio entre 1 y 3
    #Llamar a las funciones de mezcla de texto con diferentes combinaciones para cada posible número aleatorio (1, 2 o 3).
#Después que el texto haya sido mezclado, el programa debería:
    #Asegurar que la contraseña final tiene exactamente 10 caracteres.
    #Mostrar la contraseña.

#Programa inicial
import random

def generar_numero_aleatorio():
    # Generar un número aleatorio entre 1 y 3
    numeroAleatorio = random.randint(1, 3)
    return numeroAleatorio

# Ejemplo de uso de la función
numero = generar_numero_aleatorio()
palabra = (input("Por favor, introduce tu palabra: "))
combinacion = numero

#Funciones
def cambiaTexto1(palabra):
    longitudPalabra = len(palabra)
    if longitudPalabra <=2:
        return palabra
    elif longitudPalabra>2 and longitudPalabra<=6:
        temp1 = palabra[0:2]
        temp2 = palabra[len(palabra)-2:]
        palabra = temp2 + palabra + temp1
        return palabra
    else:
        temp1 = palabra[0:3]
        temp2 = palabra[len(palabra)-3:]
        print(temp1,temp2)
        palabra = temp2 + temp1
        return palabra

def cambiaTexto2(palabra):
    if palabra.lower() == palabra:
        return palabra.upper()
    elif palabra.upper() == palabra:
        return palabra.lower()
    else:
        return "mezclado"

def cambiaTexto3(palabra):
    longitud = 5 * len(palabra)
    palabra = str(longitud-5) + palabra + str(longitud)
    return palabra

def cambiaTexto4(palabra):
    palabra = palabra+palabra
    return palabra


#Combinaciones
contraseña = palabra
if numero == 1:
    contraseña = cambiaTexto4(cambiaTexto2(cambiaTexto1(cambiaTexto3(palabra))))
if numero == 2:
    contraseña = cambiaTexto4(cambiaTexto1(cambiaTexto3(cambiaTexto2(palabra))))
if numero == 3:
    contraseña = cambiaTexto4(cambiaTexto3(cambiaTexto2(cambiaTexto1(palabra))))

#Recorte o suma de contraseña
if len(contraseña) < 10:
    contraseña = contraseña + "5"
if len(contraseña) > 10:
    contraseña = contraseña[:10]
else:
    contraseña = contraseña

#Frase final
print(f"Tu contraseña final es {contraseña}")