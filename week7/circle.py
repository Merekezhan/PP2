import pygame
pygame.init()

clock_time = pygame.time.Clock()
width = 400
length = 500
radius = 10
surface = pygame.display.set_mode((width , length))

running = True
color = (255, 0, 0)
x = width / 2
y = length / 2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            color = (255, 0, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            color = (0, 255, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            color = (0, 0, 255)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]  and y >= radius: y-=3
    if pressed[pygame.K_DOWN] and y <= length - radius: y+=3
    if pressed[pygame.K_LEFT] and x >= radius : x-=3
    if pressed[pygame.K_RIGHT] and x <= width - radius : x+=3


    surface.fill((255, 255, 255))
    pygame.draw.circle(surface, color, (x, y), radius)

    pygame.display.flip()
    clock_time.tick(60)