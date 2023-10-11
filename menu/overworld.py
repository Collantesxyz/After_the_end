import pygame
from game_data import levels
from support import import_folder
from decoration import Sky

# Definición de la clase Node, que representa los nodos o niveles en el juego.
class Node(pygame.sprite.Sprite):
    def __init__(self, pos, status, icon_speed, path):
        super().__init__()
        self.frames = import_folder(path)  # Carga imágenes relacionadas con el nodo.
        self.frame_index = 0  # Índice para la animación de imágenes.
        self.image = self.frames[self.frame_index]  # Configura la imagen inicial.
        if status == 'available':
            self.status = 'available'
        else:
            self.status = 'locked'
        self.rect = self.image.get_rect(center=pos)

        # Zona de detección utilizada para interactuar con el nodo.
        self.detection_zone = pygame.Rect(self.rect.centerx - (icon_speed / 2),
                                         self.rect.centery - (icon_speed / 2),
                                         icon_speed, icon_speed)

    # Realiza la animación del nodo si está disponible.
    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    # Actualiza el nodo en cada fotograma.
    def update(self):
        if self.status == 'available':
            self.animate()
        else:
            # Si el nodo está bloqueado, aplica un efecto de oscurecimiento.
            tint_surf = self.image.copy()
            tint_surf.fill('black', None, pygame.BLEND_RGBA_MULT)
            self.image.blit(tint_surf, (0, 0))

# Definición de la clase Icon, que representa un ícono en el mapa del mundo.
class Icon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.image.load('graphics/overworld/Hat.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    # Actualiza la posición del ícono en cada fotograma.
    def update(self):
        self.rect.center = self.pos

# Definición de la clase Overworld, que gestiona el mundo y la navegación del juego.
class Overworld:
    def __init__(self, start_level, max_level, surface, create_level):
        # Configuración inicial.
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level
        self.create_level = create_level

        # Lógica de movimiento.
        self.moving = False
        self.move_direction = pygame.math.Vector2(0, 0)
        self.speed = 8

        # Configuración de sprites y objetos.
        self.setup_nodes()
        self.setup_icon()
        self.sky = Sky(8, 'overworld')

        # Temporizador para habilitar la entrada del jugador.
        self.start_time = pygame.time.get_ticks()
        self.allow_input = False
        self.timer_length = 300

    # Configura los nodos (niveles) en el mundo.
    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()

        for index, node_data in enumerate(levels.values()):
            if index <= self.max_level:
                node_sprite = Node(node_data['node_pos'], 'available', self.speed, node_data['node_graphics'])
            else:
                node_sprite = Node(node_data['node_pos'], 'locked', self.speed, node_data['node_graphics'])
            self.nodes.add(node_sprite)

    # Dibuja las conexiones entre nodos en el mapa.
    def draw_paths(self):
        if self.max_level > 0:
            points = [node['node_pos'] for index, node in enumerate(levels.values()) if index <= self.max_level]
            pygame.draw.lines(self.display_surface, 'blue', False, points, 6)

    # Configura el ícono en el nivel actual.
    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprite)

    # Captura la entrada del jugador.
    def input(self):
        keys = pygame.key.get_pressed()

        if not self.moving and self.allow_input:
            if keys[pygame.K_RIGHT] and self.current_level < self.max_level:
                self.move_direction = self.get_movement_data('next')
                self.current_level += 1
                self.moving = True
            elif keys[pygame.K_LEFT] and self.current_level > 0:
                self.move_direction = self.get_movement_data('previous')
                self.current_level -= 1
                self.moving = True
            elif keys[pygame.K_SPACE]:
                self.create_level(self.current_level)

    # Obtiene el vector de dirección de movimiento entre nodos.
    def get_movement_data(self, target):
        start = pygame.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)
        
        if target == 'next': 
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level + 1].rect.center)
        else:
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level - 1].rect.center)

        return (end - start).normalize()

    # Actualiza la posición del ícono en función del movimiento.
    def update_icon_pos(self):
        if self.moving and self.move_direction:
            self.icon.sprite.pos += self.move_direction * self.speed
            target_node = self.nodes.sprites()[self.current_level]
            if target_node.detection_zone.collidepoint(self.icon.sprite.pos):
                self.moving = False
                self.move_direction = pygame.math.Vector2(0, 0)

    # Controla el temporizador de entrada del jugador.
    def input_timer(self):
        if not self.allow_input:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= self.timer_length:
                self.allow_input = True

    # Método principal para ejecutar el juego.
    def run(self):
        self.input_timer()
        self.input()
        self.update_icon_pos()
        self.icon.update()
        self.nodes.update()

        # Dibuja el fondo, las conexiones, los nodos y el ícono en la superficie de visualización.
        self.sky.draw(self.display_surface)
        self.draw_paths()
        self.nodes.draw(self.display_surface)
        self.icon.draw(self.display_surface)

