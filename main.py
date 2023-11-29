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

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit(0)

    screen_width = 600
    screen_height = 600
    screen=pygame.display.set_mode([screen_width, screen_height])
    screen.fill("black")
    pygame.display.flip()

    