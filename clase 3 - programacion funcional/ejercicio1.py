listareal = list(range(1,101))

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