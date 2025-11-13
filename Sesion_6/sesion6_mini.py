import pygame
import sys
import random

# 1. Inicializar Pygame y el módulo de fuentes
pygame.init()
pygame.font.init() # Inicializar el módulo para mostrar texto

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Sesión 6 - Mini-Proyecto: ¡Esquiva y Recoge!")

# --- Colores ---
COLOR_FONDO = (10, 20, 30)       # Azul espacial
COLOR_PUNTO = (255, 220, 0)    # Amarillo (Punto)
COLOR_OBSTACULO = (255, 50, 50) # Rojo (Peligro)
COLOR_TEXTO = (255, 255, 255)   # Blanco

# --- Cargar la Imagen del Jugador (Sprite) ---
try:
    # Asegúrate de tener "nave.png" en tu carpeta "Sesion6/"
    nave_original = pygame.image.load("Sesion_6/Nave.jpg").convert_alpha()
    # Escalamos la nave a un tamaño manejable
    nave_img = pygame.transform.scale(nave_original, (50, 60))
except pygame.error as e:
    print(f"Error al cargar la imagen 'Sesion6/nave.png': {e}")
    print("Por favor, asegúrate de tener la imagen en la carpeta Sesion6.")
    sys.exit()

# --- Configuración del Jugador ---
rect_jugador = nave_img.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA - 50))
VELOCIDAD_JUGADOR = 8

# --- Configuración de Puntos y Obstáculos ---
VELOCIDAD_OBSTACULO = 5
puntuacion = 0
obstaculos = [] # Lista para guardar los rects de los obstáculos
RADIO_PUNTO = 10
RADIO_OBSTACULO = 15

# Función para crear un nuevo punto
def crear_punto():
    x = random.randint(RADIO_PUNTO, ANCHO_VENTANA - RADIO_PUNTO)
    y = random.randint(RADIO_PUNTO, ALTO_VENTANA - RADIO_PUNTO)
    return pygame.Rect(x - RADIO_PUNTO, y - RADIO_PUNTO, RADIO_PUNTO * 2, RADIO_PUNTO * 2)

# Función para crear un nuevo obstáculo (empieza arriba, fuera de pantalla)
def crear_obstaculo():
    x = random.randint(RADIO_OBSTACULO, ANCHO_VENTANA - RADIO_OBSTACULO)
    y = random.randint(-100, -RADIO_OBSTACULO) # Empieza arriba
    return pygame.Rect(x - RADIO_OBSTACULO, y - RADIO_OBSTACULO, RADIO_OBSTACULO * 2, RADIO_OBSTACULO * 2)

# Crear el primer punto
rect_punto = crear_punto()

# Crear 5 obstáculos iniciales
for _ in range(5):
    obstaculos.append(crear_obstaculo())

# --- Configuración de Fuente ---
try:
    mi_fuente = pygame.font.Font(None, 40) # Fuente por defecto, tamaño 40
    fuente_game_over = pygame.font.Font(None, 80)
except:
    mi_fuente = pygame.font.SysFont("Arial", 30) # Respaldo
    fuente_game_over = pygame.font.SysFont("Arial", 60) # Respaldo

# --- Variables de Estado del Juego ---
game_over = False
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
            # Opcional: Reiniciar el juego con 'R' si ha terminado
            if game_over and evento.key == pygame.K_r:
                game_over = False
                puntuacion = 0
                obstaculos = []
                for _ in range(5):
                    obstaculos.append(crear_obstaculo())
                rect_punto = crear_punto()
                rect_jugador.center = (ANCHO_VENTANA // 2, ALTO_VENTANA - 50)

    # Solo actualizamos el juego si NO es game over
    if not game_over:
        
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
            obs.y += VELOCIDAD_OBSTACULO
            # Si el obstáculo sale por abajo, lo reinicia arriba
            if obs.top > ALTO_VENTANA:
                obs.x = random.randint(RADIO_OBSTACULO, ANCHO_VENTANA - RADIO_OBSTACULO)
                obs.y = random.randint(-100, -RADIO_OBSTACULO)

        # 5. Lógica de Colisiones
        
        # A. Jugador vs. Punto (Recolectar)
        if rect_jugador.colliderect(rect_punto):
            puntuacion += 1
            rect_punto = crear_punto() # Nuevo punto
            
        # B. Jugador vs. Obstáculos (Perder)
        for obs in obstaculos:
            if rect_jugador.colliderect(obs):
                game_over = True # ¡Juego terminado!

    # 6. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar el punto
    pygame.draw.circle(pantalla, COLOR_PUNTO, rect_punto.center, RADIO_PUNTO)
    
    # Dibujar los obstáculos
    for obs in obstaculos:
        pygame.draw.circle(pantalla, COLOR_OBSTACULO, obs.center, RADIO_OBSTACULO)

    # Dibujar al jugador (el sprite)
    pantalla.blit(nave_img, rect_jugador)
    
    # Dibujar la puntuación
    texto_superficie = mi_fuente.render(f'Puntos: {puntuacion}', True, COLOR_TEXTO)
    pantalla.blit(texto_superficie, (10, 10))
    
    # Si es Game Over, mostrar mensaje
    if game_over:
        texto_go = fuente_game_over.render('¡GAME OVER!', True, COLOR_OBSTACULO)
        texto_go_rect = texto_go.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2 - 40))
        pantalla.blit(texto_go, texto_go_rect)
        
        texto_r = mi_fuente.render('Presiona R para reiniciar', True, COLOR_TEXTO)
        texto_r_rect = texto_r.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 20))
        pantalla.blit(texto_r, texto_r_rect)

    # 7. Actualizar la pantalla
    pygame.display.flip()

# 8. Salir del programa
print(f"Juego terminado. Puntuación final: {puntuacion}")
pygame.quit()
sys.exit()