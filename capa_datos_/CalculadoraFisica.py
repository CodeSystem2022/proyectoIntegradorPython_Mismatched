from logger_base import log


class CalculadoraFisica:
    def __init__(self, id_calculo_fisica=None, numero_ingresado=None, tipo_dato_ingresado=None):
        self._id_calculo_fisica = id_calculo_fisica
        self._numero_ingresado = numero_ingresado
        self._tipo_dato_ingresado = tipo_dato_ingresado

    def __str__(self):
        return f'''
        id_calculo_fisica: {self._id_calculo_fisica},
        Numero Ingresado: {self._numero_ingresado},
        Tipo Dato Ingresado: {self._tipo_dato_ingresado}
        '''

    @property
    def id_calculo_fisica(self):
        return self._id_calculo_fisica

    @id_calculo_fisica.setter
    def id_calculo_fisica(self, id_calculo_fisica):
        self._id_calculo_fisica = id_calculo_fisica

    @property
    def numero_ingresado(self):
        return self._numero_ingresado

    @numero_ingresado.setter
    def numero_ingresado(self, numero_ingresado):
        self._numero_ingresado = numero_ingresado

    @property
    def tipo_dato_ingresado(self):
        return self._tipo_dato_ingresado

    @tipo_dato_ingresado.setter
    def tipo_dato_ingresado(self, tipo_dato_ingresado):
        self._tipo_dato_ingresado = tipo_dato_ingresado


if __name__ == '__main__':
    calculadoraFisica1 = CalculadoraFisica(1, 52, "Hola")
    log.debug(calculadoraFisica1)
