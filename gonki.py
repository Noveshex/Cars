import pygame
import random

pygame.init()
win = pygame.display.set_mode((800, 650))

pygame.display.set_caption("Cars")

bg = pygame.image.load('bg.png')
player = pygame.image.load('car.png')
other_cars = pygame.image.load('other_cars.png')

clock = pygame.time.Clock()

speed = 10
player_pos_x = 380
player_pos_y = 460

class oponent():
    speed = 5
    def __init__(self, x, y, speed):
        self.pos_x = x
        self.pos_y = y
        self.speed = speed

    def draw(self, win):
        win.blit(other_cars, (self.pos_x, self.pos_y))


def drawWindow():
    win.blit(bg, (0, 0))
    win.blit(player, (player_pos_x, player_pos_y))

    for car in cars:
        car.draw(win)

    pygame.display.update()

cars = []
spawnCar = 0
run = True
stop = False
while run:
    clock.tick(30)
    spawnCar += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not(stop):
        for car in cars:
            if player_pos_x == car.pos_x and player_pos_y == car.pos_y:
                stop = True

            if car.pos_y < 650:
                car.pos_y += car.speed
            else:
                cars.pop(cars.index(car))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos_x > 180:
            player_pos_x -= speed
        elif keys[pygame.K_RIGHT] and player_pos_x < 590:
            player_pos_x += speed
        if keys[pygame.K_UP] and player_pos_y > 300:
            player_pos_y -= speed
        elif keys[pygame.K_DOWN] and player_pos_y < 460:
            player_pos_y += speed

        if spawnCar % 70 == 0:
            cars.append(oponent(random.randint(185, 585), -50, random.randint(4, 6)))

        drawWindow()

pygame.quit()
