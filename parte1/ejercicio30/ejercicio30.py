"""En python, debe realizar lo siguiente
-Pedir al usuario ingresar una palabra
-Este texto debe guardarlo en un texto plano, pero por cada dígito de la palabra ingresada debe de
 agregar una x. Esta encriptación realizalo en una función
"""

def encrip():
    a = input("Ingrese una palabra: ")
    encriptado = ""

    for i in a:
        encriptado += i + "x"

    return encriptado

val = encrip()
f = open("archivo1.txt", "w")
f.write(val)
f.close()
