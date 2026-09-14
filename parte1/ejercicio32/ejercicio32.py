"""En Python, ahora realiza funciones “encriptarArchivo” y “desencriptarArchivo”. Luego debe preguntar al usuario lo siguiente
-Presione E para encriptar y D para desencriptar
-Ingrese ruta del archivo.
Cuando ingrese los datos el programa debe de encriptar o desencriptar según lo especificado y cuando haya terminado debe mostrar mensaje “Se ha encriptado correctamente” o “Se ha desencriptado correctamente” según corresponda
Debes tener en cuenta que el archivo debe existir la primera vez y tiene que tener datos que deseamos encriptar. Es decir no se va preguntar el texto que deseamos encriptar y la encriptación debe ser agregando una “x” y la desencriptación debe ser quitando la “x” agregada
"""
import os


def encriptarArchivo(a):
    result= ""
    for i in a:
        result += i + "x"
    return result
def desencriptarArchivo(b):
    resultado = ""
    for i in range(0,len(b),2):
        resultado += b[i]
    return resultado

while True:
    opcion = input("Ingrese 'E' para encriptar o 'D' para desencriptar:  ").upper()
    if opcion in ["E", "D"]:
        break
    else:
        print("Opcion invalida")
while True:
    ruta = input("Ingrese la ruta del archivo: ")
    if os.path.exists(ruta):
        with open(ruta, "r", encoding = "utf-8") as f:
            archivo = f.read()
        break
    else:
        print("La ruta especificada no es válida o el archivo no existe.")

if opcion == "E":
    archivo =encriptarArchivo(archivo)
    with open(ruta, "w")as encriptado:
            encriptado.write(archivo)
    
else: 
    archivo=desencriptarArchivo(archivo)
    with open(ruta, "w")as desencripado:
        desencripado.write(archivo)







