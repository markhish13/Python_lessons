class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    @property
    def extrato(self):
        print("Nome do titular...........: {}".format(self.__titular))
        print("Saldo Atual...............: {}".format(self.__saldo))
        print("Limite da conta...........: {}".format(self.__limite))
        print("Saldo total disponível....: {}".format((self.__saldo) + (self.__limite)))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        sdo_dispo = self.__saldo + self.__limite
        return valor_saque <= sdo_dispo

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Transação não efetuada - Saldo Indisponível")

    def tranferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
            return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'CEF':'104', 'Bradesco':'237', 'Itaú':'341'}
