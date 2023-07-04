from capa_datos_.CalculadoraFisicaDAO import CalculadoraFisicaDAO
from capa_datos_.CalculadoraFisica import CalculadoraFisica


class CalculadoraFisicaService:
    def menuFisica(self):
        from capa_datos_.MenuPrincipal import MenuPrincipal  # Importación tardía
        opcion = input("-----------------------------------\n"
                        "CALCULADORA FÍSICA\n-----------------------------------\n"
                        "\n1: CALCULADORA VOLUMEN"
                        "\n2: CALCULADORA AREA\n"
                        "\n3: CALCULADORA TEMPERATURA\n"
                        "4: MENÚ PRINCIPAL\n"
                        "\nSeleccione una opcion: ")
        if opcion == "1":
            self.cVolumen(opcion)
        if opcion == "2":
            self.cArea(opcion)
        if opcion == "3":
            self.cTemperatura(opcion)
        if opcion == "4":
            MenuPrincipal.menuPrincipal()


    def cVolumen(self, entrada):

        tipo_dato01 = "Volumen"
        opcion = input("ELIJA EL VOLUMEN INICIAL\n"
                        "\n"
                        "1: CENTIMETRO CUBICO [cm3]\n"
                        "2: DECIMETRO CUBICO [dm3]\n"
                        "3: METRO CUBICO [m3]\n"
                        "4: MILILITROS [mL]\n"
                        "5: DECILITRO [dL]\n"
                        "6: LITRO [lts]\n"
                        "7: GALON [gal]\n"
                        "8: REGRESAR A LA CALCULADORA DE FISICA \n"
                        "\nSeleccione una opcion: ")

        if opcion == "1":
            cantidad = float(input("Digite la cantidad de dicho volumen: "))
            print("CANTIDAD INGRESADA:   |  {}  [cm3]  |\n".format(cantidad))
            print("Equivalente a:\n")
            print("Decímetro cúbico: {} [dm3]".format(cantidad / 1000))
            print("Mililitro: {} [mL]".format(cantidad))
            print("Decilitro: {} [dL]".format(cantidad / 100))
            print("Litro: {} [lts]".format(cantidad / 1000))
            print("Galon: {} [gal]".format(cantidad / 3785))

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato01)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "2":
            cantidad = float(input("Digite la cantidad de dicho volumen: "))
            print("CANTIDAD INGRESADA:   |  {}  [dm3]  |\n".format(cantidad))
            print("Equivalente a:\n")
            print("Centímetro cúbico: {} [cm3]".format(cantidad * 1000))
            print("Mililitro: {} [mL]".format(cantidad * 1000))
            print("Decilitro: {} [dL]".format(cantidad * 100))
            print("Litro: {} [lts]".format(cantidad / 10))
            print("Galon: {} [gal]".format(cantidad / 37.854))

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato01)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "3":
            cantidad = float(input("Digite la cantidad de dicho volumen: "))
            print("CANTIDAD INGRESADA:   |  {}  [m3]  |\n".format(cantidad))
            print("Equivalente a:\n")
            print("Centímetro cúbico: {} [cm3]".format(cantidad * 1000000))
            print("Decímetro cúbico: {} [dm3]".format(cantidad * 1000))
            print("Mililitro: {} [mL]".format(cantidad * 1000000))
            print("Decilitro: {} [dL]".format(cantidad * 100000))
            print("Litro: {} [lts]".format(cantidad * 1000))
            print("Galon: {} [gal]".format(cantidad / 3.785))

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato01)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "4":
            cantidad = float(input("Digite la cantidad de dicho volumen: "))
            print("CANTIDAD INGRESADA:   |  {}  [mL]  |\n".format(cantidad))
            print("Equivalente a:\n")
            print("Centímetro cúbico: {} [cm3]".format(cantidad))
            print("Decímetro cúbico: {} [dm3]".format(cantidad / 1000))
            print("Metro cúbico: {} [m3]".format(cantidad / 1000000))
            print("Decilitro: {} [dL]".format(cantidad / 100))
            print("Litro: {} [lts]".format(cantidad / 1000))
            print("Galon: {} [gal]".format(cantidad / 3785))

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato01)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "5":
            cantidad = float(input("Digite la cantidad de dicho volumen: "))
            print("CANTIDAD INGRESADA:   |  {}  [dL]  |\n".format(cantidad))
            print("Equivalente a:\n")
            print("Centímetro cúbico: {} [cm3]".format(cantidad * 100))
            print("Decímetro cúbico: {} [dm3]".format(cantidad / 10))
            print("Metro cúbico: {} [m3]".format(cantidad / 100000))
            print("Mililitro: {} [mL]".format(cantidad * 100))
            print("Litro: {} [lts]".format(cantidad / 10))
            print("Galon: {} [gal]".format(cantidad / 37.854))

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato01)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "6":
            cantidad = float(input("Digite la cantidad de dicho volumen: "))
            print("CANTIDAD INGRESADA:   |  {}  [lts]  |\n".format(cantidad))
            print("Equivalente a:\n")
            print("Centímetro cúbico: {} [cm3]".format(cantidad * 1000))
            print("Decímetro cúbico: {} [dm3]".format(cantidad * 10))
            print("Metro cúbico: {} [m3]".format(cantidad / 1000))
            print("Mililitro: {} [mL]".format(cantidad * 1000))
            print("Decilitro: {} [dL]".format(cantidad * 100))
            print("Galon: {} [gal]".format(cantidad / 3.785))

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato01)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "7":
            cantidad = float(input("Digite la cantidad de dicho volumen: "))
            print("CANTIDAD INGRESADA:   |  {}  [gal]  |\n".format(cantidad))
            print("Equivalente a:\n")
            print("Centímetro cúbico: {} [cm3]".format(cantidad * 3785))
            print("Decímetro cúbico: {} [dm3]".format(cantidad * 37.854))
            print("Metro cúbico: {} [m3]".format(cantidad * 3.785))
            print("Mililitro: {} [mL]".format(cantidad * 3785))
            print("Decilitro: {} [dL]".format(cantidad * 378.5))
            print("Litro: {} [lts]".format(cantidad * 3.785))

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato01)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "8":
            self.menuFisica()

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            self.menuFisica()


    def cArea(self, entrada):
        tipo_dato02 = "Volumen"
        opcion = input("ELIJA EL AREA INICIAL\n"
                        + "\n"
                        + "1: CENTIMETRO CUADRADO [cm2]\n"
                        + "2: DECIMETRO CUADRADO [dm2]\n"
                        + "3: METRO CUADRADO [m2]\n"
                        + "4: MILIMETRO CUADRADO [mm2]\n"
                        + "5: KILOMETRO CUADRADO [km2]\n"
                        + "6: MILLA CUADRADA [MI2]\n"
                        + "7: HECTAREA [ha]\n"
                        + "8: MENU FISICA\n"
                        + "\n"
                        + "Ingrese una opción: ")

        if opcion == "1":
            cantidad = float(input("Digite la cantidad de dicho area: "))
            print("CANTIDAD INGRESADA:   |  " + str(cantidad) + "  [cm2]  |\n"
                    + "\n"
                    + "Equivalente a: \n"
                    + "\n"
                    + "Decímetro cuadrado: " + str(cantidad / 100) + " [dm2]\n"
                    + "Metro cuadrado: " + str(cantidad / 10000) + " [m2]\n"
                  + "Milimetro cuadrado: " + str(cantidad * 100) + " [mm2]\n"
                  + "Kilometro cuadrado: " + str(cantidad / (10 ** 10)) + " [km2]\n"
                  + "Milla cuadrado: " + str(cantidad / (2.59 * (10 ** 10))) + " [MI2]\n"
                  + "Hectárea: " + str(cantidad / (10 ** 8)) + " [ha]\n"
                    + "\n")

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato02)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "2":
            cantidad = float(input("Digite la cantidad de dicho area: "))
            print("CANTIDAD INGRESADA:   |  " + str(cantidad) + "  [dm2]  |\n"
                    + "\n"
                    + "Equivalente a: \n"
                    + "\n"
                  + "Centímetro cuadrado: " + str(cantidad * 100) + " [cm2]\n"
                    + "Metro cuadrado: " + str(cantidad / 100) + " [m2]\n"
                  + "Milimetro cuadrado: " + str(cantidad * 10000) + " [mm2]\n"
                  + "Kilometro cuadrado: " + str(cantidad / (10 ** 8)) + " [km2]\n"
                  + "Milla cuadrado: " + str(cantidad / (2.59 * (10 ** 8))) + " [MI2]\n"
                  + "Hectárea: " + str(cantidad / (10 ** 6)) + " [ha]\n"
                    + "\n")

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato02)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "3":
            cantidad = float(input("Digite la cantidad de dicho area: "))
            print("CANTIDAD INGRESADA:   |  " + str(cantidad) + "  [m2]  |\n"
                    + "\n"
                    + "Equivalente a: \n"
                    + "\n"
                  + "Centímetro cuadrado: " + str(cantidad * 10000) + " [cm2]\n"
                  + "Decímetro cuadrado: " + str(cantidad * 100) + " [dm2]\n"
                  + "Milimetro cuadrado: " + str(cantidad * (10 ** 6)) + " [mm2]\n"
                  + "Kilometro cuadrado: " + str(cantidad / (10 ** 6)) + " [km2]\n"
                  + "Milla cuadrado: " + str(cantidad / (2.59 * (10 ** 6))) + " [MI2]\n"
                    + "Hectárea: " + str(cantidad / 10000) + " [ha]\n"
                    + "\n")

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato02)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "4":
            cantidad = float(input("Digite la cantidad de dicho area: "))
            print("CANTIDAD INGRESADA:   |  " + str(cantidad) + "  [mm2]  |\n"
                    + "\n"
                    + "Equivalente a: \n"
                    + "\n"
                    + "Centímetro cuadrado: " + str(cantidad / 100) + " [cm2]\n"
                    + "Decímetro cuadrado: " + str(cantidad / 10000) + " [dm2]\n"
                  + "Metro cuadrado: " + str(cantidad / (10 ** 6)) + " [m2]\n"
                  + "Kilometro cuadrado: " + str(cantidad / (10 ** 12)) + " [km2]\n"
                  + "Milla cuadrado: " + str(cantidad / (2.59 * (10 ** 12))) + " [MI2]\n"
                  + "Hectárea: " + str(cantidad / (10 ** 10)) + " [ha]\n"
                    + "\n")

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato02)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "5":
            cantidad = float(input("Digite la cantidad de dicho area: "))
            print("CANTIDAD INGRESADA:   |  " + str(cantidad) + "  [km2]  |\n"
                    + "\n"
                    + "Equivalente a: \n"
                    + "\n"
                  + "Centímetro cuadrado: " + str(cantidad * (10 ** 10)) + " [cm2]\n"
                  + "Decímetro cuadrado: " + str(cantidad * (10 ** 8)) + " [dm2]\n"
                  + "Metro cuadrado: " + str(cantidad * (10 ** 6)) + " [m2]\n"
                  + "Milimetro cuadrado: " + str(cantidad * (10 ** 12)) + " [mm2]\n"
                    + "Milla cuadrado: " + str(cantidad / 2.59) + " [MI2]\n"
                  + "Hectárea: " + str(cantidad * 100) + " [ha]\n"
                    + "\n")

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato02)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "6":
            cantidad = float(input("Digite la cantidad de dicho area: "))
            print("CANTIDAD INGRESADA:   |  " + str(cantidad) + "  [MI2]  |\n"
                    + "\n"
                    + "Equivalente a: \n"
                    + "\n"
                  + "Centímetro cuadrado: " + str(cantidad * (2.59 * (10 ** 10))) + " [cm2]\n"
                  + "Decímetro cuadrado: " + str(cantidad * (2.59 * (10 ** 8))) + " [dm2]\n"
                  + "Metro cuadrado: " + str(cantidad * (2.59 * (10 ** 6))) + " [m2]\n"
                  + "Milimetro cuadrado: " + str(cantidad * 2.59 * (10 ** 12)) + " [mm2]\n"
                  + "Kilometro cuadrado: " + str(cantidad * 2.59) + " [km2]\n"
                  + "Hectárea: " + str(cantidad * 259) + " [ha]\n"
                    + "\n")

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato02)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()


        elif opcion == "7":
            cantidad = float(input("Digite la cantidad de dicho area: "))
            print("CANTIDAD INGRESADA:   |  " + str(cantidad) + "  [ha]  |\n"
                    + "\n"
                    + "Equivalente a: \n"
                    + "\n"
                  + "Centímetro cuadrado: " + str(cantidad * (10 ** 8)) + " [cm^2]\n"
                  + "Decímetro cuadrado: " + str(cantidad * (10 ** 6)) + " [dm^2]\n"
                  + "Milimetro cuadrado: " + str(cantidad * (10 ** 10)) + " [mm^2]\n"
                  + "Metro cuadrado: " + str(cantidad * 10000) + " [m^2]\n"
                  + "Milimetro cuadrado: " + str(cantidad * (10 ** 10)) + " [mm^2]\n"
                    + "Kilometro cuadrado: " + str(cantidad / 100) + " [km^2]\n"
                    + "\n")

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=cantidad, tipo_dato_ingresado=tipo_dato02)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()

        elif opcion == "8":
            self.menuFisica()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            self.menuFisica()


    def cTemperatura(self, entrada):
        tipo_dato03 = "Temperatura"
        opcion = input("-----------------------------------\n"
                    + "ELIJA LA TEMPERATURA INICIAL\n-----------------------------------\n"
                    + "\n"
                    + "1: KELVIN [K]\n"
                    + "2: CELCIUS [ºC]\n"
                    + "3: FAHRENHEIT [ºF]\n"
                    + "4: MENU FISICA\n"
                    + "\nSeleccione una opción: ")

        if opcion == "1":
            temperatura = float(input("Digite la cantidad de dicha temperatura: "))
            print("CANTIDAD INGRESADA:   |  ", temperatura, "  [K]  |\n"
                + "\n"
                + "Equivalente a: \n"
                + "\n"
                + "Celsius: ", (temperatura - 273.15), " [ºC]\n"
                + "Fahrenheit: ", (temperatura - 273.15) * 9/5 + 32, " [ºF]\n"
                + "\n")

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=temperatura, tipo_dato_ingresado=tipo_dato03)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()


        elif opcion == "2":
            temperatura = float(input("Digite la cantidad de dicha temperatura: "))
            print("CANTIDAD INGRESADA:   |  ", temperatura, "  [ºC]  |\n"
                + "\n"
                + "Equivalente a: \n"
                + "\n"
                + "Kelvin: ", (temperatura + 273.15), " [K]\n"
                + "Fahrenheit: ", (temperatura * 9/5) + 32, " [ºF]\n"
                + "\n")
            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=temperatura, tipo_dato_ingresado=tipo_dato03)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()


        elif opcion == "3":
            temperatura = float(input("Digite la cantidad de dicha temperatura: "))
            print("TEMPERATURA INGRESADA:   |  ", temperatura, "  [ºF]  |\n"
                + "\n"
                + "Equivalente a: \n"
                + "\n"
                + "Kelvin: ", ((temperatura - 32) * 5/9 + 273.15), " [K]\n"
                + "Celcius: ", ((temperatura - 32) * 5/9), " [ºC]\n"
                + "\n")

            calculadoraFisica1 = CalculadoraFisica(numero_ingresado=temperatura, tipo_dato_ingresado=tipo_dato03)
            calculo_insertado = CalculadoraFisicaDAO.insertar(calculadoraFisica1)

            input("PRESIONE ENTER PARA CONTINUAR\n")
            self.menuFisica()


        elif opcion == "4":
            self.menuFisica()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            self.menuFisica()



calculadora = CalculadoraFisica()
# calculadora.menuFisica()