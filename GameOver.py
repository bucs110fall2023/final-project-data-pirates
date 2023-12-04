import pygame

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

game_state = "start_menu"
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit(0)

    bigger_font = pygame.font.Font(None, 100)
    font = pygame.font.Font(None, 36)

    def Game_over_screen():
        screen.fill("black")
        title = bigger_font.render("Game Over", True, "white")
        restart_button = font.render("Press R to restart", True, "green")
        quit_button = font.render("Press Q to quit", True, "red")
        screen.blit(title, (WINDOW_WIDTH/2 - title.get_width()/2, WINDOW_HEIGHT/2 - title.get_height()))
        screen.blit(restart_button, (WINDOW_WIDTH/2 - restart_button.get_width()/2, WINDOW_HEIGHT/2 + restart_button.get_height()/2))
        screen.blit(quit_button, (WINDOW_WIDTH/2 - quit_button.get_width()/2, WINDOW_HEIGHT/2 + quit_button.get_height()/.5))
        pygame.display.update()


    def You_escaped_screen():
            screen.fill("black")
            title = bigger_font.render("You Escaped!", True, "white")
            restart_button = font.render("Press R to restart", True, "green")
            quit_button = font.render("Press Q to quit", True, "red")
            screen.blit(title, (WINDOW_WIDTH/2 - title.get_width()/2, WINDOW_HEIGHT/2 - title.get_height()))
            screen.blit(restart_button, (WINDOW_WIDTH/2 - restart_button.get_width()/2, WINDOW_HEIGHT/1.9 + restart_button.get_height()/2))
            screen.blit(quit_button, (WINDOW_WIDTH/2 - quit_button.get_width()/2, WINDOW_HEIGHT/2 + quit_button.get_height()/.35))
            pygame.display.update()


    if game_state == "game_over" or "you_escaped":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

    Game_over_screen()
    You_escaped_screen()