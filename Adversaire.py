import pygame


class Adva(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 1
        self.image = pygame.image.load("image/mummy.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 950
        self.rect.y = 320
        self.velocity = 1
        self.Max_health = 100
        self.health = 100
        self.degat_attack = 10
        
    def Hamono_AnLah(self):
        if not self.game.collision_check(self, self.game.All_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
            
    def damage(self, degat):
        self.health -= degat
        if self.health <= 0:
            self.rect.x = 950
            self.health = self.Max_health
        
    def update_healf_monsters(self, surface):
        # barre de vie
        bar_position = (self.rect.x + 15, self.rect.y - 20, self.health, 7)
        bar_color = (250, 000, 10)
        bar_shadow = (12, 16, 20)
        bar_position_2 = (self.rect.x + 17, self.rect.y - 20, self.Max_health, 9)
        pygame.draw.rect(surface, bar_shadow, bar_position_2)
        pygame.draw.rect(surface, bar_color, bar_position)
        
        