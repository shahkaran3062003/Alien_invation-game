from ship import Ship
import pygame.font as pf
from pygame.sprite import Group


class Score_Board():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = ai_settings.score_text_color
        self.font = pf.SysFont(None, 48, True)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_img = self.font.render(
            score_str, True, self.text_color, None)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = str(self.stats.high_score)
        self.high_score_img = self.font.render(
            high_score, True, self.text_color, None)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        current_level = str(self.stats.level)
        self.level_img = self.font.render(
            current_level, True, self.text_color, None)
        self.level_img_rect = self.level_img.get_rect()
        self.level_img_rect.right = self.score_rect.right
        self.level_img_rect.top = self.screen_rect.top + 100

    def prep_ship(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.ai_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_img_rect)
        self.ships.draw(self.screen)
