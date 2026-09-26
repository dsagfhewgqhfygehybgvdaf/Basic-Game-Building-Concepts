import pygame
def main():
    pygame.init()
    screen_width,screen_height=500,400
    screen=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Mini Sprite Adventures")
    x,y=50,50
    width,height=60,60
    speed=4
    RED=(255,0,0)
    BLUE=(0,0,255)
    BLACK=(0,0,0)
    WHITE=(255,255,255)
    YELLOW=(255,255,0)
    CYAN=(0,255,255)
    color=CYAN
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        if pygame.key.get_pressed()[pygame.K_w]:
            y-=speed
        if pygame.key.get_pressed()[pygame.K_s]:
            y+=speed
        if pygame.key.get_pressed()[pygame.K_a]:
            x-=speed
        if pygame.key.get_pressed()[pygame.K_d]:
            x+=speed
        x=min(max(0,x),screen_width-width)
        y=min(max(0,y),screen_height-height)
        if x==0:
            color=BLACK
        elif x==screen_width-width:
            color=WHITE
        elif y==0:
            color=YELLOW
        elif y== screen_height-height:
            color=RED
        else:
            color=CYAN
        screen.fill(BLUE)
        pygame.draw.circle(screen, YELLOW,(420,320),35)
        pygame.draw.circle(screen, BLACK,(80,320),35,4)
        sprite_rect=pygame.Rect(x,y, width,height)
        pygame.draw.rect(screen,color,sprite_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    main()