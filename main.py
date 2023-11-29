import pygame
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
   
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

# pygame.display.flip()
screen_width = 1200
screen_height = 800
a = 0
start_pos = 0

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Scary Game Title")

font = pygame.font.Font(None, 48)
choice_1 = font.render("Start", True , "white")

while a == 0:
    screen.fill("black")
    pos = pygame.mouse.get_pos()
    if 10 <= pos[0] <= 210 and 10 <= pos[1] <= 110:
        pygame.draw.rect(screen, "white", [500, 400, 200, 100] )
    else:
        pygame.draw.rect(screen, "gray" , [500, 400, 200, 100])
     
    screen.blit(choice_1, (550, 450))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if  500<= pos[0] <= 600 and 400<= pos[1] <= 500:
                start_pos += 1
                a += 1
    pygame.display.update()


    
    while a == 1:
        screen=pygame.display.set_mode([screen_width, screen_height])
        screen.fill("black")
        pygame.display.flip()