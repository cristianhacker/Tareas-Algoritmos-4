"""Crea la clase Doctor con sus atributos (id, nombre y especialidad) y crea un objeto instanciando la
 clase e imprime su id, nombre y especialidad"""
class Doctor:
    def __init__(self,id,nombre,especialidad):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
nombre = input("Ingrese su nombre: ")
id = input("Ingrese su ID: ")
especialidad = input("Ingreses su especialida: ")
objeto1 = Doctor(id, nombre, especialidad)
print(f"Su ID es: {objeto1.id}\nSu nombre es: {objeto1.nombre}\nSu especiaidad es: {objeto1.especialidad}")