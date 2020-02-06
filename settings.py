
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # screen Settings
        self.screen_width = 800
        self.screen_height = 575
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_limit = 3
        self.ship_speed_factor = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 255, 60, 60
        self.bullets_allowed = 15

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # How quickly the alien point values increase
        self.score_scale = 1.1

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 10

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
