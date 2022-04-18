class TiposMetodos:

    # Método de instancia
    def metodo(self, mensaje):
        return mensaje

    # Método de clase
    @classmethod
    def metododeclase(cls, mensaje):
        return mensaje

    # Método estático
    @staticmethod
    def metodoestatico(mensaje):
        return mensaje

if __name__ == "__main__":
    metodo = TiposMetodos()

    print(TiposMetodos.metodoestatico("Método estático"))
    print(TiposMetodos.metododeclase("Método de clase"))
    print(metodo.metodo("Método de instancia"))
