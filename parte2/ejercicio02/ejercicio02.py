"""Crea la clase Paciente con sus atributos (nombre, email, direccion, numero de celular, fecha de nacimiento, 
tamaño, peso, tipo de sangre) y crea un objeto instanciando la clase e imprime cada uno de sus atributos
"""
class Paciente:
    def __init__(self,nombre,email,direccion,celular,nacimiento, tamaño, peso, sangre):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.celular = celular
        self.nacimiento = nacimiento
        self.tamaño = tamaño
        self.peso = peso
        self.sangre = sangre

paciente1 = Paciente("Juan", "juan@gmail.com", "Av. Jose Granda ", 910849456, "05/08/2003",1.70, 68, "b1" )
paciente2 = Paciente("Carlos", "carlos@gmail.com", "Av. Alfredo Mendiola ", 970849456,"15/08/2000", 1.70, 68, "a1" )
paciente3 = Paciente("Maarcos", "marcos@gmail.com", "Av. Los Álamos ", 998849456,"10/05/2013", 1.70, 68, "c1" )

lista = [paciente1,paciente2, paciente3 ]
for e,i in enumerate(lista):
    print(f"\n{e +1}. El nombre del paciente es: {i.nombre}.\nEl correo electrónico del paciente es: {i.email}.\nLa dirección del paciente es: {i.direccion}.\nEl número telefónico del paciente es: {i.celular}.\nLa fecha de nacimiento del paciente es: {i.nacimiento}.\nLa estarura del paciente es: {i.tamaño} m.\nEL peso del paciente es: {i.peso}kg.\nEl tipo de sangre del paciente es: {i.sangre} ")
