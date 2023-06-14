import pygame
from utils import constants
from game.button import Button

class Game:
    def __init__(self):
        # Inicializar Pygame
        pygame.init()

        self.window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption(constants.GAME_TITLE)
        self.button_start = Button(300, 325, 200, 50, "Iniciar juego",self.iniciar)
        self.button_exit = Button(300, 400, 200, 50, "Salir", self.exit)

    def run(self):
        # Bucle principal del juego
        running = True
        clock = pygame.time.Clock()

        while running:
            # Eventos del juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                self.button_start.handle_event(event)
                self.button_exit.handle_event(event)
            # Lógica del juego

            # Dibujar en la ventana
            self.window.fill((0, 0, 0))

            self.button_start.draw(self.window)
            self.button_exit.draw(self.window)

            # Actualizar la ventana
            pygame.display.flip()

        pygame.quit()
        
    def exit(self):
        pygame.quit()
    
    def iniciar(self):
        print('iniciado juego')
