import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('image/ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.virtical = float(self.rect.bottom)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.ai_settings = ai_settings

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.speed_factor

        # if self.moving_left and self.img_rect.left > self.screen_rect.left:
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.speed_factor

        # if self.moving_up and self.img_rect.top > self.screen_rect.top:
        #     self.virtical -= self.ai_settings.speed_factor

        # if self.moving_down and self.img_rect.bottom < self.screen_rect.bottom:
        #     self.virtical += self.ai_settings.speed_factor

        self.rect.centerx = self.center
        # self.img_rect.bottom = self.virtical

    def center_ship(self):
        self.center = self.screen_rect.centerx
