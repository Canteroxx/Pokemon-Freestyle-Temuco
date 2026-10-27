import pygame
from src.settings import ROOT, WIDTH, HEIGHT, CREAM, GOLD

OPTIONS = ('JUGAR', 'SELECCIONAR PERSONAJE', 'GALERÍA DE PERSONAJES', 'CONFIGURACIÓN', 'SALIR')

class MainMenu:
    def __init__(self):
        self.selected = 0
        self.background = None

    def load_background(self):
        path = ROOT / 'assets' / 'backgrounds' / 'menu.jpg'
        if path.is_file():
            image = pygame.image.load(str(path)).convert()
            self.background = pygame.transform.scale(image, (WIDTH, HEIGHT))

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return None
        if event.key in (pygame.K_DOWN, pygame.K_s):
            self.selected = (self.selected + 1) % len(OPTIONS)
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.selected = (self.selected - 1) % len(OPTIONS)
        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            return ('world', 'select', 'gallery', 'settings', 'quit')[self.selected]
        return None

    def draw(self, screen, text, fonts):
        if self.background is not None:
            screen.blit(self.background, (0, 0))
            # Dark overlay to keep menu text readable on bright images.
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 110))
            screen.blit(overlay, (0, 0))
        text('POKÉMON RAP', 125, fonts['big'], GOLD)
        text('EDICIÓN FREESTYLE TEMUCO', 180, fonts['small'])
        for i, option in enumerate(OPTIONS):
            color = GOLD if i == self.selected else CREAM
            prefix = '>  ' if i == self.selected else '   '
            text(prefix + option, 295 + i * 55, fonts['normal'], color)
        text('BLOODMONEY  ·  VACIO   ·   Y TODA ESA MIERDA', HEIGHT - 35, fonts['small'])
