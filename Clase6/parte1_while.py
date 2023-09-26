# Si bien en clases anteriores utilizamos los ciclos 'for' para repetir un bloque de codigo una cantidad finita de veces, 
# los ciclos 'while' se utilizan para repetir un bloque de código mientras se cumpla una condición.
# La condición se evalúa antes de cada iteración. Si la condición es verdadera, el ciclo continúa; de lo contrario, 
# se detiene.

# Ejemplo: Contador Regresivo para un Lanzamiento de Cohetes
# Supongamos que estamos lanzando un cohete y queremos hacer un contador regresivo desde 10 hasta el despegue:

import time
contador = 10

while contador >= 1:  # Mientras el contador sea mayor o igual a 1
    print(contador)
    contador -= 1     # Disminuir el contador en 1 en cada iteración
    time.sleep(1)

print("¡Despegue del cohete!")

# En este ejemplo, utilizamos un ciclo 'while' para contar hacia atrás desde 10 hasta 1.
# La condición 'contador >= 1' se verifica antes de cada iteración. Mientras 'contador' sea mayor o igual a 1, 
# el ciclo continuará.
# En cada iteración, imprimimos el valor de 'contador' y luego disminuimos su valor en 1 con 'contador -= 1'.
# Cuando 'contador' llega a 0, la condición se vuelve falsa y el ciclo se detiene.
# Esto simula un contador regresivo comúnmente utilizado en lanzamientos de cohetes u otras situaciones de cuenta regresiva.