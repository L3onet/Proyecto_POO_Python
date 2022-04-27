class Empleado:
    _nombreEmpleado = str("")
    _salario = float(0.0)
    _total = float(0.0)
    _numeroSemana = str("")
    _salarioTotal = float(0.0)

    def __init__(self, nombreEmpleado, salario, numeroSemana):
        self._nombreEmpleado = nombreEmpleado
        self._salario = salario
        self._numeroSemana = numeroSemana

    def calcularSalario(self):
        pass

    def getsalarioTotal(self):
        return self._salarioTotal

class EmpleadoHorasExtras(Empleado):
    __horasExtra = int(0)
    __totalHorasExtra = float(0.0)

    def __init__(self, nombreEmpleado, salario, numeroSemana, horasExtra):
        Empleado.__init__(self, nombreEmpleado,salario, numeroSemana)
        self.__horasExtra = horasExtra
        self.calcularSalario()


    def calcularSalario(self):
        self.__totalHorasExtra = self.__horasExtra * (self._salario * 1.5)
        self._salarioTotal += self.__totalHorasExtra


class EmpleadoNormal(Empleado):
    __horasTrabajadas = int(0)

    def __init__(self,nombreEmpleado, salario, numeroSemana, horasTrabajadas):
        Empleado.__init__(self, nombreEmpleado, salario, numeroSemana)
        self.__horasTrabajadas = horasTrabajadas
        self.calcularSalario()

    def calcularSalario(self):
        self._salarioTotal = self.__horasTrabajadas * self._salario