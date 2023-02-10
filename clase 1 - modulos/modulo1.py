
#funcion (objetos)

def validar_prestamo(ingresos_mensuales, bienes_raices):
  if ingresos_mensuales > 1200000 and bienes_raices == True:
    return "Felicidades tienes el prestamo"
  else:
    return "Lo sentimos vuelve pronto"