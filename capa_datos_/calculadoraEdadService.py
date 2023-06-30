from datetime import date


class CalculadoraEdadService:   # Creamos la clase
    def __init__(self):
        self.nombre_apellido = ""
        self.dia = 0
        self.mes = 0
        self.anio = 0

    # Menu
    def menuCalculadoraEdad(self):
        print("Calculadora de Edad")
        print("--------------------")
        self.nombre_apellido = input("Ingrese su nombre y apellido: ")
        print("--------------------")
        self.dia = int(input("Ingresa tu día de nacimiento: "))
        self.mes = int(input("Ingresa tu mes de nacimiento: "))
        self.anio = int(input("Ingresa tu año de nacimiento: "))

    # Metodo para calcular la edad
    def calcular_edad(self):
        hoy = date.today()   # Se usa datetime para identificar la fecha actual
        fecha_nacimiento = date(self.anio, self.mes, self.dia)
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
        return edad, meses, dias, dias_restantes

    # Para mostrar el resultado del cálculo
    def mostrar_resultado(self, edad, meses, dias, dias_restantes):
        if dias_restantes == 0:   #
            print(f"\n¡Feliz cumpleaños, {self.nombre_apellido}!")
            print(f"¡Hoy cumpliste {edad} años!")
        else:
            edad_actual = f"{edad} años, {meses} meses, {dias} dias."
            # print("edad actual en string" + edad_actual)
            print(f"\nTu edad es: {edad} años, {meses} meses y {dias} días.")
            print(f"Faltan {dias_restantes} días para tu próximo cumpleaños.")

    def ingresar_datos(self):
        self.menuCalculadoraEdad()
        edad, meses, dias, dias_restantes = self.calcular_edad()
        self.mostrar_resultado(edad, meses, dias, dias_restantes)
