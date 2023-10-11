# volumen.py
import sys
import pygame
import os
# Obtiene la ruta al directorio raíz del proyecto (GameAlexisLzL)
ruta_directorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_directorio)
from botones import Button
from ahorrar import get_font
from ahorrar import idioma_actual,cambiar_idioma, VOLUMENB,volumen


PANTALLA = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("AFTER THE END")


# Función para la ventana de volumen
def volumen1():
    global volumen
    from ahorrar import idioma_actual
    clock = pygame.time.Clock()
    FPS = 60

    dragging = False  # Variable para rastrear si el usuario está arrastrando el control

    # Colores
    barra_color = (255, 255, 255, 128)  # Blanco semitransparente
    puntero_color = (173, 216, 230)  # Azul claro
    borde_color = (0, 0, 0)  # Color del borde negro

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        PANTALLA.blit(VOLUMENB, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    from opciones import options
                    options()  # Regresar a la pantalla de opciones
                elif 200 < OPTIONS_MOUSE_POS[0] < 1080 and 280 < OPTIONS_MOUSE_POS[1] < 320:
                    dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False

        # Dibuja la barra de volumen redondeada con borde negro
        barra_rect = pygame.Rect(199, 290, 880, 40)
        pygame.draw.rect(PANTALLA, borde_color, barra_rect, border_radius=20)  # Borde redondeado negro
        pygame.draw.rect(PANTALLA, barra_color, barra_rect, border_radius=20)  # Borde redondeado blanco (relleno)

        # Dibuja el puntero como una forma compuesta (parte frontal redondeada y borde negro)
        puntero_rect = pygame.Rect(200, 290, 880 * volumen, 40)
        pygame.draw.rect(PANTALLA, borde_color, puntero_rect, border_radius=20)  # Borde redondeado negro
        pygame.draw.rect(PANTALLA, puntero_color, puntero_rect, border_radius=20)  # Parte frontal redondeada


        volumen_text = get_font(30).render(f"{idioma_actual['Volumen_button']} {int(volumen * 100)} %", True, "cyan")
        PANTALLA.blit(volumen_text, (600, 400))

        OPTIONS_BACK = Button(image=None, pos=(50, 40), 
                            text_input=idioma_actual["back_button"], font=get_font(30), base_color="white", hovering_color="Green")

        for button in [ OPTIONS_BACK]:
            font_size = 30
            if button.rect.collidepoint(OPTIONS_MOUSE_POS):
                font_size = 45  # Tamaño más grande cuando el mouse está encima

            button.update_font_size(font_size)  # Actualizar el tamaño de fuente
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(PANTALLA)

        # Control del volumen
        if dragging and pygame.mouse.get_pressed()[0]:
            mouse_x, _ = pygame.mouse.get_pos()
            volumen = max(0, min(1, (mouse_x - 200) / 880))

            pygame.mixer.music.set_volume(volumen)

        pygame.display.update()
        clock.tick(FPS)
