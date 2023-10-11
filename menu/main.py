import pygame, sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI
from gameover import GameOver

class Game:
    def __init__(self):
        # game attributes
        self.max_level = 2
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0

        # audio 
        self.level_bg_music = pygame.mixer.Sound('audio/level_music.wav')
        self.overworld_bg_music = pygame.mixer.Sound('audio/overworld_music.wav')

        # user interface 
        self.ui = UI(screen)

        # overworld creation
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.current_bg_music = None  # Variable para rastrear la música de fondo actual

        # Reproduce la música de overworld en el inicio
        if self.current_bg_music != self.overworld_bg_music:
            if self.current_bg_music is not None:
                self.current_bg_music.stop()
            self.overworld_bg_music.play(loops=-1)
            self.current_bg_music = self.overworld_bg_music

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
            # Cambia la pantalla de Overworld por la de Game Over
            game_over = GameOver(screen)
            while True:
                if game_over.handle_events():
                    # Si el jugador presiona "R", reinicia el juego
                    self.overworld = Overworld(0, self.max_level, screen, self.create_level)
                    self.status = 'overworld'
                    return
                game_over.draw()
                pygame.display.update()

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()

            # Verifica si el juego ha terminado y muestra la pantalla de Game Over
            if self.cur_health <= 0 or self.level.player.sprite.rect.y > screen_height:
                game_over = GameOver(screen)
                while True:
                    if game_over.handle_events():
                        # Si el jugador presiona "R", reinicia el juego
                        return
                    game_over.draw()
                    pygame.display.update()

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    game.run()

    pygame.display.update()
    clock.tick(60)
