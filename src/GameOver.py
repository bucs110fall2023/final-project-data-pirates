# import pygame
# pygame.init()

# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600

# window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("title of game") #replace with actual game title
# font = pygame.font.Font(None, 48)
# game_over_text = font.render("GAME OVER", True , "white")
# restart_button = font.render('press R to restart', True, ("white"))
# quit_button = font.render("press Q to quit", True, ("white"))

# while True:
#     for event in pygame.event.get():
#         if (event.type == pygame.QUIT):
#             exit(0)

#     def game_over_screen():
#         window.fill("black")
#         if start_exit_buttons_visible:
#             font = pygame.font.Font(None, 48)
#             game_over_text = font.render("GAME OVER", True , "red")
#             restart_button = font.render('press R to restart', True, ("red"))
#             quit_button = font.render("press Q to quit", True, ("red"))
#             window.blit(game_over_text,(220, 50)) #(WINDOW_WIDTH/2 - game_over_text.get_width()/2, WINDOW_HEIGHT/2 - game_over_text.get_height()/3))
#             window.blit(restart_button, (220, 60)) #(WINDOW_WIDTH/2 - restart_button.get_width()/2, WINDOW_HEIGHT/1.9 + restart_button.get_height()))
#             window.blit(quit_button, (220, 20)) #(WINDOW_WIDTH/2 - quit_button.get_width()/2, WINDOW_HEIGHT/2 + quit_button.get_height()/2))
        
#     pygame.display.update()

