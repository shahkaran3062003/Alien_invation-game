import pygame


class Button():
    def __init__(self, screen, ai_settings, msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.ai_settings = ai_settings

        self.width = self.ai_settings.button_width
        self.height = self.ai_settings.button_height
        self.button_bg_color = self.ai_settings.button_bg_color
        self.text_color = self.ai_settings.text_color
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
