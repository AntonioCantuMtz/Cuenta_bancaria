#Proyecto - Cuenta Bancaria
from random import randint

class Persona:

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class Cliente(Persona):

    def __init__(self, numero_cuenta, balance, nombre, apellidos):
        super().__init__(nombre, apellidos)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Bienvenido(a) {self.nombre} {self.apellidos}\nSu número de cuenta es: {self.numero_cuenta}\nSu saldo es: ${self.balance} MXN"


#Funciones
def inicio():

    print("¡Bienvenido(a)!\nInicia sesión ingresando el número 1.¿Eres un cliente nuevo? Regístrate aquí, ingresa el número 2.\n1.- Iniciar sesión\n2.- Registrarse")
    opcion_ingresada = input()

    if opcion_ingresada == 1:
        nombre,apellido = datos_ingresados()
        validacion,nombre_validado,apellido_validado = validar_datos(nombre, apellido)
        nuevo_cliente(validacion, nombre_validado, apellido_validado)


def datos_ingresados():

    nombre = input("Ingresa tu nombre: ")
    apellidos = input("Ingresa tus apellidos")

    return nombre, apellidos


def validar_datos(validar_nombre, validar_apellidos):

    for letra in validar_nombre:
        if letra.isdigit():
            return False, validar_nombre, validar_apellidos

    for letra in validar_apellidos:
        if letra.isdigit():
            return False, validar_nombre, validar_apellidos

    return True, validar_nombre, validar_apellidos


def nuevo_cliente(validacion, nombre, apellidos):

    numero_de_cuenta = generar_numero_cuenta()

    if validacion is True:
        cliente = Cliente(numero_de_cuenta, 0, nombre, apellidos)
        return cliente
    else:
        return "ERROR. El nombre ingresado o su apellido no es válido, favor de ingresar sus datos nuevamente."

#Esta funcion genera el numero de la cuenta bancaria :p
def generar_numero_cuenta():

    numero_cuenta_bancaria = randint(1000000000000000, 9999999999999999)

    return numero_cuenta_bancaria








