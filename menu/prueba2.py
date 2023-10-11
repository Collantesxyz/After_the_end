import pygame
import sys
import os
# Obtiene la ruta al directorio raíz del proyecto (GameAlexisLzL)
ruta_directorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_directorio)
from botones import Button 
from ahorrar import get_font, idioma_actual,BG, CREADOR
# Inicialización de pygame
pygame.init()
PANTALLA = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("AFTER THE END")

# Función para el menú principal
def main_menu():
    pygame.init()
    PANTALLA = pygame.display.set_mode((1280, 720))

    while True:
        PANTALLA.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("AFTER THE END", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        from ahorrar import idioma_actual
        OPTIONS_TEXT = Button(image=None, pos=(140, 250),
                              text_input=idioma_actual["start"], font=get_font(30), base_color="#d7fcd4", hovering_color="Yellow")
        OPTIONS_BUTTON = Button(image=None, pos=(140, 350),
                                text_input=idioma_actual["opcion_button"], font=get_font(30), base_color="#d7fcd4", hovering_color="Yellow")
        CREADORES_BUTTON = Button(image=None, pos=(140, 450),
                                  text_input=idioma_actual["creador_button"], font=get_font(30), base_color="#d7fcd4", hovering_color="Yellow")
        QUIT_BUTTON = Button(image=None, pos=(125, 550),
                             text_input=idioma_actual["exit_button"], font=get_font(30), base_color="#d7fcd4", hovering_color="Yellow")

        PANTALLA.blit(MENU_TEXT, MENU_RECT)

        for button in [OPTIONS_TEXT, OPTIONS_BUTTON, CREADORES_BUTTON, QUIT_BUTTON]:
            font_size = (30)
            if button.rect.collidepoint(MENU_MOUSE_POS):
                font_size = 45  # Tamaño más grande cuando el mouse está encima

            button.update_font_size(font_size)  # Actualizar el tamaño de fuente
            button.changeColor(MENU_MOUSE_POS)
            button.update(PANTALLA)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_TEXT.checkForInput(MENU_MOUSE_POS):
                    import start
                    start.bienvenida()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    from opciones import options
                    options()
                if CREADORES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    creadores()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



# Función para crear una imagen redonda a partir de una imagen dada
def crear_imagen_redonda(imagen, radio):
    # Crea una máscara circular con fondo transparente
    mascara = pygame.Surface((radio * 2, radio * 2), pygame.SRCALPHA)
    pygame.draw.circle(mascara, (0, 0, 0, 0), (radio, radio), radio)

    # Aplica la máscara a la imagen
    imagen = pygame.transform.scale(imagen, (radio * 2, radio * 2))
    imagen_redonda = pygame.Surface((radio * 2, radio * 2), pygame.SRCALPHA)
    imagen_redonda.blit(imagen, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    return imagen_redonda

# Función para la ventana de creadores
def creadores():
    global idioma_actual

    clock = pygame.time.Clock()
    FPS = 60

    # Lista de nombres para las tarjetas
    nombres = ["Alex LzL", "Joel", "Gustavo Ceja", "Brandon"]

    # Lista de rutas de archivo de imagen para las fotos de perfil
    fotos_perfil = ["assets/alexsupreme.png", "assets/perfila.png", "assets/gustav1.png", "assets/bran1.png"]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        PANTALLA.blit(CREADOR, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        # Definir las propiedades de las tarjetas
        card_spacing = 20  # Espacio entre tarjetas
        card_width = 270
        card_height = 360
        card_x = 60

        for nombre, foto_path in zip(nombres, fotos_perfil):  # Iterar sobre las listas de nombres y fotos de perfil
            # Crea un rectángulo para la tarjeta de presentación con bordes redondeados
            tarjeta_rect = pygame.Rect(card_x, 180, card_width, card_height)
            borde_color = (255, 255, 255) if tarjeta_rect.collidepoint(OPTIONS_MOUSE_POS) else (50, 50, 50)

            pygame.draw.rect(PANTALLA, (0, 0, 0), tarjeta_rect, border_radius=20)
            pygame.draw.rect(PANTALLA, borde_color, tarjeta_rect, width=5, border_radius=20)

            # Carga la foto de perfil correspondiente
            foto_perfil = pygame.image.load(foto_path)

            # Escala la imagen para que sea más pequeña
            radio_circulo = 100
            foto_perfil = pygame.transform.scale(foto_perfil, (radio_circulo * 2, radio_circulo * 2))

            # Dibuja la foto de perfil en la tarjeta con el color del borde
            imagen_rect = foto_perfil.get_rect(center=(tarjeta_rect.centerx, tarjeta_rect.centery - 50))

            # Dibuja un círculo exterior alrededor de la foto de perfil
            pygame.draw.circle(PANTALLA, borde_color, imagen_rect.center, radio_circulo + 5)

            # Asegúrate de que la imagen se dibuje correctamente en la tarjeta
            PANTALLA.blit(foto_perfil, imagen_rect.topleft)

            # Crea un objeto de texto para el nombre y obtén su rectángulo
            texto_nombre = get_font(30).render(nombre, True, "White")
            texto_rect = texto_nombre.get_rect(center=(tarjeta_rect.centerx, tarjeta_rect.centery + 100))

            # Cambia el color del texto cuando el mouse está sobre la tarjeta
            if tarjeta_rect.collidepoint(OPTIONS_MOUSE_POS):
                texto_nombre = get_font(30).render(nombre, True, "Yellow")

            # Dibuja el texto en la tarjeta
            PANTALLA.blit(texto_nombre, texto_rect)

            card_x += card_width + card_spacing  # Avanzar a la siguiente tarjeta
        from ahorrar import idioma_actual
        CREDITOS_TEXT = get_font(30).render(idioma_actual["creador_button"], True, "White")
        CREDITOS = CREDITOS_TEXT.get_rect(center=(640, 110))
        PANTALLA.blit(CREDITOS_TEXT, CREDITOS)

        OPTIONS_BACK = Button(image=None, pos=(50, 40),
                              text_input=idioma_actual["back_button"], font=get_font(30), base_color="White",
                              hovering_color="Green")
        #EFECTO DE BOTON MAS GRANDE
        OPTIONS_BACK_POS = pygame.mouse.get_pos()
        for button in [ OPTIONS_BACK]:
            font_size = (30)
            if button.rect.collidepoint(OPTIONS_BACK_POS):
                font_size = 60  # Tamaño más grande cuando el mouse está encima
            button.update_font_size(font_size)  # Actualizar el tamaño de fuente
            button.changeColor(OPTIONS_BACK_POS)
            button.update(PANTALLA)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        clock.tick(FPS)

# Iniciar el menú principal
main_menu()
