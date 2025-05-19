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

    def __str__(self):
        return f"Bienvenido(a) {self.nombre} {self.apellidos}\nSu número de cuenta es: {self.numero_cuenta}\nSu saldo es: {self.balance}"

    




