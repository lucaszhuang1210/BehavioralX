import pygame
from settings import *

class Overlay:
    def __init__(self, player):
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # imports
        overlay_path = '../graphics/overlay/'
        self.tools_surface = {tool:pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        self.seeds_surface = {seed:pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}

    def display(self):
        # tool
        tool_surface = self.tools_surface[self.player.selected_tool]
        tool_rect = tool_surface.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
        self.display_surface.blit(tool_surface, tool_rect)

        # seeds
        seed_surface = self.seeds_surface[self.player.selected_seed]
        seed_rect = seed_surface.get_rect(midbottom=OVERLAY_POSITIONS['seed'])
        self.display_surface.blit(seed_surface, seed_rect)
