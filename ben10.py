import pygame


class Power():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ben10.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)
