import pygame
import os
import pygame.image
from game.score import Score
from utils import constants
from font.font import Font
from game.image import Images
class GameLogic:
    def __init__(self):
         # Inicializar la lógica del juego
        self.font = Font('./font/FUTURISM.TTF', 32)
        self.fontContenido = Font('./font/Technology.ttf', 25)
        #instaciamos las imagenes
        self.image_manager = Images()
        #cargar las imagenes
        #obtengo la ruta base del directorio actual
        # Obtener la ruta base del directorio actual
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.paleta1 =self.image_manager.load_image(os.path.join(base_path,"assets/Paleta1.png"),50,220)
        self.paleta2= self.image_manager.load_image(os.path.join(base_path,"assets/Paleta2.png"),50,220)
        self.imageBall = self.image_manager.load_image(os.path.join(base_path,"assets/Bola.png"), 40,40)
        #escena de para controlar si entro o no
        self.is_scene_entered = False
        #Poscision de las paletas en y
        self.y_paleta1 = 100
        self.y_paleta2 = 100
        #Posicion de la bola al centro de la pantalla
        self.bola_pos = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
        #Velocidad de la pelota en x, y
        self.ball_velocity_x = 1
        self.ball_velocity_y = 1
        #inicializamos la clase score
        self.score = Score()
        #Creacion de los rectangulos de colicion
        self.paleta1_rect = pygame.Rect(0, self.y_paleta1, 50, 220)
        self.paleta2_rect = pygame.Rect(constants.SCREEN_WIDTH - 50, self.y_paleta2, 50, 220)
        self.bola_rect = pygame.Rect(self.bola_pos[0], self.bola_pos[1], 40, 40)
        
    def draw_inicio(self, window, button_start, button_exit):
        text_surface = self.font.render_text("Pong Wars", (255, 255, 255), 50)
        text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH / 2, 200))
        window.blit(text_surface, text_rect)
        button_start.draw(window)
        button_exit.draw(window)
        
    def draw_juego(self, window):
        
        # Posición inicial de la paleta 2 (en el borde derecho de la ventana)
        x2 = constants.SCREEN_WIDTH - self.paleta2.get_width()
        
        #Manejando movimiento de las paletas
        self.y_paleta1 = self.moverPaletas(pygame.K_w, pygame.K_s, self.y_paleta1)
        self.y_paleta2 = self.moverPaletas(pygame.K_UP, pygame.K_DOWN, self.y_paleta2)

        #Actualizar las pocisiones de los rectangulos de colision de las paletas
        self.paleta1_rect.y = self.y_paleta1
        self.paleta2_rect.y = self.y_paleta2
        
        #Dibujando las pelotas
        self.image_manager.draw_image(window, self.paleta1, 0, self.y_paleta1)
        self.image_manager.draw_image(window, self.paleta2, x2, self.y_paleta2)
        
        #Bola
        self.moverPelota()
        
        # Comprobar colisiones y actualizar puntaje
        score = self.update_score()
        
        #Dibujando la pelota
        self.image_manager.draw_image(window, self.imageBall, self.bola_pos[0], self.bola_pos[1])

        # Mostrar el puntaje en la ventana de juego
        score_text = f"Jugador 1: {score.get_score1()}   Jugador 2: {score.get_score2()}"
        text_surface = self.fontContenido.render_text(score_text, (255, 255, 255),25)
        text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH / 2, 50))
        window.blit(text_surface, text_rect)
        
    def moverPaletas(self, key_up, key_down, position_y):
        """
        Mueve la posición vertical de las paletas del juego según las teclas presionadas.

        Parámetros:
        key_up (int): Código de tecla que representa la tecla de movimiento hacia arriba.
        key_down (int): Código de tecla que representa la tecla de movimiento hacia abajo.
        position_y (int): La posición actual de la paleta en el eje Y.

        Retorna:
        int: La nueva posición vertical de la paleta después de aplicar el movimiento.

        Comportamiento:
        - Si la tecla key_up está presionada, la posición_y se decrementa en 1 unidad.
        - Si la tecla key_down está presionada, la posición_y se incrementa en 1 unidad.
        - Si la posición_y es menor que 0, se ajusta a 0 para evitar que la paleta se salga de la pantalla.
        - Si la posición_y es mayor que constants.SCREEN_HEIGHT - 220, se ajusta a constants.SCREEN_HEIGHT - 220
        para evitar que la paleta se salga de la pantalla en la parte inferior.

        Ejemplo de uso:
        position_y = moverPaletas(pygame.K_UP, pygame.K_DOWN, position_y)

        Notas:
        - Esta función asume que se está utilizando la biblioteca pygame para manejar la entrada de teclado.
        - La función debe ser llamada dentro del bucle principal del juego para actualizar continuamente la posición de la paleta.

        """
        if pygame.key.get_pressed()[key_up]:
            position_y -= 1
        elif pygame.key.get_pressed()[key_down]:
            position_y += 1
        
        if position_y < 0:
            position_y = 0
        elif position_y > constants.SCREEN_HEIGHT - 220:
            position_y = constants.SCREEN_HEIGHT - 220
        
         # Actualizar la posición del rectángulo de colisión de la paleta
        self.paleta1_rect.y = position_y
        self.paleta2_rect.y = position_y
        
        return position_y
    
    def moverPelota(self):
        """
        Actualiza la posición de la pelota según la velocidad y comprueba si ha alcanzado los límites de la ventana para cambiar su dirección si es necesario.
        """
        # Actualizar la posición de la pelota según la velocidad
        self.bola_pos = (self.bola_pos[0] + self.ball_velocity_x, self.bola_pos[1] + self.ball_velocity_y)
        
        # Comprobar si la pelota ha alcanzado los límites de la ventana y cambiar la dirección si es necesario
        if self.bola_pos[0] <= 0 or self.bola_pos[0] >= constants.SCREEN_WIDTH - 40:
            self.ball_velocity_x *= -1
        if self.bola_pos[1] <= 0 or self.bola_pos[1] >= constants.SCREEN_HEIGHT - 40:
            self.ball_velocity_y *= -1
        
        # Actualizar la posición del rectángulo de colisión de la bola
        self.bola_rect.x = self.bola_pos[0]
        self.bola_rect.y = self.bola_pos[1]
         
    def update_score(self):
    
        if self.bola_rect.colliderect(self.paleta1_rect):
            self.ball_velocity_x *= -1  # Cambiar dirección horizontal de la pelota
        elif self.bola_rect.colliderect(self.paleta2_rect):
            self.ball_velocity_x *= -1  # Cambiar dirección horizontal de la pelota 
    
        # Verificar si la pelota ha alcanzado los límites de la ventana y actualizar el puntaje correspondiente
        if self.bola_pos[0] <= 0:
            self.score.increaseScore2()
        elif self.bola_pos[0] >= constants.SCREEN_WIDTH - 40:
            self.score.increaseScore1()
    
        return self.score
