#Proyecto - Cuenta Bancaria
from random import randint

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, numero_cuenta, balance, nombre, apellido):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"¡Bienvenido(a) {self.nombre} {self.apellido}!\nSu número de cuenta es: {self.numero_cuenta}\nSu saldo es: ${self.balance} MXN"

    def deposito(self, operacion_deposito):
        self.balance = self.balance + operacion_deposito
        return f"Su balance es: ${self.balance} MXN"

    def retiro(self, operacion_retiro):
        if self.balance >= 0:
            return "La cantidad que deseas retirar sobrepasa tu balance. Intenta con otra cantidad."
        else:
            self.balance = self.balance - operacion_retiro
            return f"Su balance es: ${self.balance} MXN"


#Funciones
def inicio():
    print("¡Bienvenido(a) a tu cuenta bancaria! \nInicia tu registro para poder acceder a tu balance.")
    nombre,apellido = datos_ingresados()
    validacion, nombre_validado, apellido_validado = validar_datos(nombre, apellido)
    cliente_nuevo = nuevo_cliente(validacion, nombre_validado, apellido_validado)
    #Aqui se limpia la pantalla




def datos_ingresados():

    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")

    return nombre,apellido


def validar_datos(validar_nombre, validar_apellido):

    for letra in validar_nombre:
        if letra.isdigit():
            return False, validar_nombre, validar_apellido

    for letra in validar_apellido:
        if letra.isdigit():
            return False, validar_nombre, validar_apellido

    return True, validar_nombre, validar_apellido


def nuevo_cliente(validacion, nombre, apellido):

    numero_de_cuenta = generar_numero_cuenta()

    if validacion is True:
        cliente_nuevo = Cliente(numero_de_cuenta, 0, nombre, apellido)
        return cliente_nuevo
    else:
        return "ERROR. El nombre ingresado o su apellido no es válido, favor de ingresar sus datos nuevamente."

#Esta funcion genera el numero de la cuenta bancaria
def generar_numero_cuenta():

    numero_cuenta_bancaria = randint(1000000000000000, 9999999999999999)

    return numero_cuenta_bancaria

#Iniciamos el programa
inicio()





