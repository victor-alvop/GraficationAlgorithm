import turtle
import math

def dibujar_circulo_dda(cx, cy, radio):
    # Configuración de la pantalla de turtle
    pantalla = turtle.Screen()
    pantalla.title("Círculo con DDA y Turtle")
    pantalla.bgcolor("black")
    
    # Configuración del objeto turtle
    lapiz = turtle.Turtle()
    lapiz.speed(1)
    lapiz.penup()
    
    # Inicialización de variables
    x = radio
    y = 0
    theta = 0
    pasos = 100  # Número de pasos, puedes ajustar este valor
    incremento_theta = (2 * math.pi) / pasos
    
    # Dibujar el círculo y mostrar coordenadas
    for i in range(pasos + 1):
        x = radio * math.cos(theta)
        y = radio * math.sin(theta)
        
        # Coordenadas reales trasladas al centro del círculo
        real_x = cx + x
        real_y = cy + y
        
        # Dibujar el punto y mostrar las coordenadas
        print(f"Coordenada {i}: ({real_x:.2f}, {real_y:.2f})")
        lapiz.goto(round(real_x), round(real_y))
        lapiz.dot(3, "red")
        
        # Incrementar el ángulo theta
        theta += incremento_theta
    
    # Mantener la ventana abierta hasta que se cierre manualmente
    pantalla.mainloop()

# Ejemplo de uso
dibujar_circulo_dda(0, 0, 100)

'''
Explicación del Código:
Importación de Librerías:

turtle para gráficos y math para funciones matemáticas como cos y sin.
Función dibujar_circulo_dda:

Configuración de la pantalla y el objeto turtle: Se configura la pantalla y el objeto Turtle para el dibujo.
Inicialización de variables: Se inicializan las variables para las coordenadas (x, y), el radio del círculo, el ángulo theta y el número de pasos pasos para definir la precisión del círculo.
Cálculo de incremento de ángulo: Se calcula incremento_theta, que es el ángulo que se incrementará en cada paso.
Bucle de trazado: Un bucle se utiliza para calcular las coordenadas (x, y) del círculo en cada paso utilizando las funciones cos y sin. Las coordenadas se trasladan al centro del círculo (cx, cy), y luego se dibuja el punto en esas coordenadas utilizando turtle.
Impresión de las coordenadas: Las coordenadas calculadas se imprimen en la consola.
Uso de la Función:

La función se llama con el centro del círculo (0, 0) y el radio 100. Puedes cambiar estos valores para dibujar círculos en diferentes posiciones y tamaños.
Este algoritmo traza puntos a lo largo del perímetro del círculo utilizando la fórmula paramétrica del círculo: 
𝑥
=
𝑟
cos
⁡
(
𝜃
)
x=rcos(θ) y 
𝑦
=
𝑟
sin
⁡
(
𝜃
)
y=rsin(θ). El uso de DDA en este contexto se aplica al incremento uniforme del ángulo para obtener puntos a lo largo de la circunferencia del círculo.
'''
