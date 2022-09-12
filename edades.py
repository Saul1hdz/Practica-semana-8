# miembros
# Saul Oswaldo Lopez Hernandez
# Fatima del Carmen Ayala Santos
# Naser Audeli Claros Rivera

#La edad se calculara a partir de su fecha de nacimiento 
from datetime import date
import datetime

def calcular(anio):
    date = datetime.date.today()
    actual_year = round(int(date.strftime("%Y")),0)
    resultado = actual_year - anio


    return resultado


