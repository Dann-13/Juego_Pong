import pygame
import pygame.image
from utils import constants

class GameLogic:
    def __init__(self):
         # Inicializar la lógica del juego
        self.font = pygame.font.Font('./font/FUTURISM.TTF', 50)
        self.is_scene_entered = False
        self.y_paleta1 = 100
        self.y_paleta2 = 100
        
        self.bola_pos = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
        
        self.ball_velocity_x = 1
        self.ball_velocity_y = 1
        
    def draw_inicio(self, window, button_start, button_exit):
        text_surface = self.font.render("PONG WARS", True, (255, 255, 255))
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
        self.moverPelota(50,220)
        images.draw_image(window, imageBall, self.bola_pos[0], self.bola_pos[1])


    def moverPaletas(self, key_up, key_down, position_y):
        if pygame.key.get_pressed()[key_up]:
            position_y -= 1
        elif pygame.key.get_pressed()[key_down]:
            position_y += 1
        
        if position_y < 0:
            position_y = 0
        elif position_y > constants.SCREEN_HEIGHT - 220:
            position_y = constants.SCREEN_HEIGHT - 220
        
        return position_y
    
    def moverPelota(self, paleta_width, paleta_height):
        """
        Esta funcion se encarga de mover la pelota, verificar su colision en pantalla y
        y a su ver verificar la colision con las paletas
        Parámetros:
        paleta_width (int): Ancho de la paleta.
        paleta_height (int): Alto de la Paleta
        """
        # Actualizar la posición de la pelota según la velocidad
        self.bola_pos = (self.bola_pos[0] + self.ball_velocity_x, self.bola_pos[1] + self.ball_velocity_y)

        # Comprobar si la pelota ha alcanzado los límites de la ventana y cambiar la dirección si es necesario
        if self.bola_pos[0] <= 0 or self.bola_pos[0] >= constants.SCREEN_WIDTH - 50:
            self.ball_velocity_x *= -1
        if self.bola_pos[1] <= 0 or self.bola_pos[1] >= constants.SCREEN_HEIGHT - 50:
            self.ball_velocity_y *= -1
            
        #Verificar colisión con la paleta 1
        # Verificar colisión con la paleta 1
        paleta1_rect = pygame.Rect(0, self.y_paleta1, paleta_width, paleta_height)
        bola_rect = pygame.Rect(self.bola_pos[0], self.bola_pos[1], 40, 40)
        if bola_rect.colliderect(paleta1_rect):
            self.ball_velocity_x *= -1  # Cambiar dirección horizontal de la pelota

        # Verificar colisión con la paleta 2
        paleta2_rect = pygame.Rect(constants.SCREEN_WIDTH - paleta_width, self.y_paleta2, paleta_width, paleta_height)
        if bola_rect.colliderect(paleta2_rect):
            self.ball_velocity_x *= -1  # Cambiar dirección horizontal de la pelota