import pygame
from settings import *

class Paddle:
    def __init__(self, x, speed, image):
        self.speed = speed
        self.image = image
        self.rect = pygame.Rect(x, HEIGHT / 2 - 70, 120, 140)

    def move_player(self, keys_pressed):
        if keys_pressed[pygame.K_UP]:
            self.rect.top -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.rect.bottom += self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def move_opponent(self, ball):
        if self.rect.y < ball.y:
            self.rect.y += self.speed
        if self.rect.y > ball.y:
            self.rect.y-= self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def draw(self, screen):
        screen.blit(self.image, self.image.get_rect(midleft=self.rect.midleft))


def rebound_players_racket(player, ball):
    if ball.rect.colliderect(player.rect) and ball.x_speed > 0:
        ball.x_speed = -(abs(ball.x_speed) + 0.25)
        ball.y_speed = round((ball.rect.centery - player.rect.centery) / 15)


def rebound_opponent_racket(opponent, ball):
    if ball.rect.colliderect(opponent.rect) and ball.x_speed < 0:
        ball.x_speed = abs(ball.x_speed) + 0.25
        ball.y_speed = round((ball.rect.centery - opponent.rect.centery) / 15)



