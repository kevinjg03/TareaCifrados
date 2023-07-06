"""
ULACIT
Especialización en Ciberseguridad
Criptografía
TAREA PROGRAMADA
ELABORADO POR: KEVIN JIMENEZ
Ultima modificacion: 07/06/2023 a las 7am
"""

import numpy as np #numpy es una de las librerias más famosas de Python. Tiene muchas funcionalidad numericas.
from random import random #Librería para generar
from random import randint
from random import seed
from random import sample
import math

#################################Variables##############################################################################################

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abecedarioSalida = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']
alfabetoSalNumerico = ["21","22","23","31","32","33","41","42","43","51","52","53","61","62","63","71","72","73","74","81","82","83","91","92","93","94","*"] #Alfabeto Salida del cifrado codigo Telefonico
alfabetoNum = [i for i in range(1,28)] #Alfabeto Numerico
alfabetoBin = ["00000","00001","00010","00011","00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","01111","10000","10001","10010","10011","10100","10101","10110","10111","11000","11001","*"]
separador = "*"*120
separador2 = "-"*120
opcionCifDescif = "Seleccione la operación que desea realizar:"+"\n"+"1. Cifrar"+"\n"+"2. Descifrar"+"\n"+"3. Para Salir de la opción"
numeros_primos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
combined = np.append(abecedario, numeros_primos)
np.random.shuffle(combined)
key = []

#####################################################################################################################################

##############################Funciones Secundarias##################################################################################


def crearSemilla(mensaje):
     # ----------------creación de semilla pseuda-aleatoria---------#
    seed = []
    for i in range(500):
        seed.append(randint(0, 36))

    subset = sample(seed, len(mensaje))
    return subset



def crearKey(mensaje):
    subset = crearSemilla(mensaje)
    for i in range(len(subset)):
        key.append(combined[subset[i]])

    return listToString(key)

def listToString(s):
    """Funcion que permite pasar de una variable tipo lista a string"""
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def cifrarOTP(key,mensaje):
  """Funcion que cifra el mensaje mediante una funcion XOR con la llave. Retorna un ciphertext"""
  cipher=""
  for i in range(len(mensaje)):
    t = mensaje[i]
    k = key[i%len(key)]
    x = ord(k) ^ ord(t)
    cipher += chr(x) #Vamos añadiendo los valores producto del XOR al cipher.
  return cipher.encode("utf-8").hex() #Retorna el ciphertex en HEXADECIMAL

def descifrarOTP(key, ciphertext):
  """Funcion de descripcion, realiza una funcion XOR entre el ciphertext y la llave y retorna el mensaje original"""
  a_string = bytes.fromhex(ciphertext)
  a_string = a_string.decode("utf-8")
  mensaje = ""
  for i in range(len(a_string)):
    t = a_string[i]
    k = key[i%len(key)]
    x = ord(k) ^ ord(t)
    mensaje += chr(x)
  return mensaje


"""
Funcion para el menu, que llama al cifrado OTP
Entrada:
Salidas:
"""
def opcionOTP():  #Funcion para el menu
    print("\nCifrado OTP")      
    print(opcionCifDescif)  #Llama a la variable que contiene las opciones de cifrado y descifrado
    try:
        global key
        opcion = int(input("Digite la opción: "))   #Pide introducir la opcion deseada 
        if opcion == 1:     #Llama a la funcion de cifrado
            oracion = input("Escriba la mensaje que desea cifrar: \n")  #Pide la oracion a cifrar
            key = crearKey(oracion)
            print("\n" + oracion + "\n"+ "cifrada con OTP es:"+"\n"+cifrarOTP(key, oracion)+"\n") #Imprime el resultado final
        elif opcion == 2:   #Llama a la funcion de Descifrado
            if key == []:
                print("Primero debe cifrar un texto para generar una llave y poder descifrar otro")
                return opcionOTP()
            oracion = input("Escriba la mensaje que desea descifrar: \n")   #Pide la oracion a descifrar
            print("\n" + oracion + "\n"+"Cifrada con OTP, al descifrarla es:"+"\n"+descifrarOTP(key, oracion)+"\n") #Imprimer el resultado
            key = []
            print("\n Borrando llave de único uso... \n")
        elif opcion == 3:   #Vuelve al menu
            pass
        else:
            print("La opción digitada es inválida") #Error en caso de que se seleccione una opcion que diferente a las mostradas
            return opcionOTP()    #Llama a la funcion, para volver a realizar la operacion
    except:
        print("La opción introducida no es un número o introdujo datos incorrectos, vuelva a intentarlo\n") #Error en caso de introducir numero en la oracion o de introducir una letra como opcion a seleccionar
        return opcionOTP()    #Llama a la funcion, para volver a realizar la operacion


"""
Funcion Es par
Entrada: Numero
Salida: Verdadero o Falso
Restricciones: parametro debe ser un numero
"""
def esPar(numero):
    if numero%2 == 0:
        return True
    else:
        return False

"""
Funcion que comprueba el largo de un numero
Entrada: Numero = x
Salida: Longitud de un numero
Restricciones: x igual a un numero
"""

def largoNum(x):
    if x <= 999999999999997:
        return int(math.log10(x)) + 1
    else:
        return len(str(x))
    
"""
Funcion que comprueba que un caracter sea una letra o pertenezca al alfabeto
Entradas: Alfabeto, caracter a comprobar
Salidas: Verdadero o Falso
"""

def comprobarCaracter(caracter):
    if isinstance(caracter, str):   #Comprueba que el caracter sea un string
        return True if (caracter.lower() in abecedario) else False    #Verifica si el caracter pertenece al alfabeto
    else:
        return "El carácter debe ser un string" #Error en caso de que no sea un string

"""
Funcion que ubica un caracter dentro de un alfabeto
Entradas: Alfabeto, caracter a buscar
Salidas: La posicion que ocupa el caracter dentro del  alfabeto
Restricciones: Caracter debe ser un string
"""

def ubicarEnAlfabetoAux(alfabeto, caracter):
    return alfabeto.index(caracter)

def ubicarEnAlfabeto(alfabeto, caracter):
    if isinstance(caracter, str):   #Comprueba que el caracter sea un string
        if caracter == "" or alfabeto == "":    #Comprueba que no sean vacios
            return "Carácter o alfabeto inválido"
        else:
            if comprobarCaracter:
                caracter = caracter.lower()     #Convierte el caracter a mayuscula
                return ubicarEnAlfabetoAux(alfabeto, caracter)  #Llama a la funcion en caso de cumplir todos los requisitos
            else:
                return "El carácter no pertenece al alfabeto"
    else:
        return "El carácter introducido no es de tipo string"   #Error en caso de que el caracter no sea una letra


#####################################################################################################################################

###############################Funciones Principales###################################################################################

"""
Funcion: Cifrado Cesar
Entradas: Alfabeto de entrada, Alfabeto de salida, oracion a codificar
Salidas: La oracion cifrada
Restricciones: Oracion de tipo string
**************************************Nota*************************************
*El cifrado y el descifrado se llevan a cabo con la misma funcion,            *
*pero en el caso del descifrado, se utiliza el alfabeto de entrada del cifrado*
*como alfabeto de salida del descifrado, y el alfabeto de salida del cifrado, *
*se convierte en el alfabeto de entrada del descifrado.                       *                                     
*******************************************************************************
"""

def cifrarCesarAux(alfabetoEntrada, alfabetoSalida, oracion):   #Funcion principal que realiza el cifrado cesar
    if oracion == "":   #Condicion para que termine
        return ""       #Valor que retorna al terminar
    else:
        indiceCaracter = ubicarEnAlfabeto(alfabetoEntrada, oracion[0]) #Buscar el primer caracter de la oracion en el alfabeto
        return alfabetoSalida[indiceCaracter] + cifrarCesarAux(alfabetoEntrada, alfabetoSalida, oracion[1:]) #devuelve el caracter cifrado concatenado con la funcion que ahora recorta la cabeza de la oracion
    
def cifrarCesar(alfabetoEntrada, alfabetoSalida, oracion):  #Funcion que realiza comprobaciones
    if isinstance(oracion, str):    #Comprueba que la oracion sea un string
        if oracion == "":   #Comprueba que la oracion sea diferente de vacio
            return "La oración debe contener caracteres"    #Error en caso de que la oracion este vacia
        else:
            oracion = oracion.lower()   #Convierte la oracion a mayusculas
            return cifrarCesarAux(alfabetoEntrada, alfabetoSalida, oracion) #Llama a la funcion que cifra la oracion
    else:
        return "La oración debe ser un string" #Error en caso de que la oracion no sea un string



"""
Funcion Que invierte un mensaje
Entradas: Texto
Salidas: Texto invertido
**************************************Nota*************************************
*El cifrado y el descifrado se llevan a cabo con la misma funcion.            *                                    
*******************************************************************************
"""

def mensajeInversoAux(texto): #Funcion que realiza la operacion
    if texto == "": #Condicion para que termine
        return ""   #Valor de retorno
    else:
        return mensajeInversoAux(texto[1:]) + texto[0] #Retorna la funcion recortando el string y poniendo el primer caracter del texto al final del mismo

def mensajeInverso(texto):  #Funcion que realiza las comprobaciones
    if isinstance(texto, str):  #Comprueba que el parametro sea un str
        if texto == "": #Si es vacio
            return ""   #Devuelve vacio
        else:
            texto = texto.lower()   #Convierte el texto a mayusculas
            return mensajeInversoAux(texto) #Llama a la funcion
    else:
        return "La oración no es un string" #Error en caso de que el parametro no sea un string



"""
Funcion que codifica un texto en cifrado telefonico
Entradas: Alfabeto Entrada, alfabeto salida, texto
Salidas: Texto cifrafo
"""



def cifradoTelefonicoAux(alfabetoEnt, alfabetoSal, oracion):
    if oracion == "":   #Condicion de terminar
        return ""   #Retorna vacio para finalizar
    else:
        if oracion[0] == " ":   #Comprueba si el primer caracter es un espacio
            return alfabetoSal[27] + " " + cifradoTelefonicoAux(alfabetoEnt, alfabetoSal, oracion[1:]) #Concatena el equivalente en el alfabeto de salida + un espacio y la funcion
        else:
            indiceCaracter = ubicarEnAlfabeto(alfabetoEnt, oracion[0])  #Busca el caracter en el alfabeto y le asigna la posicion a una variable
            return str(alfabetoSal[indiceCaracter]) + " " + cifradoTelefonicoAux(alfabetoEnt, alfabetoSal, oracion[1:]) #Concatena el numero convertido en string y la funcion


def cifradoTelefonico(alfabetoEnt, alfabetoSal, oracion):
    if isinstance(oracion, str):    #Comprueba que la oracion sea un string
        if oracion == "":   #Comprueba que la oracion sea diferente de vacio
            return "La oración debe contener caracteres"    #Error en caso de que la oracion este vacia
        else:
            oracion = oracion.lower()   #Convierte la oracion a mayusculas
            return cifradoTelefonicoAux(alfabetoEnt, alfabetoSal, oracion) #Llama a la funcion que cifra la oracion
    else:
        return "La oración debe ser un string" #Error en caso de que la oracion no sea un string





"""
Funcion que descifra un texto en cifrado telefonico
Entradas: alfabeto de entrada, alfabeto de salida, texto cifrado
Salidas: texto descifrado
"""



def descifrarTelefonicoAux(alfabetoEnt, alfabetoSal, oracion):
    if oracion == "":       #Condicion para que termine
        return ""   #Finaliza la funcion
    else:
        if oracion[:2] == "* ": #Compara el caracter
            indiceCaracter = ubicarEnAlfabeto(alfabetoEnt, oracion[0])  #Busca la letra en el alfabeto
            return " " + descifrarTelefonicoAux(alfabetoEnt, alfabetoSal, oracion[2:])  #Devuelve el string mas la funcion 
        else:   
            numero = oracion[:2]    #Asigna un string con un numero, recortando la oracion cifrada
            indiceCaracter = ubicarEnAlfabeto(alfabetoEnt, numero)  #Busca la variable dentro del alfabeto
            return alfabetoSal[indiceCaracter] + descifrarTelefonicoAux(alfabetoEnt, alfabetoSal, oracion[3:])  #Retorna un string y lo concatena con la funcion

def descifrarTelefonico(alfabetoEnt, alfabetoSal, oracion):
    if isinstance(oracion, str):    #Comprueba que la oracion sea un string
        if oracion == "":   #Comprueba que la oracion sea diferente de vacio
            return "La oración debe contener caracteres"    #Error en caso de que la oracion este vacia
        else:
            if oracion[-1] == " ":
                return descifrarTelefonicoAux(alfabetoEnt, alfabetoSal, oracion) #Llama a la funcion que cifra la oracion
            else:
                oracion += " "
                return descifrarTelefonicoAux(alfabetoEnt, alfabetoSal, oracion) #Llama a la funcion que cifra la oracion                
    else:
        return "La oración debe ser un string" #Error en caso de que la oracion no sea un string





"""
Funcion Cifrado Vigenere
Entradas: Alfabeto entrada, oracion, clave
Salidas: Texto Cifrado
Restricciones: Clave de 2 digitos
"""

def cifVigenereAux(alfabetoEnt, oracion, claveNum, contador):
    if oracion == "":   #Condicion para terminar
        return ""   #Finaliza con un string vacio
    else:
        if contador > 1:    #Verifica si el contador es mayor a 1 
            contador = 0   #Dado ese caso, el contador se vuelve 0
        if oracion[0] == " ":   #Si el primer caracter de la oracion es un espacio
            return " " + cifVigenereAux(alfabetoEnt, oracion[1:], claveNum, contador + 1)   #Concatena un espacio con la funcion.
        else:   
            indice = ubicarEnAlfabeto(alfabetoEnt, oracion[0])  #Busca el caracter en el alfabeto y le asigna la posicion a una variable
            if esPar(contador): #Si el contador es par
                indice += (claveNum//10)    #Suma el primer(Izquierda) numero de la clave
            else:   
                indice += (claveNum%10) #Sino suma el segundo(derecha) digito de la clave
            if indice > 26: #Si al sumar el indice con la clave es mayor a 26(largo del abecedario)
                indice -= 26    #Le resta 26 para obtener un indice valido
            return alfabetoEnt[indice] + cifVigenereAux(alfabetoEnt, oracion[1:], claveNum, contador + 1)   #Concatena el nuevo caracter con la funcion

def cifVigenere(alfabetoEnt, oracion, clave):   #Comprueba los parametros 
    if isinstance(oracion, str) and isinstance(clave, int): #Si la oracion es string y la clave un numero, pasa
        if oracion == "": #Si oracion es vacia devuelve vacio
            return ""   
        else:
            oracion = oracion.lower()   #Convierte la oracion a mayusculas para seguir el estandar
            return cifVigenereAux(alfabetoEnt, oracion, clave, 0)   #Llama a la funcion auxiliar
    else:
        return "La oración no es un texto o la clave no es un número"   #Error en caso de que la oracion no sea string o la clave no sea numero





"""
Funcion Descifrado Vigenere
Entradas: Alfabeto entrada, oracion, clave
Salidas: Texto Cifrado
Restricciones: Clave de 2 digitos
"""

def descifrarVigAux(alfabetoEnt, oracion, claveNum, contador):
    if oracion == "":   #Condicion para terminar
        return ""   #Finaliza con un string vacio
    else:
        if contador > 1:    #Verifica si el contador es mayor a 1 
            contador = 0   #Dado ese caso, el contador se vuelve 0
        if oracion[0] == " ":   #Si el primer caracter de la oracion es un espacio
            return " " + descifrarVigAux(alfabetoEnt, oracion[1:], claveNum, contador + 1)   #Concatena un espacio con la funcion.
        else:   
            indice = ubicarEnAlfabeto(alfabetoEnt, oracion[0])  #Busca el caracter en el alfabeto y le asigna la posicion a una variable
            if esPar(contador): #Si el contador es par
                indice -= (claveNum//10)    #Resta el primer(Izquierda) numero de la clave
            else:   
                indice -= (claveNum%10) #Sino Resta el segundo(derecha) digito de la clave
            if indice < 0: #Si al sumar el indice con la clave es mayor a 26(largo del abecedario)
                indice += 26    #Le suma 26 para obtener un indice valido
            return alfabetoEnt[indice] + descifrarVigAux(alfabetoEnt, oracion[1:], claveNum, contador + 1)   #Concatena el nuevo caracter con la funcion

def descifrarVig(alfabetoEnt, oracion, clave):   #Comprueba los parametros 
    if isinstance(oracion, str) and isinstance(clave, int): #Si la oracion es string y la clave un numero, pasa
        if oracion == "": #Si oracion es vacia devuelve vacio
            return ""   
        else:
            oracion = oracion.lower()   #Convierte la oracion a mayusculas para seguir el estandar
            return descifrarVigAux(alfabetoEnt, oracion, clave, 0)   #Llama a la funcion auxiliar
    else:
        return "La oración no es un texto o la clave no es un número"   #Error en caso de que la oracion no sea string o la clave no sea numero
 


    
"""
Funcion Cifrado de Llave
Entradas: predefinidas : Alfabeto entrada, alfabeto salida, cont. Dadas por Usuario: texto y codigo
Salidas: Texto Cifrado
Restricciones: Texto y codigo deben tener elemento pertenecientes al abecedario
"""

def cifradoLlaveAux(alfabetoEnt, alfabetoSal, texto, codigo, cont):
    if texto == '': #Condicion Para que termine
        return ''   #Devuelve un string vacio para terminar la funcion
    else:
        if cont > len(codigo)-1:  #Si el contador es mayor que el largo del  codigo, se reinicia, para iterar sobre el codigo
            cont = 0 
        if texto[0] == " ":
            cont = 0
            return " " + cifradoLlaveAux(alfabetoEnt, alfabetoSal, texto[1:], codigo, cont)
        else:
            indiceTxt = ubicarEnAlfabeto(alfabetoEnt, texto[0]) #Busca el caracter en el abecedario
            indiceCode = ubicarEnAlfabeto(alfabetoEnt, codigo[cont])    #Buscar el caracter del codigo en el abecedario
            numTxt = alfabetoSal[indiceTxt] #Obtiene el equivalente en numero
            numCode = alfabetoSal[indiceCode]   #Obtiene el equivalente en numero
            nuevoIndice = numTxt + numCode #Suma los equivalentes para obtener el nuevo indice del caracter
            if nuevoIndice > 26: #Si es mayor que 26, resta 26 para obtener un caracter valido
                nuevoIndice -= 26
            return alfabetoEnt[nuevoIndice-1] + cifradoLlaveAux(alfabetoEnt, alfabetoSal, texto[1:], codigo, cont+1)

"""
Funcion Cifrado de llave
Entradas: Alfabeto entrada, alfabeto de salida, texto y codigos dados por el usuario
Salidas: Funcion que cifra el texto
Restricciones: Codigo y texto de tipo string y con char pertenecientes al abecedario
"""

def cifradoLlave(alfabetoEnt, alfabetoSal, texto, codigo):
    if isinstance(texto, str) and isinstance(codigo, str):
        if texto == "":
            return "String Vacío"
        else:
            texto = texto.lower()
            codigo = codigo.lower()
            return cifradoLlaveAux(alfabetoEnt, alfabetoSal, texto, codigo, 0)
    else:
        return "El texto o el código no pertenecen al alfabeto o no son cadenas de texto"
            



"""
Funcion descifrado de llave
Entradas: Alfabeto Entrada, Alfabeto salida, texto y codigo, contador(para reiterar sobre el codigo)
Salidas: Texto Codificado
Resticciones: Texto y codigo tipo string, con caracteres dentro del abecedario
"""

def descifrarLlaveAux(alfabetoEnt, alfabetoSal, texto, codigo, cont):
    if texto == '': #Condicion Para que termine
        return '' #Devuelve un string vacio para terminar la funcion
    else:
        if cont > len(codigo)-1: #Si el contador es mayor que el largo del  codigo, se reinicia, para iterar sobre el codigo
            cont = 0
        if texto[0] == " ": #Si es un espacio, reicinia el contador para comenzar desde la cabeza del codigo, y concatena un espacio
            cont = 0
            return " " + descifrarLlaveAux(alfabetoEnt, alfabetoSal, texto[1:], codigo, cont)
        else:
            indiceTxt = ubicarEnAlfabeto(alfabetoEnt, texto[0]) #Busca el caracter en el abecedario
            indiceCode = ubicarEnAlfabeto(alfabetoEnt, codigo[cont])    #Buscar el caracter del codigo en el abecedario
            numTxt = alfabetoSal[indiceTxt] #Obtiene el equivalente en numero
            numCode = alfabetoSal[indiceCode]   #Obtiene el equivalente en numero
            nuevoIndice = numTxt - numCode #Resta los equivalentes para obtener el nuevo indice del caracter
            if nuevoIndice < 0: #Si es menor que 0, suma 26 para obtener un caracter valido
                nuevoIndice += 26
            return alfabetoEnt[nuevoIndice-1] + descifrarLlaveAux(alfabetoEnt, alfabetoSal, texto[1:], codigo, cont+1)

def descifrarLlave(alfabetoEnt, alfabetoSal, texto, codigo):
    if isinstance(texto, str) and isinstance(codigo, str):
        if texto == "":
            return "String Vacío"
        else:
            texto = texto.lower()
            codigo = codigo.lower()
            return descifrarLlaveAux(alfabetoEnt, alfabetoSal, texto, codigo, 0)
    else:
        return "El texto o el código no pertenecen al alfabeto o no son cadenas de texto"


"""
Funcion Cifrado XOR y Llave
Entradas: Texto, codigo y un contador
Salidas: Texto cifrado en caracteres ASCII
Restricciones: Es sensible a mayusculas y minusculas, por lo que la forma de escrbir el texto, cuenta
"""


def cifradoXORLlaveAux(texto, codigo, cont):
    if texto == '': #Condicion Para que termine
        return ''   #Devuelve un string vacio para terminar la funcion
    else:
        if cont > len(codigo)-1:  #Si el contador es mayor que el largo del  codigo, se reinicia, para iterar sobre el codigo
            cont = 0 
        if texto[0] == " ": #Si es un espacio en blanco
            cont = 0 #Reinicia el contador
            return chr(31) + cifradoXORLlaveAux(texto[1:], codigo, cont)    #Agrega el caracter ascii equivalente al espacio en blanco
        else:
            numTxt = ord(texto[0]) #Obtiene el equivalente en numero
            numCode = ord(codigo[cont])   #Obtiene el equivalente en numero
            nuevoIndice = numTxt ^ numCode #Suma los equivalentes para obtener el nuevo indice del caracter
            return chr(nuevoIndice) + cifradoXORLlaveAux(texto[1:], codigo, cont+1)

def cifradoXORLlave(texto, codigo):
    if isinstance(texto, str) and isinstance(codigo, str):
        if texto == "":
            return "String Vacío"
        else:
            return cifradoXORLlaveAux(texto, codigo, 0)
    else:
        return "El texto o el código no pertenecen al alfabeto o no son cadenas de texto"

"""
Funcion de Descifrado XOR y Llave
Entradas: Texto, codigo, cont predeterminado
Salidas: Texto descifrado
Restricciones: Respetar el formato de salida del texto cifrado para introducir el texto a descifrar, por ejemplo '\x1f'
"""

def descifrarXORAux(texto, codigo, cont):
    if texto == '': #Condicion Para que termine
        return ''   #Devuelve un string vacio para terminar la funcion
    else:
        if cont > len(codigo)-1:  #Si el contador es mayor que el largo del  codigo, se reinicia, para iterar sobre el codigo
            cont = 0 
        if texto[0] == "\x1f": #Si la cabeza de texto es el caracter de espacio en blanco
            cont = 0 #Reinicia el contador
            return chr(32) + descifrarXORAux(texto[1:], codigo, cont)   #Agrega un espacio en blanco a la cadena de texto
        else:
            numTxt = ord(texto[0]) #Obtiene el equivalente en numero
            numCode = ord(codigo[cont])   #Obtiene el equivalente en numero
            nuevoIndice = numTxt ^ numCode #Suma los equivalentes para obtener el nuevo indice del caracter
            return chr(nuevoIndice) + descifrarXORAux(texto[1:], codigo, cont+1)    

def descifrarXOR(texto, codigo):
    if isinstance(texto, str) and isinstance(codigo, str):
        if texto == "":
            return "String Vacío"
        else:
            return descifrarXORAux(texto, codigo, 0)
    else:
        return "El texto o el código no pertenecen al alfabeto o no son cadenas de texto"


"""
Funcion Cifrado Binario
Entradas: Alfabeto Entrada, Alfabeto salida, oracion
Salidas: Texto cifrado
Restricciones:
"""

def cifradoBinAux(alfabetoEnt, alfabetoSal, oracion):
    if oracion == "":   #Condicion de terminar
        return ""   #Retorna vacio para finalizar
    else:
        if oracion[0] == " ":   #Comprueba si el primer caracter es un espacio
            return "*" + " " + cifradoBinAux(alfabetoEnt, alfabetoSal, oracion[1:]) #Concatena el equivalente en el alfabeto de salida + un espacio y la funcion
        else:
            indiceCaracter = ubicarEnAlfabeto(alfabetoEnt, oracion[0])  #Busca el caracter en el alfabeto y le asigna la posicion a una variable
            return str(alfabetoSal[indiceCaracter]) + " " + cifradoBinAux(alfabetoEnt, alfabetoSal, oracion[1:]) #Concatena el numero convertido en string y la funcion


def cifradoBin(alfabetoEnt, alfabetoSal, oracion):
    if isinstance(oracion, str):    #Comprueba que la oracion sea un string
        if oracion == "":   #Comprueba que la oracion sea diferente de vacio
            return "La oración debe contener caracteres"    #Error en caso de que la oracion este vacia
        else:
            oracion = oracion.lower()   #Convierte la oracion a mayusculas
            return cifradoBinAux(alfabetoEnt, alfabetoSal, oracion) #Llama a la funcion que cifra la oracion
    else:
        return "La oración debe ser un string" #Error en caso de que la oracion no sea un string

"""
Funcion Descifrado Binario
Entradas: Alfabeto Entrada, Alfabeto salida, oracion
Salidas: Texto descifrado
Restricciones: Respetar el formato de entrada de datos, igual que la salida del cifrado binario, numero espacio numero.
"""

def descifrarBinAux(alfabetoEnt, alfabetoSal, oracion):
    if oracion == "":       #Condicion para que termine
        return ""   #Finaliza la funcion
    else:
        if oracion[:2] == "* ": #Compara el caracter
            indiceCaracter = ubicarEnAlfabeto(alfabetoEnt, oracion[0])  #Busca la letra en el alfabeto
            return " " + descifrarBinAux(alfabetoEnt, alfabetoSal, oracion[2:])  #Devuelve el string mas la funcion 
        else:   
            numero = oracion[:5]    #Asigna un string con un numero, recortando la oracion cifrada
            indiceCaracter = ubicarEnAlfabeto(alfabetoEnt, numero)  #Busca la variable dentro del alfabeto
            return alfabetoSal[indiceCaracter] + descifrarBinAux(alfabetoEnt, alfabetoSal, oracion[6:])  #Retorna un string y lo concatena con la funcion

def descifrarBin(alfabetoEnt, alfabetoSal, oracion):
    if isinstance(oracion, str):    #Comprueba que la oracion sea un string
        if oracion == "":   #Comprueba que la oracion sea diferente de vacio
            return "La oración debe contener caracteres"    #Error en caso de que la oracion este vacia
        else:
            if oracion[-1] == " ":
                return descifrarBinAux(alfabetoEnt, alfabetoSal, oracion) #Llama a la funcion que cifra la oracion
            else:
                oracion += " "
                return descifrarBinAux(alfabetoEnt, alfabetoSal, oracion) #Llama a la funcion que cifra la oracion                
    else:
        return "La oración debe ser un string" #Error en caso de que la oracion no sea un string

"""
"""
def palabraInversaAux(texto):
    if texto == []:
        return ""
    else:
        return mensajeInverso(texto[0]) + " " + palabraInversaAux(texto[1:])

def palabraInversa(texto):  #Funcion que realiza las comprobaciones
    if isinstance(texto, str):  #Comprueba que el parametro sea un str
        if texto == "": #Si es vacio
            return ""   #Devuelve vacio
        else:
            texto = texto.lower()   #Convierte el texto a mayusculas
            texto = texto.split()
            return palabraInversaAux(texto) #Llama a la funcion
    else:
        return "La oración no es un string" #Error en caso de que el parametro no sea un string
            
   
######################################################################################################################################

#########################Comprobaciones e Introduccion de Datos#######################################################################

"""
Funcion para el menu, que llama al cifrado cesar
Entrada:
Salidas:
"""
def opcionCesar():  #Funcion para el menu
    print("Cifrado César")      
    print(opcionCifDescif)  #Llama a la variable que contiene las opciones de cifrado y descifrado
    try:
        opcion = int(input("Digite la opción: "))   #Pide introducir la opcion deseada 
        if opcion == 1:     #Llama a la funcion de cifrado
            oracion = input("Escriba la oración que desea cifrar: \n")  #Pide la oracion a cifrar
            print(oracion + "\n"+ "En cifrado César es:"+"\n"+cifrarCesar(abecedario, abecedarioSalida, oracion)+"\n") #Imprime el resultado final
        elif opcion == 2:   #Llama a la funcion de Descifrado
            oracion = input("Escriba la oración que desea descifrar: \n")   #Pide la oracion a descifrar
            print(oracion + "\n"+"Cifrada César, al descifrarla es:"+"\n"+cifrarCesar(abecedarioSalida, abecedario, oracion)+"\n") #Imprimer el resultado
        elif opcion == 3:   #Vuelve al menu
            pass
        else:
            print("La opción digitada es inválida") #Error en caso de que se seleccione una opcion que diferente a las mostradas
            return opcionCesar()    #Llama a la funcion, para volver a realizar la operacion
    except:
        print("La opción introducida no es un número o introdujo datos incorrectos, vuelva a intentarlo\n") #Error en caso de introducir numero en la oracion o de introducir una letra como opcion a seleccionar
        return opcionCesar()    #Llama a la funcion, para volver a realizar la operacion




"""
Funcion para el menu, que llama al mensaje Inverso
Entrada:
Salidas:
"""

def opcionMensInv():
    print("Mensaje Inverso")
    print(opcionCifDescif) #Llama a la variable que contiene las opciones de cifrado y descifrado
    try:
        opcion = int(input("Digite la opción: "))   #Pide introducir la opcion deseada 
        if opcion == 1:     #Llama a la funcion de cifrado
            oracion = input("Escriba la oración que desea cifrar: \n")  #Pide la oracion a cifrar
            print("\n"+ "Invertida es:"+"\n"+ mensajeInverso(oracion)+ "\n") #Imprime el resultado final
        elif opcion == 2:   #Llama a la funcion de Descifrado
            oracion = input("Escriba la oración que desea descifrar: \n")   #Pide la oracion a descifrar
            print("\n"+"Invertida, al descifrarla es:"+"\n"+mensajeInverso(oracion)+"\n") #Imprimer el resultado
        elif opcion == 3:   #Vuelve al menu
            pass
        else:
            print("La opción digitada es inválida") #Error en caso de que se seleccione una opcion que diferente a las mostradas
            return opcionMensInv()    #Llama a la funcion, para volver a realizar la operacion
    except:
        print("La opción introducida no es un número o introdujo datos incorrectos, vuelva a intentarlo\n") #Error en caso de introducir numero en la oracion o de introducir una letra como opcion a seleccionar
        return opcionMensInv()     #Llama a la funcion, para volver a realizar la operacion

"""
Funcion para el menu, que llama al cifrado Telefonico
Entrada:
Salidas:
"""

def opcionTelefonico():
    print("Cifrado Telefónico")
    print(opcionCifDescif) #Llama a la variable que contiene las opciones de cifrado y descifrado
    try:
        opcion = int(input("Digite la opción: "))   #Pide introducir la opcion deseada 
        if opcion == 1:     #Llama a la funcion de cifrado
            oracion = input("Escriba la oración que desea cifrar: \n")  #Pide la oracion a cifrar
            print(oracion + "\n"+ "Cifrada es:"+"\n"+cifradoTelefonico(abecedario, alfabetoSalNumerico, oracion)[:-1]+"\n") #Imprime el resultado final
        elif opcion == 2:   #Llama a la funcion de Descifrado
            print("""Nota:
                     *******************************************************
                     *Debe Escribir el texto cifrado de la siguiente forma:*
                     *numero espacio numero, por ejemplo: 81 82 21,        *
                     *asi como el espacio en blanco normal,                *
                     *se sustituye con *, ejemplo: 21 * 23, indicando que  *
                     *en el texto original habia un espacio en blanco.     *
                     *******************************************************\n""")
            oracion = input("Escriba la oración que desea descifrar: \n")   #Pide la oracion a descifrar
            print("\n"+"al descifrarla es:"+"\n"+descifrarTelefonico(alfabetoSalNumerico,abecedario, oracion)+"\n") #Imprimer el resultado
        elif opcion == 3:   #Vuelve al menu
            pass
        else:
            print("La opción digitada es inválida") #Error en caso de que se seleccione una opcion que diferente a las mostradas
            return opcionTelefonico()    #Llama a la funcion, para volver a realizar la operacion
    except:
        print("La opción introducida no es un número o introdujo datos incorrectos, vuelva a intentarlo\n") #Error en caso de introducir numero en la oracion o de introducir una letra como opcion a seleccionar
        return opcionTelefonico()     #Llama a la funcion, para volver a realizar la operacion

"""
Funcion para el menu, que llama al cifrado Vigenere
Entrada:
Salidas:
"""
def opcionVigenere():
    print("Cifrado Vigenére")
    print(opcionCifDescif) #Llama a la variable que contiene las opciones de cifrado y descifrado
    print("La clave a ingresar debe ser de dos dígitos")
    try:
        opcion = int(input("Digite la opción: "))   #Pide introducir la opcion deseada
        if opcion == 1:     #Llama a la funcion de cifrado
            oracion = input("Escriba la oración que desea cifrar: \n")  #Pide la oracion a cifrar
            clave = int(input("Ingrese la clave numérica (debe ser de dos digitos) para cifrar: \n"))
            if largoNum(clave) == 2:
                print(oracion + "\n"+ "cifrada es:"+"\n"+cifVigenere(abecedario, oracion, clave)+"\n") #Imprime el resultado final
            else:
                print("La clave debe ser de dos dígitos \n")
                return opcionVigenere()
        elif opcion == 2:   #Llama a la funcion de Descifrado
            oracion = input("Escriba la oración que desea descifrar: \n")   #Pide la oracion a descifrar
            clave = int(input("Ingrese la clave numérica (debe ser de dos digitos) para cifrar: \n"))
            if largoNum(clave) == 2:
                print(oracion + "\n"+"al descifrarla es:"+"\n"+descifrarVig(abecedario, oracion, clave)+"\n") #Imprimer el resultado
            else:
                print("La clave debe ser de dos dígitos \n")
                return opcionVigenere()
        elif opcion == 3:   #Vuelve al menu
            pass
        else:
            print("La opción digitada es inválida") #Error en caso de que se seleccione una opcion que diferente a las mostradas
            return opcionVigenere()    #Llama a la funcion, para volver a realizar la operacion
    except:
        print("La opción introducida no es un número o introdujo datos incorrectos, vuelva a intentarlo\n") #Error en caso de introducir numero en la oracion o de introducir una letra como opcion a seleccionar
        return opcionVigenere()     #Llama a la funcion, para volver a realizar la operacion

"""
Funcion para el menu, que llama al cifrado de llave
Entrada:
Salidas:
"""

def opcionLlave():
    print("Cifrado Llave")
    print(opcionCifDescif) #Llama a la variable que contiene las opciones de cifrado y descifrado
    try:
        opcion = int(input("Digite la opción: "))   #Pide introducir la opcion deseada
        if opcion == 1:     #Llama a la funcion de cifrado
            oracion = input("Escriba la oración que desea cifrar: \n")  #Pide la oracion a cifrar
            clave = input("Ingrese el código de texto para cifrar: \n")
            print(oracion + "\n"+ "con el código: "+clave+"\n"+"al cifrarla es:"+"\n"+cifradoLlave(abecedario, alfabetoNum, oracion, clave)+"\n") #Imprime el resultado final
        elif opcion == 2:   #Llama a la funcion de Descifrado
            oracion = input("Escriba la oración que desea descifrar: \n")   #Pide la oracion a descifrar
            clave = input("Ingrese la clave de texto para cifrar: \n")
            print(oracion + "\n"+ "con el código: "+clave+"\n"+"al descifrarla es:"+"\n"+descifrarLlave(abecedario, alfabetoNum, oracion, clave)+"\n") #Imprimer el resultado
        elif opcion == 3:   #Vuelve al menu
            pass
        else:
            print("La opción digitada es inválida") #Error en caso de que se seleccione una opcion que diferente a las mostradas
            return opcionLlave()    #Llama a la funcion, para volver a realizar la operacion
    except:
        print("La opción introducida no es un número o introdujo datos incorrectos, vuelva a intentarlo\n") #Error en caso de introducir numero en la oracion o de introducir una letra como opcion a seleccionar
        return opcionLlave()     #Llama a la funcion, para volver a realizar la operacion

"""
Funcion para el menu, que llama al cifrado de llave
Entrada:
Salidas:
"""

def opcionXOR():
    print("Cifrado XOR y Llave")
    print(opcionCifDescif) #Llama a la variable que contiene las opciones de cifrado y descifrado
    try:
        opcion = int(input("Digite la opción: "))   #Pide introducir la opcion deseada
        if opcion == 1:     #Llama a la funcion de cifrado
            oracion = input("Escriba la oración que desea cifrar: \n")  #Pide la oracion a cifrar
            clave = input("Ingrese el código para cifrar: \n")
            print(oracion + "\n"+ "con el código: "+clave+"\n"+"al cifrarla es:"+"\n"+cifradoXORLlave(oracion, clave)+"\n") #Imprime el resultado final
        elif opcion == 2:   #Llama a la funcion de Descifrado
            print("\n"+"***Nota***")
            print("Respetar el formato de salida del texto cifrado para introducir el texto a descifrar, por ejemplo '\\x1f'")
            print("O su equivalente en carácter ASCII \n")
            oracion = input("Escriba la oración que desea descifrar: \n")   #Pide la oracion a descifrar
            clave = input("Ingrese la clave numérica para cifrar: \n")
            print(oracion + "\n"+ "con el código: "+clave+"\n"+"al descifrarla es:"+"\n"+descifrarXOR(oracion, clave)+"\n") #Imprimer el resultado
        elif opcion == 3:   #Vuelve al menu
            pass
        else:
            print("La opción digitada es inválida") #Error en caso de que se seleccione una opcion que diferente a las mostradas
            return opcionLlave()    #Llama a la funcion, para volver a realizar la operacion
    except:
        print("La opción introducida no es un número o introdujo datos incorrectos, vuelva a intentarlo\n") #Error en caso de introducir numero en la oracion o de introducir una letra como opcion a seleccionar
        return opcionLlave()     #Llama a la funcion, para volver a realizar la operacion


"""
Funcion para el menu, que llama al cifrado Binario
Entrada:
Salidas:
"""

def opcionBin():
    print("Cifrado Binario")
    print(opcionCifDescif) #Llama a la variable que contiene las opciones de cifrado y descifrado
    #try:
    opcion = int(input("Digite la opción: "))   #Pide introducir la opcion deseada 
    if opcion == 1:     #Llama a la funcion de cifrado
        oracion = input("Escriba la oración que desea cifrar: \n")  #Pide la oracion a cifrar
        print("\n"+ "Cifrada es:"+"\n"+cifradoBin(abecedario, alfabetoBin, oracion)[:-1]+"\n") #Imprime el resultado final
    elif opcion == 2:   #Llama a la funcion de Descifrado
        print("""Nota:
                 ***********************************************************
                 *Debe Escribir el texto cifrado de la siguiente forma:    *
                 *"número" espacio "número", por ejemplo: 10000 00010 10100*
                 *así como el espacio en blanco normal,                    *
                 *se sustituye con *, ejemplo: 10101 * 01000, indicando    *                            
                 *que en el texto original había un espacio en blanco.     *
                 ***********************************************************\n""")
        oracion = input("Escriba la oración que desea descifrar: \n")   #Pide la oracion a descifrar
        print("\n"+"al descifrarla es:"+"\n"+descifrarBin(alfabetoBin,abecedario, oracion)+"\n") #Imprimer el resultado
    elif opcion == 3:   #Vuelve al menu
        pass
    else:
        print("La opción digitada es inválida") #Error en caso de que se seleccione una opcion que diferente a las mostradas
        return opcionBin()    #Llama a la funcion, para volver a realizar la operacion
    #except:
    #    print("La opción introducida no es un número o introdujo datos incorrectos, vuelva a intentarlo\n") #Error en caso de introducir numero en la oracion o de introducir una letra como opcion a seleccionar
    #    return opcionBin()     #Llama a la funcion, para volver a realizar la operacion

"""
Funcion para el menu, que llama al mensaje Inverso
Entrada:
Salidas:
"""

def opcionPalabraInv():
    print("Palabra Inversa")
    print(opcionCifDescif) #Llama a la variable que contiene las opciones de cifrado y descifrado
    try:
        opcion = int(input("Digite la opción: "))   #Pide introducir la opcion deseada 
        if opcion == 1:     #Llama a la funcion de cifrado
            oracion = input("Escriba la oración que desea cifrar: \n")  #Pide la oracion a cifrar
            print("\n"+ "Invertiendo palabras es:"+"\n"+ palabraInversa(oracion)+ "\n") #Imprime el resultado final
        elif opcion == 2:   #Llama a la funcion de Descifrado
            oracion = input("Escriba la oración que desea descifrar: \n")   #Pide la oracion a descifrar
            print("\n"+"al descifrarla es:"+"\n"+palabraInversa(oracion)+"\n") #Imprimer el resultado
        elif opcion == 3:   #Vuelve al menu
            pass
        else:
            print("La opción digitada es inválida") #Error en caso de que se seleccione una opcion que diferente a las mostradas
            return opcionPalabraInv()    #Llama a la funcion, para volver a realizar la operacion
    except:
        print("La opción introducida no es un número o introdujo datos incorrectos, vuelva a intentarlo\n") #Error en caso de introducir numero en la oracion o de introducir una letra como opcion a seleccionar
        return opcionPalabraInv()     #Llama a la funcion, para volver a realizar la operacion

######################################################################################################################################

#####################################Menu#############################################################################################


print("Bienvenido al Sistema de Cifrado")
def menu():
    print(separador+ "\n"+ separador2)
    print("Seleccione la opción que desea:"+"\n"+"0. Cifrado OTP"+"\n"+"1. Cifrado César"+"\n"+"2. Cifrado por Llave"+"\n"+"3. Sustitución Vigenére")
    print("4. Sustitución por XOR y Llave"+"\n"+"5. Palabra Inversa"+"\n"+"6. Mensaje Inverso"+"\n"+"7. Cifrado Telefónico"+"\n"+"8. Cifrado Binario")
    print("9. Salir")
    print(separador2+ "\n"+ separador)
    #try:
    opcion = int(input("Digite la opción: "))
    print("\n")
    match opcion:
        case 0:
            print(separador)
            opcionOTP()
            print(separador+"\n")
        case 1:
            print(separador)
            opcionCesar()           #Llama a la funcion de cifrado cesar
            print(separador+"\n")
        case 2:
            print(separador)
            opcionLlave()           #Llama a la funcion de Cifrado Llave
            print(separador+"\n")
        case 3:
            print(separador)
            opcionVigenere()        #Llama a la funcion de cifrado vigenere
            print(separador+"\n")
        case 4:
            print(separador)
            opcionXOR()             #Llama a la funcion de cifrado XOR y llave
            print(separador+"\n")
        case 5:
            print(separador)
            opcionPalabraInv()
            print(separador+"\n")
        case 6:
            print(separador)
            opcionMensInv()         #Llama a la funcion de mensaje inverso
            print(separador+"\n")
        case 7:
            print(separador)
            opcionTelefonico()      #Llama a la funcion de Cifrado Telefonico
            print(separador+"\n")
        case 8:
            print(separador)
            opcionBin()
            print(separador+"\n")
        case 9:
            print("Gracias por usar nuestro programa :)")
            # Fin
            return #Sale del programa
        case _:
            print("Opción inválida, seleccione una de las opciones mostradas")  #Error en caso de que se introduzca un numero mayor a 9 o menor a 0
    #except:
    #    print("La opción introducida no es un número"+"\n") #Error en caso de introducir algo diferente a un numero
    print("\n")
    menu()  #Llama el menu
    

######################################################################################################################################


menu()  #Llama al menu para que inicie el programa
