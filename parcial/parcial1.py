from functools import reduce

print("Bienvenido")

valores = int (input("Por favor define el tamaño de la lista: "))

listareal = list(range(0,valores))

print(listareal)

def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  
#num = listareal; 
#print("El factorial del numero ",num,"es", factorial(num))

mapeado = list(map(factorial,listareal))

print("El factorial de la lista es", mapeado)

print("El valor reducido es  : ", end="")
print(reduce(lambda a, b: a+b, mapeado))

print("El elemento de mayor valor es  : ", end="")
print(reduce(lambda a, b: a if a > b else b, mapeado))