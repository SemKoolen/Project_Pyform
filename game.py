import pygame
from objects.Player import Player

pygame.init()
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 36)
gameDisplay = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Sudoku Solver')
clock = pygame.time.Clock()


def redraw_game_window():
    gameDisplay.fill((0, 0, 0))
    player1.draw(gameDisplay)
    pygame.display.update()

    
player1 = Player(200, 400, 64, 64)
while True:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys_pressed = pygame.key.get_pressed()
    player1.check_action(keys_pressed, gameDisplay)
            
    redraw_game_window()



