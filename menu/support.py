from csv import reader
from settings import tile_size
import os
import pygame

def import_folder(folder_name):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    folder_path = os.path.join(script_directory, folder_name)
    
    surface_list = []

    for _, _, image_files in os.walk(folder_path):
        for image in image_files:
            full_path = os.path.join(folder_path, image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

        return surface_list

def import_csv_layout(file_name):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, file_name)

    terrain_map = []
    with open(file_path) as map_file:
        level = reader(map_file, delimiter=',')
        for row in level:
            terrain_map.append(list(row))
    return terrain_map

def import_cut_graphics(path):
	surface = pygame.image.load(path).convert_alpha()
	tile_num_x = int(surface.get_size()[0] / tile_size)
	tile_num_y = int(surface.get_size()[1] / tile_size)

	cut_tiles = []
	for row in range(tile_num_y):
		for col in range(tile_num_x):
			x = col * tile_size
			y = row * tile_size
			new_surf = pygame.Surface((tile_size,tile_size),flags = pygame.SRCALPHA)
			new_surf.blit(surface,(0,0),pygame.Rect(x,y,tile_size,tile_size))
			cut_tiles.append(new_surf)

	return cut_tiles
