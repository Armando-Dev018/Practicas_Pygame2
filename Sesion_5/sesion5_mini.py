import pygame
import sys
import math

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 900
ALTO_VENTANA = 700
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Sesión 5 - Mini-Proyecto: Nave Hacia el Ratón")

# --- Colores ---
COLOR_FONDO = (10, 20, 30) # Azul espacial oscuro

# --- Cargar y Escalar la Imagen ---
try:
    # Cargamos la imagen original
    # (Asegúrate de tener "nave.png" en tu carpeta "Sesion5/")
    nave_original = pygame.image.load("Sesion_5/Nave.jpg").convert_alpha()
except pygame.error:
    print("Error: No se encontró la imagen 'Sesion5/nave.png'")
    print("Por favor, descarga una imagen y guárdala en esa ubicación.")
    sys.exit()

# [cite_start]Asegúrate de que la imagen tenga un tamaño adecuado (usa scale) [cite: 34]
# La escalamos a un tamaño fijo de 60x80 píxeles
nave_original = pygame.transform.scale(nave_original, (60, 80))

# Esta será la imagen que se dibuja (la versión rotada)
nave_rotada = nave_original.copy()
# Usamos un rect para la posición (se actualizará desde los floats)
nave_rect = nave_rotada.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

# --- Variables de la Nave ---
# Usamos flotantes para la posición para un movimiento suave
pos_x = float(nave_rect.centerx)
pos_y = float(nave_rect.centery)
velocidad = 5
angulo_actual_rad = 0.0 # Guardaremos el ángulo en radianes para el movimiento

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

    # [cite_start]3. Lógica de Rotación (Hacia el ratón) [cite: 33]
    
    # Obtener la posición del ratón
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Calcular la diferencia (vector) entre la nave y el ratón
    delta_x = mouse_x - pos_x
    delta_y = mouse_y - pos_y
    
    # Calcular el ángulo en radianes usando arcotangente2
    # 'atan2' maneja todos los cuadrantes correctamente
    angulo_actual_rad = math.atan2(delta_y, delta_x)
    
    # Convertir a grados para la función de rotación de Pygame
    angulo_grados = math.degrees(angulo_actual_rad)
    
    # Ajuste de rotación:
    # math.atan2 da 0° hacia la derecha (eje X positivo).
    # Nuestra imagen original apunta ARRIBA (a 90° o -90° en el sistema de pygame).
    # -angulo_grados invierte la rotación (pygame rota anti-horario).
    # - 90 compensa la orientación original de nuestra imagen.
    angulo_para_rotar = -angulo_grados - 90
    
    # Rotar la imagen original (¡nunca rotes la imagen ya rotada!)
    nave_rotada = pygame.transform.rotate(nave_original, angulo_para_rotar)
    # Recalcular el rect con la nueva imagen rotada, manteniendo el centro
    nave_rect = nave_rotada.get_rect(center=(pos_x, pos_y))


    # [cite_start]4. Lógica de Movimiento (Hacia adelante) [cite: 33]
    
    # Revisar si la tecla 'W' (o espacio) está presionada
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] or teclas[pygame.K_SPACE]:
        
        # Moverse "hacia adelante" significa moverse en la dirección
        # del ángulo que ya calculamos (angulo_actual_rad)
        
        # Calcular el movimiento en X e Y usando Coseno y Seno
        mov_x = math.cos(angulo_actual_rad) * velocidad
        mov_y = math.sin(angulo_actual_rad) * velocidad
        
        # Aplicar el movimiento a la posición (float)
        pos_x += mov_x
        pos_y += mov_y
        
        # Actualizar el centro del rect (int) para el dibujado
        nave_rect.centerx = int(pos_x)
        nave_rect.centery = int(pos_y)

    # (Opcional) Evitar que la nave se salga
    if pos_x > ANCHO_VENTANA: pos_x = 0
    if pos_x < 0: pos_x = ANCHO_VENTANA
    if pos_y > ALTO_VENTANA: pos_y = 0
    if pos_y < 0: pos_y = ALTO_VENTANA
    nave_rect.center = (int(pos_x), int(pos_y))


    # 5. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar la nave rotada en la posición del rect
    pantalla.blit(nave_rotada, nave_rect)

    # 6. Actualizar la pantalla
    pygame.display.flip()

# 7. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()