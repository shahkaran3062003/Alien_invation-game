from pygame.image import load


class Settings():
    def __init__(self):

        # screen settings
        self.screen_width = 1300
        self.screen_height = 650
        self.speed_factor = 1.5
        self.screen_bg = load("image/bg_image.jpg")

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullet_allow = 5

        # alian setting
        self.alien_speed_factor = 3
        self.speed_up_rate = 1.1

        # ship settings
        self.ship_limit = 3

        # button settings
        self.button_width = 200
        self.button_height = 50
        self.button_bg_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.temp_setting()

        # score board
        self.score_text_color = (255, 255, 255)

    def temp_setting(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.alien_point = 50

    def increse_speeds(self):
        self.ship_speed_factor *= self.speed_up_rate
        self.bullet_speed_factor *= self.speed_up_rate
        self.fleet_drop_speed *= self.speed_up_rate
