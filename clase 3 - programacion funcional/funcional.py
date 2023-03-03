"""
def suma (a,b):
    return a+b

suma2 = suma

print(int(suma(3,5)))
"""

lista_des = ["diego", "edinson","juan F","carlos","angie"]

lista_des_op = list(map(str.upper, lista_des)) #se convierte en una lista
#lista_des_op2 = list(map(str.lower, lista_des))

#print(lista_des_op2)
print(lista_des_op)

#map recibe una funcion y una lista

#filter - es una funcion booleana

def long (x):
    return len(x) >= 7

lista_des_sh = list(filter(long, lista_des_op))

print(lista_des_sh)
