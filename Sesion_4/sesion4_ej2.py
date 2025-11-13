import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Sesión 4 - Ejercicio 2: Animación de Pulsación")

# --- Colores ---
COLOR_FONDO = (0, 0, 0)
COLOR_CIRCULO = (0, 200, 200) # Cian

# --- Configuración de la Pulsación ---
CENTRO_VENTANA = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2)

# Límites del radio 
RADIO_MIN = 20
RADIO_MAX = 50

# Variables de estado
# Usamos flotantes para un crecimiento/decrecimiento suave
radio_actual = float(RADIO_MIN)
velocidad_radio = 0.5 # Píxeles por frame (1.0 = más rápido, 0.2 = más lento)
# Iniciamos creciendo (velocidad positiva)

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

    # 3. Lógica de Animación (Pulsación)
    
    # Actualizamos el radio sumando la velocidad
    radio_actual += velocidad_radio
    
    # Comprobamos los límites para cambiar la dirección 
    
    # Si el radio supera el máximo...
    if radio_actual >= RADIO_MAX:
        radio_actual = RADIO_MAX # Aseguramos que no se pase
        velocidad_radio *= -1 # Invertimos la dirección (empieza a encogerse)
        
    # Si el radio es menor que el mínimo...
    elif radio_actual <= RADIO_MIN:
        radio_actual = RADIO_MIN # Aseguramos que no se pase
        velocidad_radio *= -1 # Invertimos la dirección (empieza a crecer)

    # 4. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)
    
    # Dibujamos el círculo con el radio actual
    # Hay que convertir el radio_actual a 'int' porque la función lo requiere
    pygame.draw.circle(pantalla, COLOR_CIRCULO, CENTRO_VENTANA, int(radio_actual))

    # 5. Actualizar la pantalla
    pygame.display.flip()

# 6. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()