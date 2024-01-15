class Usuario:
    def __init__(self, nombre, apellidos, edad, asignatura, seccion, rol):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.asignatura = asignatura
        self.seccion = seccion
        self.rol = rol

class Alumno(Usuario):
    pass

class Profesor(Usuario):
    pass

class Notas:
    def __init__(self):
        self.notas_alumnos = {}

    def agregar_notas(self, alumno, nota1, nota2, nota3):
        if alumno.nombre in self.notas_alumnos:
            self.notas_alumnos[alumno.nombre]['notas'].append((nota1, nota2, nota3))
        else:
            self.notas_alumnos[alumno.nombre] = {'notas': [(nota1, nota2, nota3)], 'alumno': alumno}

    def mostrar_notas(self):
        for alumno, info in self.notas_alumnos.items():
            print("Alumno: {info['alumno'].nombre} {info['alumno'].apellidos}")
            print("Notas:")
            for nota in info['notas']:
                print(f"Nota 1: {nota[0]}, Nota 2: {nota[1]}, Nota 3: {nota[2]}")
            print()

def crear_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    apellidos = input("Ingrese los apellidos del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))
    asignatura = input("Ingrese la asignatura del usuario: ")
    seccion = input("Ingrese la sección del usuario: ")
    if input("Ingrese el rol del usuario (alumno/profesor): ").lower() == 'alumno':
        rol = 'alumno'
    else:
        rol = 'profesor'
    if nombre not in [user.nombre for user in usuarios]:
        if rol == 'alumno':
            usuarios.append(Alumno(nombre, apellidos, edad, asignatura, seccion, rol))
        else:
            usuarios.append(Profesor(nombre, apellidos, edad, asignatura, seccion, rol))
    else:
        print("El usuario ya existe.")

def ingresar_notas():
    if input("Ingrese su nombre: ").lower() not in [user.nombre for user in usuarios if user.rol == 'profesor']:
        print("No tiene permiso para ingresar notas.")
        return
    asignatura = input("Ingrese la asignatura: ")
    seccion = input("Ingrese la sección: ")
    notas = Notas()
    for alumno in [user for user in usuarios if user.asignatura == asignatura and user.seccion == seccion and user.rol == 'alumno']:
        nota1 = float(input(f"Ingrese la nota 1 de {alumno.nombre} {alumno.apellidos}: "))
        nota2 = float(input(f"Ingrese la nota 2 de {alumno.nombre} {alumno.apellidos}: "))
        nota3 = float(input(f"Ingrese la nota 3 de {alumno.nombre} {alumno.apellidos}: "))
        notas.agregar_notas(alumno, nota1, nota2, nota3)
    notas.mostrar_notas()

def actualizar_alumno():
    if input("Ingrese su nombre: ").lower() not in [user.nombre for user in usuarios if user.rol == 'profesor']:
        print("No tiene permiso para actualizar alumnos.")
        return
    nombre = input("Ingrese el nombre del alumno a actualizar: ")
    alumno = next((user for user in usuarios if user.nombre == nombre and user.rol == 'alumno'), None)
    if alumno is None:
        print("El alumno no existe.")
        return
    print("Alumno: {alumno.nombre} {alumno.apellidos}")
    print("Asignatura: {alumno.asignatura}")
    print("Sección: {alumno.seccion}")
    if input("¿Está seguro de actualizar este alumno? (si/no): ").lower() == 'si':
        alumno.nombre = input("Ingrese el nuevo nombre del alumno: ")
        alumno.apellidos = input("Ingrese los nuevos apellidos del alumno: ")
        alumno.edad = int(input("Ingrese la nueva edad del alumno: "))
        alumno.asignatura = input("Ingrese la nueva asignatura del alumno: ")
        alumno.seccion = input("Ingrese la nueva sección del alumno: ")

usuarios = []

while True:
    print("\nMenú principal:")
    print("1. Crear usuarios")
    print("2. Ingresar notas")
    print("3. Actualizar alumnos")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        crear_usuario()
    elif opcion == 2:
        ingresar_notas()
    elif opcion == 3:
        actualizar_alumno()
    
