import pandas as pd
import openpyxl

listareal = list(range(1,100))

def es_primo(num):
    """Función que comprueba si un número es primo"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numeros = listareal

numeros_primos = filter(es_primo, numeros)

numeros_primos = list(numeros_primos)

numeros_primos_str = map(str, numeros_primos)

print("Los números primos son: " + ", ".join(numeros_primos_str))


df = pd.DataFrame(numeros_primos)

# Especificar la ruta completa del archivo de Excel
ruta_archivo = 'C:/Users/kherr/OneDrive/Escritorio/Proyectos python/clase_python/datos.xlsx'

# Exportar el DataFrame a un archivo de Excel
df.to_excel(ruta_archivo, index=False)