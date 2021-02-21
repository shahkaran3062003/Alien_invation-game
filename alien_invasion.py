import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import Game_Stats as gs
from button import Button
from score_board import Score_Board as sb


def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)

    bullets = Group()

    aliens = Group()
    gf.creat_alien_fleet(ai_settings, screen, aliens, ship)

    stats = gs(ai_settings)
    button = Button(screen, ai_settings, "Play")
    SB = sb(ai_settings, screen, stats)

    while True:
        gf.chech_events(ship, ai_settings, screen,
                        bullets, button, stats, aliens, SB)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings,
                              screen, ship, stats, SB)
            gf.update_aliens(ai_settings, aliens, ship,
                             stats, screen, bullets, SB)
        gf.update_screen(ai_settings, screen, ship,
                         bullets, aliens, button, stats, SB)


run_game()
