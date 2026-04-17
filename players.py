import pygame
from pouvoir import Projectile
import time as t

class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.Max_health = 100
        self.attack = 15
        self.vitesse = 3
        #on charge l image du joueur
        self.image = pygame.image.load("image/myplayer.png")
        # Grouping attack
        self.All_attack = pygame.sprite.Group()
        # on prend sa position
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 350
        self.j = 5
        self.is_left = False
        self.is_right = True
        # vitesse miakatra
           
    def move_right(self):
        if not self.game.collision_check(self, self.game.All_AdvaMaivana):
            self.rect.x += self.vitesse
            self. image = pygame.image.load("image/myplayer.png")
            self.is_right = True
            self.is_left = False

        elif self.game.collision_check(self, self.game.All_AdvaMaivana):
            self.rect.x -= 40
            self.is_right = False
            self.is_left = True
        
    def move_left(self):
        if not self.game.collision_check(self, self.game.All_AdvaMaivana):
            self.rect.x -= self.vitesse
            self. image = pygame.image.load("image/myplayer11.png")
            self.is_left = True
            self.is_right = False
        elif self.game.collision_check(self, self.game.All_AdvaMaivana):
            self.rect.x += 40
            self.is_left = False
            self.is_right = True
            
    def Attack(self):
        self.All_attack.add(Projectile(self))
        
    def update_healf(self, surface):
        # barre de vie
        bar_position = (self.rect.x - 10, self.rect.y - 20, self.health, 7)
        bar_color = (250, 000, 10)
        bar_shadow = (12, 16, 20)
        bar_position_2 = (self.rect.x -5, self.rect.y - 20, self.Max_health, 9)
        pygame.draw.rect(surface, bar_shadow, bar_position_2)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, att):
        self.health -= att
    
    def jump(self):
        for i in range(0,10):
            self.rect.y += self.j
            t.sleep(200)
