from logger_base import log


class CalculadoraEdad:
    def __init__(self, id_calculo_edad=None, nombre_apellido=None, diaNac=None, mesNac=None, añoNac=None,
                 edad_actual=None):
        self._id_calculo_edad = id_calculo_edad
        self._nombre_apellido = nombre_apellido
        self._diaNac = diaNac
        self._mesNac = mesNac
        self._añoNac = añoNac
        self._edad_actual = edad_actual

    def __str__(self):
        return f'''
        id_calculo_edad: {self._id_calculo_edad}
        nombre_apellido: {self._nombre_apellido}
        diaNac:          {self._diaNac}
        mesNac:          {self._mesNac}
        añoNac:          {self._añoNac}
        edad_actual:     {self._edad_actual}
        '''

    # Getters and Setters
    @property
    def id_calculo_edad(self):
        return self._id_calculo_edad

    @id_calculo_edad.setter
    def id_calculo_edad(self, id_calculo_edad):
        self._id_calculo_edad = id_calculo_edad

    @property
    def nombre_apellido(self):
        return self._nombre_apellido

    @nombre_apellido.setter
    def nombre_apellido(self, nombre_apellido):
        self._nombre_apellido = nombre_apellido

    @property
    def diaNac(self):
        return self._diaNac

    @diaNac.setter
    def diaNac(self, diaNac):
        self._diaNac = diaNac

    @property
    def mesNac(self):
        return self._mesNac

    @mesNac.setter
    def mesNac(self, mesNac):
        self._mesNac = mesNac

    @property
    def añoNac(self):
        return self._añoNac

    @añoNac.setter
    def añoNac(self, añoNac):
        self._añoNac = añoNac

    @property
    def edad_actual(self):
        return self._edad_actual

    @edad_actual.setter
    def edad_actual(self, edad_actual):
        self._edad_actual = edad_actual


if __name__ == '__main__':
    calculadoraEdad1 = CalculadoraEdad(0, "Santiago Martos", 6, 2, 2003, edad_actual=f"20 años, 7 meses, 15 dias, ")
    log.debug(calculadoraEdad1)
