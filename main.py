import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game stats.
    stats = GameStats(ai_settings)

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group of aliens
    aliens = pygame.sprite.Group()
    # xz sho eto
    all = pygame.sprite.RenderUpdates()

    # Make a group to store bullets in.
    bullets = Group()

    # Make a Scoreboard
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a Star
    star = Group()

    # Стартовый флот
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.create_stars_background(ai_settings, screen, star)
        all.update()
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button, star)


run_game()
