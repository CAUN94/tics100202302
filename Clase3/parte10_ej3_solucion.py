import math
import time

def funcion_cuadratica(dia, mes, anio):
    resultado = (anio**2) + (mes**3) - (dia*2)
    return resultado

fecha_actual = time.localtime()
dia_actual = fecha_actual.tm_mday
mes_actual = fecha_actual.tm_mon
anio_actual = fecha_actual.tm_year
print(f"Fecha actual: {dia_actual}/{mes_actual}/{anio_actual}")

resultado_funcion = funcion_cuadratica(dia_actual, mes_actual, anio_actual)
print(f"El resultado de la función cuadrática es: {resultado_funcion}")
