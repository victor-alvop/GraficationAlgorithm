import turtle

def dibujar_linea_bresenham(x1, y1, x2, y2):
    # Configuración de la pantalla de turtle
    pantalla = turtle.Screen()
    pantalla.title("Línea con Bresenham y Turtle")
    pantalla.bgcolor("black")
    
    # Configuración del objeto turtle
    lapiz = turtle.Turtle()
    lapiz.speed(1)
    lapiz.penup()
    lapiz.goto(x1, y1)
    lapiz.pendown()
    
    # Variables iniciales
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    err = dx - dy

    while True:
        # Dibujar y mostrar las coordenadas
        print(f"Coordenada: ({x}, {y})")
        lapiz.goto(x, y)
        lapiz.dot(3, "red")
        
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    
    # Mantener la ventana abierta hasta que se cierre manualmente
    pantalla.mainloop()

# Ejemplo de uso
dibujar_linea_bresenham(-100, -100, 100, 50)

'''
Explicación del Código:
Importación de turtle:

Se importa la librería turtle para poder dibujar gráficos.
Función dibujar_linea_bresenham:

Configuración de la pantalla y el objeto turtle: Se inicializa la pantalla de turtle y se configura un objeto Turtle para el dibujo.
Variables iniciales: Se establecen las variables iniciales para las coordenadas actuales (x, y), las diferencias absolutas en x y y (dx, dy), y las direcciones de los incrementos (sx, sy).
Cálculo del error inicial (err): Se calcula el valor inicial del error, que es dx - dy.
Bucle de trazado: Un bucle while se utiliza para trazar los puntos de la línea. En cada iteración, el punto actual se dibuja y se imprime en la consola. Luego, se ajustan las coordenadas x y y de acuerdo con el valor del error err y las direcciones sx y sy.
Condición de parada: El bucle se detiene cuando se alcanza el punto final (x2, y2).
Uso de la Función:

Se llama a la función dibujar_linea_bresenham con las coordenadas de los puntos inicial y final de la línea. En el ejemplo proporcionado, la línea se dibuja desde (-100, -100) hasta (100, 50).
Este código implementa el algoritmo de Bresenham para el trazado de líneas, que es más eficiente que el DDA en términos de uso de enteros y precisión. Es particularmente útil en gráficos de computadora donde se necesita evitar el uso de operaciones de punto flotante para mantener la precisión y eficiencia.
'''
