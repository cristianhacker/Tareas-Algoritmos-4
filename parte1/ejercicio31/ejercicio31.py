"""En Python, teniendo un archivo encriptado (por cada letra de una
 palabra se ha agregado x), ahora debe de desencriptar el texto y sobreescribirlo
   en el  archivo. La desencriptación realizalo en una función
"""

def desencrip(a):
    result = ""
    for i in range(0,len(a),2):
        result += a[i]
    return result

with open("archivo1.txt", "r") as f:
    contenido = f.read()
desencriptado = desencrip(contenido)

with open("archivo1.txt", "w")as v:
    v.write(desencriptado)



