import turtle

def dibujar_linea_dda(x1, y1, x2, y2):
    # Configuración de la pantalla de turtle
    pantalla = turtle.Screen()
    pantalla.title("Línea con DDA y Turtle")
    pantalla.bgcolor("black")
    
    # Configuración del objeto turtle
    lapiz = turtle.Turtle()
    lapiz.speed(1)
    lapiz.penup()
    lapiz.goto(x1, y1)
    lapiz.pendown()
    
    # Calcula las diferencias en x y y
    dx = x2 - x1
    dy = y2 - y1
    
    # Determina el número de pasos necesarios
    pasos = max(abs(dx), abs(dy))
    
    # Calcula los incrementos en cada paso
    x_incremento = dx / pasos
    y_incremento = dy / pasos
    
    # Variables iniciales
    x = x1
    y = y1
    
    # Dibujar la línea y mostrar coordenadas
    for i in range(int(pasos) + 1):
        print(f"Coordenada {i}: ({x:.2f}, {y:.2f})")
        lapiz.goto(round(x), round(y))
        lapiz.dot(3, "red")
        x += x_incremento
        y += y_incremento
    
    # Mantener la ventana abierta hasta que se cierre manualmente
    pantalla.mainloop()

# Ejemplo de uso
dibujar_linea_dda(-100, -100, 100, 50)


'''
Explicación del Código:
Importación de turtle:

Se importa la librería turtle para crear gráficos.
Función dibujar_linea_dda:

Configuración de la pantalla y el objeto turtle: Se inicializa la pantalla de turtle y se configura un objeto Turtle para el dibujo.
Cálculo de diferencias (dx y dy): Se calculan las diferencias en las coordenadas x e y entre los puntos inicial y final.
Determinación del número de pasos (pasos): Se determina el número de pasos necesarios como el valor máximo absoluto entre dx y dy.
Cálculo de los incrementos por paso: Se calculan los incrementos en las coordenadas x e y por cada paso.
Inicialización de las coordenadas: Se empiezan las coordenadas desde el punto inicial (x1, y1).
Dibujo de la línea y muestra de las coordenadas: Un bucle itera a través de cada paso, calcula las coordenadas, imprime en la consola y dibuja un punto rojo en la posición correspondiente utilizando turtle.
Mantenimiento de la ventana abierta: Se mantiene la ventana abierta para que se pueda visualizar el resultado.
Uso de la Función:

Se llama a la función dibujar_linea_dda con las coordenadas de los puntos inicial y final de la línea. En este ejemplo, se dibuja una línea desde (-100, -100) hasta (100, 50).
Este código implementa el algoritmo DDA para dibujar una línea y es adecuado para aprender cómo funcionan las interpolaciones lineales en gráficos rasterizados.
'''