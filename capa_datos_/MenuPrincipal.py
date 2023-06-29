from capa_datos_.CalculadoraRegular import CalculadoraRegular


class MenuPrincipal:
    @staticmethod
    def menuPrincipal():
        from capa_datos_.calculadoraRegularService import CalculadoraRegularService  # Importación tardía
        cr = CalculadoraRegularService()
        # cm = CalculadoraMatrices()
        # cf = CalculadoraFisica()
        # cd = CalculadoraDivisas()
        # ce = CalculadoraEdad()

        opcion = input("|MENU|\n"
                       + "1: CALCULADORA REGULAR\n"
                       + "2: CALCULADORA DE FISICA\n"
                       + "3: CALCULADORA DE EDAD\n"
                       + "4: CALCULADORA DE MATRICES\n"
                       + "5: APAGAR\n")

        if opcion == "1":
            cr.calcular_operaciones()
        # elif opcion == "2":
        #     cf.menuFisica()
        # elif opcion == "3":
        #     ce.menuEdad()
        # elif opcion == "4":
        #     cm.menuMatrices()
        elif opcion == "5":
            import sys
            sys.exit(0)


if __name__ == '__main__':
    MenuPrincipal.menuPrincipal()
