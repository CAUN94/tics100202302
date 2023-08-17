# Ejercicio: Cambio Aleatorio de Tamaño y Posición de Cuadrados en Pygame

# En este ejercicio, vamos a utilizar el módulo Pygame para crear una interfaz gráfica en la que se mostrarán tres cuadrados de distintos colores en una ventana. La particularidad de este ejercicio es que el tamaño y la posición de los cuadrados cambiarán de forma aleatoria en cada actualización, con una pausa de 3 segundos entre cada actualización. A lo largo de este ejercicio, aprenderás a:

#     Importar el módulo Pygame y configurar una ventana.
#     Dibujar cuadrados en la ventana.
#     Generar números aleatorios para cambiar el tamaño y la posición de los cuadrados.
#     Cambiar los colores de los cuadrados.
#     Utilizar la función time.sleep() para crear pausas entre actualizaciones.
#     Mantener la ventana abierta y actualizar los cuadrados de forma continua.

# Recomendación del Paso a Paso:

#     Importa el módulo pygame y configura una ventana con un ancho de 800 y un alto de 600 píxeles. Asigna a la ventana el título "Cuadrados Aleatorios".

#     Define tres colores diferentes que usarás para los cuadrados. Puedes crear variables para almacenar los valores de los colores en formato RGB.

#     Crea un bucle principal infinito para controlar la actualización continua de los cuadrados.

#     Dentro del bucle principal, llena la ventana con un color de fondo blanco utilizando ventana.fill((255, 255, 255)).

#     Genera tamaños aleatorios para los cuadrados utilizando random.randint() y también posiciones aleatorias para los cuadrados dentro de la ventana.

#     Dibuja los cuadrados en la ventana utilizando la función pygame.draw.rect() y los valores aleatorios generados.

#     Utiliza la función time.sleep(3) para crear una pausa de 3 segundos entre actualizaciones.

#     Actualiza la ventana utilizando pygame.display.update() para mostrar los cuadrados con sus nuevos tamaños y posiciones.

#     Mantén la ventana abierta y actualizada para que los cuadrados cambien de tamaño y posición de forma continua con pausas de 3 segundos entre actualizaciones.

# Nota: Asegúrate de utilizar las funciones y técnicas que hemos aprendido en la introducción a Pygame para completar este ejercicio. ¡Diviértete experimentando con los cambios aleatorios en los cuadrados y las pausas entre actualizaciones!