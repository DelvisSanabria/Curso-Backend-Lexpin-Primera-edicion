#Ejercicios Medios
#Ahora, te doy un problema y tú debes escribir la línea de código (la condición lógica) para resolverlo.

""" 1. Acceso a un concierto
Un usuario puede entrar a un concierto si tiene 18 años o más, y tiene un boleto (tiene_boleto es True).

Variables: """

edad = 20
tiene_boleto = True
puede_entrar = (edad >= 18) and (tiene_boleto == True)
print(puede_entrar)

""" 2. Beca universitaria
Un estudiante califica para una beca si su promedio (promedio) es 9 o más, o si vive a más de 50 km de la universidad (distancia_km).

Variables: """

promedio = 8.5
distancia_km = 60
califica_beca = (promedio >= 9) or (distancia_km > 50)
print(califica_beca)

""" 3. Acceso a sistema (Admin)
Un usuario puede acceder a una sección de "admin" si su rol es "admin" o si es un "editor" y está activo (esta_activo).

Variables: """

rol = "editor"
esta_activo = True

tiene_acceso_admin = (rol == "admin") or (rol == "editor" and esta_activo == True)

print(tiene_acceso_admin)

""" 4. Fuera de rango (Usando not)
Queremos saber si una temperatura (temp) está fuera del rango "seguro", que es de 20 a 30 grados. Es decir, es True si hace demasiado frío (menos de 20) o demasiado calor (más de 30).

Pista: A veces es más fácil definir el rango "seguro" y luego negarlo con not.

Variables:
 """

temp = 35
es_temperatura_peligrosa = (temp < 20) or (temp > 30)
print(es_temperatura_peligrosa)