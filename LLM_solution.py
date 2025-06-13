def suma_de_numeros_en_lista(N):
    """
    Calcula la suma de los n�meros que est�n en la lista despu�s de N pasos.
    
    :param N: El n�mero de pasos.
    :return: La suma de los n�meros en la lista m�dulo 1234567891.
    """
    MOD = 1234567891
    
    # Calcula el mayor entero k tal que k al cuadrado es menor o igual a N
    k = int(N ** 0.5)
    
    # Calcula la suma de los cuadrados perfectos menores o iguales a N
    suma = (k * (k + 1) * (2 * k + 1)) // 6
    
    return suma % MOD

# Lectura de la entrada
T = int(input())

# Procesamiento de cada caso de prueba
for _ in range(T):
    N = int(input())
    resultado = suma_de_numeros_en_lista(N)
    print(resultado)
