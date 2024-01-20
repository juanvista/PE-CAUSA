

    class Usuario:
    def __init__(self, nombre, apellidos, edad, asignatura, rol, seccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.asignatura = asignatura
        self.rol = rol
        self.seccion = seccion

Usuario = [
    {'nombre': 'JORGE EDUARDO', 'apellido': 'ALIAGA QUINTANA', 'edad': 31, 'rut': '17705131-4', 'asignatura': 'ANALISIS', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 61},
    {'nombre': 'RAMIRO IGNACIO', 'apellido': 'ALVAREZ MOLINA', 'edad': 22, 'rut': '20345313-2', 'asignatura': 'ANALISIS', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 61},
    {'nombre': 'JUAN LUIS', 'apellido': 'AYALA PEREZ', 'edad': 28, 'rut': '16277951-6', 'asignatura': 'ANALISIS', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 62},
    {'nombre': 'MIGUEL ANGEL ANDRES', 'apellido': 'BRAVO PINO', 'edad': 36, 'rut': '18054340-6', 'asignatura': 'PROGRAMACION', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 61},
    {'nombre': 'CRISTIAN ISAIAS', 'apellido': 'BUSTOS CABRERA', 'edad': 34, 'rut': '18357224-5', 'asignatura': 'PROGRAMACION', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 61},
    {'nombre': 'EDUARDO JESUS', 'apellido': 'DOMINGUEZ CAMPOS', 'edad': 26, 'rut': '17709058-1', 'asignatura': 'PROGRAMACION', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 61},
    {'nombre': 'CRISTHIAN ANDRÉS', 'apellido': 'ECHEVERRÍA BUSTAMANTE', 'edad': 38, 'rut': '15921029-4', 'asignatura': 'PROGRAMACION', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 61},
    {'nombre': 'NICOLAS ALEXANDER', 'apellido': 'ESPINOZA REYES', 'edad': 33, 'rut': '18026553-8', 'asignatura': 'PROGRAMACION', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 62},
    {'nombre': 'JAVIER EDUARDO', 'apellido': 'FIGUEROA ESCOBAR', 'edad': 31, 'rut': '16104424-5', 'asignatura': 'PROGRAMACION', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 62},
    {'nombre': 'FRANKLIN EDUARDO', 'apellido': 'MARTINEZ PORTILLO', 'edad': 20, 'rut': '26320485-9', 'asignatura': 'BASE DE DATOS', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 1},
    {'nombre': 'FRANCISCO JAVIER', 'apellido': 'MEDINA MALDONADO', 'edad': 28, 'rut': '18881480-8', 'asignatura': 'BASE DE DATOS', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 1},
    {'nombre': 'OMAR IGNACIO', 'apellido': 'MENA VERGARA', 'edad': 33, 'rut': '17766939-3', 'asignatura': 'BASE DE DATOS', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 2},
    {'nombre': 'SAMUEL ANDRES', 'apellido': 'MENDOZA BELLORIN', 'edad': 34, 'rut': '26141750-2', 'asignatura': 'BASE DE DATOS', 'nota': None, 'rol': 'ESTUDIANTE', 'seccion': 2},]

Docente = [{'nombre': 'PATRICIO EDUARDO', 'apellido': 'VERGARA MALDONADO', 'edad': 33, 'rut': '16814286-2', 'asignatura': 'ANALISIS - PROGRAMACION', 'nota': None, 'rol': 'PROFESOR', 'seccion': '61-62'},
    {'nombre': 'DIEGO RICARDO', 'apellido': 'YAÑEZ MUÑOZ', 'edad': 40, 'rut': '19112325-5', 'asignatura': 'BASE DE DATOS - ANALISIS', 'nota': None, 'rol': 'PROFESOR', 'seccion': '62-1-2'},
    {'nombre': 'FELIPE', 'apellido': 'ARAYA LUNA', 'edad': 40, 'rut': '15533868-7', 'asignatura': 'PROGRAMACION - BASE DE DATOS','nota': None, 'rol': 'PROFESOR', 'seccion': '62-1-2'},]



def ingresar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    apellidos = input("Ingrese los apellidos del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))
    asignatura = input("Ingrese la asignatura: ")
    rol = input("Ingrese el rol del usuario (profesor/alumno): ").lower()
    seccion = input("Ingrese la sección: ")

    if any(u.nombre == nombre and u.apellidos == apellidos for u in usuarios):
        print("El usuario ya existe.")
    else:
        nuevo_usuario = Usuario(nombre, apellidos, edad, asignatura, rol, seccion)
        usuarios.append(nuevo_usuario)
        print("Usuario {rol} agregado con éxito.")

def ingresar_notas():
    docente = validar_docente()
    if docente:
        seccion = docente.seccion
        asignatura = docente.asignatura
        for usuario in usuarios:
            if usuario.rol == 'alumno' and usuario.seccion == seccion and usuario.asignatura == asignatura:
                print("\nIngresar notas para" , usuario.nombre, usuario.apellidos , " : ")
                nota1 = float(input("Ingrese Nota 1: "))
                nota2 = float(input("Ingrese Nota 2: "))
                nota3 = float(input("Ingrese Nota 3: "))
                usuario.notas = {'nota1': nota1, 'nota2': nota2, 'nota3': nota3}
                print("Notas ingresadas con éxito.")

def actualizar_alumno():
    docente = validar_docente()
    if docente:
        nombre = input("Ingrese el nombre del alumno a actualizar: ")
        apellidos = input("Ingrese los apellidos del alumno a actualizar: ")

        alumno_encontrado = None
        for usuario in usuarios:
            if usuario.rol == 'alumno' and usuario.nombre == nombre and usuario.apellidos == apellidos:
                alumno_encontrado = usuario
                break

        if alumno_encontrado:
            if docente.seccion == alumno_encontrado.seccion and docente.asignatura == alumno_encontrado.asignatura:
                print("\nDatos actuales del alumno" ,nombre, apellidos, ":")
                print("Sección:" ,alumno_encontrado.seccion, )
                print("Asignatura:" ,alumno_encontrado.asignatura,)
                print("Edad:" ,alumno_encontrado.edad, )

                confirmacion = input("¿Está seguro de actualizar este alumno? (SI/NO): ").upper()
                if confirmacion == "SI":
                    alumno_encontrado.edad = int(input("Ingrese la nueva edad del alumno: "))
                    print("Alumno actualizado con éxito.")
                else:
                    print("Actualización cancelada.")
            else:
                print("No tiene permisos para actualizar a este alumno.")
        else:
            print("Alumno no encontrado.")

def eliminar_alumno():
    docente = validar_docente()
    if docente:
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        apellidos = input("Ingrese los apellidos del alumno a eliminar: ")

        alumno_encontrado = None
        for usuario in usuarios:
            if usuario.rol == 'alumno' and usuario.nombre == nombre and usuario.apellidos == apellidos:
                alumno_encontrado = usuario
                break

        if alumno_encontrado:
            if docente.seccion == alumno_encontrado.seccion and docente.asignatura == alumno_encontrado.asignatura:
                print("\nDatos del alumno" , nombre, apellidos, "a eliminar:")
                print("Sección:" ,alumno_encontrado.seccion, )
                print("Asignatura:" ,alumno_encontrado.asignatura, )
                print("Edad:" ,alumno_encontrado.edad, )

                confirmacion = input("¿Está seguro de eliminar este alumno? (SI/NO): ").upper()
                if confirmacion == "SI":
                    usuarios.remove(alumno_encontrado)
                    print("Alumno eliminado con éxito.")
                else:
                    print("Eliminación cancelada.")
            else:
                print("No tiene permisos para eliminar a este alumno.")
        else:
            print("Alumno no encontrado.")

def listar_por_secciones():
    docente = validar_docente()
    if docente:
        seccion = input("Ingrese la sección a listar: ")
        asignatura = input("Ingrese la asignatura (opcional): ")

        alumnos_seccion = [u for u in usuarios if u.rol == 'alumno' and u.seccion == seccion and (not asignatura or u.asignatura == asignatura)]

        if alumnos_seccion:
            print("\nLista de Alumnos:")
            for alumno in alumnos_seccion:
                print(" \nNombre:", alumno.nombre ," " ,alumno.apellido,  " : "  )
               print("Sección:" ,alumno_encontrado.seccion)
                print("Asignatura:" ,alumno.asignatura,)
                if hasattr(alumno, 'notas'):
                    print("Notas:" ,alumno.notas, )
                else:
                    print("Notas:" No ingresadas)
            print("\nDocente a cargo: ,docente.nombre, docente.apellidos")
        else:
            print("No hay alumnos en la sección o asignatura especificada.")

def mostrar_por_alumnos():
    docente = validar_docente()
    if docente:
        nombre = input("Ingrese el nombre del alumno a mostrar: ")
        apellidos = input("Ingrese los apellidos del alumno a mostrar: ")

        alumno_encontrado = None
        for usuario in usuarios:
            if usuario.rol == 'alumno' and usuario.nombre == nombre and usuario.apellidos == apellidos:
                alumno_encontrado = usuario
                break

        if alumno_encontrado:
            if docente.seccion == alumno_encontrado.seccion and docente.asignatura == alumno_encontrado.asignatura:
                print("\nDatos del alumno ", nombre , apellido , ":" )
                print("Sección:" ,alumno_encontrado.seccion,")
                print("Asignatura:" ,alumno_encontrado.asignatura,")
                if hasattr(alumno_encontrado, 'notas'):
                    print("Notas:" ,alumno_encontrado.notas, ")
                else:
                    print("Notas: No ingresadas")
            else:
                print("No tiene permisos para mostrar a este alumno.")
        else:
            print("Alumno no encontrado.")

def mostrar_por_docentes():
    docente = validar_docente()
    if docente:
        print("\nLista de Docentes:")
        for d in docentes:
            print("\nNombre:" ,d.nombre, ,d.apellidos,)
            print("Asignatura:" ,d.asignatura, )
            print("Sección:" ,d.seccion, )
        print("\nFin de la lista.")

def validar_docente():
    nombre = input("Ingrese su nombre como docente: ")
    apellidos = input("Ingrese sus apellidos como docente: ")
    asignatura = input("Ingrese la asignatura: ")
    seccion = input("Ingrese la sección: ")

    docente_encontrado = None
    for d in docentes:
        if d.nombre == nombre and d.apellidos == apellidos and d.asignatura == asignatura and d.seccion == seccion:
            docente_encontrado = d
            break

    if docente_encontrado:
        return docente_encontrado
    else:
        print("Docente no encontrado o datos incorrectos.")
        return None

usuarios = [Usuario("Juan", "Perez", 25, "Matemáticas", "alumno", "A"),
            Usuario("Maria", "Lopez", 30, "Historia", "alumno", "B")]

docentes = [Docente("Profesor", "Apellido", "Matematicas", "A")]

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Ingresar Usuario")
    print("2. Ingresar Notas")
    print("3. Actualizar Alumno")
    print("4. Eliminar Alumno")
    print("5. Mostrar")
    print("6. Salir del Programa")

    opcion_principal = input("Ingrese la opción deseada (1, 2, 3, 4, 5, 6): ").upper()

    if opcion_principal == "1":
        ingresar_usuario()
    elif opcion_principal == "2":
        ingresar_notas()
    elif opcion_principal == "3":
        actualizar_alumno()
    elif opcion_principal == "4":
        eliminar_alumno()
    elif opcion_principal == "5":
        while True:
            print("\nMenú Mostrar:")
            print("A. Listar por Secciones")
            print("B. Mostrar por Alumnos")
            print("C. Mostrar por Docentes")
            print("D. Volver al Menú Principal")

            opcion_mostrar = input("Ingrese la opción deseada (A, B, C, D): ").upper()

            if opcion_mostrar == "A":
                listar_por_secciones()
            elif opcion_mostrar == "B":
                mostrar_por_alumnos()
            elif opcion_mostrar == "C":
                mostrar_por_docentes()
            elif opcion_mostrar == "D":
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    elif opcion_principal == "6":
        salir = input("¿Desea salir del programa? (SI/NO): ").upper()
        if salir == "SI":
            print("¡Hasta luego!")
            break
        elif salir == "NO":
            continue
        else:
            print("Opción no válida. Volviendo al Menú Principal.")
    else:
        print("Opción no válida. Intente nuevamente.")
