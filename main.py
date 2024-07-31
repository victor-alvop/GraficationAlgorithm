import turtle
import math


def mostrar_menu():
    print("\n*** Menú de opciones ***")
    print("1. Línea DDA")
    print("2. Línea Bressenham")
    print("3. Círculo DDA")
    print("4. Círculo Punto Medio")
    print("5. Elipse Punto Medio")
    print("6. Salir")

    # Fin funcion mosntrar menu 

def linea_dda(x1, y1, x2, y2):
    print("\n*** Has seleccionado Línea DDA ***")

    # Configuración de la pantalla de turtle
    pantalla = turtle.Screen()
    pantalla.title("Línea DDA")
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
    #pantalla.mainloop()
    pantalla.ontimer(pantalla.clearscreen, 3000)

    # Fin funcion linea DDA

def linea_bressenham(x1, y1, x2, y2):
    print("\n*** Has seleccionado Línea Bressenham ***")

    pantalla = turtle.Screen()
    pantalla.title("Línea con Bresenham")
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
    #pantalla.mainloop()
    pantalla.ontimer(pantalla.clearscreen, 3000)

    # Fin funcion Linea Bressenham

def circulo_dda(cx, cy, radio):
    print("\n*** Has seleccionado Círculo DDA ***")

    pantalla = turtle.Screen()
    pantalla.title("Círculo con DDA")
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
    #pantalla.mainloop()
    pantalla.ontimer(pantalla.clearscreen, 3000)

    # Fin funcion circulo DDA 

def dibujar_punto_circulo(x, y, cx, cy, lapiz):

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
    
    # Fin funcion dibujar circulo

def dibujar_circulo_punto_medio(cx, cy, radio):
    print("\n*** Has seleccionado Círculo Punto Medio ***")


    # Configuración de la pantalla de turtle
    pantalla = turtle.Screen()
    pantalla.title("Círculo con Punto Medio")
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
    dibujar_punto_circulo(x, y, cx, cy, lapiz)
    
    # Bucle para calcular todos los puntos en un octante
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        dibujar_punto_circulo(x, y, cx, cy, lapiz)
    
    # Mantener la ventana abierta hasta que se cierre manualmente
    #pantalla.mainloop()
    pantalla.ontimer(pantalla.clearscreen, 3000)

    # Fin funcion circulo punto medio

def dibujar_punto_elipse(x, y, cx, cy, lapiz):
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

    # Fin funcion dibujar punto elipse 

def dibujar_elipse_punto_medio(cx, cy, rx, ry):
    print("\n*** Has seleccionado Elipse Punto Medio *** ")

    # Configuración de la pantalla de turtle
    pantalla = turtle.Screen()
    pantalla.title("Elipse con Punto Medio")
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
        dibujar_punto_elipse(x, y, cx, cy, lapiz)
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
        dibujar_punto_elipse(x, y, cx, cy, lapiz)
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
    #pantalla.mainloop()
    pantalla.ontimer(pantalla.clearscreen, 3000)

    # Fin funcion dibujar elipse punto medio


############### FUNCION MAIN ###############
def main():

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == '1':
            x1 = int(input('\nIngresa X1: '))
            y1 = int(input('Ingresa Y1: '))
            x2 = int(input('Ingresa X2: '))
            y2 = int(input('Ingresa Y2: '))
            linea_dda(x1, y1, x2, y2)

        elif opcion == '2':
            x1 = int(input('\nIngresa X1: '))
            y1 = int(input('Ingresa Y1: '))
            x2 = int(input('Ingresa X2: '))
            y2 = int(input('Ingresa Y2: '))
            linea_bressenham(x1, y1, x2, y2)

        elif opcion == '3':
            cx = int(input('\nIngresa la coordenada X: '))
            cy = int(input('Ingresa la coordenada Y: '))
            radio = int(input('Ingresa el radio: '))
            circulo_dda(cx, cy, radio)

        elif opcion == '4':
            cx = int(input('\nIngresa la coordenada X: '))
            cy = int(input('Ingresa la coordenada Y: '))
            radio = int(input('Ingresa el radio: '))
            dibujar_circulo_punto_medio(cx, cy, radio)
    
        elif opcion == '5':
            cx = int(input('\nIngresa la coordenada X: '))
            cy = int(input('Ingresa la coordenada Y: '))
            rx = int(input('Ingresa el radio mayor: '))
            ry = int(input('Ingresa el radio menor: '))
            dibujar_elipse_punto_medio(cx, cy, rx, ry)             

        elif opcion == '6':
            print("\n\nSaliendo del programa...\n")
            break
        else:
            print("\n*** Opción no válida. Por favor, elige una opción del 1 al 4. ***\n")


if __name__ == "__main__":
    main()