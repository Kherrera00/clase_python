from cargardatos import *

archivo = input("Nombre del archivo de datos?: ")
load_csv_py(archivo)

def camu (comu):
    return "atraco" > 1000

comu_filtrada = list(filter(camu, archivo))

#comu_filtrada = list(filter(lambda x: x["atraco"] > 1000, archivo))
print(comu_filtrada)