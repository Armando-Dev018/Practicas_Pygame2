import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Sesión 5 - Ejercicio 2: Sprite Animado")

# --- Colores ---
COLOR_FONDO = (50, 50, 50) # Gris

# --- ¡CONFIGURACIÓN COMPLETA CON TUS VALORES! ---
# 1. El nombre de tu archivo guardado en la carpeta Sesion5
#    (Si le pusiste un nombre diferente, cámbialo aquí)
NOMBRE_SPRITESHEET = "Sesion_5/pokemon.png" 

# 2. Los valores que calculamos de tu imagen (449x576)
NUM_FRAMES = 4        # (Animamos 4 frames)
FRAME_ANCHO = 112     # (Ancho total 449 / 4 frames ≈ 112)
FRAME_ALTO = 144      # (Alto total 576 / 4 filas = 144)

# 3. Los valores (R, G, B) de tu captura
COLOR_TRANSPARENTE = (89, 169, 185)
# --- Fin de la configuración ---

# --- Constantes de Animación ---
INTERVALO_ANIM = 100  # 100 milisegundos por frame

# --- Cargar y "Cortar" la Hoja de Sprites ---
frames_animacion = []
try:
    # Cargamos la hoja de sprites
    # Usamos .convert() porque vamos a definir la transparencia manualmente
    spritesheet = pygame.image.load(NOMBRE_SPRITESHEET).convert()
    
    # Bucle para "cortar" cada frame de la PRIMERA fila
    for i in range(NUM_FRAMES):
        # Calcular la 'x' de este frame
        x_frame = i * FRAME_ANCHO
        # Crear el rectángulo que define el "corte" (en y=0, la primera fila)
        rect_corte = pygame.Rect(x_frame, 0, FRAME_ANCHO, FRAME_ALTO)
        
        # "Cortar" el frame
        frame = spritesheet.subsurface(rect_corte)
        
        # --- Hacer el fondo azul transparente ---
        frame.set_colorkey(COLOR_TRANSPARENTE)
        
        frames_animacion.append(frame)

except pygame.error as e:
    print(f"Error al cargar o cortar el spritesheet '{NOMBRE_SPRITESHEET}': {e}")
    print("Asegúrate de que el nombre y las constantes (ancho/alto) sean correctos.")
    sys.exit()

if not frames_animacion:
    print("¡No se cargaron frames! Revisa la configuración.")
    sys.exit()

# --- Variables de Estado de Animación ---
frame_actual = 0  
ultimo_update = pygame.time.get_ticks() 

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

    # 3. Lógica de Animación
    ahora = pygame.time.get_ticks()
    
    if ahora - ultimo_update > INTERVALO_ANIM:
        ultimo_update = ahora 
        frame_actual += 1
        
        if frame_actual >= len(frames_animacion):
            frame_actual = 0

    # 4. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)
    
    imagen_a_dibujar = frames_animacion[frame_actual]
    
    # Escalamos la imagen x4 para que se vea mejor (el pixel art es pequeño)
    imagen_escalada = pygame.transform.scale(imagen_a_dibujar, (FRAME_ANCHO * 4, FRAME_ALTO * 4))
    
    rect_dibujo = imagen_escalada.get_rect(
        center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
    )
    
    pantalla.blit(imagen_escalada, rect_dibujo)

    # 5. Actualizar la pantalla
    pygame.display.flip()

# 6. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()