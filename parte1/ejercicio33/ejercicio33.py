"""Ahora la encriptación y desencriptación por cada dígito del texto debes realizarla con su correspondiente código ASCII.
 Para ello en python puedes pasar con los métodos ord(dígito) para pasar a ASCII  y el método chr(código ASCII). 
 Para que nuestra encriptación sea más complicada, a nuestro valor  de código ASCII sumémosle 1 y para desencriptar restémosla 1
"""
import os
texto = os.path.join(os.path.dirname(os.path.abspath(__file__)),"texto.txt")
def encontrar():
    if not texto:
        with open(texto, "a") as product:
            pass
def encriptar(a):
    codif = []
    for i in a:
        codif.append(ord(i)+1)
    return str(codif)
def desencriptar(b):
    borrador  = b.strip("[]").split(",")
    borrador = [int(borra)-1 for borra in borrador]
    original = []
    
    for i in borrador:
        original.append(chr(i))
    return "".join(original)

while True:
    opcion = input("Ingrese 'E' para encriptar o 'D' para desencriptar:  ").upper()
    if opcion in ["E", "D"]:
        break
    else:
        print("Esa opcion no es válida")

if opcion == "E":
    encontrar()
    nom = input("Ingrese un texto para encriptarlo en codigo ASCII: ")
    resultado = encriptar(nom)
    with open(texto,"w") as text:
        text.write(resultado)
    print("¡Encriptado exitoso!")
else:
    encontrar()
    with open(texto,"r") as text:
        contenido  = text.read()
        if not contenido:
            print("No hay texto que desencriptar.")
        else:
            print("Voy a desencriptar el texto anteriormente desencriptado.")
            desencrip = desencriptar(contenido)
            with open(texto,"w") as text:
                    text.write(desencrip)
                    print("¡El contenido ha sido desncriptado!") 
    
        
        
      






