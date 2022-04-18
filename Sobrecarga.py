# Crear la clase Jornada Laboral de un empleado

"""
    La jornada de trabajo normal de un empleado durante una semana comprende 40 horas.
    Por cada hora trabajada dentro de esas 40 horas un empleado recibe el salario normal.
    Todas las horas trabajadas por encima de esas 40 horas se consideran horas extras.
    Por cada hora extra el empleado recibe 1.5 veces el salario que recibe por una hora normal.
    El usuario ingresa el salario normal por hora que gana un empleado y el número de horas
    trabajadas durante la semana. Mostrar el salario total semanal que gana el empleado.

    Autor: Mariana Lilibeth Antúnez García
    """

class JornadaLaboral:
    """
    Esta clase calcula el salario que debe recibir un empleado después de una jornada laboral
    """

    # Declarar atributos
    # Sintaxis es:
    # __nombreatributo = tipo(valor)
    __nombreEmpleado = str("")
    __numeroSemana = str("")
    __horasTrabajadas = int(0)
    __horasExtras = int(0)
    __salario = float(0.0)
    __total = float(0.0)
    __totalHorasExtras = float(0.0)
    __salarioTotal = float(0.0)

    # Declarar métodos
    # Sintáxis es:
    #
    # def nombreMetodo(self,parametros):
    """ Documentación"""

    # instrucciones


    def calcularSalario(self,horasTrabajadas = None, salario = None, horasExtras = None):
        # Sobrecarga de dos parámetros
        if horasTrabajadas is not None and salario is not None and horasExtras is None:
            self.__horasTrabajadas = horasTrabajadas
            self.__salario = salario
            self.calcularSalarioNormal()
        # Sobrecarga de tres parámetros
        elif horasTrabajadas is not None and salario is not None and horasExtras is not None:
            self.__horasTrabajadas = horasTrabajadas
            self.__salario = salario
            self.__horasExtras = horasExtras
            self.calcularSalarioNormal()
            self.calcularCostoHorasExtras()

    def getsalarioTotal(self):
        return self.__salarioTotal

    def calcularSalarioNormal(self):
        """
        El sistema calculará el salario normal de un empleado que trabaja en una jornada
        de 40 horas sin contar horas extras.

        Parámetros de entrada:
        horasTrabajadas: Son las horas trabajadas en una Jornada Laboral.
        salario: El pago que se recibe por hora.

        Salida:
        El sistema dispondrá del salario que recibe el empleado.
        """
        self.__salarioTotal = self.__horasTrabajadas * self.__salario


    def calcularCostoHorasExtras(self):
        """  El sistema calculará el costo de las horas extras trabajadas sabiendo
        que a estas se le pagan 1.5 más que una hora normal.

        Parámetros de entrada:
        horasExtras: Son las horas extras trabajadas por un empleado.
        salario: El pago que recibe por hora.

        Salida:
        El sistema dispondrá del costo total por las horas extras trabajadas.
        """
        self.__totalHorasExtras = self.__horasExtras * (self.__salario * 1.5)
        self.__salarioTotal += self.__totalHorasExtras

if __name__ == "__main__":
    recibo = JornadaLaboral()
    recibo.calcularSalario(40,100,5)
    print(recibo.getsalarioTotal())
