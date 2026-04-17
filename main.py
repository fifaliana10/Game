import pygame
from games import Game

pygame.init()

title = pygame.display.set_caption("Heros")
screen = pygame.display.set_mode((1000, 550), pygame.RESIZABLE)
background = pygame.image.load("image/backLand1.jpg")

#iconre_game = pygame.display.set_icon("image/iconGame.png")
# charger le joueur

game = Game()
run = True
while run:
    screen.blit(background, (0, 0))
    # Appliquer l image du joueur
    screen.blit(game.player.image, game.player.rect)
    # drawevana ilay ataqui
    game.player.All_attack.draw(screen)
    
    game.player.update_healf(screen)
    # Appliquer l adva maivana
    game.All_AdvaMaivana.draw(screen)
    
    # Affecter sur tous les projectiles l effet qui le deplace
    for lance in game.player.All_attack:
        if game.player.is_left:
            lance.removing()
            lance.L_lancer_projectile()
        
        elif game.player.is_right:
            lance.removing()
            lance.R_lancer_projectile()
     
    # mdepla le adva kely
    for AdvaMaivana in game.All_AdvaMaivana:
        AdvaMaivana.Hamono_AnLah()
        AdvaMaivana.update_healf_monsters(screen)
    # get event in instant
    if game.player.health == 0:
        pygame.quit()
    if game.Prs.get(pygame.K_RIGHT):
        if game.player.rect.x < 930:
            game.player.move_right()
            game.player.is_right = True
    elif game.Prs.get(pygame.K_LEFT):
        if game.player.rect.x > 0:
            game.player.move_left()
            game.player.is_left = True
            
    pygame.display.flip()
# event boucle

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            game.Prs[e.key] = True
            if e.key == pygame.K_UP:
                game.player.jump()
            elif e.key == pygame.K_SPACE:
                game.player.Attack()
                
