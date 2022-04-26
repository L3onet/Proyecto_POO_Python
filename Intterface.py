from abc import abstractmethod
from abc import ABCMeta
import math

class Figura(metaclass=ABCMeta):
    _area = float(0)
    _perimetro = float(0)

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimetro(self):
        pass

class Circulo(Figura):
    __radio = float(0)

    def __init__(self, radio):
        if (radio < 0):
            self.__radio = 0
        else:
            self.__radio = radio
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        self._area = math.pi * (self.__radio * self.__radio)

    def calcularPerimetro(self):
        self._perimetro = (2 * math.pi) * self.__radio

    def getArea(self):
        return self._area

    def getPerimetro(self):
        return self._perimetro

class Cuadrado(Figura):
    __lado = float(0)

    def __init__(self, lado):
        if (lado < 0):
            self.__lado = 0
        else:
            self.__lado = lado
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        self._area = self.__lado * self.__lado

    def calcularPerimetro(self):
        self._perimetro = self.__lado * 4

    def getArea(self):
        return self._area

    def getPerimetro(self):
        return self._perimetro


class Rectangulo(Figura):
    __base = float(0)
    __altura = float(0)

    def __init__(self, base, altura):
        if (base < 0 or altura < 0):
            self.__base = 0
            self.__altura = 0
        else:
            self.__base = base
            self.__altura = altura
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        self._area = (self.__base * self.__altura)

    def calcularPerimetro(self):
        self._perimetro = (self.__base * 2) + (self.__altura * 2)

    def getArea(self):
        return self._area

    def getPerimetro(self):
        return self._perimetro