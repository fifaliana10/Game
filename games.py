import pygame

from players import Player
from Adversaire import Adva

class Game:
    
    def __init__(self):
        # generer le joueur
        self.All_players = pygame.sprite.Group()
        self.player = Player(self)
        self.All_players.add(self.player)
        self.AdvaMaivana = Adva(self)
        self.All_AdvaMaivana = pygame.sprite.Group()
        self.Prs = {}
        self.mptr_Adva()
        
    def mptr_Adva(self):
        self.All_AdvaMaivana.add(self.AdvaMaivana)
        
    def collision_check(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
