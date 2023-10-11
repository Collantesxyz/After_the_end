import pygame
import sys
import os
# Obtiene la ruta al directorio raíz del proyecto (GameAlexisLzL)
ruta_directorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_directorio)
from ahorrar import BG

# Obtiene la ruta al directorio raíz del proyecto (GameAlexisLzL)
ruta_directorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_directorio)
from botones import Button
from ahorrar import get_font

# Inicializa Pygame
pygame.init()

# Crea una ventana
PANTALLA = pygame.display.set_mode((1280, 720))

# Define las dimensiones de los botones y los márgenes
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 100
MARGIN = 20

# Define la velocidad de desplazamiento de las tarjetas
SCROLL_SPEED = 10

def bienvenida():
    from ahorrar import idioma_actual

    pygame.display.set_caption(idioma_actual["options_titulo"])

    nivel1_button = Button(
        image=None,
        pos=(0, 360),  # Posición inicial del primer nivel
        text_input=idioma_actual["Facil"],
        font=get_font(45),
        base_color="White",
        hovering_color="Green"
    )
    nivel1_button.numero_de_nivel = 0  # Asigna un número de nivel a este botón

    nivel2_button = Button(
        image=None,
        pos=(BUTTON_WIDTH + MARGIN, 360),  # Posición inicial del segundo nivel
        text_input=idioma_actual["Dificil"],
        font=get_font(45),
        base_color="White",
        hovering_color="Green"
    )
    nivel2_button.numero_de_nivel = 1  # Asigna un número de nivel a este botón

    nivel3_button = Button(
        image=None,
        pos=(2 * (BUTTON_WIDTH + MARGIN), 360),  # Posición inicial del tercer nivel
        text_input="Nivel 3",
        font=get_font(45),
        base_color="White",
        hovering_color="Green"
    )
    nivel3_button.numero_de_nivel = 2  # Asigna un número de nivel a este botón

    nivel_buttons = [nivel1_button, nivel2_button, nivel3_button]
    current_level = 0

    while True:

        PANTALLA.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("AFTER THE END SESION", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        OPTIONS_BACK = Button(image=None, pos=(50, 40), 
                            text_input=idioma_actual["back_button"], font=get_font(30), base_color="#d7fcd4", hovering_color="Green")

        PANTALLA.blit(MENU_TEXT, MENU_RECT)
        for button in [ OPTIONS_BACK]:
            font_size = 30
            if button.rect.collidepoint(PLAY_MOUSE_POS):
                font_size = 45  # Tamaño más grande cuando el mouse está encima

            button.update_font_size(font_size)  # Actualizar el tamaño de fuente
            button.changeColor(PLAY_MOUSE_POS)
            button.update(PANTALLA)   

        for button in nivel_buttons:
            button_x = button.rect.x
            # Calcula la posición x deseada para el botón
            target_x = 640 + (BUTTON_WIDTH + MARGIN) * (button.numero_de_nivel - current_level)
            # Mueve el botón hacia la posición deseada suavemente
            if button_x < target_x:
                button_x += 10
                if button_x > target_x:
                    button_x = target_x
            elif button_x > target_x:
                button_x -= 10
                if button_x < target_x:
                    button_x = target_x
            button.rect.x = button_x
            button.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(PLAY_MOUSE_POS):
                    from prueba2 import main_menu
                    main_menu()
                if nivel1_button.checkForInput(PLAY_MOUSE_POS):
                    import Nivel1
                    Nivel1()
                if nivel2_button.checkForInput(PLAY_MOUSE_POS):
                    from Nivel2 import ScreenNivel2
                    ScreenNivel2()
                if nivel3_button.checkForInput(PLAY_MOUSE_POS):                 
                    from Nivel3 import ScreenNivel3
                    ScreenNivel3()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if current_level < len(nivel_buttons) - 1:
                        current_level += 1
                elif event.key == pygame.K_LEFT:
                    if current_level > 0:
                        current_level -= 1


        pygame.display.update()

# Llama a la función bienvenida() para iniciar la pantalla de bienvenida

bienvenida()