import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("bob is pygame")

done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(250,250,60,60))
    print("jeff,droco--.--bob._.")