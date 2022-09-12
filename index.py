# miembros
# Saul Oswaldo Lopez Hernandez
# Fatima del Carmen Ayala Santos
# Naser Audeli Claros Rivera

import math
from unittest import result
from unittest.util import _MAX_LENGTH
from xmlrpc.client import MAXINT 
import edades
import dui
math.e

anio = int(input("Ingrese el año de su nacimiento: "))

resultado = edades.calcular(anio)
print(f" Su edad es de ", resultado, " años")

if resultado >= 18:
    print("Eres mayor de Edad")
    if resultado >= 18:


        duis = input("Ingrese su numero de DUI: ")
        resulta = dui.carac(duis)
        
else:
    print("Eres menor de Edad")


