# Importar de libreria predefinidas
import pandas as pd
from tkinter import *
from tkinter import messagebox

# Importar de archivos
from Estadistica import estadistica
import math

class Main:
    numerador = 10
    denominador = 0
    division = 0

    def main(self):
        print("Antes de la division")
        try:
            division = self.numerador / self.denominador
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
        print("Despues de la division")

if __name__ == "__main__":
    programa = Main()
    programa.main()