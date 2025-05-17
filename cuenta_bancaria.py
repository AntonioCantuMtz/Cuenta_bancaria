#Proyecto - Cuenta Bancaria

class Persona:

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class Cliente(Persona):

    def __init__(self, numero_cuenta, balance, nombre, apellidos):
        super().__init__(nombre, apellidos)
        self.numero_cuenta = numero_cuenta
        self.balance = balance




