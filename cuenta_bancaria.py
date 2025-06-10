#Proyecto - Cuenta Bancaria
from random import randint
from os import system

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
        return f"¡Hola {self.nombre} {self.apellido}! \U0001FAAA \nSu número de cuenta es: {self.numero_cuenta} \U0001F4B3 \nSu balance es: ${self.balance} MXN \U0001F4B5 \n"

    def deposito(self, operacion_deposito):
        self.balance = self.balance + operacion_deposito
        return print(f"Su balance es: ${self.balance} MXN")

    def retiro(self, operacion_retiro):
        if self.balance < operacion_retiro or self.balance == 0:
            return print("La cantidad que deseas retirar sobrepasa tu balance. Intenta con otra cantidad.")
        else:
            self.balance = self.balance - operacion_retiro
            return print(f"Su balance es: ${self.balance} MXN")

#Funciones
def inicio():
    print("\U0001F3E6 ¡Bienvenido(a) a tu cuenta bancaria! \U0001F3E7 \nInicia tu registro para poder acceder a tu balance.")
    nombre, apellido = datos_ingresados()
    validacion, nombre_validado, apellido_validado = validar_datos(nombre, apellido)

    if validacion is False:
        return print("Ha ocurrido un error. \U0000274C \nFavor de volver a ingresar sus datos. \U0001F615")

    cliente_nuevo = nuevo_cliente(validacion, nombre_validado, apellido_validado)
    system("cls")

    opcion = 0
    while opcion != 3:
        print(cliente_nuevo.__str__())
        print("Ingrese la operación que desea hacer:\n1.- Depositar dinero\n2.- Retirar dinero\n3.- Salir")
        opcion = int(input())
        system("cls")
        if opcion == 1:
            print("Ingresa la cantidad que deseas depositar: ")
            deposito = int(input())
            system("cls")
            cliente_nuevo.deposito(deposito)
        elif opcion == 2:
            print("Ingresa la cantidad que deseas retirar: ")
            retiro = int(input())
            system("cls")
            cliente_nuevo.retiro(retiro)
        elif opcion == 3:
            pass
        else:
            print("ERROR \U0000274C Esa opción no existe. Favor de ingresar una opción valida.\n")

    return print("Gracias por usar nuestro sistema bancario. ¡Que tenga un excelente día! \U0001F607 \n\U0001F47A Elaborado por Anton Mtz. \U0001F30A")


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
        return print("ERROR \U0000274C El nombre ingresado o su apellido no es válido, favor de ingresar sus datos nuevamente.")

#Esta funcion genera el numero de la cuenta bancaria
def generar_numero_cuenta():

    numero_cuenta_bancaria = randint(1000000000000000, 9999999999999999)

    return numero_cuenta_bancaria

#Iniciamos el programa
inicio()

