from capa_datos_.CalculadoraRegular import CalculadoraRegular
from capa_datos_.calculadoraRegularDao import CalculadoraRegularDAO

class CalculadoraRegularService:
    @staticmethod
    def calcular_operaciones():
        from capa_datos_.MenuPrincipal import MenuPrincipal  # Importación tardía
        numer = ""
        while numer.lower() != "salir":
            numer = input("Digite una operación: ")
            poss1 = (numer.find("+")) + 1
            poss2 = (numer.find("-")) + 1
            poss3 = (numer.find("*")) + 1
            poss4 = (numer.find("/")) + 1
            if poss1 > 0:
                numero1 = float(numer[:poss1-1])
                numero2 = float(numer[poss1:])
                resultado = numero1 + numero2
                print(resultado)
                calculadoraRegular1 = CalculadoraRegular(numero_ingresado=numer, resultado=resultado)
                CalculadoraRegularDAO.insertar(calculadoraRegular1)
            if poss2 > 0:
                numero1 = float(numer[:poss2-1])
                numero2 = float(numer[poss2:])
                resultado = numero1 - numero2
                print(resultado)
                calculadoraRegular1 = CalculadoraRegular(numero_ingresado=numer, resultado=resultado)
                CalculadoraRegularDAO.insertar(calculadoraRegular1)
            if poss3 > 0:
                numero1 = float(numer[:poss3-1])
                numero2 = float(numer[poss3:])
                resultado = numero1 * numero2
                print(resultado)
                calculadoraRegular1 = CalculadoraRegular(numero_ingresado=numer, resultado=resultado)
                CalculadoraRegularDAO.insertar(calculadoraRegular1)
            if poss4 > 0:
                numero1 = float(numer[:poss4 - 1])
                numero2 = float(numer[poss4:])
                resultado = numero1 / numero2
                print(resultado)
                calculadoraRegular1 = CalculadoraRegular(numero_ingresado=numer, resultado=resultado)
                CalculadoraRegularDAO.insertar(calculadoraRegular1)
        MenuPrincipal.menuPrincipal()
