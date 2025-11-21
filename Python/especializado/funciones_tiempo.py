#Funciones de tiempo 

#Soon funciones que nos permiten trabajar con fechas y horas en Python.

import time as tm

actualTm = tm.localtime()
print("Tiempo actual:", actualTm)


#Saquemos el año, mes y día actual
year = actualTm.tm_year
month = actualTm.tm_mon
day = actualTm.tm_mday
print("Año:", year)
print("Mes:", month)
print("Dia:", day)

#construir una fecha específica

specific_date = tm.struct_time((2023, 12, 25, 0, 0, 0, 0, 0, -1))
print("Fecha específica:", specific_date)

"""
    +------------------------------------------------------------+
    |           Propiedades de la estructura de tiempo           |
    +------------+-----------------------------------------------+
    | Propiedad  | Descripción                                   |
    +------------+-----------------------------------------------+
    | tm_year    | Año (por ejemplo, 2024).                      |
    | tm_mon     | Mes del año (1-12).                           |
    | tm_mday    | Día del mes (1-31).                           |
    | tm_hour    | Hora (0-23).                                  |
    | tm_min     | Minuto (0-59).                                |
    | tm_sec     | Segundo (0-61, permite 60 y 61 para segundos  |
    |            | intercalares).                                |
    | tm_wday    | Día de la semana (0-6, donde 0 es lunes).     |
    | tm_yday    | Día del año (1-366, donde 1 es 1 de enero).   |
    | tm_isdst   | Horario de verano (1 si está en efecto, 0 si  |
    |            | no, -1 si no se sabe).                        |
    +------------+-----------------------------------------------+
"""

#Formatear fechas y horas
formatted_time = tm.strftime("%Y-%m-%d %H:%M:%S", actualTm)
print("Fecha y hora formateada:", formatted_time)