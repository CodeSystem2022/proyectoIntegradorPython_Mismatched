from logger_base import log


class CalculadoraEdad:
    def __init__(self, id_calculo_edad=None, nombre_apellido=None, dia_nac=None, mes_nac=None, ano_nac=None,
                 edad_actual=None):
        self._id_calculo_edad = id_calculo_edad
        self._nombre_apellido = nombre_apellido
        self._dia_nac = dia_nac
        self._mes_nac = mes_nac
        self._ano_nac = ano_nac
        self._edad_actual = edad_actual

    def __str__(self):
        return f'''
        id_calculo_edad: {self._id_calculo_edad}
        nombre_apellido: {self._nombre_apellido}
        diaNac:          {self._dia_nac}
        mesNac:          {self._mes_nac}
        anioNac:          {self._ano_nac}
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
    def dia_nac(self):
        return self._dia_nac

    @dia_nac.setter
    def dia_nac(self, dia_nac):
        self._dia_nac = dia_nac

    @property
    def mes_nac(self):
        return self._mes_nac

    @mes_nac.setter
    def mes_nac(self, mes_nac):
        self._mes_nac = mes_nac

    @property
    def ano_nac(self):
        return self._ano_nac

    @ano_nac.setter
    def ano_nac(self, ano_nac):
        self._ano_nac = ano_nac

    @property
    def edad_actual(self):
        return self._edad_actual

    @edad_actual.setter
    def edad_actual(self, edad_actual):
        self._edad_actual = edad_actual


# if __name__ == '__main__':
#     calculadoraEdad1 = CalculadoraEdad(0, "Santiago Martos", 6, 2, 2003, edad_actual=f"20 años, 7 meses, 15 dias, ")
#     log.debug(calculadoraEdad1)
