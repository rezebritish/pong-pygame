import pygame
from settings import*

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        if self.rect.top <= 0:
            self.y_speed = abs(self.y_speed)  # always down
        if self.rect.bottom >= HEIGHT:
            self.y_speed = -abs(self.y_speed)

        self.rect.x += self.x_speed * 2
        self.rect.y += self.y_speed * 2


    def draw(self, screen):
        glow = pygame.Surface((60, 60), pygame.SRCALPHA)
        pygame.draw.circle(glow, (255, 210, 90, 40), (30, 30), 30)
        pygame.draw.circle(glow, (255, 210, 90, 90), (30, 30), 20)
        screen.blit(glow, glow.get_rect(center=self.rect.center))
        pygame.draw.circle(screen, (255, 235, 160), self.rect.center, 10)