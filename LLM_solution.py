import math

def suma_cuadrados(N):
    """
    Calcula la suma de los cuadrados perfectos menores o iguales a N
    """
    limite = int(math.sqrt(N))  # El límite es la raíz cuadrada de N
    suma = 0
    for i in range(1, limite + 1):
        suma += i ** 2
    return suma % 1234567891  # Devuelve la suma módulo 1234567891

T = int(input())  # Lee el número de casos de prueba
for _ in range(T):
    N = int(input())  # Lee el valor de N
    print(suma_cuadrados(N))  # Imprime la respuesta
