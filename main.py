import pygame
from fighter import Fighter

pygame.init()

#Game Window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Project EnigmaBug")

#Background Image
bg_image = pygame.image.load("assets/background.jpeg").convert_alpha()

#displaying background adn function
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


#Create Character display
fighter_1 = Fighter (200, 310)
fighter_2 = Fighter (700, 310)

#Game Loop
run = True
while run :

    #draw background
    draw_bg()

    #Move Fighters
    fighter_1.move()
    fighter_2.move()

    #Draw Fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #update display
    pygame.display.update()

#exit pygame
pygame.quit()