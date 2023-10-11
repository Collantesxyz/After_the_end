import pygame
from pausabtn import PauseButton

class PauseScreen:
    def __init__(self, screen, resume_callback, quit_callback, return_to_overworld_callback):
        self.screen = screen
        self.resume_button = PauseButton(None, (screen.get_width() // 2, screen.get_height() // 2 - 50), "Reanudar")
        self.quit_button = PauseButton(None, (screen.get_width() // 2, screen.get_height() // 2 + 50), "Salir")
        self.resume_callback = resume_callback
        self.quit_callback = quit_callback
        self.return_to_overworld_callback = return_to_overworld_callback  # Callback para regresar al Overworld
    
    def run_pause(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.resume_callback()
                        running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.resume_button.checkForClick(event):
                        running = False
                        self.resume_callback()
                    elif self.quit_button.checkForClick(event):
                        running = False
                        self.quit_callback()
                        self.return_to_overworld_callback()  # Llama al callback para regresar al Overworld

            self.resume_button.changeColor(pygame.mouse.get_pos())
            self.quit_button.changeColor(pygame.mouse.get_pos())

            self.screen.fill((0, 0, 0))  # Rellenar la pantalla de pausa con negro
            self.resume_button.update(self.screen)
            self.quit_button.update(self.screen)
            pygame.display.update()
