from capa_datos_.CalculadoraFisicaService import CalculadoraFisicaService
from capa_datos_.calculadoraEdadService import CalculadoraEdadService

class MenuPrincipal:
    @staticmethod
    def menuPrincipal():

        from capa_datos_.calculadoraRegularService import CalculadoraRegularService  # Importación tardía
        from capa_datos_.calculadoraEdadService import CalculadoraEdadService  # Importación tardía

        cr = CalculadoraRegularService()
        cf = CalculadoraFisicaService()
        ce = CalculadoraEdadService()
        opcion = input("|MENU PRINCIPAL|\n"
                       + "1: CALCULADORA REGULAR\n"
                       + "2: CALCULADORA DE FISICA\n"
                       + "3: CALCULADORA DE EDAD\n"
                       + "4: APAGAR\n")

        if opcion == "1":
            cr.calcular_operaciones()
        elif opcion == "2":
            cf.menuFisica()
        elif opcion == "3":
            ce.menuEdad()
        elif opcion == "4":
            import sys
            sys.exit(0)


if __name__ == '__main__':
    MenuPrincipal.menuPrincipal()
