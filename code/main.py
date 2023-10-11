import pygame
import sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI
from gameover import GameOver
from pause import PauseScreen

class Game:
    def __init__(self):
        # Atributos del juego
        self.max_level = 2
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0

        # Audio
        self.level_bg_music = pygame.mixer.Sound('audio/level_music.wav')
        self.overworld_bg_music = pygame.mixer.Sound('audio/overworld_music.wav')

        # Interfaz de usuario
        self.ui = UI(screen)

        # Creación del mundo principal
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.current_bg_music = None
        self.paused = False

        # Superficie para pantalla de pausa
        self.pause_message = pygame.font.Font(None, 36).render("Juego en pausa", True, (255, 255, 255))

        # Variable para controlar el estado del botón de pausa
        self.pause_button_clicked = False

    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health)
        self.status = 'level'
        if self.current_bg_music != self.level_bg_music:
            if self.current_bg_music is not None:
                self.current_bg_music.stop()
            self.level_bg_music.play(loops=-1)
            self.current_bg_music = self.level_bg_music

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        if self.current_bg_music != self.overworld_bg_music:
            if self.current_bg_music is not None:
                self.current_bg_music.stop()
            self.overworld_bg_music.play(loops=-1)
            self.current_bg_music = self.overworld_bg_music

    def change_coins(self, amount):
        self.coins += amount

    def change_health(self, amount):
        self.cur_health += amount

    def check_game_over(self):
        if self.cur_health <= 0 or (self.status == 'level' and self.level.player.sprite.rect.y > screen_height):
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0
            if self.current_bg_music == self.level_bg_music:
                self.current_bg_music.stop()
                self.overworld_bg_music.play(loops=-1)
                self.current_bg_music = self.overworld_bg_music
            game_over = GameOver(screen)
            while True:
                if game_over.handle_events():
                    self.overworld = Overworld(0, self.max_level, screen, self.create_level)
                    self.status = 'overworld'
                    return
                game_over.draw()
                pygame.display.update()

    def show_pause_screen(self):
    # Pausa el juego
        self.paused = True
        pygame.mixer.pause()
    # Muestra la pantalla de pausa
        pause_screen = PauseScreen(screen, self.resume_game, self.return_to_overworld, self.resume_game)
        pause_screen.run_pause()


    def resume_game(self):
        self.paused = not self.paused
        if self.paused:
            pygame.mixer.pause()
            self.show_pause_screen()
        else:
            pygame.mixer.unpause()

    def return_to_overworld(self):
        self.status = 'overworld'
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        pygame.mixer.unpause()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                    if self.paused:
                        pygame.mixer.pause()
                        self.show_pause_screen()
                    else:
                        pygame.mixer.unpause()

        if not self.paused:
            pygame.mixer.unpause()

            if self.status == 'overworld':
                self.overworld.run()
            else:
                self.level.run()
                self.ui.show_health(self.cur_health, self.max_health)
                self.ui.show_coins(self.coins)
                self.check_game_over()

                if self.cur_health <= 0 or self.level.player.sprite.rect.y > screen_height:
                    game_over = GameOver(screen)
                    while True:
                        if game_over.handle_events():
                            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
                            self.status = 'overworld'
                            return
                        game_over.draw()
                        pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    game.run()
    pygame.display.update()
    clock.tick(60)
