"""En python, debe realizar lo siguiente
-Pedir al usuario ingresar una palabra
-Este texto debe guardarlo en un texto plano
"""
word = input("Ingrese una palabra: ")
f = open("archivo.txt","x")
f.write(word)
f.close()



