import math

# Leer el número de casos de prueba
T = int(input())

# Procesar cada caso de prueba
for _ in range(T):
    # Leer el valor de N
    N = int(input())
    
    # Calcular el número de cuadrados perfectos hasta N
    n = int(math.sqrt(N))
    
    # Calcular la suma de los cuadrados perfectos hasta N utilizando la fórmula
    suma = n*(n+1)*(2*n+1)//6
    
    # Imprimir el resultado módulo 1234567891
    print(suma % 1234567891)
