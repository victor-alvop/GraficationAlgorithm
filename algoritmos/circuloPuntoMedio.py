import turtle

def dibujar_punto(x, y, cx, cy, lapiz):
    # Dibuja los puntos en los ocho octantes usando simetría
    puntos = [
        (x + cx, y + cy),
        (-x + cx, y + cy),
        (x + cx, -y + cy),
        (-x + cx, -y + cy),
        (y + cx, x + cy),
        (-y + cx, x + cy),
        (y + cx, -x + cy),
        (-y + cx, -x + cy)
    ]
    for punto in puntos:
        lapiz.goto(punto)
        lapiz.dot(3, "red")
        print(f"Coordenada: ({punto[0]}, {punto[1]})")

def dibujar_circulo_punto_medio(cx, cy, radio):
    # Configuración de la pantalla de turtle
    pantalla = turtle.Screen()
    pantalla.title("Círculo con Punto Medio y Turtle")
    pantalla.bgcolor("black")
    
    # Configuración del objeto turtle
    lapiz = turtle.Turtle()
    lapiz.speed(1)
    lapiz.penup()
    
    # Inicialización de variables
    x = 0
    y = radio
    p = 1 - radio  # Valor inicial de p (decision parameter)
    
    # Dibuja el primer conjunto de puntos
    dibujar_punto(x, y, cx, cy, lapiz)
    
    # Bucle para calcular todos los puntos en un octante
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        dibujar_punto(x, y, cx, cy, lapiz)
    
    # Mantener la ventana abierta hasta que se cierre manualmente
    pantalla.mainloop()

# Ejemplo de uso
dibujar_circulo_punto_medio(0, 0, 100)


'''
Explicación del Código:
Función dibujar_punto:

Esta función toma las coordenadas de un punto en el primer octante y las usa para calcular y dibujar los puntos correspondientes en los ocho octantes utilizando la simetría del círculo. Luego, dibuja esos puntos con turtle y los imprime en la consola.
Función dibujar_circulo_punto_medio:

Configuración de turtle: Se inicializa la pantalla y el objeto Turtle.
Variables iniciales:
x = 0 y y = radio son las coordenadas iniciales.
p = 1 - radio es el parámetro de decisión inicial que determina si el siguiente punto a dibujar está más cerca de la circunferencia.
Bucle de cálculo:
Se incrementa x en cada iteración.
Si p < 0, el siguiente punto está dentro de la circunferencia, por lo que solo se ajusta p.
Si p >= 0, el siguiente punto está fuera de la circunferencia, se disminuye y y se ajusta p.
Dibujo de puntos: En cada iteración, se llama a dibujar_punto para dibujar los puntos calculados.
Ejemplo de uso:

La función dibujar_circulo_punto_medio se llama con las coordenadas del centro (0, 0) y el radio 100. Esto dibujará un círculo centrado en (0, 0) con un radio de 100.
Notas:
El algoritmo de punto medio es eficiente porque solo utiliza operaciones con enteros, lo que lo hace rápido y preciso para gráficos rasterizados.
Este código dibuja un círculo utilizando la librería turtle, mostrando los cálculos de las coordenadas en cada paso.
'''