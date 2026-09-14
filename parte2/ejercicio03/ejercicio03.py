"""Crea la clase Usuario con sus atributos (id, nombre, email, direccion, celular) y crea un objeto instanciando 
la clase e imprime cada uno de sus atributos
"""
class Usuario:
    def __init__(self,id,nombre,email,direccion, celular):
        self.id= id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.celular = celular

objeto1 = Usuario("001739368","Jan Perez", "perezj@outlook.com","Av Jose Granda.", 978456123 )
print(f"El ID del usuario es: {objeto1.id}\nEl nombre del usuario es: {objeto1.nombre}.\nEl email es: {objeto1.email}.\nSu dirección es: {objeto1.direccion}.\nSu celular es: {objeto1.celular}. ")