class Monedas:
    __cantidadDinero = int(0)
    __mCincuenta = int(0)
    __mVeintiCinco = int(0)
    __mDiez = int(0)
    __mCinco = int(0)
    __mUno = int(0)

    def obtenerCambio(self, cantidadDinero):
        self.__cantidadDinero = cantidadDinero
        while self.__cantidadDinero > 0:
            if self.__cantidadDinero >= 50:
                self.__mCincuenta += 1
                self.__cantidadDinero -= 50
            elif self.__cantidadDinero >= 25:
                self.__mVeintiCinco += 1
                self.__cantidadDinero -= 25
            elif self.__cantidadDinero >= 10:
                self.__mDiez += 1
                self.__cantidadDinero -= 10
            elif self.__cantidadDinero >= 5:
                self.__mCinco += 1
                self.__cantidadDinero -= 5
            else:
                self.__mUno += 1
                self.__cantidadDinero -= 1

    def getMCincuenta(self):
        return self.__mCincuenta

    def getMVeintiCinco(self):
        return self.__mVeintiCinco

    def getMDiez(self):
        return self.__mDiez

    def getMCinco(self):
        return self.__mCinco

    def getMUno(self):
        return self.__mUno

if __name__ == "__main__":
    moneda = Monedas()
    moneda.obtenerCambio(49)
    print(moneda.getMCincuenta())
    print(moneda.getMVeintiCinco())
    print(moneda.qgetMDiez())
    print(moneda.getMCinco())
    print(moneda.getMUno())