import pygame

class GameOver:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)
        self.game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        self.restart_text = self.font.render("Press R to Restart", True, (255, 255, 255))
        self.game_over_rect = self.game_over_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        self.restart_rect = self.restart_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fondo negro
        self.screen.blit(self.game_over_text, self.game_over_rect)
        self.screen.blit(self.restart_text, self.restart_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Presiona "R" para reiniciar el juego
                    return True  # Indica que el juego debe reiniciarse
        return False
