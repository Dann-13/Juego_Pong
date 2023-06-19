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
        image1 = images.load_image("./assets/Paleta1.png",50,220)
        image2 = images.load_image("./assets/Paleta2.png",50,220)
        imageBall = images.load_image("./assets/Bola.png", 40,40)
        # Posición inicial de la paleta 2 (en el borde derecho de la ventana)
        x2 = constants.SCREEN_WIDTH - image2.get_width()
        
        #Manejando movimiento de las imagenes paleta 1
        self.y_paleta1 = self.moverPaletas(pygame.K_w, pygame.K_s, self.y_paleta1)
        images.draw_image(window, image1, 0, self.y_paleta1)
        
        #Paleta 2
        self.y_paleta2 = self.moverPaletas(pygame.K_UP, pygame.K_DOWN, self.y_paleta2)
        images.draw_image(window, image2, x2, self.y_paleta2)
        
        #Bola
        self.bola_pos = (self.bola_pos[0] + self.ball_velocity_x, self.bola_pos[1] + self.ball_velocity_y)
        # Comprueba si la pelota ha alcanzado los límites de la ventana y cambia la dirección si es necesario
        if self.bola_pos[0] <= 0 or self.bola_pos[0] >= constants.SCREEN_WIDTH - 40:
            self.ball_velocity_x *= -1
        if self.bola_pos[1] <= 0 or self.bola_pos[1] >= constants.SCREEN_HEIGHT - 40:
            self.ball_velocity_y *= -1
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
        