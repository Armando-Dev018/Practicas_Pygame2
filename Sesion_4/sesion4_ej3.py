import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Sesión 4 - Ejercicio 3: Simulación de Gravedad")

# --- Colores ---
COLOR_FONDO = (10, 10, 30)
COLOR_CIRCULO = (200, 200, 20) # Amarillo
COLOR_SUELO = (100, 100, 100)  # Gris

# --- Constantes de Física ---
# Aceleración de gravedad (píxeles por frame al cuadrado)
GRAVEDAD = 0.5 
# Pérdida de energía en el rebote (80% se conserva, 20% se pierde)
PERDIDA_ENERGIA = 0.8 

# --- Configuración del Círculo (Pelota) ---
RADIO = 30
# Usamos flotantes para la posición y velocidad
pos_x_f = float(ANCHO_VENTANA // 2)
pos_y_f = float(50) # Empezar cerca de la parte superior
velocidad_y = 0.0   # Empezar sin velocidad vertical

# Rect para posición (se actualizará desde los flotantes)
rect_circulo = pygame.Rect(pos_x_f - RADIO, pos_y_f - RADIO, RADIO * 2, RADIO * 2)

# --- Control de Tiempo ---
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

    # 3. Lógica de Física (Gravedad)
    
    # 1. Aplicar aceleración (gravedad) a la velocidad
    velocidad_y += GRAVEDAD
    
    # 2. Aplicar velocidad a la posición
    pos_y_f += velocidad_y
    
    # 3. Actualizar el Rect
    rect_circulo.centery = int(pos_y_f)

    # 4. Lógica de Colisión (Rebote en el suelo)
    
    # Comprobar si la parte inferior del círculo golpea el suelo
    if rect_circulo.bottom >= ALTO_VENTANA:
        
        # Corrección de posición:
        # Si se pasó del suelo, lo colocamos exactamente en el suelo
        # para evitar que se "hunda" en el siguiente frame.
        rect_circulo.bottom = ALTO_VENTANA
        pos_y_f = float(rect_circulo.centery)
        
        # Invertir la dirección de la velocidad
        velocidad_y *= -1
        
        # Aplicar pérdida de energía (reducir velocidad en 20%)
        velocidad_y *= PERDIDA_ENERGIA
        
        # (Opcional) Detener si la velocidad es muy baja
        if abs(velocidad_y) < 1:
            velocidad_y = 0


    # 5. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar el suelo
    pygame.draw.rect(pantalla, COLOR_SUELO, (0, ALTO_VENTANA - 10, ANCHO_VENTANA, 10))
    
    # Dibujar el círculo
    pygame.draw.circle(pantalla, COLOR_CIRCULO, rect_circulo.center, RADIO)

    # 6. Actualizar la pantalla
    pygame.display.flip()

# 7. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()