class Menu:
    def __init__(self, dato):
        self.dato = dato

    def crear_usuarios(self):
        name = input("Ingrese el nombre del usuario: ").strip()
        last_name = input("Ingrese el apellido del usuario: ").strip()

        if name in self.dato:
            print("El usuario ya se encuentra ingresado.")
            return

        age = int(input("Ingrese la edad del usuario: "))
        subject = input("Ingrese la asignatura del usuario: ").strip()
        section = input("Ingrese la sección del usuario: ").strip()
        role = input("Ingrese el rol del usuario (profesor/alumno): ").strip()

        if role not in ('profesor', 'alumno'):
            print("El rol del usuario debe ser profesor o alumno.")
            return

        if role == 'alumno':
            self.dato[name] = {
                'last_name': last_name,
                'age': age,
                'subject': subject,
                'role': role,
                'section': section
            }
        elif role == 'profesor':
            self.dato[name] = {
                'last_name': last_name,
                'age': age,
                'subject': subject,
                'role': role,
                'section': section
            }

        print("El usuario ha sido creado.")

dato = {}

menu = Menu(dato)
menu.crear_usuarios()