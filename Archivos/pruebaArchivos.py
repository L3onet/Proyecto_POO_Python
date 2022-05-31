class pruebaArchivos:

    def leerArchivo(self, archivo):
        file = open(archivo, 'r')
        lineas = []
        for linea in file.readlines():
            lineas.append(linea)
        file.close()
        return lineas

if __name__ == "__main__":
    prueba = pruebaArchivos()
    print(prueba.leerArchivo("retos.txt"))