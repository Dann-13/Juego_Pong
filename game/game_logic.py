import pygame
import pygame.image
from game.score import Score
from utils import constants
from font.font import Font
class GameLogic:
    def __init__(self):
         # Inicializar la lógica del juego
        self.font = Font('./font/FUTURISM.TTF', 32)
        self.fontContenido = Font('./font/Technology.ttf', 25)
        self.is_scene_entered = False
        self.y_paleta1 = 100
        self.y_paleta2 = 100
        
        self.bola_pos = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
        
        self.ball_velocity_x = 1
        self.ball_velocity_y = 1
        
        self.score = Score()
        
    def draw_inicio(self, window, button_start, button_exit):
        text_surface = self.font.render_text("Pong Wars", (255, 255, 255), 50)
        text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH / 2, 200))
        window.blit(text_surface, text_rect)
        button_start.draw(window)
        button_exit.draw(window)
        
    def draw_juego(self, window, images):
        #cargar las imagenes
        paleta1 = images.load_image("./assets/Paleta1.png",50,220)
        paleta2= images.load_image("./assets/Paleta2.png",50,220)
        imageBall = images.load_image("./assets/Bola.png", 40,40)
        # Posición inicial de la paleta 2 (en el borde derecho de la ventana)
        x2 = constants.SCREEN_WIDTH - paleta2.get_width()
        
        #Manejando movimiento de las imagenes paleta 1
        self.y_paleta1 = self.moverPaletas(pygame.K_w, pygame.K_s, self.y_paleta1)
        images.draw_image(window, paleta1, 0, self.y_paleta1)
        
        #Paleta 2
        self.y_paleta2 = self.moverPaletas(pygame.K_UP, pygame.K_DOWN, self.y_paleta2)
        images.draw_image(window, paleta2, x2, self.y_paleta2)
        
        #Bola
        self.moverPelota()
        score = self.update_score(50,220)
        images.draw_image(window, imageBall, self.bola_pos[0], self.bola_pos[1])

        # Mostrar el puntaje en la ventana de juego
        score_text = f"Jugador 1: {score.get_score1()}   Jugador 2: {score.get_score2()}"
        text_surface = self.fontContenido.render_text(score_text, (255, 255, 255),15)
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



            
    def update_score(self, paleta_width, paleta_height):
        # Verificar colisión con la paleta 1
        paleta1_rect = pygame.Rect(0, self.y_paleta1, paleta_width, paleta_height)
        paleta2_rect = pygame.Rect(constants.SCREEN_WIDTH - paleta_width, self.y_paleta2, paleta_width, paleta_height)
        bola_rect = pygame.Rect(self.bola_pos[0], self.bola_pos[1], 40, 40)
    
        if bola_rect.colliderect(paleta1_rect):
            self.ball_velocity_x *= -1  # Cambiar dirección horizontal de la pelota
        elif bola_rect.colliderect(paleta2_rect):
            self.ball_velocity_x *= -1  # Cambiar dirección horizontal de la pelota 
    
        # Verificar si la pelota ha alcanzado los límites de la ventana y actualizar el puntaje correspondiente
        if self.bola_pos[0] <= 0:
            self.score.increaseScore2()
        elif self.bola_pos[0] >= constants.SCREEN_WIDTH - 40:
            self.score.increaseScore1()
    
        return self.score
