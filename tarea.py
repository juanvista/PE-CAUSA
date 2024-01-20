

    class Usuario:
    def __init__(self, nombre, apellidos, edad, asignatura, rol, seccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.asignatura = asignatura
        self.rol = rol
        self.seccion = seccion




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
        print(f"Usuario {rol} agregado con éxito.")

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
                print(f"\nDatos actuales del alumno {nombre} {apellidos}:")
                print(f"Sección: {alumno_encontrado.seccion}")
                print(f"Asignatura: {alumno_encontrado.asignatura}")
                print(f"Edad: {alumno_encontrado.edad}")

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
                print(f"\nDatos del alumno {nombre} {apellidos} a eliminar:")
                print(f"Sección: {alumno_encontrado.seccion}")
                print(f"Asignatura: {alumno_encontrado.asignatura}")
                print(f"Edad: {alumno_encontrado.edad}")

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
                print(f"\nNombre: {alumno.nombre} {alumno.apellidos}")
                print(f"Sección: {alumno.seccion}")
                print(f"Asignatura: {alumno.asignatura}")
                if hasattr(alumno, 'notas'):
                    print(f"Notas: {alumno.notas}")
                else:
                    print("Notas: No ingresadas")
            print(f"\nDocente a cargo: {docente.nombre} {docente.apellidos}")
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
                print(f"\nDatos del alumno {nombre} {apellidos}:")
                print(f"Sección: {alumno_encontrado.seccion}")
                print(f"Asignatura: {alumno_encontrado.asignatura}")
                if hasattr(alumno_encontrado, 'notas'):
                    print(f"Notas: {alumno_encontrado.notas}")
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
            print(f"\nNombre: {d.nombre} {d.apellidos}")
            print(f"Asignatura: {d.asignatura}")
            print(f"Sección: {d.seccion}")
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
    print("I. Ingresar Usuario")
    print("II. Ingresar Notas")
    print("III. Actualizar Alumno")
    print("IV. Eliminar Alumno")
    print("V. Mostrar")
    print("VI. Salir del Programa")

    opcion_principal = input("Ingrese la opción deseada (I, II, III, IV, V, VI): ").upper()

    if opcion_principal == "I":
        ingresar_usuario()
    elif opcion_principal == "II":
        ingresar_notas()
    elif opcion_principal == "III":
        actualizar_alumno()
    elif opcion_principal == "IV":
        eliminar_alumno()
    elif opcion_principal == "V":
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

    elif opcion_principal == "VI":
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
