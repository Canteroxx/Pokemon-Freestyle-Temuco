import pygame
from src.settings import WIDTH, HEIGHT, GOLD, CREAM, CHARACTERS


class Gallery:
    def __init__(self):
        self.selected = 0
        self.punki_unlocked = False

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return None

        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.selected = (self.selected + 1) % len(CHARACTERS)

        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.selected = (self.selected - 1) % len(CHARACTERS)

        return None

    def draw(self, screen, text, fonts, player):
        text("GALERÍA DE PERSONAJES", 90, fonts["normal"], GOLD)

        name = CHARACTERS[self.selected]
        locked = name == "punki" and not self.punki_unlocked

        sprite = player.frame(name, scale=2)

        if locked:
            sprite = self.make_shadow(sprite)

        screen.blit(
            sprite,
            sprite.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        )

        label = "???" if locked else name.upper()

        text(
            f"◀   {label}   ▶",
            HEIGHT - 130,
            fonts["normal"],
            GOLD
        )

        if locked:
            text(
                "RECOGE LAS 4 MANZANAS PARA DESBLOQUEARLO",
                HEIGHT - 80,
                fonts["small"],
                CREAM
            )
        else:
            text(
                "PERSONAJE DESBLOQUEADO",
                HEIGHT - 80,
                fonts["small"],
                CREAM
            )

    @staticmethod
    def make_shadow(sprite):
        shadow = sprite.copy()
        shadow.fill(
            (45, 45, 50, 255),
            special_flags=pygame.BLEND_RGBA_MULT
        )
        return shadow
