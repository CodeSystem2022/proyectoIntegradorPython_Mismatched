from capa_datos_.CalculadoraRegular import CalculadoraRegular
from capa_datos_.conexion import Conexion
from capa_datos_.cursor_del_pool import CursorDelPool
from logger_base import log


class CalculadoraRegularDAO:
    _SELECCIONAR = 'SELECT * FROM CALCULADORAS_REGULARES ORDER BY id_calculo_regular'
    _INSERTAR = 'INSERT INTO CALCULADORAS_REGULARES(numero_ingresado, resultado) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE CALCULADORAS_REGULARES SET id_calculo_regular=%s, numero_ingresado=%s, resultado=%s'
    _ELIMINAR = 'DELETE FROM CALCULADORAS_REGULARES WHERE id_calculo_regular=%s'
    _LISTAR = 'SELECT * FROM CALCULADORAS_REGULARES'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            calculosRegulares = []
            for registro in registros:
                calculoRegular = CalculadoraRegular(registro[0], registro[1], registro[2])
                calculosRegulares.append(calculoRegular)
            return calculosRegulares

    @classmethod
    def insertar(cls, calculoRegular):
        with CursorDelPool() as cursor:
            valores = (calculoRegular.numero_ingresado, calculoRegular.resultado)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Calculo Regular Insertado: {calculoRegular}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, calculoRegular):
        with CursorDelPool() as cursor:
            valores = (calculoRegular.id_calculadora_regular,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Los objetos eliminados son: {calculoRegular}')
            return cursor.rowcount


if __name__ == '__main__':
    # Insertar un registro
    calculadoraRegular1 = CalculadoraRegular(numero_ingresado="-569*96", resultado="-54624")
    calculos_insertados = CalculadoraRegularDAO.insertar(calculadoraRegular1)
    log.debug(f'Calculo ingresado : {calculos_insertados}')

    # Seleccionar objetos
    calculadoras_regulares = CalculadoraRegularDAO.seleccionar()
    for calculadora_regular in calculadoras_regulares:
        log.debug(calculadora_regular)
