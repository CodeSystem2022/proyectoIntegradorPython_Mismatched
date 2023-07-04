from capa_datos_.calculadoraEdad import CalculadoraEdad
from capa_datos_.cursor_del_pool import CursorDelPool
from logger_base import log


class CalculadoraEdadDAO:
    _SELECCIONAR = 'SELECT * FROM CALCULADORAS_EDADES ORDER BY id_calculo_edad'
    _INSERTAR = 'INSERT INTO CALCULADORAS_EDADES(nombre_apellido, dia_nac, mes_nac, ano_nac, edad_actual) VALUES (%s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE CALCULADORAS_EDADES SET id_calculo_edad=%s, nombre_apellido=%s, diaNac=%s, mesNac=%s, añoNac=%s, edad_actual=%s'
    _ELIMINAR = 'DELETE FROM CALCULADORAS_EDADES WHERE id_calculo_edad=%s'
    _LISTAR = 'SELECT * FROM CALCULADORAS_EDADES'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            calculos_edad = []
            for registro in registros:
                calculo_edad = CalculadoraEdad(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5])
                calculos_edad.append(calculo_edad)
            return calculos_edad


    @classmethod
    def insertar(cls, calculoEdad):
        with CursorDelPool() as cursor:
            valores = (calculoEdad.nombre_apellido, calculoEdad.dia_nac, calculoEdad.mes_nac, calculoEdad.ano_nac, calculoEdad.edad_actual)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Calculo Edad insertado: {calculoEdad}')
            return cursor.rowcount



# if __name__ == '__main__':
    # Insertar un registro
    # calculadora_edad01 = CalculadoraEdad(nombre_apellido="Santiago Martos", dia_nac=6, mes_nac=6, ano_nac=2003, edad_actual="20 años, 7 meses, 15 dias.")
    # calculos_insertados = CalculadoraEdadDAO.insertar(calculadora_edad01)
    # log.debug(f"Calculo ingresado: {calculos_insertados}")



    # calculos_edades = CalculadoraEdadDAO.seleccionar()
    # for calculo_edad in calculos_edades:
    #     log.debug(calculo_edad)
