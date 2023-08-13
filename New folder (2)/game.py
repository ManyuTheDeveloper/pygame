import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Game")

# Car properties
car_image = pygame.image.load("C:\Users\Manish Srivastav\Downloads\Car.png")
car_rect = car_image.get_rect()
car_speed = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_rect.x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_rect.x += car_speed

    screen.fill((255, 255, 255))
    screen.blit(car_image, car_rect)
    pygame.display.flip()

    clock.tick(60)
