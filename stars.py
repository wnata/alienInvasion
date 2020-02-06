import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Draw a star"""

    def __init__(self, screen):
        """Create a star object at the ship's current position."""
        super(Star, self).__init__()
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new star at the left center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

    def blitme(self):
        """Draw the star at its current loc."""
        self.screen.blit(self.image, self.rect)
