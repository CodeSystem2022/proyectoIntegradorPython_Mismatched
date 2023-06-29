from capa_datos_.CalculadoraRegular import CalculadoraRegular
from capa_datos_.calculadoraRegularDao import CalculadoraRegularDAO
from logger_base import log

class CalculadoraRegularService:
    @staticmethod
    def calcular_operaciones():
        while numer != "salir":
            numer = input("Digite una operación: ")
            poss1 = (numer.find("+")) + 1
            poss2 = (numer.find("-")) + 1
            poss3 = (numer.find("*")) + 1
            poss4 = (numer.find("/")) + 1
            resultado = None
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

# CalculadoraRegularService.calcular_operaciones()


# def calcular():
#     # mP = MenuPrincipal()
#     numer = ""
#
#     while numer != "salir":
#         try:
#             # Pedimos valor al usuario
#             numer = input("Ingrese la operacion a realizar o 'Salir' para regresar al menu principal: ").lower()
#
#             # Si el string numer contiene el valor indicado, entramos en el if, en este caso la suma
#             if "+" in numer:
#                 partes = numer.split("+")  # Aquí dividimos el array en el operador necesario
#                 parte1 = partes[0]
#                 parte2 = partes[1]
#
#                 num1 = float(parte1)
#                 num2 = float(parte2)
#                 suma = num1 + num2
#
#                 print(suma)
#
#             # Si el string numer contiene el valor indicado, entramos en el if, en este caso el producto
#             if "*" in numer:
#                 partes = numer.split("*")  # Aquí dividimos el array en el operador necesario
#                 parte1 = partes[0]
#                 parte2 = partes[1]
#
#                 num1 = float(parte1)
#                 num2 = float(parte2)
#                 producto = num1 * num2
#
#                 print(producto)
#
#             # Si el string numer contiene el valor indicado, entramos en el if, en este caso la division
#             if "/" in numer:
#                 partes = numer.split("/")  # Aquí dividimos el array en el operador necesario
#                 parte1 = partes[0]
#                 parte2 = partes[1]
#
#                 num1 = float(parte1)
#                 num2 = float(parte2)
#                 division = num1 / num2
#
#                 print(division)
#
#             # Si el string numer contiene el valor indicado, entramos en el if, en este caso la resta
#             if "-" in numer:
#                 partes = numer.split("-")  # Aquí dividimos el array en el operador necesario
#
#                 # Cuando entramos con una resta simple, entra por aquí
#                 if len(partes) <= 2:
#                     parte1 = partes[0]
#                     parte2 = partes[1]
#                     num1 = float(parte1)
#                     num2 = float(parte2)
#                     resta = num1 - num2
#                 else:  # Aquí se contempla la resta de 2 números negativos
#                     parte1 = partes[0]
#                     parte2 = partes[1]
#                     parte3 = partes[2]
#
#                     if parte1.strip() == "":
#                         parte1 = "0"
#
#                     num1 = float(parte1)
#                     num2 = float(parte2)
#                     num3 = float(parte3)
#                     resta = num1 - num2 - num3
#
#                 print(resta)
#
#         except (ValueError, IndexError):
#             pass
# mP.MenuPrincipal()