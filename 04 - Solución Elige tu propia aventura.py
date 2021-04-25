
#4. Construye una historia del estilo de los libros de Construye tu propia aventura de forma que la historia derive según se elija una u otra opción.


dimeNombre = input ("¿Como te llamas?: ")
print("Hola", dimeNombre, "bienvenido a elige tu propia aventura")


primeraElección = input ("Te has despertado y ves una nota en tu mesilla citándote en un aeropuerto de las afueras. ¿vas a ir?")

if primeraElección is "Y" or primeraElección is "y":
    print("Bien, has elegido volar, allá vamos!")

if primeraElección is "N" or primeraElección is "n":
    print("Hoy no es tu día de aventuras, te quedas en casa")

else:
    input("Tienes que pulsar Y o N")