"""Crea un programa que tenga un menú que tenga las opciones
1. Ingresar Doctor
2. Ingresar Paciente
3.Mostrar Doctores
4.Mostrar Pacientes
0. Salir
Si eliges la opción 1, debes ingresar cantidad de doctores a ingresar y debes ingresar cada uno de ellos 
Si eliges la opción2, debes ingresar cantidad de pacientes a ingresar y debes ingresar cada uno de ellos
Si eliges la opción 3, debes mostrar todos los doctores ingresados
Si eliges la opción 4, debes mostrar todos los pacientes ingresados
Si eliges la opción 0, debe salir
"""
class Doctor:
    def __init__(self,doc):
        self.doc = doc
class Paciente(Doctor):
    pass
doctors = []
pacientes = []  
def  ingresarDoc():
    
    while True:
        try:
            cant = int(input("Ingrese la cantidad de doctores a registrar: "))
            if cant > 0:
                break
            else:
                print("Ingrese una cantidad mayor a 0")
        except ValueError:
            print("Esa cantidad no es válida.")
    for i in range(cant):
        doc = input("Ingrese el nombre coompleto del doctor: ")
        objet = Doctor(doc)
        doctors.append(objet)

 
def ingresarPac():
    
    while True:
            try:
                cant = int(input("Ingrese la cantidad de pacientes a registrar: "))
                if cant > 0:
                    break
                else:
                    print("Ingrese una cantidad mayor a 0")
            except ValueError:
                print("Esa cantidad no es válida.")
    for i in range(cant):
            pac = input("Ingrese el nombre completo del paciente: ")
            objet = Paciente(pac)
            pacientes.append(objet)
        
    
def mostrarDoc():
    
    if not doctors:
        print("Todavía no se han registrado doctores")
    for e,i in enumerate(doctors):
        print(f"{e+1}. Se ha registrado el Doctor:{i.doc} ")
    menu()
def mostrarPaciente():
    
    if not pacientes:
        print("Todavia no hay pacientes registrados.")
    for e,i in enumerate(pacientes):
        print(f"{e+1}. Se ha registrado el paciente: {i.doc}")
    menu()
def salir():
    print("\n Gracias por usar el programa")
    exit()
def menu():
    while True:
        print("="*35)
        print("  Bienvenido al menú principal")
        print("="*35)
        print("\n Escoja un numero:")
        print("'1' - Ingresar doctores.")
        print("'2' - Ingresar pacientes")
        print("'3' - Mostrar doctores.")
        print("'4' - Mostar pacientes")
        print("'5' - Salir.")
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            ingresarDoc()
        elif opcion == '2':
            ingresarPac()
        elif opcion == '3':
            mostrarDoc()
        elif opcion == '4':
            mostrarPaciente()
        elif opcion == '5':
            salir()
        else:
            print("Esa opción no es correcta.")
menu()
    
    