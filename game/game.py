import pygame
import sys
from utils import constants
from game.button import Button
from game.image import Images
from game.game_logic import GameLogic


class Game:
    def __init__(self):
        # Inicializar Pygame
        pygame.init()
        # estado inicial del juego sera la pantalla de inicio
        self.current_scene='inicio'
        #Definimos el tamaño de la pantalla
        self.window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        #Definimos el titulo
        pygame.display.set_caption(constants.GAME_TITLE)
        #Los dos botones que tendremos
        self.button_start = Button(300, 325, 200, 50, "Iniciar juego",self.iniciar)
        self.button_exit = Button(300, 400, 200, 50, "Salir", self.exit)
        #Verificamos que al iniciar a un no hemos ingresado a la escena del juego
        self.is_scene_entered = False
        # Instanciamos la lógica del juego
        self.game_logic = GameLogic()
        #instaciamos las imagenes
        self.image_manager = Images()


    def run(self):
        # Bucle principal del juego
        running = True
        clock = pygame.time.Clock()

        while running:
            # Eventos del juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                self.button_start.handle_event(event, self)
                self.button_exit.handle_event(event, self)
            # Lógica del juego
            
            # Dibujar en la ventana
            self.window.fill((0, 0, 0))

            if self.current_scene == "inicio":
                self.game_logic.draw_inicio(self.window, self.button_start, self.button_exit)
            elif self.current_scene == "juego":
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                # Mostrar contenido específico de la escena "juego"
                self.game_logic.draw_juego(self.window, self.image_manager)
            # Restaurar detección de eventos del mouse en la siguiente iteración del bucle
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
            # Actualizar la ventana
            pygame.display.flip()

        pygame.quit()
        
    def exit(self):
        sys.exit()
    
    def iniciar(self):
        self.current_scene = "juego"
        self.is_scene_entered = False
        print('iniciado juego')
