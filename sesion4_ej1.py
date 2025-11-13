import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Sesión 4 - Ejercicio 1: Rebote Acelerado")

# --- Colores ---
COLOR_FONDO = (10, 10, 30)
COLOR_CIRCULO = (255, 100, 100)

# --- Configuración del Círculo ---
RADIO = 25
# Usamos flotantes para la posición para que la aceleración 0.1 funcione
pos_x_f = float(ANCHO_VENTANA // 2)
pos_y_f = float(ALTO_VENTANA // 2)

# Creamos un Rect para manejar las colisiones fácilmente
# Su posición se actualizará desde las variables flotantes
rect_circulo = pygame.Rect(pos_x_f - RADIO, pos_y_f - RADIO, RADIO * 2, RADIO * 2)

# --- Configuración de velocidad ---
velocidad_x = 4.0
velocidad_y = 4.0

# --- Control de Tiempo ---
# Usa pygame.time.Clock para mantener 60 FPS 
reloj = pygame.time.Clock()

# --- Bucle principal del "juego" ---
ejecutando = True
while ejecutando:
    
    # Controlar la velocidad del bucle (60 FPS)
    reloj.tick(60)

    # 2. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    # 3. Lógica de Movimiento
    # Actualizamos las posiciones flotantes con la velocidad
    pos_x_f += velocidad_x
    pos_y_f += velocidad_y
    
    # Actualizamos el centro del Rect (redondeando a enteros)
    rect_circulo.centerx = int(pos_x_f)
    rect_circulo.centery = int(pos_y_f)

    # 4. Lógica de Colisión (Rebote)
    
    # Rebote en bordes horizontales (Izquierda / Derecha)
    if rect_circulo.left < 0 or rect_circulo.right > ANCHO_VENTANA:
        velocidad_x *= -1 # Invertir dirección
        
        # --- Lógica de Aceleración ---
        # Incrementa velocidad_x en 0.1 cada vez que rebota [cite: 8]
        if velocidad_x > 0:
            velocidad_x += 0.1
        else:
            velocidad_x -= 0.1
        print(f"¡Rebote horizontal! Nueva velocidad_x: {velocidad_x:.1f}")

    # Rebote en bordes verticales (Arriba / Abajo)
    if rect_circulo.top < 0 or rect_circulo.bottom > ALTO_VENTANA:
        velocidad_y *= -1 # Invertir dirección

    # 5. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)
    pygame.draw.circle(pantalla, COLOR_CIRCULO, rect_circulo.center, RADIO)

    # 6. Actualizar la pantalla
    pygame.display.flip()

# 7. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()