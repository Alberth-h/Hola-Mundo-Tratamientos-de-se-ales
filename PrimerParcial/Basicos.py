#Esto es un comentario
#print("comentario")
print("Hola mundo!")
print("Adios mundo!")

#Operadores aritmeticos
5+1
print(4+6)
print(5-2)
print(3*4)
print(20/4)
#precedencia de operadores
print(5+8*(3+2))

#Tipos de datos
print(type(2))
print(type(8.62))
print(type("texto"))
print(type('texto'))
print(type("5"))

#Variables
mensaje = "Esto es un mensaje"
print(mensaje)
mensaje = "mensaje modificado"
print(mensaje)
print(type(mensaje))
mensaje = 100
print(mensaje)
print(type(mensaje))

tres_animales = "el perico, el chivo y el coyote"
print(tres_animales)

textoUno = "mi texto"
textoDos = "mi segundo texto"

print(textoUno + textoDos)

edad = "20"
print("La edad del usuario es: " + str(edad))
print("el tipo de dato de edad es: " + str(type(edad)))

import math

grados = 45.0
radianes = grados * math.pi / 180.0
seno = math.sin(radianes)
print("seno de 45° :" + str(seno))

def saludar(nombre):
    print("hola" + nombre)
    print("como estas?")
    print("te saludo de lejos por eso dle virus UnU")

def despedir():
    print("ahi los vidrios")
    print("Ya que pase todo esto nos wachamos")

def concatenar(parte1, parte2):
    return parte1 + parte2

print("Esto no es parte de la funcion")
saludar("Pana Miguel")
despedir()

frase = concatenar("hola ", "adios")
print(frase)