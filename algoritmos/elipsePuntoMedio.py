import turtle

def dibujar_punto(x, y, cx, cy, lapiz):
    # Dibuja los puntos en los cuatro cuadrantes usando simetría
    puntos = [
        (x + cx, y + cy),
        (-x + cx, y + cy),
        (x + cx, -y + cy),
        (-x + cx, -y + cy)
    ]
    for punto in puntos:
        lapiz.goto(punto)
        lapiz.dot(3, "red")
        print(f"Coordenada: ({punto[0]}, {punto[1]})")

def dibujar_elipse_punto_medio(cx, cy, rx, ry):
    # Configuración de la pantalla de turtle
    pantalla = turtle.Screen()
    pantalla.title("Elipse con Punto Medio y Turtle")
    pantalla.bgcolor("black")
    
    # Configuración del objeto turtle
    lapiz = turtle.Turtle()
    lapiz.speed(1)
    lapiz.penup()
    
    # Región 1
    x = 0
    y = ry
    p1 = ry**2 - rx**2 * ry + 0.25 * rx**2
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y
    
    while dx < dy:
        dibujar_punto(x, y, cx, cy, lapiz)
        if p1 < 0:
            x += 1
            dx += 2 * ry**2
            p1 += dx + ry**2
        else:
            x += 1
            y -= 1
            dx += 2 * ry**2
            dy -= 2 * rx**2
            p1 += dx - dy + ry**2
    
    # Región 2
    p2 = ry**2 * (x + 0.5)**2 + rx**2 * (y - 1)**2 - rx**2 * ry**2
    
    while y >= 0:
        dibujar_punto(x, y, cx, cy, lapiz)
        if p2 > 0:
            y -= 1
            dy -= 2 * rx**2
            p2 += rx**2 - dy
        else:
            y -= 1
            x += 1
            dx += 2 * ry**2
            dy -= 2 * rx**2
            p2 += dx - dy + rx**2
    
    # Mantener la ventana abierta hasta que se cierre manualmente
    pantalla.mainloop()

# Ejemplo de uso
dibujar_elipse_punto_medio(0, 0, 100, 50)


'''
Explicación del Código:
Función dibujar_punto:

Dibuja los puntos calculados en los cuatro cuadrantes de la elipse usando simetría.
Para cada punto (x, y) calculado, se dibujan también los puntos (-x, y), (x, -y) y (-x, -y).
Función dibujar_elipse_punto_medio:

Configuración de turtle: Se configura la pantalla y el objeto Turtle.
Región 1:
Se inicia con el punto (0, ry) y se calcula el parámetro de decisión p1.
Se itera aumentando x y ajustando y según el valor de p1 hasta que dx (el cambio en x) sea menor que dy (el cambio en y), lo que marca el fin de la región 1.
Región 2:
Inicia con el parámetro de decisión p2.
Se itera disminuyendo y y ajustando x según el valor de p2 hasta que y sea negativo, lo que marca el fin de la región 2.
Dibujo de puntos: En cada iteración, se llama a dibujar_punto para dibujar los puntos calculados.
Ejemplo de uso:

La función dibujar_elipse_punto_medio se llama con el centro de la elipse (0, 0), el radio horizontal 100 y el radio vertical 50. Puedes cambiar estos valores para dibujar elipses de diferentes tamaños y posiciones.
Notas:
El algoritmo de punto medio para elipses es una adaptación del algoritmo de punto medio para círculos y permite un trazado eficiente utilizando operaciones con enteros.
La función dibujar_punto se asegura de que se dibujen todos los puntos correspondientes a los cuadrantes de la elipse, manteniendo la simetría.
'''
