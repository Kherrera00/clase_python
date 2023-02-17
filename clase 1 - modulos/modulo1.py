
#funcion (objetos)

def validar_prestamo(ingresos_mensuales, bienes_raices):
  if ingresos_mensuales > 1200000 and bienes_raices == True:
    return "Felicidades tienes el prestamo"
  #elif ingresos_mensuales < 1200000 and bienes_raices == False or bienes_raices == True:
  else:
    return "Lo sentimos vuelve pronto"