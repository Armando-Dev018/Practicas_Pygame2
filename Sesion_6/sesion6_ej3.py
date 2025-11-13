import pygame
import sys
import random

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Sesión 6 - Ejercicio 3: Evitar Obstáculos")

# --- Colores ---
COLOR_FONDO = (10, 10, 10)
COLOR_JUGADOR = (50, 150, 255) # Azul
COLOR_OBSTACULO = (255, 50, 50) # Rojo

# --- Configuración del Jugador ---
rect_jugador = pygame.Rect(375, 500, 40, 40) # (x, y, ancho, alto)
VELOCIDAD_JUGADOR = 6

# --- Configuración de los Obstáculos ---
obstaculos = [] # Usaremos una lista para guardar los obstáculos
RADIO_OBSTACULO = 20

# Creamos 3 obstáculos y los añadimos a la lista
# Cada obstáculo será un diccionario para guardar su Rect y su velocidad
obstaculo_1 = {
    "rect": pygame.Rect(100, 100, RADIO_OBSTACULO * 2, RADIO_OBSTACULO * 2),
    "velocidad_x": 3
}
obstaculo_2 = {
    "rect": pygame.Rect(600, 250, RADIO_OBSTACULO * 2, RADIO_OBSTACULO * 2),
    "velocidad_x": -5 # Se mueve en la otra dirección
}
obstaculo_3 = {
    "rect": pygame.Rect(300, 400, RADIO_OBSTACULO * 2, RADIO_OBSTACULO * 2),
    "velocidad_x": 4
}

obstaculos.append(obstaculo_1)
obstaculos.append(obstaculo_2)
obstaculos.append(obstaculo_3)

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

    # 3. Lógica de Movimiento (Jugador)
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT] and rect_jugador.left > 0:
        rect_jugador.x -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_RIGHT] and rect_jugador.right < ANCHO_VENTANA:
        rect_jugador.x += VELOCIDAD_JUGADOR
    if teclas[pygame.K_UP] and rect_jugador.top > 0:
        rect_jugador.y -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_DOWN] and rect_jugador.bottom < ALTO_VENTANA:
        rect_jugador.y += VELOCIDAD_JUGADOR

    # 4. Lógica de Movimiento (Obstáculos)
    for obs in obstaculos:
        # Mover el obstáculo
        obs["rect"].x += obs["velocidad_x"]
        
        # Hacer que rebote en los bordes izquierdo/derecho
        if obs["rect"].left < 0 or obs["rect"].right > ANCHO_VENTANA:
            obs["velocidad_x"] *= -1 # Invertir velocidad

    # 5. Lógica de Colisión (Jugador vs Obstáculos)
    for obs in obstaculos:
        # Comprobar si el jugador choca con el rect del obstáculo
        if rect_jugador.colliderect(obs["rect"]):
            # ¡Colisión! Terminar el juego.
            print("¡Has chocado! Juego terminado.")
            ejecutando = False # Esto detiene el bucle principal

    # 6. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar al jugador
    pygame.draw.rect(pantalla, COLOR_JUGADOR, rect_jugador)
    
    # Dibujar todos los obstáculos
    for obs in obstaculos:
        pygame.draw.circle(pantalla, COLOR_OBSTACULO, obs["rect"].center, RADIO_OBSTACULO)

    # 7. Actualizar la pantalla
    pygame.display.flip()

# 8. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()  