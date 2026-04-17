import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity_projectile = 4
        self.player = player
        self.image = pygame.image.load("image/pouvoir.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 30
        self.rect.y = player.rect.y + 20
        self.source_image = self.image
        self.angle = 0
        
    def L_lancer_projectile(self,):
        self.rect.x -= self.velocity_projectile
        self.removing()
        self.rotation(1)

    def R_lancer_projectile(self):
        self.rect.x += self.velocity_projectile
        self.removing()
        self.rotation(1)
    
       
        
    def removing(self):
        for Adveresera in self.player.game.collision_check(self, self.player.game.All_AdvaMaivana):
            self.remove_projectile()
            Adveresera.damage(self.player.attack)
            
        if self.rect.x > 940:
            self.remove_projectile()
            self.player.All_attack.remove(self)
        elif self.rect.x < 0:
            self.remove_projectile()
            self.rotation(1)
        
    def rotation(self, power):
        self.angle += 20
        self.image = pygame.transform.rotozoom(self.source_image, self.angle, power)
        self.rect = self.image.get_rect(center = self.rect.center)
        
    def remove_projectile(self):
        self.player.All_attack.remove(self)