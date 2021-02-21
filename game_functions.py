import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown(ship, event, ai_settings, screen, bullets, stats, aliens, SB):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_q:
        sys.exit()

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_p:
        stats.press_p = True
        check_p(stats, aliens, bullets, ai_settings, screen, ship, SB)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allow:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False

    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def chech_events(ship, ai_settings, screen, bullets, button, stats, aliens, SB):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(ship, event, ai_settings,
                          screen, bullets, stats, aliens, SB)

        elif event.type == pygame.KEYUP:
            check_keyup(ship, event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            chech_button(stats, button, mouse_x, mouse_y, aliens,
                         bullets, ai_settings, screen, ship, SB)


def chech_button(stats, button, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship, SB):
    button_chech = button.rect.collidepoint(mouse_x, mouse_y)
    # if button_chech:
    if button_chech and not stats.game_active:
        reset_screen(ai_settings, stats, aliens, bullets, screen, ship, SB)

    else:
        stats.game_active = False
        stats.press_p = False
        pygame.mouse.set_visible(True)


def check_p(stats, aliens, bullets, ai_settings, screen, ship, SB):
    if stats.press_p and not stats.game_active:
        reset_screen(ai_settings, stats, aliens, bullets, screen, ship, SB)


def reset_screen(ai_settings, stats, aliens, bullets, screen, ship, SB):
    ai_settings.temp_setting()
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True

    SB.prep_score()
    SB.prep_high_score()
    SB.prep_level()
    SB.prep_ship()

    aliens.empty()
    bullets.empty()

    creat_alien_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()


def update_screen(ai_settings, screen, ship, bullets, aliens, button, stats, SB):

    screen.blit(ai_settings.screen_bg, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    SB.show_score()

    if not stats.game_active:
        button.draw_button()

    pygame.display.flip()


def update_bullets(bullets, aliens, ai_settings, screen, ship, stats, SB):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(
        bullets, aliens, ai_settings, screen, ship, stats, SB)


def check_bullet_alien_collisions(bullets, aliens, ai_settings, screen, ship, stats, SB):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += ai_settings.alien_point
        SB.prep_score()
        check_high_score(stats, SB)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increse_speeds()
        stats.level += 1
        SB.prep_level()
        creat_alien_fleet(ai_settings, screen, aliens, ship)


def check_high_score(stats, SB):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        SB.prep_high_score()


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (2*alien_width)
    number_aliens_x = int(available_space_x/(2*alien_width))

    return number_aliens_x


def get_number_rows(ai_settings, aliens_height, ship_height):
    available_space_y = (ai_settings.screen_height -
                         (3*aliens_height)-ship_height)

    number_rows = int(available_space_y/(2*aliens_height))
    return number_rows


def creat_alien(alien_number, screen, ai_settings, aliens, row_number):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height*row_number
    aliens.add(alien)


def creat_alien_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(screen, ai_settings)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, alien.rect.height, ship.rect.height)

    for row_number in range(number_rows):
        for aline_number in range(number_aliens_x):
            creat_alien(aline_number, screen, ai_settings, aliens, row_number)


def chech_fleet_edge(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, SB):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        SB.prep_ship()

        aliens.empty()
        bullets.empty()

        creat_alien_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False


def update_aliens(ai_settings, aliens, ship, stats, screen, bullets, SB):
    chech_fleet_edge(ai_settings, aliens)
    aliens.update()
    check_aliens_bottom(ai_settings, aliens, ship, stats, screen, bullets, SB)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, SB)


def check_aliens_bottom(ai_settings, aliens, ship, stats, screen, bullets, SB):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, SB)
            break
