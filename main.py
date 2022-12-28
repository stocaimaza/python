def almacenar():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    while len(contraseña) < 4:
        print("La contraseña debe tener al menos 4 dígitos")
        contraseña = input("Ingrese la contraseña: ")
    diccionario[usuario] = contraseña


def mostrar():
    print("Los usuarios registrados son: ")
    for usuario in diccionario:
        print(usuario)


def login():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    while usuario not in diccionario or diccionario[usuario] != contraseña:
        print("Usuario o contraseña incorrectos")
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
    print("Bienvenido al sistema")



diccionario = {}

almacenar()
mostrar()
login()