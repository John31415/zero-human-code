import math

def suma_cuadrados(N):
    """
    Calcula la suma de los cuadrados perfectos menores o iguales a N
    """
    limite = int(math.sqrt(N))  # El l�mite es la ra�z cuadrada de N
    suma = 0
    for i in range(1, limite + 1):
        suma += i ** 2
    return suma % 1234567891  # Devuelve la suma m�dulo 1234567891

T = int(input())  # Lee el n�mero de casos de prueba
for _ in range(T):
    N = int(input())  # Lee el valor de N
    print(suma_cuadrados(N))  # Imprime la respuesta
