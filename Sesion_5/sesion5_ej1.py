import pygame
import sys

# --- Constantes ---
# ¡Asegúrate de que esta ruta sea correcta!
NOMBRE_IMAGEN = "Sesion_5/Tu_Papa_Raphinha.jpg" 
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
COLOR_FONDO = (30, 30, 30) # Gris oscuro
PASO_ESCALADO = 10 # Cuántos píxeles cambiará por tecla

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Sesión 5 - Ejercicio 1: Escalado de Imagen")

# --- Cargar la imagen ---
try:
    # Cargamos la imagen original UNA SOLA VEZ
    imagen_original = pygame.image.load(NOMBRE_IMAGEN).convert_alpha()
except pygame.error as e:
    print(f"Error al cargar la imagen '{NOMBRE_IMAGEN}': {e}")
    print("Asegúrate de tener una imagen en la carpeta del script.")
    sys.exit()

# --- Configuración de Escalado ---
# Guardamos las dimensiones originales y la proporción
ancho_original = imagen_original.get_width()
alto_original = imagen_original.get_height()
# Calculamos la proporción para no distorsionar la imagen
proporcion_aspecto = float(alto_original) / float(ancho_original)

# Variables de estado para el tamaño actual
ancho_actual = ancho_original

# Creamos la primera imagen escalada y su rect
# (Al principio, es la imagen original)
imagen_escalada = imagen_original.copy()
rect_escalado = imagen_escalada.get_rect(
    center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
)

# --- Control de Tiempo ---
reloj = pygame.time.Clock()

# --- Bucle principal del "juego" ---
ejecutando = True
while ejecutando:
    
    reloj.tick(60)
    
    # Variable para saber si necesitamos recalcular la imagen
    hay_que_redimensionar = False

    # 2. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False
            
            # --- LÓGICA DE ESCALADO CORREGIDA ---
            # Usamos 'evento.unicode' para detectar el caracter '+' o '-'
            # independientemente de la tecla física (numpad o principal)
            
            if evento.unicode == '+':
                ancho_actual += PASO_ESCALADO
                hay_que_redimensionar = True
            elif evento.unicode == '-':
                ancho_actual -= PASO_ESCALADO
                hay_que_redimensionar = True
            # --- FIN DE LA CORRECCIÓN ---

    # 3. Lógica de Escalado
    if hay_que_redimensionar:
        
        # Límite para que no desaparezca
        if ancho_actual < 10:
            ancho_actual = 10
            
        # Calculamos el nuevo alto manteniendo la proporción
        alto_actual = int(ancho_actual * proporcion_aspecto)
        
        print(f"Cambiando tamaño a: {ancho_actual} x {alto_actual}")
        
        # Creamos la NUEVA imagen escalada desde la ORIGINAL
        # Esto evita la pérdida de calidad progresiva
        imagen_escalada = pygame.transform.scale(
            imagen_original, (ancho_actual, alto_actual)
        )
        
        # Actualizamos el rect con el nuevo tamaño, manteniendo el centro
        rect_escalado = imagen_escalada.get_rect(
            center=rect_escalado.center
        )


    # 4. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)
    
    # Dibujamos la imagen escalada (la más reciente)
    pantalla.blit(imagen_escalada, rect_escalado)

    # 5. Actualizar la pantalla
    pygame.display.flip()

# 6. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()