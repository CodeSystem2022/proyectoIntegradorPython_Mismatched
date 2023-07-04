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
            calculos_fisica = []
            for registro in registros:
                calculo_fisica = CalculadoraFisica(registro[0], registro[1], registro[2])
                calculos_fisica.append(calculo_fisica)
            return calculos_fisica


    @classmethod
    def insertar(cls, calculoFisica):
        with CursorDelPool() as cursor:
            valores = (calculoFisica.numero_ingresado, calculoFisica.tipo_dato_ingresado)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Calculo Fisico Insertado: {calculoFisica}')
            return cursor.rowcount

# if __name__ == '__main__':
    # calculadoraFisica1 = CalculadoraFisica(numero_ingresado=895, tipo_dato_ingresado="CTMR")
    # calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)
    # log.debug(f"Calculo ingresado: {calculo_insertado}")

    # log.debug(f"Calculo ingresado: {calculos_insertados}")

    # calculos_fisica = CalculadoraFisicaDAO.seleccionar()
    # for calculo_fisica in calculos_fisica:
    #     log.debug(calculo_fisica)