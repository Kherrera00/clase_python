import modulo1#importamos el archivo


#pedir datos

#usuario

ingresos_mensuales = int (input("¿De cuanto son sus ingresos mensuales? "))


#bienes raices

bienes_raices = bool (input("¿Tienes bienes raices? "))

#llama la funcion

tiene_prestamos = modulo1.validar_prestamo (ingresos_mensuales, bienes_raices)

print(tiene_prestamos)


lista_datos = [[100000, "SI"], [900000, "SI"], [20000000, "NO"]]

for elemento in lista_datos:
  print(modulo1.validar_prestamo(elemento[0], elemento[1]))