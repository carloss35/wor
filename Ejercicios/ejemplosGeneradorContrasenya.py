# Ejemplo 1
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


#realiza el else
contrasenya = "ruiseñor"
contrasenya = cambiaTexto1(contrasenya)
print("La contraseña es: ",contrasenya)

#realiza el palabra <=2
contrasenya = "ok"
contrasenya = cambiaTexto1(contrasenya)
print("La contraseña es: ",contrasenya)

#realiza el<=6
contrasenya = "votado"
contrasenya = cambiaTexto1(contrasenya)
print("La contraseña es: ",contrasenya)

#Palabra en mayuscula
contrasenya = "PELOTA"
contrasenya = cambiaTexto2(contrasenya)
print("La contraseña es: ",contrasenya)

#Palabra en minuscula
contrasenya = "españa"
contrasenya = cambiaTexto2(contrasenya)
print("La contraseña es: ",contrasenya)



#cambia texto 3
contrasenya = "Oculto"
contrasenya = cambiaTexto3(contrasenya)
print("La contraseña es: ",contrasenya)



#mayusculas y minusculas mezcladas + cambia texto 3
contrasenya = "Gos"
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto3(contrasenya)
print("La contraseña es: ",contrasenya)

#mayusculas + cambia texto 3
contrasenya = "GOS"
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto3(contrasenya)
print("La contraseña es: ",contrasenya)

#minusculas + cambia texto 3
contrasenya = "gos"
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto3(contrasenya)
print("La contraseña es: ",contrasenya)


# combinación de los 3 cambiatextos en palabra minuscula de dos caracteres (recuerda que cuando se cambia el 'cambiatexto3' es la nueva variable 'contraseña')
contrasenya = "xu"
contrasenya = cambiaTexto3(contrasenya)
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto1(contrasenya)
print("La contraseña es: ",contrasenya)


#combinación de los 3 cambiatextos en palabra minuscula mayor de 2 y menor de 6 caracteres (recuerda que cuando se cambia el 'cambiatexto3' es la nueva variable 'contraseña')
contrasenya = "gnome"
contrasenya = cambiaTexto3(contrasenya)
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto1(contrasenya)
print("La contraseña es: ",contrasenya)


#combinación de los 3 cambiatextos en palabra mezclada mayor de 2 y menor de 6 caracteres (recuerda que cuando se cambia el 'cambiatexto3' es la nueva variable 'contraseña')
contrasenya = "Bruv"
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto2(contrasenya)
contrasenya = cambiaTexto3(contrasenya)
contrasenya = cambiaTexto3(contrasenya)
print("La contraseña es: ",contrasenya)


#Misma prueba de combinación de los 3 cambiatextos con solo una linea
contrasenya = "hard"
contrasenya = cambiaTexto3(cambiaTexto2(cambiaTexto1(contrasenya)))
print("La contraseña es: ",contrasenya)
