class Listas:
    __autos = [32,34,25,98]

    def agregarDatos(self, dato):
        self.__autos.append(dato)

    def mostrarDatos(self):
        for x in self.__autos:
            print(x)

    def mostrarLista(self):
        print(self.__autos)

    def limpiarLista(self):
        self.__autos.clear()

    def contarElementos(self):
        print(self.__autos.count(78))

    def mostrarTamanio(self):
        print(len(self.__autos))

    def insertarIndice(self, indice, dato):
        self.__autos.insert(indice, dato)

    def eliminarElemento(self, indice):
        self.__autos.pop(indice)

    def buscarYEliminar(self, dato):
        try:
            self.__autos.remove(dato)
        except ValueError:
            print("El valor " + str(dato) + " no se encuentra en la lista.")

    def ordenarLista(self):
        self.__autos.sort()

if __name__ == "__main__":
    lista = Listas()
    lista.agregarDatos(78)
    lista.mostrarLista()
    lista.insertarIndice(3,23)
    lista.mostrarLista()
    lista.eliminarElemento(2)
    lista.mostrarLista()
    lista.buscarYEliminar(89)
    lista.mostrarLista()
    lista.ordenarLista()
    lista.mostrarLista()
    # lista.contarElementos()
    # lista.mostrarTamanio()

    #lista.limpiarLista()
    #lista.mostrarDatos()
    #lista.contarElementos()