import pygame
import sys
import random # ¡Necesario para las posiciones aleatorias!

# 1. Inicializar Pygame y el módulo de fuentes
pygame.init()
pygame.font.init() # Inicializar el módulo para mostrar texto

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Sesión 6 - Ejercicio 2: Recolección de Objetos")

# --- Colores ---
COLOR_FONDO = (20, 20, 20)
COLOR_JUGADOR = (50, 150, 255) # Azul
COLOR_OBJETO = (255, 200, 0)  # Amarillo
COLOR_TEXTO = (255, 255, 255) # Blanco

# --- Configuración del Jugador ---
rect_jugador = pygame.Rect(375, 500, 50, 50) # (x, y, ancho, alto)
VELOCIDAD = 7

# --- Configuración del Objeto (Círculo) ---
RADIO_OBJETO = 15

# Función para crear un nuevo objeto en un lugar aleatorio
def crear_nuevo_objeto():
    # Usamos random.randint para obtener posiciones aleatorias [cite: 47]
    # Restamos el radio/borde para que no aparezca medio fuera
    x = random.randint(RADIO_OBJETO, ANCHO_VENTANA - RADIO_OBJETO)
    y = random.randint(RADIO_OBJETO, ALTO_VENTANA - RADIO_OBJETO)
    
    # Creamos un Rect en esa posición. El rect facilitará la colisión.
    return pygame.Rect(x - RADIO_OBJETO, y - RADIO_OBJETO, RADIO_OBJETO * 2, RADIO_OBJETO * 2)

# Crear el primer objeto
rect_objeto = crear_nuevo_objeto()

# --- Configuración de Puntuación y Fuente ---
puntuacion = 0
# Cargamos una fuente (None usa la fuente por defecto de Pygame)
try:
    mi_fuente = pygame.font.Font(None, 40) # Fuente por defecto, tamaño 40
except:
    print("Error al cargar la fuente por defecto.")
    mi_fuente = pygame.font.SysFont("Arial", 30) # Fuente de respaldo

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

    # 4. Lógica de Colisión (Recolección)
    
    # Comprobamos si el jugador toca el objeto
    if rect_jugador.colliderect(rect_objeto):
        # ¡Colisión!
        puntuacion += 1 # Incrementar el contador
        rect_objeto = crear_nuevo_objeto() # Crear un objeto nuevo [cite: 48]
        print(f"¡Objeto recogido! Puntuación: {puntuacion}")

    # 5. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar el objeto (como un círculo, usando el centro del rect)
    pygame.draw.circle(pantalla, COLOR_OBJETO, rect_objeto.center, RADIO_OBJETO)
    
    # Dibujar al jugador
    pygame.draw.rect(pantalla, COLOR_JUGADOR, rect_jugador)
    
    # --- Dibujar la puntuación en pantalla --- [cite: 49]
    # 1. Crear la superficie de texto (render)
    texto_superficie = mi_fuente.render(
        f'Puntuación: {puntuacion}', # El texto a mostrar
        True,                      # 'Anti-aliasing' (bordes suaves)
        COLOR_TEXTO                # El color del texto
    )
    
    # 2. Dibujar la superficie de texto en la pantalla (blit)
    # La pondremos en la esquina superior izquierda (10, 10)
    pantalla.blit(texto_superficie, (10, 10))

    # 6. Actualizar la pantalla
    pygame.display.flip()

# 7. Salir del programa
print(f"Juego terminado. Puntuación final: {puntuacion}")
pygame.quit()
sys.exit()