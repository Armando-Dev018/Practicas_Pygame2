import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Sesión 6 - Ejercicio 1: Colisión y Color")

# --- Colores ---
COLOR_FONDO = (0, 0, 0)
COLOR_JUGADOR_NORMAL = (255, 255, 255) # Blanco
COLOR_JUGADOR_COLISION = (0, 255, 0)   # Verde 
COLOR_OBJETIVO = (255, 0, 0)         # Rojo

# --- Configuración del Jugador ---
rect_jugador = pygame.Rect(375, 500, 50, 50) # (x, y, ancho, alto)
VELOCIDAD = 5
color_actual_jugador = COLOR_JUGADOR_NORMAL # Variable de estado

# --- Configuración del Objetivo ---
# Usamos un Rect para la colisión, aunque dibujemos un círculo
RADIO_OBJETIVO = 30
rect_objetivo = pygame.Rect(
    (ANCHO_VENTANA // 2) - RADIO_OBJETIVO,
    (ALTO_VENTANA // 2) - RADIO_OBJETIVO,
    RADIO_OBJETIVO * 2,
    RADIO_OBJETIVO * 2
)

# --- Control de Tiempo ---
reloj = pygame.time.Clock()

# --- Bucle principal del "juego" ---
ejecutando = True
while ejecutando:
    
    reloj.tick(60) # 60 FPS

    # 2. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    # 3. Lógica de Movimiento (Teclado)
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT] and rect_jugador.left > 0:
        rect_jugador.x -= VELOCIDAD
    if teclas[pygame.K_RIGHT] and rect_jugador.right < ANCHO_VENTANA:
        rect_jugador.x += VELOCIDAD
    if teclas[pygame.K_UP] and rect_jugador.top > 0:
        rect_jugador.y -= VELOCIDAD
    if teclas[pygame.K_DOWN] and rect_jugador.bottom < ALTO_VENTANA:
        rect_jugador.y += VELOCIDAD

    # 4. Lógica de Colisión
    
    # Comprobamos si los dos rectángulos se superponen
    if rect_jugador.colliderect(rect_objetivo):
        # Si hay colisión, cambiar color a verde 
        color_actual_jugador = COLOR_JUGADOR_COLISION
    else:
        # Si no hay colisión, volver al color normal
        color_actual_jugador = COLOR_JUGADOR_NORMAL

    # 5. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar el objetivo (como un círculo, usando el centro del rect)
    pygame.draw.circle(pantalla, COLOR_OBJETIVO, rect_objetivo.center, RADIO_OBJETIVO)
    
    # Dibujar al jugador con su color actual
    pygame.draw.rect(pantalla, color_actual_jugador, rect_jugador)

    # 6. Actualizar la pantalla
    pygame.display.flip()

# 7. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()