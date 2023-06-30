from capa_datos_.calculadoraEdad import CalculadoraEdad
from capa_datos_.conexion import Conexion
from capa_datos_.cursor_del_pool import CursorDelPool
from logger_base import log


class CalculadoraEdadDAO:
    _SELECCIONAR = 'SELECT * FROM CALCULADORAS_EDADES ORDER BY id_calculo_edad'
    _INSERTAR = 'INSERT INTO CALCULADORAS_EDADES(nombre_apellido, diaNac, mesNac, añoNac, edad_actual) VALUES (%s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE CALCULADORAS_EDADES SET id_calculo_edad=%s, nombre_apellido=%s, diaNac=%s, mesNac=%s, añoNac=%s, edad_actual=%s'
    _ELIMINAR = 'DELETE FROM CALCULADORAS_EDADES WHERE id_calculo_edad=%s'
    _LISTAR = 'SELECT * FROM CALCULADORAS_EDADES'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute("SELECT * FROM calculadoras_edades")
            rows = cursor.fetchall()
            # Procesar los resultados según sea necesario
            for row in rows:
                id_calculo_edad = row[0]
                nombre_apellido = row[1]
                diaNac = row[2]
                mesNac = row[3]
                añoNac = row[4]
                edad_actual = row[5]

    @classmethod
    def insertar(cls, calculoEdad):
        with CursorDelPool() as cursor:
            data = (
                calculoEdad.id_calculo_edad,
                calculoEdad.nombre_apellido,
                calculoEdad.diaNac,
                calculoEdad.mesNac,
                calculoEdad.añoNac,
                calculoEdad.edad_actual
            )
            cursor.execute(
                "INSERT INTO calculadoras_edades (id_calculo_edad, nombre_apellido, diaNac, mesNac, añoNac, edad_actual) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                data
            )

    @classmethod
    def eliminar(cls, calculoRegular):
        with CursorDelPool() as cursor:
            cursor.execute("DELETE FROM calculadoras_edades WHERE id_calculo_edad = %s",
                           (calculoRegular.id_calculo_edad,))


if __name__ == '__main__':
    # Insertar un registro
    calculadoraEdad1 = CalculadoraEdad(id_calculo_edad=0, nombre_apellido="Santiago Martos", diaNac=6, mesNac=6, añoNac=2003, edad_actual="20 años, 7 meses, 15 dias.")
    calculos_insertados = CalculadoraEdadDAO.insertar(calculadoraEdad1)
    log.debug(f"Calculo ingresado: {calculos_insertados}")
