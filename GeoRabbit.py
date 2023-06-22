import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Creación de la pantalla
W,H=1000,600
PANTALLA = pygame.display.set_mode((W, H))
# Especificación de título
pygame.display.set_caption('Georabbit')
icono=pygame.image.load("icon/icogeorabbit.png")
pygame.display.set_icon(icono)


# Colores
white = (255, 255, 255)        # Blanco
black = (0, 0, 0)              # Negro
red = (255, 0, 0)              # Rojo
green = (0, 255, 0)            # Verde
blue = (0, 0, 255)             # Azul
yellow = (255, 255, 0)         # Amarillo
magenta = (255, 0, 255)        # Magenta
cyan = (0, 255, 255)           # Cian
gray = (128, 128, 128)         # Gris
orange = (255, 165, 0)         # Naranja
pink = (255, 192, 203)         # Rosa
violet = (238, 130, 238)       # Violeta
brown = (165, 42, 42)          # Marrón
sky_blue = (135, 206, 235)     # Celeste
light_green = (144, 238, 144)  # Verde claro
light_gray = (211, 211, 211)   # Gris claro
gold = (255, 215, 0)           # Dorado
silver = (192, 192, 192)       # Plata





#fondo

fondo = pygame.image.load("icon/Fondo.png").convert()
# Música de fondo
pygame.mixer.music.load('Sonido/musica2.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
#PERSONAJE
# Sin movimiento
quieto = pygame.image.load('icon/frente1.png')
# Movimiento a la izquierda
caminaIzquierda = [pygame.image.load('icon/Izquierda1.png'),
				pygame.image.load('icon/Izquierda2.png'),
				pygame.image.load('icon/Izquierda3.png'),
				pygame.image.load('icon/Izquierdo4.png')]
# Movimiento a la derecha
caminaDerecha = [pygame.image.load('icon/Derecha1.png'),
				pygame.image.load('icon/Derecha2.png'),
                pygame.image.load('icon/Derecha3.png'),
				pygame.image.load('icon/Derecha4.png')]
#salto
salta= [pygame.image.load('icon/Salto1.png'),
		pygame.image.load('icon/Salto2.png'),
		pygame.image.load('icon/Salto2.png')]

# Sonido
sonido_arriba = pygame.image.load('icon/icogeorabbit.png')
sonido_abajo = pygame.image.load('icon/icogeorabbit.png')
sonido_mute = pygame.image.load('icon/icogeorabbit.png')
sonido_max = pygame.image.load('icon/icogeorabbit.png')


x = 0
px = 50
py = 400
ancho = 40
velocidad = 5
# Control de FPS
reloj = pygame.time.Clock()

# Variables salto
salto = False
# Contador de salto
cuentaSalto = 10

# Variables dirección
izquierda = False
derecha = False

# Pasos
cuentaPasos = 0

# Movimiento
def recarga_pantalla():
	# Variables globales
	global cuentaPasos
	global x

	# Fondo en movimiento
	x_relativa = x % fondo.get_rect().width
	PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
	if x_relativa < W:
		PANTALLA.blit(fondo, (x_relativa, 0))
	x -= 5
	# Contador de pasos
	if cuentaPasos + 1 >= 4:
		cuentaPasos = 0
	# Movimiento a la izquierda
	if izquierda:
		PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

		# Movimiento a la derecha
	elif derecha:
		PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	elif salto + 1 >= 2:
		PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	else:
		PANTALLA.blit(quieto,(int(px), int(py)))

ejecuta = True

# Bucle de acciones y controles
while ejecuta:
	# FPS
	reloj.tick(16)


	# Bucle del juego
	for event in pygame.event.get():
		if event.type == pygame.QUIT:

			ejecuta = False

	# Opción tecla pulsada
	keys = pygame.key.get_pressed()

	# Tecla A - Moviemiento a la izquierda
	if keys[pygame.K_a] and px > velocidad:
		px -= velocidad
		izquierda = True
		derecha = False

	# Tecla D - Moviemiento a la derecha
	elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
		px += velocidad
		izquierda = False
		derecha = True

	# Personaje quieto
	else:
		izquierda = False
		derecha = False
		cuentaPasos = 0

	# Tecla W - Moviemiento hacia arriba
	if keys[pygame.K_w] and py > 300:
		py -= velocidad

	# Tecla S - Moviemiento hacia abajo
	if keys[pygame.K_s] and py < 450:
		py += velocidad
	# Tecla SPACE - Salto
	if not salto:
		if keys[pygame.K_SPACE]:
			salto = True
			izquierda = False
			derecha = False
			cuentaPasos = 0
	else:
		if cuentaSalto >= -10:
			py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
			cuentaSalto -= 1
		else:
			cuentaSalto = 10
			salto = False
		# Control del audio
		# Baja volumen
		if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
			pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.05)
			PANTALLA.blit(sonido_abajo, (850, 25))
		elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
			PANTALLA.blit(sonido_mute, (850, 25))

		# Sube volumen
		if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
			pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
			PANTALLA.blit(sonido_arriba, (850, 25))
		elif keys[pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
			PANTALLA.blit(sonido_max, (850, 25))

		# Desactivar sonido
		elif keys[pygame.K_m]:
			pygame.mixer.music.set_volume(0.0)
			PANTALLA.blit(sonido_mute, (850, 25))

		# Reactivar sonido
		elif keys[pygame.K_COMMA]:
			pygame.mixer.music.set_volume(1.0)
			PANTALLA.blit(sonido_max, (850, 25))

	# Actualización de la ventana
	pygame.display.update()
	#Llamada a la función de actualización de la ventana
	recarga_pantalla()

# Salida del juego
pygame.quit()