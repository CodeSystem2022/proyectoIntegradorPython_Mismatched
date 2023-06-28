from logger_base import log

class CalculadoraRegular:
    def __init__(self, id_calculo_regular=None, numero_ingresado=None, resultado=None):
        self._id_calculo_regular = id_calculo_regular
        self._numero_ingresado = numero_ingresado
        self._resultado = resultado

    def __str__(self):
        return f'''
        id_calculo_regular: {self._id_calculo_regular},
        Numero Ingresado: {self._numero_ingresado},
        Resultado: {self._resultado}
        '''

    @property
    def id_calculo_regular(self):
        return self._id_calculo_regular

    @id_calculo_regular.setter
    def id_calculo_regular(self, id_calculo_regular):
        self._id_calculo_regular = id_calculo_regular

    @property
    def numero_ingresado(self):
        return self._numero_ingresado

    @numero_ingresado.setter
    def numero_ingresado(self, numero_ingresado):
        self._numero_ingresado = numero_ingresado

    @property
    def resultado(self):
        return self._resultado

    @resultado.setter
    def resultado(self, resultado):
        self._resultado = resultado

if __name__ == '__main__':
    calculadoraRegular1 = CalculadoraRegular(1, '-56*96', '-5376')
    log.debug(calculadoraRegular1)