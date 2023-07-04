from datetime import date

from capa_datos_.calculadoraEdad import CalculadoraEdad
from capa_datos_.calculadoraEdadDao import CalculadoraEdadDAO


class CalculadoraEdadService:
    # Menu
    def menuEdad(self):
        from capa_datos_.MenuPrincipal import MenuPrincipal  # Importación tardía
        opcion = input("-----------------------------------\n"
                            "MENU CALCULADORA EDAD\n-----------------------------------\n"
                            "\n1: CALCULO ETARIO "
                            "\n2: VOLVER AL MENÚ PRINCIPAL\n"
                            "\n Seleccione una opcion: ")

        if opcion == "1":
            self.menuCalculoEdad()
        if opcion == "2":
            MenuPrincipal.menuPrincipal()

    def menuCalculoEdad(self):
        print("MENU CALCULADORA EDAD")
        print("--------------------")

        nombre_apellido = input("Ingrese su nombre y apellido: ")
        print("--------------------")
        dia = int(input("Ingresa tu día de nacimiento: "))
        mes = int(input("Ingresa tu mes de nacimiento: "))
        anio = int(input("Ingresa tu año de nacimiento: "))

        self.calcular_edad(nombre_apellido, dia, mes, anio)

    # Metodo para calcular la edad
    def calcular_edad(self,nombre_apellido,dd,mm,aa):
        hoy = date.today()   # Se usa datetime para identificar la fecha actual
        fecha_nacimiento = date(aa, mm, dd)
        edad = hoy.year - fecha_nacimiento.year

        # Verificamos si el cumpleaños ya ha pasado este año
        if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1   # Si el dia y mes de hoy, es menor al mes y dia de nacimiento, se le resta uno (Para poder expresarlo en meses y dias)

        # Calculamos el cumpleaños
        cumpleanios = fecha_nacimiento.replace(year=hoy.year)
        dias_restantes = (cumpleanios - hoy).days

        # Si la fecha actual es mayor a la fecha de nacimiento:
        if hoy.month > fecha_nacimiento.month:
            meses = hoy.month - fecha_nacimiento.month
            dias = hoy.day - fecha_nacimiento.day

        # Si el mes actual es menor al mes de nacimiento:
        elif hoy.month < fecha_nacimiento.month:
            meses = hoy.month + 12 - fecha_nacimiento.month   # Se calculan los meses
            dias = hoy.day - fecha_nacimiento.day   # Se calcula los dias

        # Si el dia actual es mayor o igual al dia de la fecha de nacimiento:
        elif hoy.day >= fecha_nacimiento.day:
            meses = 0
            dias = hoy.day - fecha_nacimiento.day   # Se calculan los dias

        # Si no se cumple ninguna de las condiciones:
        else:
            meses = 11
            dias = hoy.day + 30 - fecha_nacimiento.day

        # Si los dias son negativos, se le resta 1 mes (para agregarle dias en vez de meses), se convierte a positivo y se ajusta la fecha
        if dias < 0:
            meses -= 1
            dias *= -1
            dias += 30 - dias

        # Se ajustan los dias restantes en caso de que el cumpleaños ya haya pasado
        if dias_restantes < 0:
            cumpleanios_proximo_anio = fecha_nacimiento.replace(year=hoy.year + 1)   # Se reemplaza el año y se agrega 1
            dias_restantes = (cumpleanios_proximo_anio - hoy).days

        return self.mostrar_resultado(nombre_apellido, edad, meses, dias, dias_restantes,dd,mm,aa)

    # Para mostrar el resultado del cálculo
    def mostrar_resultado(self,nombre_apellido, edad, meses, dias, dias_restantes,dd,mm,aa):
        if dias_restantes == 0:   #
            print(f"\n¡Feliz cumpleaños, {nombre_apellido}!")
            print(f"¡Hoy cumpliste {edad} años!")

            calculadora_edad01 = CalculadoraEdad(nombre_apellido=nombre_apellido, dia_nac=dd, mes_nac=mm, ano_nac=aa, edad_actual=edad)
            CalculadoraEdadDAO.insertar(calculadora_edad01)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuEdad()

        else:
            edad_actual = f"{edad} años, {meses} meses, {dias} dias."
            # print("edad actual en string" + edad_actual)
            print(f"\nTu edad es: {edad} años, {meses} meses y {dias} días.")
            print(f"Faltan {dias_restantes} días para tu próximo cumpleaños.")

            calculadora_edad01 = CalculadoraEdad(nombre_apellido=nombre_apellido, dia_nac=dd, mes_nac=mm, ano_nac=aa, edad_actual=edad_actual)
            CalculadoraEdadDAO.insertar(calculadora_edad01)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuEdad()