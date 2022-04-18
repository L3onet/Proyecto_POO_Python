from Herencia import *
from Ejemplo2 import *

def main():
    figuraPeque = Figura()

    circuloPeque = Circulo(23)
    print(circuloPeque.getPerimetro())

    cuadradoPeque = Cuadrado(12)
    print(cuadradoPeque.getPerimetro())

    rectanguloPeque = Rectangulo(15, 20)
    print(rectanguloPeque.getPerimetro())

    print("Clase y método abstracto")
    print(ReciboLuzAbs.calcularTotalConsumo(400,200,1.5))

if __name__ == "__main__":
    main() 