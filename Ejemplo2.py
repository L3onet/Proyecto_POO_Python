import math as m
from abc import abstractmethod
from abc import ABCMeta

class ReciboLuzAbs(ABCMeta):

    # Método estático
    @staticmethod
    def calcularTotalConsumo(lecturaActual, lecturaAnterior, costoKW):
        consumoKw = lecturaActual - lecturaAnterior
        costoConsumo = consumoKw * costoKW
        if consumoKw < 500:
            totalAPagar = costoConsumo * 1.22
        elif consumoKw >= 500 and consumoKw < 900:
            totalAPagar = costoConsumo * 1.18
        else:
            totalAPagar = costoConsumo * 1.12
        totalAPagar = round(totalAPagar,2)
        return totalAPagar


class ReciboLuz:

    __costoKw = float(0.0)          # El costo por KW
    __lecturaAnterior = int(0)      # La lectura anterior del medidor
    __lecturaActual = int(0)        # La lectura actual del medidor
    __consumoKw = int(0)            # El total de consumo de KW en el periodo
    __costoConsumo = float(0.0)     # El total a pagar sin impuestos
    __totalAPagar = float(0.0)      # El total a pagar con impuestos

    def __init__(self, lecturaActual, lecturaAnterior, costoKw):
        self.__lecturaActual = lecturaActual
        self.__lecturaAnterior = lecturaAnterior
        self.__costoKw = costoKw
        self.calcularConsumo()
        self.calcularCostoConsumo()
        self.calcularTotalConsumo()

    # Método destructor
    def __del__(self):
        print ("Destructor llamado")

    def setLecturaActual(self, lecturaActual):
        self.__lecturaActual = lecturaActual

    def getCostoKw(self):
        return self.__costoKw

    def getTotalAPagar(self):
        return self.__totalAPagar

    def calcularConsumo(self):
        self.__consumoKw = self.__lecturaActual - self.__lecturaAnterior

    def calcularCostoConsumo(self):
        self.__costoConsumo = self.__consumoKw * self.__costoKw

    def calcularTotalConsumo(self):
        if self.__consumoKw < 500:
            self.__totalAPagar = self.__costoConsumo * 1.22
        elif self.__consumoKw >= 500 and self.__consumoKw < 900:
            self.__totalAPagar = self.__costoConsumo * 1.18
        else:
            self.__totalAPagar = self.__costoConsumo * 1.12
        self.__totalAPagar = round(self.__totalAPagar,2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()