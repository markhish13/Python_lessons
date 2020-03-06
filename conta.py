class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Nome do titular.....: {}".format(self.__titular))
        print("Saldo Atual.........: {}".format(self.__saldo))
        print("Limite da conta.....: {}".format(self.__limite))
        print("Saldo disponível....: {}".format((self.__saldo) + (self.__limite)))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        sdo_dispo = self.__saldo + self.__limite
        if sdo_dispo >= valor:
            self.__saldo -= valor
        else:
            print("Transação não efetuada - Saldo Indisponível")
            sdo_dispo += valor


    def alterar_limite(self, valor):
        self.__limite += valor

    def tranferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)


