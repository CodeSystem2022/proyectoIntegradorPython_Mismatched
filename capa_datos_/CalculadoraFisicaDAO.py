from capa_datos_.CalculadoraFisica import CalculadoraFisica
from capa_datos_.conexion import Conexion
from capa_datos_.cursor_del_pool import CursorDelPool
from logger_base import log

class CalculadoraFisicaDAO:
    _INSERTAR = 'INSERT INTO CALCULADORAS_FISICAS(numero_ingresado, tipo_dato_ingresado) VALUES (%s, %s)'
    _SELECCIONAR = 'SELECT * FROM CALCULADORAS_FISICAS ORDER BY id_calculo_fisica'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            calculadoras_fisicas = []
            for registro in registros:
                calculo = CalculadoraFisica(registro[0], registro[1], registro[2])
                calculadoras_fisicas.append(calculo)
            return calculadoras_fisicas


    @classmethod
    def insertar(cls, calculadoras_fisicas):
        with CursorDelPool() as cursor:
            valores = (calculadoras_fisicas.numero_ingresado, calculadoras_fisicas.tipo_dato_ingresado)
            cursor.execute(cls._INSERTAR, valores)
            # log.debug(f'Calculo Fisico Insertado: {calculadoras_fisicas}')
            return cursor.rowcount